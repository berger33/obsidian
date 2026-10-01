#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARTS="$ROOT/archives/split-assets"
OUT="$ROOT/archives/reconstructed"
mkdir -p "$OUT"

cat "$PARTS"/merge-completo-materializado-1m.tar.xz.part-* > "$OUT/merge-completo-materializado-1m.tar.xz"
cat "$PARTS"/ledger-v1000000-mat8000.zip.part-* > "$OUT/ledger-v1000000-mat8000.zip"

(
  cd "$OUT"
  cp "$PARTS/SHA256SUMS.txt" .
  sha256sum -c SHA256SUMS.txt --ignore-missing
)

echo "Arquivos reconstruídos em: $OUT"
echo "Para extrair o merge:"
echo "tar -xJf $OUT/merge-completo-materializado-1m.tar.xz"
