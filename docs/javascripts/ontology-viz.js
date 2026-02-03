/**
 * Ontology Visualization - Interactive class diagrams using N3.js + Vis.js
 *
 * Features:
 * - Lazy loading with Intersection Observer
 * - Client-side TTL parsing via N3.js
 * - Interactive force-directed graphs via Vis.js
 * - External domain redirect (gx → Gaia-X docs)
 * - Cross-domain navigation with clickable nodes
 * - Search/filter functionality
 * - Dark mode support
 */

(function () {
  "use strict";

  // Configuration
  const CONFIG = {
    // External domains that redirect to official documentation
    externalDomains: {
      gx: {
        name: "Gaia-X",
        url: "https://docs.gaia-x.eu/ontology/development/",
        classUrlPattern:
          "https://docs.gaia-x.eu/ontology/development/classes/{class}/",
        description:
          "The Gaia-X ontology is maintained by the Gaia-X community. View the official documentation for complete class definitions and interactive visualizations.",
      },
    },

    // RDF namespaces
    namespaces: {
      rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      rdfs: "http://www.w3.org/2000/01/rdf-schema#",
      owl: "http://www.w3.org/2002/07/owl#",
      sh: "http://www.w3.org/ns/shacl#",
      xsd: "http://www.w3.org/2001/XMLSchema#",
    },

    // Vis.js network options
    networkOptions: {
      nodes: {
        font: { size: 14, face: "system-ui, sans-serif" },
        borderWidth: 2,
        shadow: { enabled: true, size: 5 },
        scaling: { min: 20, max: 40 },
      },
      edges: {
        font: { size: 10, align: "middle", face: "system-ui, sans-serif" },
        smooth: { type: "cubicBezier", roundness: 0.4 },
        arrows: { to: { enabled: true, scaleFactor: 0.8 } },
      },
      physics: {
        solver: "forceAtlas2Based",
        forceAtlas2Based: {
          gravitationalConstant: -50,
          centralGravity: 0.01,
          springLength: 150,
          springConstant: 0.08,
        },
        stabilization: { iterations: 150, fit: true },
      },
      interaction: {
        hover: true,
        tooltipDelay: 200,
        zoomView: true,
        dragView: true,
      },
      layout: {
        improvedLayout: true,
      },
    },

    // Node colors by type
    colors: {
      class: { background: "#6366f1", border: "#4f46e5", font: "#ffffff" },
      external: { background: "#94a3b8", border: "#64748b", font: "#1e293b" },
      property: { background: "#22c55e", border: "#16a34a", font: "#ffffff" },
      datatype: { background: "#f59e0b", border: "#d97706", font: "#ffffff" },
    },
  };

  /**
   * Main Ontology Visualizer class
   */
  class OntologyVisualizer {
    constructor() {
      this.observer = null;
      this.loadedGraphs = new Map(); // Cache parsed graphs
      this.globalClassIndex = new Map(); // Cross-domain class index
      this.init();
    }

    init() {
      // Wait for DOM to be ready
      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", () =>
          this.setupObserver()
        );
      } else {
        this.setupObserver();
      }
    }

    setupObserver() {
      // Find all visualization containers
      const containers = document.querySelectorAll("[data-ontology-viz]");
      console.log("[ontology-viz] Found containers:", containers.length);
      if (containers.length === 0) return;

      // Setup Intersection Observer for lazy loading
      this.observer = new IntersectionObserver(
        (entries) => this.onIntersection(entries),
        { rootMargin: "100px", threshold: 0.1 }
      );

      containers.forEach((container) => {
        console.log("[ontology-viz] Setting up container:", container.dataset.ontologyViz);
        this.showLoadingState(container);
        this.observer.observe(container);
      });
    }

    onIntersection(entries) {
      entries.forEach((entry) => {
        console.log("[ontology-viz] Intersection:", entry.target.dataset.ontologyViz, "isIntersecting:", entry.isIntersecting);
        if (entry.isIntersecting) {
          this.observer.unobserve(entry.target);
          this.loadVisualization(entry.target);
        }
      });
    }

    /**
     * Show loading spinner
     */
    showLoadingState(container) {
      container.innerHTML = `
        <div class="viz-loading">
          <div class="spinner"></div>
          <span>Loading ontology...</span>
        </div>
      `;
    }

    /**
     * Show error state
     */
    showErrorState(container, message) {
      container.innerHTML = `
        <div class="viz-error">
          <span class="error-icon">⚠️</span>
          <span>${message}</span>
        </div>
      `;
    }

    /**
     * Load and render visualization for a container
     */
    async loadVisualization(container) {
      const ttlPath = container.dataset.ontologyViz;
      const domain = container.dataset.domain;
      const focusClass = container.dataset.focusClass;

      console.log("[ontology-viz] Loading visualization:", { ttlPath, domain, focusClass });

      // Check if this is an external domain
      if (domain && CONFIG.externalDomains[domain]) {
        console.log("[ontology-viz] External domain detected:", domain);
        this.renderExternalDomainCard(container, domain);
        return;
      }

      try {
        // Fetch and parse TTL
        console.log("[ontology-viz] Fetching:", ttlPath);
        const response = await fetch(ttlPath);
        if (!response.ok) {
          throw new Error(`Failed to load ${ttlPath}: ${response.status}`);
        }

        const ttlText = await response.text();
        console.log("[ontology-viz] Fetched TTL, length:", ttlText.length);
        const graphData = await this.parseTTL(ttlText, ttlPath);
        console.log("[ontology-viz] Parsed TTL, store size:", graphData.store.size);

        // Cache the graph
        this.loadedGraphs.set(ttlPath, graphData);

        // Build visualization data
        const vizData = this.buildVisualizationData(graphData, focusClass);
        console.log("[ontology-viz] Built viz data, nodes:", vizData.nodes.length, "edges:", vizData.edges.length);

        // Render the network
        this.renderNetwork(container, vizData, graphData);
        console.log("[ontology-viz] Network rendered");
      } catch (error) {
        console.error("[ontology-viz] Error:", error);
        this.showErrorState(container, error.message);
      }
    }

    /**
     * Parse TTL using N3.js
     */
    async parseTTL(ttlText, sourcePath) {
      return new Promise((resolve, reject) => {
        if (typeof N3 === "undefined") {
          reject(new Error("N3.js library not loaded"));
          return;
        }

        const parser = new N3.Parser();
        const store = new N3.Store();

        parser.parse(ttlText, (error, quad, prefixes) => {
          if (error) {
            reject(error);
            return;
          }
          if (quad) {
            store.add(quad);
          } else {
            // Parsing complete
            resolve({
              store,
              prefixes: prefixes || {},
              sourcePath,
            });
          }
        });
      });
    }

    /**
     * Build visualization nodes and edges from parsed graph
     */
    buildVisualizationData(graphData, focusClass = null) {
      const { store } = graphData;
      const nodes = [];
      const edges = [];
      const nodeMap = new Map();
      const ns = CONFIG.namespaces;

      // Helper to create node ID
      const addNode = (iri, type = "class") => {
        if (nodeMap.has(iri)) return nodeMap.get(iri);

        const label = this.getLabel(store, iri) || this.localName(iri);
        const isExternal = this.isExternalClass(iri);
        const nodeType = isExternal ? "external" : type;
        const colors = CONFIG.colors[nodeType];

        const node = {
          id: iri,
          label: label,
          title: this.buildTooltip(store, iri, label),
          group: nodeType,
          color: {
            background: colors.background,
            border: colors.border,
            highlight: { background: colors.background, border: "#000" },
            hover: { background: colors.background, border: "#000" },
          },
          font: { color: colors.font },
          shape: type === "class" ? "ellipse" : "box",
          // Store metadata for click handling
          _iri: iri,
          _domain: this.extractDomain(iri),
          _isExternal: isExternal,
        };

        nodes.push(node);
        nodeMap.set(iri, node);
        return node;
      };

      // Extract owl:Class and rdfs:Class
      const classTypes = [
        N3.DataFactory.namedNode(ns.owl + "Class"),
        N3.DataFactory.namedNode(ns.rdfs + "Class"),
      ];

      classTypes.forEach((classType) => {
        store
          .getQuads(null, N3.DataFactory.namedNode(ns.rdf + "type"), classType)
          .forEach((quad) => {
            if (quad.subject.termType === "NamedNode") {
              addNode(quad.subject.value, "class");
            }
          });
      });

      // Extract rdfs:subClassOf relationships
      store
        .getQuads(
          null,
          N3.DataFactory.namedNode(ns.rdfs + "subClassOf"),
          null
        )
        .forEach((quad) => {
          if (
            quad.subject.termType === "NamedNode" &&
            quad.object.termType === "NamedNode"
          ) {
            const subClass = quad.subject.value;
            const superClass = quad.object.value;

            // Ensure both nodes exist
            addNode(subClass, "class");
            addNode(superClass, "class");

            edges.push({
              from: subClass,
              to: superClass,
              label: "subClassOf",
              color: { color: "#94a3b8" },
              dashes: false,
            });
          }
        });

      // Extract object property relationships from OWL restrictions
      store
        .getQuads(null, N3.DataFactory.namedNode(ns.owl + "onProperty"), null)
        .forEach((quad) => {
          const restriction = quad.subject;
          const property = quad.object;

          // Find what class this restriction is on
          store
            .getQuads(
              null,
              N3.DataFactory.namedNode(ns.rdfs + "subClassOf"),
              restriction
            )
            .forEach((subQuad) => {
              if (subQuad.subject.termType === "NamedNode") {
                // Find range (someValuesFrom, allValuesFrom)
                const rangePredicates = [
                  ns.owl + "someValuesFrom",
                  ns.owl + "allValuesFrom",
                ];

                rangePredicates.forEach((pred) => {
                  store
                    .getQuads(restriction, N3.DataFactory.namedNode(pred), null)
                    .forEach((rangeQuad) => {
                      if (rangeQuad.object.termType === "NamedNode") {
                        const fromClass = subQuad.subject.value;
                        const toClass = rangeQuad.object.value;

                        addNode(fromClass, "class");
                        addNode(toClass, "class");

                        edges.push({
                          from: fromClass,
                          to: toClass,
                          label: this.localName(property.value),
                          color: { color: "#22c55e" },
                          dashes: [5, 5],
                        });
                      }
                    });
                });
              }
            });
        });

      return {
        nodes: new vis.DataSet(nodes),
        edges: new vis.DataSet(edges),
        nodeMap,
      };
    }

    /**
     * Check if IRI belongs to an external domain
     */
    isExternalClass(iri) {
      for (const [domain, config] of Object.entries(CONFIG.externalDomains)) {
        if (
          iri.includes(`gaia-x`) ||
          iri.includes(`/gx/`) ||
          iri.includes(`/gx#`)
        ) {
          return true;
        }
      }
      return false;
    }

    /**
     * Extract domain from IRI
     */
    extractDomain(iri) {
      // Match patterns like /manifest/, /scenario/, etc.
      const match = iri.match(/\/([a-z-]+)\/v\d+\//i);
      if (match) return match[1];

      // Check for gx domain
      if (iri.includes("gaia-x") || iri.includes("/gx")) {
        return "gx";
      }

      return null;
    }

    /**
     * Get rdfs:label for an IRI
     */
    getLabel(store, iri) {
      const labelQuad = store.getQuads(
        N3.DataFactory.namedNode(iri),
        N3.DataFactory.namedNode(CONFIG.namespaces.rdfs + "label"),
        null
      )[0];

      if (labelQuad) {
        return labelQuad.object.value;
      }
      return null;
    }

    /**
     * Extract local name from IRI
     */
    localName(iri) {
      const hashIndex = iri.lastIndexOf("#");
      const slashIndex = iri.lastIndexOf("/");
      const index = Math.max(hashIndex, slashIndex);
      return index >= 0 ? iri.substring(index + 1) : iri;
    }

    /**
     * Build tooltip HTML for a node
     */
    buildTooltip(store, iri, label) {
      const comment = store.getQuads(
        N3.DataFactory.namedNode(iri),
        N3.DataFactory.namedNode(CONFIG.namespaces.rdfs + "comment"),
        null
      )[0];

      let html = `<div class="viz-tooltip">`;
      html += `<div class="tooltip-title">${label}</div>`;
      html += `<div class="tooltip-iri">${iri}</div>`;

      if (comment) {
        const desc = comment.object.value.substring(0, 150);
        html += `<div style="margin-top:0.5rem;font-size:0.8rem;">${desc}${
          comment.object.value.length > 150 ? "..." : ""
        }</div>`;
      }

      html += `</div>`;
      return html;
    }

    /**
     * Render external domain redirect card
     */
    renderExternalDomainCard(container, domain) {
      const config = CONFIG.externalDomains[domain];

      container.innerHTML = `
        <div class="external-domain-card">
          <span class="card-icon">🌐</span>
          <h3>${config.name} Ontology</h3>
          <p>${config.description}</p>
          <a href="${config.url}" target="_blank" rel="noopener noreferrer" class="external-link-btn">
            <span>View Official Documentation</span>
            <span class="icon">↗</span>
          </a>
        </div>
      `;
    }

    /**
     * Render the Vis.js network
     */
    renderNetwork(container, vizData, graphData) {
      // Clear container and add structure
      container.innerHTML = `
        <div class="viz-search">
          <input type="text" placeholder="Search classes..." />
        </div>
        <div class="viz-controls">
          <button data-action="fit" title="Fit to view">⊞</button>
          <button data-action="zoom-in" title="Zoom in">+</button>
          <button data-action="zoom-out" title="Zoom out">−</button>
        </div>
        <div class="viz-canvas" style="width:100%;height:100%;"></div>
        <div class="viz-legend">
          <div class="legend-item">
            <span class="legend-dot class"></span>
            <span>Class</span>
          </div>
          <div class="legend-item">
            <span class="legend-dot external"></span>
            <span>External</span>
          </div>
        </div>
        <div class="class-detail-panel">
          <div class="panel-header">
            <h4>Class Details</h4>
            <button class="panel-close">×</button>
          </div>
          <div class="panel-content"></div>
        </div>
      `;

      const canvas = container.querySelector(".viz-canvas");
      const network = new vis.Network(canvas, vizData, CONFIG.networkOptions);

      // Store reference for controls
      container._network = network;
      container._vizData = vizData;
      container._graphData = graphData;

      // Setup event handlers
      this.setupNetworkEvents(container, network, vizData, graphData);
      this.setupControls(container, network, vizData);
    }

    /**
     * Setup network click/hover events
     */
    setupNetworkEvents(container, network, vizData, graphData) {
      const panel = container.querySelector(".class-detail-panel");
      const panelContent = panel.querySelector(".panel-content");
      const panelClose = panel.querySelector(".panel-close");

      // Node click - show details or navigate
      network.on("click", (params) => {
        if (params.nodes.length > 0) {
          const nodeId = params.nodes[0];
          const node = vizData.nodes.get(nodeId);

          if (node._isExternal) {
            // External class - open in new tab
            const className = this.localName(node._iri);
            const url = CONFIG.externalDomains.gx.classUrlPattern.replace(
              "{class}",
              className
            );
            window.open(url, "_blank");
          } else {
            // Local class - show detail panel
            this.showClassDetails(panelContent, node, graphData);
            panel.classList.add("open");
          }
        }
      });

      // Double click - navigate to class page
      network.on("doubleClick", (params) => {
        if (params.nodes.length > 0) {
          const nodeId = params.nodes[0];
          const node = vizData.nodes.get(nodeId);

          if (!node._isExternal && node._domain) {
            const className = this.localName(node._iri);
            // Navigate to class page (will be generated by class_page_generator)
            const url = `../classes/${node._domain}/${className}/`;
            window.location.href = url;
          }
        }
      });

      // Close panel
      panelClose.addEventListener("click", () => {
        panel.classList.remove("open");
      });
    }

    /**
     * Setup control buttons
     */
    setupControls(container, network, vizData) {
      const controls = container.querySelector(".viz-controls");
      const searchInput = container.querySelector(".viz-search input");

      controls.addEventListener("click", (e) => {
        const action = e.target.dataset.action;
        if (!action) return;

        switch (action) {
          case "fit":
            network.fit({ animation: true });
            break;
          case "zoom-in":
            network.moveTo({ scale: network.getScale() * 1.3 });
            break;
          case "zoom-out":
            network.moveTo({ scale: network.getScale() / 1.3 });
            break;
        }
      });

      // Search functionality
      searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase();

        vizData.nodes.forEach((node) => {
          const matches =
            !query ||
            node.label.toLowerCase().includes(query) ||
            node.id.toLowerCase().includes(query);

          vizData.nodes.update({
            id: node.id,
            opacity: matches ? 1 : 0.2,
            font: { ...node.font, color: matches ? node.font.color : "#ccc" },
          });
        });
      });
    }

    /**
     * Show class details in side panel
     */
    showClassDetails(panelContent, node, graphData) {
      const { store } = graphData;
      const iri = node._iri;

      // Get superclasses
      const superClasses = store
        .getQuads(
          N3.DataFactory.namedNode(iri),
          N3.DataFactory.namedNode(CONFIG.namespaces.rdfs + "subClassOf"),
          null
        )
        .filter((q) => q.object.termType === "NamedNode")
        .map((q) => this.localName(q.object.value));

      // Get subclasses
      const subClasses = store
        .getQuads(
          null,
          N3.DataFactory.namedNode(CONFIG.namespaces.rdfs + "subClassOf"),
          N3.DataFactory.namedNode(iri)
        )
        .filter((q) => q.subject.termType === "NamedNode")
        .map((q) => this.localName(q.subject.value));

      // Get comment
      const commentQuad = store.getQuads(
        N3.DataFactory.namedNode(iri),
        N3.DataFactory.namedNode(CONFIG.namespaces.rdfs + "comment"),
        null
      )[0];

      const comment = commentQuad ? commentQuad.object.value : "No description";

      panelContent.innerHTML = `
        <div class="panel-section">
          <h5>IRI</h5>
          <code style="font-size:0.75rem;word-break:break-all;">${iri}</code>
        </div>
        <div class="panel-section">
          <h5>Description</h5>
          <p style="font-size:0.85rem;">${comment}</p>
        </div>
        ${
          superClasses.length > 0
            ? `
        <div class="panel-section">
          <h5>Parent Classes</h5>
          <ul>${superClasses.map((c) => `<li>${c}</li>`).join("")}</ul>
        </div>
        `
            : ""
        }
        ${
          subClasses.length > 0
            ? `
        <div class="panel-section">
          <h5>Child Classes</h5>
          <ul>${subClasses.map((c) => `<li>${c}</li>`).join("")}</ul>
        </div>
        `
            : ""
        }
        ${
          node._domain
            ? `
        <div class="panel-section">
          <a href="../classes/${node._domain}/${this.localName(
                iri
              )}/" class="md-button">
            View Full Details →
          </a>
        </div>
        `
            : ""
        }
      `;
    }
  }

  // Initialize when DOM is ready
  window.OntologyVisualizer = OntologyVisualizer;
  new OntologyVisualizer();
})();
