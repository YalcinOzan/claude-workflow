# Değişiklik günlüğü

Yalnız eklenir; yeni kayıt en üstte.

## 0.3.0 — 2026-10-21
Kaynak: Khan Borg işletim şeması gözden geçirmesi (taş arası sunum panodan tetiklenmiyordu; iki repoya dokunan iş iki panoda çift satır
olup birinde kanıtsız kaldı) ve KhanBorg'u şablona eşitleme. Ozan onayı.
- Hitap: şablon kullanıcıya "sahip" demez, "Ozan" der (Ozan, 2026-10-15). `owner/` klasör adı ve dosya sahipliği anlamı değişmedi.
- Çekirdek: **taş kuralı** (taş arası ve büyük tasarım değişikliğinde sunum + onay); kural 10'a panonun başında **Şu anki taş**; yeni kural 11
  **iki repoya dokunan iş tek satır**; kural 1 kısa tutma.
- KhanBorg'da olgunlaşan genel kurallar: gözden geçirmenin düzeltme turları Sonnet'te, bütçe kontrolü (haftalık %80), implementer/reviewer
  git güvenliği, reviewer referans adımında kaynak `dosya::fonksiyon` + karar kaydında gerekçe, kota kaydı `get_usage`.
- İskelet: `board.md` başında "Şu anki taş", `resume.md` taş satırı.
- Geçiş: `install.sh --upgrade`; `work/board.md`'nin başına "## Şu anki taş" bölümü ve `resume.md`'ye taş satırı elle eklenir.

## 0.2.0 — 2026-10-21
Kaynak: Khan Borg süreç denetimi (pano bayatlamıştı, bilgi 9 yerdeydi, ölçütü tutmayan iş "bitti" sayılabiliyordu). Sahip onayı.
- Çekirdek kural 10: pano tek iş listesi; bitti ölçütü önceden, Bitti yalnız kanıtla, tutmayan iş Açık'ta; yan yollar Sonra'ya, sahip onayı
  olmadan geçilmez; sohbetteki fikir aynı turda panoya; `reviewer` ölçütleri tek tek denetler.
- `process.md`: her bilginin tek yeri; `handout.md` "nasıl" el kitabı; kota kaydı panoda (`timelog.md` kalktı); döngü adımı 6 pano ölçütüne bağlı.
- `reviewer`: ölçüt tablosu; projede referans kuralı varsa uyarlama denetimi.
- İskelet: yeni `board.md` bölümleri, kısa `resume.md`, yeni `handout.md`, `cleanup.md` kota satırı; `timelog.md` kalktı.
- Geçiş (0.1.x kurulu projeler): `install.sh --upgrade`; iskelet dosyaları güncellenmez: `work/board.md` bölümleri ve `work/handout.md` elle
  eklenir, `work/timelog.md` arşive. Projede elle değiştirilmiş CORE/agent dosyaları `.bak-<zaman>` olarak yedeklenir: projeye özgü kurallar
  önce projenin CLAUDE.md'sine taşınmalı.

## 0.1.3 — 2026-10-03
- Çekirdek kural 9: her kilometre taşı sahibe kullanılabilir bir build bırakır (temiz kopya, duman testi); sahip
  gözden geçirirken iş durmaz. Kaynak: Khan Borg'da test sürücüsünün yayın build'ine sızması (sahip build'i oynayamadı).

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
