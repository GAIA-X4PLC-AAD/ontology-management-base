#!/usr/bin/env bash
# Update GX artifacts from the service-characteristics submodule
# Usage: ./update-from-submodule.sh [version-tag]
#
# If version-tag is provided, checks out that tag in the submodule first.
# Otherwise, uses the currently checked-out version.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SUBMODULE_DIR="$ROOT_DIR/submodules/service-characteristics"
ARTIFACTS_DIR="$SCRIPT_DIR"

if [ ! -d "$SUBMODULE_DIR" ]; then
    echo "Error: Submodule not found at $SUBMODULE_DIR"
    echo "Run: git submodule update --init --recursive"
    exit 1
fi

cd "$SUBMODULE_DIR"

# Optionally check out a specific tag
if [ $# -gt 0 ]; then
    VERSION_TAG="$1"
    echo "Checking out version $VERSION_TAG..."
    git fetch --tags
    git checkout "$VERSION_TAG"
else
    VERSION_TAG=$(git describe --tags --exact-match 2>/dev/null || git describe --tags)
    echo "Using current submodule version: $VERSION_TAG"
fi

# Extract version number (strip v prefix if present, handle -N-g... suffix)
VERSION_NUMBER="${VERSION_TAG#v}"
VERSION_NUMBER="${VERSION_NUMBER%%-*}"

echo "Copying artifacts from submodule..."
cp -v "$SUBMODULE_DIR/ontology.owl.ttl" "$ARTIFACTS_DIR/gx.owl.ttl"
cp -v "$SUBMODULE_DIR/shapes.shacl.ttl" "$ARTIFACTS_DIR/gx.shacl.ttl"
cp -v "$SUBMODULE_DIR/context.jsonld" "$ARTIFACTS_DIR/gx.context.jsonld"

echo "Updating VERSION file..."
echo "$VERSION_NUMBER" > "$ARTIFACTS_DIR/VERSION"

echo ""
echo "✓ GX artifacts updated to version $VERSION_NUMBER"
echo ""
echo "If this is a post-release fix (not an official tag), manually update VERSION:"
echo "  echo '${VERSION_NUMBER}+fix.1' > artifacts/gx/VERSION"
echo ""
echo "Next steps:"
echo "  1. Regenerate documentation:"
echo "     python3 -m src.tools.utils.registry_updater"
echo "     python3 -m src.tools.utils.properties_updater"
echo ""
echo "  2. Update artifacts/gx/README.md with fix commit details"
echo ""
echo "  3. Commit the changes:"
echo "     git add artifacts/gx/ submodules/service-characteristics"
echo "     git commit -m 'chore(gx): upgrade Gaia-X to $VERSION_NUMBER'"
