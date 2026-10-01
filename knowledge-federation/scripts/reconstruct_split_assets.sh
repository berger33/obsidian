#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVES="$ROOT/archives"
PARTS="$ARCHIVES/split-assets"
OUT="$ARCHIVES/reconstructed"
mkdir -p "$OUT"

if compgen -G "$PARTS/merge-completo-materializado-1m.tar.xz.part-*" > /dev/null; then
  cat "$PARTS"/merge-completo-materializado-1m.tar.xz.part-* > "$OUT/merge-completo-materializado-1m.tar.xz"
elif [ -f "$ARCHIVES/merge-completo-materializado-1m.tar.xz" ]; then
  cp -f "$ARCHIVES/merge-completo-materializado-1m.tar.xz" "$OUT/merge-completo-materializado-1m.tar.xz"
fi

if compgen -G "$PARTS/ledger-v1000000-mat8000.zip.part-*" > /dev/null; then
  cat "$PARTS"/ledger-v1000000-mat8000.zip.part-* > "$OUT/ledger-v1000000-mat8000.zip"
elif [ -f "$ARCHIVES/ledger-v1000000-mat8000.sqlite.xz" ]; then
  cp -f "$ARCHIVES/ledger-v1000000-mat8000.sqlite.xz" "$OUT/ledger-v1000000-mat8000.sqlite.xz"
fi

(
  cd "$ARCHIVES"
  sha256sum -c "$PARTS/SHA256SUMS.txt" --ignore-missing
)

echo "Arquivos verificados e prontos em: $ARCHIVES (e espelhados em $OUT)"
echo "Para extrair o merge completo:"
echo "tar -xJf $ARCHIVES/merge-completo-materializado-1m.tar.xz"
