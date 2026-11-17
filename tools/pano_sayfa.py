"""Bir ya da birkaç reponun panosunu (work/board.md) ve bekleyen kararlarını tek Trello tarzı sayfaya çevirir.
Kaynak md'ler; sayfa yalnız görünüm (elle düzenlenmez).
Kullanım: python .claude/workflow/tools/pano_sayfa.py <çıktı.html> <repo>[=<Ad>[=<Etiket>]] ... [--baslik <sayfa başlığı>]"""
import argparse, html, json, re
from datetime import date
from pathlib import Path

# Bölüm başlığının başı » sütun. "Gözden geçirmede", "Bekleyen" ve bekleyen kararlar aynı sütunda: kullanıcıyı bekleyen her şey.
SECTIONS = [("Fikirler", "fikir"), ("Sonra", "sonra"), ("Yapılacak", "yapilacak"), ("Sürüyor", "suruyor"), ("Açık", "acik"),
            ("Bekleyen", "bekleyen"), ("Gözden geçirmede", "bekleyen"), ("Bitti", "bitti"), ("Şu anki taş", "tas")]
BITTI_LIMIT = 6
# Alt görev: "- [ ] metin · Yapan: kim/model"; kartta tıklamadan görünür.
TASK = re.compile(r"^- \[( |x)\] (.*?)(?: · Yapan: (.*))?$")


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(https://[^\s<)]+)", r'<a href="\1" target="_blank" rel="noopener">bağlantıyı aç</a>', t)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)


def split_card(text):
    """İlk **kalın** öbek başlık olur (önündeki tarih korunur); yoksa ilk cümle."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2} )?\*\*(.+?)\*\*:?\s*(.*)$", text, re.S)
    if m:
        return (m.group(1) or "") + m.group(2).rstrip(":"), m.group(3)
    m = re.match(r"^(.{10,90}?)([.:;]\s|$)(.*)$", text, re.S)
    return (m.group(1), m.group(3)) if m else (text[:90], text[90:])


def parse_board(path):
    items, sec, cur = [], None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            sec = next((col for head, col in SECTIONS if line[3:].startswith(head)), None)
            cur = None
        elif sec and line.startswith("- "):
            cur = {"col": sec, "lines": [line[2:]]}
            items.append(cur)
        elif sec and cur and line.startswith("  "):
            cur["lines"].append(line.strip())
    out = []
    for it in items:
        first = it["lines"][0]
        if it["col"] == "tas" and first.startswith("(yok)"):
            first = it["lines"][0] = "**Taş yok** " + first[5:].lstrip(" ·")
        elif first.startswith("(yok)") or first.startswith("bkz. "):
            continue
        head_text = first
        rest = it["lines"][1:]
        # Alt maddeler ("- Amaç: ...") ayrı satır; düz devam satırları ilk satıra eklenir.
        while rest and not rest[0].startswith("- "):
            head_text += " " + rest.pop(0)
        title, body = split_card(head_text)
        tasks = [m for m in map(TASK.match, rest) if m]
        rest = [r for r in rest if not TASK.match(r) and r != "- Alt görevler:"]
        details = ([body] if body.strip() else []) + [r[2:] if r.startswith("- ") else r for r in rest]
        out.append({"col": it["col"], "title": inline(title), "details": [inline(d) for d in details],
                    "tasks": [{"done": m[1] == "x", "text": inline(m[2]), "who": inline(m[3] or "")} for m in tasks]})
    return out


def parse_decisions(path):
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    if "## Bekleyen" not in text:
        return []
    out = []
    for block in re.split(r"\n### ", text.split("## Bekleyen", 1)[1])[1:]:
        head, _, body = block.partition("\n")
        details = []
        for line in body.splitlines():
            line = line.strip()
            if line.startswith("- ") or not details:
                details.append(line[2:] if line.startswith("- ") else line)
            elif line:
                details[-1] += " " + line
        out.append({"col": "bekleyen", "title": inline("Karar " + head.strip()),
                    "details": [inline(d) for d in details if d], "tasks": []})
    return out


def parse_repo(spec, i):
    """"yol=Ad=Etiket"; Ad yoksa klasör adı, Etiket yoksa Ad."""
    path, *rest = spec.split("=")
    root = Path(path).resolve()
    name = rest[0] if rest else root.name
    return {"key": "r%d" % i, "name": name, "label": rest[1] if len(rest) > 1 else name, "root": root}


def collect(repos):
    cards = []
    for r in repos:
        board = r["root"] / "work" / "board.md"
        assert board.exists(), board
        found = parse_board(board)
        # İskeletin boş panosunda da "Şu anki taş" kartı çıkar; çıkmıyorsa biçim okunamadı.
        assert any(c["col"] == "tas" for c in found), "%s: 'Şu anki taş' okunamadı" % board
        for c in found + parse_decisions(r["root"] / "owner" / "decisions.md"):
            c["repo"] = r["key"]
            cards.append(c)
    return cards


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("out")
    ap.add_argument("repos", nargs="+")
    ap.add_argument("--baslik", default="İş Tahtası")
    a = ap.parse_args(argv)
    repos = [parse_repo(s, i) for i, s in enumerate(a.repos)]
    cards = collect(repos)
    page = (Path(__file__).with_name("pano_sayfa.html")).read_text(encoding="utf-8")
    data = json.dumps({"date": date.today().isoformat(), "title": a.baslik, "bitti_limit": BITTI_LIMIT, "cards": cards,
                       "repos": [{k: r[k] for k in ("key", "name", "label")} for r in repos]}, ensure_ascii=False)
    page = page.replace("<title>İş Tahtası</title>", "<title>%s</title>" % html.escape(a.baslik))
    Path(a.out).write_text(page.replace("/*__DATA__*/null", data.replace("</", "<\\/")), encoding="utf-8")
    counts = {}
    for c in cards:
        counts[c["col"]] = counts.get(c["col"], 0) + 1
    print(a.out, counts)
    return counts


if __name__ == "__main__":
    main()
