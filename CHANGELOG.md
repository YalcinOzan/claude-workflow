# Değişiklik günlüğü

Yalnız eklenir; yeni kayıt en üstte.

## 0.1.2 — 2026-10-03
- Gözden geçirici modeli (varsayılan Sonnet/yüksek, belirli koşullarda Opus) sahip tarafından onaylandı.

## 0.1.1 — 2026-10-03
Bağımsız gözden geçirme (reviewer, Sonnet) bulguları:
- `reviewer` açıklaması geçersiz YAML'dı (değerdeki `: `), düzeltildi.
- Çekirdek: alt agent'lar için kapsam satırı; oturum başında `owner/` da okunur; `resume.md`/`board.md` güncellemesi
  commit + push ile biter; yollar `.claude/workflow/` önekiyle.
- İş paketi çağrı mesajında verilir, dosyası orkestratörde durur; geri dönüş yalnız son mesajda (başlangıç commit'i
  ile paket dosyası arasındaki döngü ve birleştirme çakışması kalktı).
- `implementer` `isolation: worktree` ile sabit; aksi yazılmadıkça önce test. `cleanup` orkestratörün dalında çalışır,
  temizlik listesinde her maddenin sahibi yazılı.
- Gözden geçirici yazandan düşük sınıfta olmaz (orkestratörün kendi işi Opus'a).
- `resume.md` iskeletine çalışma dalı, kapı komutu, ortam/ön koşul alanları.
- `install.sh`: argüman doğrulama, sürüm düşürmeyi reddetme, manifestle yalnız elle değiştirilmiş dosyaları yedekleme,
  `.gitignore`'a `.claude/worktrees/`, CLAUDE.md satırı tam satır kontrolü.
- Geçiş (0.1.0 kurulu projeler): `install.sh --upgrade`; `work/resume.md`'ye yeni alanlar elle eklenir.

## 0.1.0 — 2026-10-03
- İlk sürüm: çekirdek kurallar (`core/CORE.md`), süreç (`core/process.md`), model sınıfları (`core/model-classes.md`),
  iş paketi ve geri dönüş şablonları, altı genel agent (reviewer, implementer, test-runner, scout, researcher,
  cleanup), `owner/` ve `work/` iskeleti, `install.sh`.
- Kaynaklar: CYPRESS (model sınıfları, yükseltme kuralları, geri dönüş sözleşmesi), r/ClaudeCode "My workflow as
  product and process owner" (repo hafızadır, sahip/orkestratör dosya ayrımı, döngü, devam dosyası, periyodik
  optimizasyon ve model karşılaştırma turları, şablona geri taşıma), Khan Borg yerelleştirme turu (paket başlangıç
  commit'ini yazar ve doğrulatır).
- Claude önerisi: gözden geçirici varsayılan Sonnet/yüksek, belirli koşullarda Opus.
