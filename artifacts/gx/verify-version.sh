#!/usr/bin/env bash
# Verify that GX VERSION file matches the submodule tag
# Usage: ./verify-version.sh
#
# Exit code 0 = synchronized
# Exit code 1 = out of sync

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SUBMODULE_DIR="$ROOT_DIR/submodules/service-characteristics"
VERSION_FILE="$SCRIPT_DIR/VERSION"

if [ ! -d "$SUBMODULE_DIR" ]; then
    echo "⚠️  Warning: Submodule not initialized"
    echo "Run: git submodule update --init --recursive"
    exit 1
fi

if [ ! -f "$VERSION_FILE" ]; then
    echo "❌ Error: VERSION file not found at $VERSION_FILE"
    exit 1
fi

cd "$SUBMODULE_DIR"
SUBMODULE_TAG=$(git describe --tags --exact-match 2>/dev/null || git describe --tags)
SUBMODULE_VERSION="${SUBMODULE_TAG#v}"
SUBMODULE_VERSION="${SUBMODULE_VERSION%%-*}"
SUBMODULE_COMMIT=$(git rev-parse --short HEAD)

VERSION_FILE_CONTENT=$(cat "$VERSION_FILE" | tr -d '[:space:]')
# Strip post-release suffix for base version comparison
VERSION_BASE="${VERSION_FILE_CONTENT%%+*}"

echo "Submodule version: $SUBMODULE_VERSION (tag: $SUBMODULE_TAG)"
echo "Submodule commit:  $SUBMODULE_COMMIT"
echo "VERSION file:      $VERSION_FILE_CONTENT"
echo ""

if [ "$VERSION_FILE_CONTENT" = "$SUBMODULE_VERSION" ]; then
    echo "✓ Versions match exactly (official release)"
    exit 0
elif [ "$VERSION_BASE" = "$SUBMODULE_VERSION" ] && [[ "$VERSION_FILE_CONTENT" == *"+"* ]]; then
    echo "✓ Version OK (post-release patch: $VERSION_FILE_CONTENT)"
    echo ""
    echo "Using version with additional fixes on top of $SUBMODULE_VERSION."
    echo "Submodule is at commit $SUBMODULE_COMMIT."
    exit 0
else
    echo "❌ Version mismatch!"
    echo ""
    echo "Expected base version: $SUBMODULE_VERSION"
    echo "VERSION file shows:    $VERSION_FILE_CONTENT"
    echo ""
    echo "To update, run:"
    echo "  cd $SCRIPT_DIR"
    echo "  ./update-from-submodule.sh"
    exit 1
fi
