#!/usr/bin/env bash
# claude-workflow kurulumu / güncellemesi.
# Kullanım: ./install.sh <proje-dizini> [--upgrade]
#   .claude/workflow/  çekirdek ve şablonlar (şablonun sahipliği; güncellemede yenilenir)
#   .claude/agents/    genel agent'lar (projede farklılaşmış dosya yedeklenir)
#   owner/, work/      iskelet (yalnız eksik dosyalar eklenir, mevcutlara dokunulmaz)
#   CLAUDE.md          çekirdeği içe aktaran satır yoksa eklenir
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:?Kullanım: install.sh <proje-dizini> [--upgrade]}"
MODE="${2:-}"
DEST="$(cd "$DEST" && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
VERSION="$(cat "$SRC/VERSION")"

installed="$DEST/.claude/workflow/VERSION"
if [[ -f "$installed" && "$MODE" != "--upgrade" ]]; then
  echo "Zaten kurulu (sürüm $(cat "$installed")). Güncellemek için --upgrade ver." >&2
  exit 1
fi

# Şablonun sahibi olduğu dosyalar: doğrudan yenilenir.
mkdir -p "$DEST/.claude/workflow/templates"
cp "$SRC"/core/*.md "$DEST/.claude/workflow/"
cp "$SRC"/templates/*.md "$DEST/.claude/workflow/templates/"

# Agent'lar: proje uyarlamışsa yedeklenir, sonra yenisi yazılır.
mkdir -p "$DEST/.claude/agents"
for f in "$SRC"/agents/*.md; do
  t="$DEST/.claude/agents/$(basename "$f")"
  if [[ -f "$t" ]] && ! cmp -s "$f" "$t"; then
    cp "$t" "$t.bak-$STAMP"
    echo "yedeklendi: ${t#$DEST/}.bak-$STAMP"
  fi
  cp "$f" "$t"
done

# İskelet: yalnız eksik olanlar.
(cd "$SRC/skeleton" && find . -type f) | while read -r rel; do
  t="$DEST/${rel#./}"
  if [[ ! -e "$t" ]]; then
    mkdir -p "$(dirname "$t")"
    cp "$SRC/skeleton/${rel#./}" "$t"
    echo "eklendi: ${rel#./}"
  fi
done

# CLAUDE.md çekirdeği içe aktarır.
LINE="@.claude/workflow/CORE.md"
if [[ ! -f "$DEST/CLAUDE.md" ]]; then
  printf '# Proje\n\n%s\n' "$LINE" > "$DEST/CLAUDE.md"
  echo "oluşturuldu: CLAUDE.md"
elif ! grep -qF "$LINE" "$DEST/CLAUDE.md"; then
  printf '\n## Çalışma düzeni\n%s\n' "$LINE" >> "$DEST/CLAUDE.md"
  echo "eklendi: CLAUDE.md çekirdek satırı"
fi

echo "$VERSION" > "$installed"
echo "claude-workflow $VERSION kuruldu: $DEST"
