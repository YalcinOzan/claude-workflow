"""İş tahtası betiğinin sınaması: iskelet panosu ve alt görev biçimi. Kullanım: python tests/pano_sayfa_test.py"""
import json, re, shutil, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.dont_write_bytecode = True  # tools/__pycache__ kurulan dosyalara karışmasın
import pano_sayfa  # noqa: E402

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    # 1) Boş iskelet: tek kart "Taş yok", bekleyen karar yok.
    shutil.copytree(ROOT / "skeleton", d / "bos")
    assert pano_sayfa.main([str(d / "bos.html"), str(d / "bos")]) == {"tas": 1}

    # 2) Alt görev + Yapan biçimi (process.md "board.md" maddesi) ve "Bekleyen" bölümü.
    shutil.copytree(ROOT / "skeleton", d / "dolu")
    board = (d / "dolu/work/board.md").read_text(encoding="utf-8")
    board = board.replace("## Sürüyor\n", "## Sürüyor\n- **Kayıt ekranı**: amaç x · bitti ölçütü y\n  - Alt görevler:\n"
                          "    - [x] Şema · Yapan: implementer (Sonnet)\n    - [ ] Arayüz\n")
    board += "\n## Bekleyen\n- **Renk seçimi**: iki seçenek\n"
    (d / "dolu/work/board.md").write_text(board, encoding="utf-8")
    out = d / "dolu.html"
    assert pano_sayfa.main([str(out), str(d / "dolu") + "=Örnek=Ö"]) == {"tas": 1, "suruyor": 1, "bekleyen": 1}
    data = json.loads(re.search(r"const DATA = (\{.*?\});\n", out.read_text(encoding="utf-8"), re.S).group(1))
    card = next(c for c in data["cards"] if c["col"] == "suruyor")
    assert card["tasks"] == [{"done": True, "text": "Şema", "who": "implementer (Sonnet)"},
                             {"done": False, "text": "Arayüz", "who": ""}], card["tasks"]
    assert data["repos"] == [{"key": "r0", "name": "Örnek", "label": "Ö"}]

    # 3) Biçimi bozuk pano kırmızı verir.
    (d / "dolu/work/board.md").write_text("# Pano\n", encoding="utf-8")
    try:
        pano_sayfa.main([str(out), str(d / "dolu")])
        raise SystemExit("bozuk pano geçti")
    except AssertionError:
        pass
print("pano_sayfa_test: tamam")
