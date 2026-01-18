import re
import sys
import textwrap
import unicodedata
from io import StringIO

from rdflib import RDF, Graph, Namespace


def normalize_text(text: str) -> str:
    """Standardizes text by scrubbing variable blank node IDs and absolute paths for test comparison."""
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _clean(text)
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    pattern = r"(={10,}\n(?:\s*=.*\n)+={10,}\n(?:\s*=.*\n)+={10,})"
    match = re.search(pattern, text)
    return match.group(0).strip() if match else ""


def _clean(val) -> str:
    """Helper to apply path and bnode normalization to a single string value."""
    if val is None:
        return ""
    v = str(val)
    v = re.sub(r"/.*/ontology-management-base/", "[ROOT]/", v)
    v = re.sub(r"N[a-f0-9]{32}", "[BNODE]", v)
    return v


def _get_visual_width(text: str) -> int:
    """Calculate visual width, counting wide emoji characters as 2 cells."""
    wide_chars = ["🔹", "❌", "✅", "⚠️", "🔍", "📌"]
    return len(text) + sum(text.count(c) for c in wide_chars)


def _print_boxed_line(text: str, width: int, file=None):
    """Prints a line framed by '= ... =' with visual width compensation."""
    inner_width = width - 4
    padding = inner_width - _get_visual_width(text)
    print(f"= {text}{' ' * max(0, padding)} =", file=file)


def _extract_and_sort_errors(report_graph: Graph):
    """Extracts and sorts errors deterministically using normalized content."""
    SH = Namespace("http://www.w3.org/ns/shacl#")
    results = list(report_graph.subjects(RDF.type, SH.ValidationResult))
    error_rows = []
    seen = set()

    for result in results:
        data = {
            "focus_node": report_graph.value(result, SH.focusNode),
            "result_path": report_graph.value(result, SH.resultPath),
            "result_message": report_graph.value(result, SH.resultMessage),
            "severity": report_graph.value(result, SH.resultSeverity),
        }
        sig = (
            str(data["focus_node"]),
            str(data["result_path"]),
            str(data["result_message"]),
        )
        if sig in seen:
            continue
        seen.add(sig)
        error_rows.append(data)

    # Sort by normalized path, then message, then node ID for stability
    error_rows.sort(
        key=lambda x: (
            _clean(x["result_path"]),
            _clean(x["result_message"]),
            _clean(x["focus_node"]),
            str(x["focus_node"]),
        )
    )
    return error_rows


def format_validate_target_classes_against_owl_classes_result(
    ontology_file, num_onto, num_shacl, matches, missing, recovered, extra
):
    """Formats validation summary using consistent boxed alignment."""
    width, buf = 150, StringIO()
    border = "=" * width
    print(f"\n{border}", file=buf)
    _print_boxed_line("VALIDATION SUMMARY".center(width - 4), width, buf)
    print(border, file=buf)
    _print_boxed_line(f"Ontology File: {_clean(ontology_file)}", width, buf)
    _print_boxed_line(f"🔹 Ontology Classes: {num_onto}", width, buf)
    _print_boxed_line(f"🔹 SHACL Target Classes: {num_shacl}", width, buf)
    _print_boxed_line(
        f"✅ Matched Classes: {len(matches) + len(recovered)}", width, buf
    )
    _print_boxed_line(f"❌ Missing Classes: {len(missing)}", width, buf)
    _print_boxed_line(f"⚠️  Extra Classes: {len(extra)}", width + 2, buf)
    if missing:
        print(border, file=buf)
        _print_boxed_line(f"❌ Missing SHACL Classes: {len(missing)}", width, buf)
        for cls in sorted(missing):
            _print_boxed_line(f"   ❌ {cls}", width, buf)
    print(border, file=buf)
    status = "❌ Validation failed!" if missing else "✅ Validation successful!"
    _print_boxed_line(status.center(width - 5), width, buf)
    print(border, file=buf)
    return buf.getvalue().strip()


def print_validation_result(
    success, onto_files=None, v_text="", report_graph=None, exit_code=None, file=None
):
    width, file = 150, file or sys.stdout
    border, inner_width = "=" * width, 146
    print(border, file=file)
    header = (
        "✅ SHACL validation passed for:"
        if success
        else "❌ SHACL validation failed for:"
    )
    _print_boxed_line(header.center(inner_width - 1), width, file=file)
    if onto_files:
        _print_boxed_line(" ", width, file=file)
        formatted_files = f"[{', '.join(f'\'{_clean(f)}\'' for f in onto_files)}]"
        for line in textwrap.wrap(formatted_files, width=inner_width):
            _print_boxed_line(line.center(inner_width), width, file=file)
        _print_boxed_line(" ", width, file=file)
        print(border, file=file)
    if not success and report_graph:
        _print_boxed_line(" ", width, file=file)
        _print_boxed_line(
            "Structured Validation Errors:".center(inner_width), width, file=file
        )
        _print_boxed_line("-" * inner_width, width, file=file)
        errors = _extract_and_sort_errors(report_graph)
        for i, row in enumerate(errors):
            sev = (
                str(row["severity"]).split("#")[-1] if row["severity"] else "Violation"
            )
            labels = [f"🔹 [{sev}] Node: ", "   Property: ", "   Error:    "]
            max_label_w = max(_get_visual_width(ll) for ll in labels)

            def pad(ll):
                return ll + (" " * (max_label_w - _get_visual_width(ll)))

            # Print Node
            node_val = _clean(row["focus_node"])
            wrapped_node = textwrap.wrap(node_val, width=inner_width - max_label_w)
            _print_boxed_line(f"{pad(labels[0])}{wrapped_node[0]}", width, file=file)
            for line in wrapped_node[1:]:
                _print_boxed_line(" " * max_label_w + line, width, file=file)

            # Print Property
            if row["result_path"]:
                prop_val = _clean(row["result_path"])
                wrapped_prop = textwrap.wrap(prop_val, width=inner_width - max_label_w)
                _print_boxed_line(
                    f"{pad(labels[1])}{wrapped_prop[0]}", width, file=file
                )
                for line in wrapped_prop[1:]:
                    _print_boxed_line(" " * max_label_w + line, width, file=file)

            # Print Error Message
            if row["result_message"]:
                msg_val = _clean(row["result_message"])
                wrapped_msg = textwrap.wrap(msg_val, width=inner_width - max_label_w)
                _print_boxed_line(f"{pad(labels[2])}{wrapped_msg[0]}", width, file=file)
                for line in wrapped_msg[1:]:
                    _print_boxed_line(" " * max_label_w + line, width, file=file)

            if i < len(errors) - 1:
                _print_boxed_line("-" * inner_width, width, file=file)
        print(border, file=file)
    if exit_code is not None:
        sys.exit(exit_code)


def print_validate_jsonld_against_shacl_result(
    success, onto_files=None, v_text="", report_graph=None, exit_code=None, file=None
):
    print_validation_result(success, onto_files, v_text, report_graph, exit_code, file)
