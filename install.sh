#!/usr/bin/env bash
# claude-workflow kurulumu / güncellemesi.
# Kullanım: ./install.sh <proje-dizini> [--upgrade]
#   .claude/workflow/  çekirdek ve şablonlar      } şablonun sahipliği: güncellemede yenilenir; projede elle
#   .claude/agents/    genel agent'lar            } değiştirilmiş dosya önce .bak-<zaman> olarak yedeklenir
#   owner/, work/      iskelet (yalnız eksik dosyalar eklenir, mevcutlara dokunulmaz)
#   CLAUDE.md          çekirdeği içe aktaran satır yoksa eklenir
#   .gitignore         .claude/worktrees/ satırı yoksa eklenir
set -euo pipefail

usage() { echo "Kullanım: install.sh <proje-dizini> [--upgrade]" >&2; exit 2; }
[[ $# -ge 1 && $# -le 2 ]] || usage
MODE="${2:-}"
case "$MODE" in ""|--upgrade) ;; *) usage ;; esac
[[ -d "$1" ]] || { echo "Dizin yok: $1" >&2; exit 2; }

SRC="$(cd -- "$(dirname -- "$0")" && pwd)"
DEST="$(cd -- "$1" && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
VERSION="$(cat "$SRC/VERSION")"
WF="$DEST/.claude/workflow"
MANIFEST="$WF/manifest.sha256"

if [[ -f "$WF/VERSION" ]]; then
  OLD="$(cat "$WF/VERSION")"
  if [[ "$MODE" != "--upgrade" ]]; then
    echo "Zaten kurulu (sürüm $OLD). Güncellemek için --upgrade ver." >&2; exit 1
  fi
  if [[ "$(printf '%s\n%s\n' "$OLD" "$VERSION" | sort -V | tail -1)" != "$VERSION" ]]; then
    echo "Kurulu sürüm ($OLD) bu şablondan ($VERSION) yeni; sürüm düşürülmez." >&2; exit 1
  fi
fi

# Kurulumda yazılan dosyanın son hali manifestte; farklıysa proje elle değiştirmiştir » yedekle.
declare -A known=()
if [[ -f "$MANIFEST" ]]; then
  while read -r sum rel; do known["$rel"]="$sum"; done < "$MANIFEST"
fi
new_manifest=""
place() {  # place <kaynak> <projeye göre hedef>
  local src="$1" rel="$2" t="$DEST/$2"
  mkdir -p "$(dirname "$t")"
  if [[ -f "$t" ]] && ! cmp -s "$src" "$t"; then
    local cur; cur="$(sha256sum "$t" | cut -d' ' -f1)"
    if [[ "${known[$rel]:-}" != "$cur" ]]; then
      cp "$t" "$t.bak-$STAMP"
      echo "yedeklendi (projede değiştirilmiş): $rel.bak-$STAMP"
    fi
  fi
  cp "$src" "$t"
  new_manifest+="$(sha256sum "$t" | cut -d' ' -f1) $rel"$'\n'
}

for f in "$SRC"/core/*.md; do place "$f" ".claude/workflow/$(basename "$f")"; done
for f in "$SRC"/templates/*.md; do place "$f" ".claude/workflow/templates/$(basename "$f")"; done
for f in "$SRC"/agents/*.md; do place "$f" ".claude/agents/$(basename "$f")"; done

# İskelet: yalnız eksik olanlar.
while read -r rel; do
  rel="${rel#./}"
  if [[ ! -e "$DEST/$rel" ]]; then
    mkdir -p "$(dirname "$DEST/$rel")"
    cp "$SRC/skeleton/$rel" "$DEST/$rel"
    echo "eklendi: $rel"
  fi
done < <(cd "$SRC/skeleton" && find . -type f | sort)

# CLAUDE.md çekirdeği içe aktarır (tam satır olarak).
LINE="@.claude/workflow/CORE.md"
if [[ ! -f "$DEST/CLAUDE.md" ]]; then
  printf '# Proje\n\n## Çalışma düzeni\n%s\n' "$LINE" > "$DEST/CLAUDE.md"
  echo "oluşturuldu: CLAUDE.md"
elif ! grep -qxF "$LINE" "$DEST/CLAUDE.md"; then
  printf '\n## Çalışma düzeni\n%s\n' "$LINE" >> "$DEST/CLAUDE.md"
  echo "eklendi: CLAUDE.md çekirdek satırı"
fi

# Agent worktree'leri repoya girmesin.
if ! { [[ -f "$DEST/.gitignore" ]] && grep -qxF ".claude/worktrees/" "$DEST/.gitignore"; }; then
  printf '.claude/worktrees/\n' >> "$DEST/.gitignore"
  echo "eklendi: .gitignore .claude/worktrees/"
fi

printf '%s' "$new_manifest" > "$MANIFEST"
echo "$VERSION" > "$WF/VERSION"
echo "claude-workflow $VERSION kuruldu: $DEST"
