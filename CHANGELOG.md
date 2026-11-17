# Değişiklik günlüğü

Yalnız eklenir; yeni kayıt en üstte.

## 0.3.3 — 2026-11-18
Kaynak: 0.4.0'ın "yalnız Khan Borg'da kalan iyileştirmeler" maddesi (Khan Borg kuralları 2026-10-22 ve 2026-10-25, iş tahtası 2026-10-25).
Ozan onayı: "üçü de olsun, Bekleyen uygun" (2026-11-18).
- `CORE.md` kural 10: panoya, `resume.md`'ye ve `handout.md`'ye yazılan olgunun yanında kanıtı durur; kanıtsız olan "tahmin, doğrulanmadı".
- `process.md`: şişen pano satırı `- Alt görevler:` altında `- [ ] metin · Yapan: <kim, model>` satırlarına bölünür; biten alt görevde Yapan
  zorunlu, commit'te `Uygulayıcı:` satırı.
- Yeni `tools/pano_sayfa.py` + `pano_sayfa.html` (iş tahtası): bir ya da birkaç reponun panosunu ve bekleyen kararlarını tek HTML sayfada
  gösterir; repolar argümanla verilir, `--baslik` sayfa adı. `install.sh` `tools/`'u `.claude/workflow/tools/`'a kurar (manifestte).
  Sınama: `python tests/pano_sayfa_test.py`. Panoda `## Bekleyen` ve `## Fikirler` bölümleri tanınır.
- Geçiş: `install.sh --upgrade`. Projede kendi kopyası olan tahta varsa silinir, komut yeni yola çevrilir; tahtanın tanımadığı kullanıcıyı
  bekleyen bölüm `## Bekleyen` diye yeniden adlandırılır (tanınmayan bölümün kartları sayfaya girmez). Proje CLAUDE.md'sindeki aynı
  kurallar (olgu kanıtla, alt görev + Yapan) çift olur, silinir.

## 0.3.2 — 2026-11-18
Kaynak: şablon herkese açık; kuran herkese "Ozan" diyordu. Ozan onayı: "kullanıcı kelimesi olsun, ad sorulmasın" (2026-11-17), uygulama
biçimi ve bu kaydın bitti ölçütü onaylı (2026-11-18). 0.3.0'daki "şablon 'Ozan' der" kaydının yerini alır.
- Kurulan dosyalarda (`core/`, `agents/`, `skeleton/`) hitap "kullanıcı"; `install.sh` ad sormaz, değişmedi. Acil girdi işareti
  **KULLANICI GİRDİSİ GEREKLİ**.
- `model-classes.md`'deki tarihli onaylarda ad düştü; tarih ve alıntı kaldı.
- `CORE.md` taş kuralında oyunun ya da ürünün kullanıcısı "son kullanıcı" oldu (hitapla karışmasın diye).
- Geçiş: `install.sh --upgrade`. İskelet dosyaları güncellenmez: var olan projelerde `owner/` başlıklarındaki ad ve
  `owner/decisions.md`'deki eski acil girdi işareti elle değiştirilebilir (isteğe bağlı; KhanBorg ve design-desk'te işareti okuyan betik yok).

## 0.3.1 — 2026-11-17
Kaynak: Khan Borg hata kaydı ve 2026-11-15 süreç incelemesi. Metni yazılı dört ayrı kural çiğnendi: betik hatasını yakalama koşulu
kuralda vardı, kapıda yoktu; git dışında kalması gereken dosyalar depoya girdi; `resume.md` kısa tutma kuralına rağmen şişti; iş tahtası
"her adımda yenile" yazılıyken yenilenmedi. Matt Pocock `retro` skill'inin kuralıyla aynı yöne varıyor (MIT). Ozan onayı.
- İskelet: yeni `work/hatalar.md` (satır biçimi + `process.md`'ye işaret; kural metni yalnız `process.md`'de).
- `process.md`: `hatalar.md` dosya listesinde; yeni "Hata kaydı" bölümü: sabit desenli ihlal ilk görüldüğünde kapıya ya da kancaya
  bağlanır, kural metni yargı isteyen hataya kalır; kapıya eklenen denetim bilerek bozulmuş girdide kırmızı verdiği görülerek gelir.
- Geçiş: `install.sh --upgrade` eksikse `work/hatalar.md`'yi ekler, var olan hata kaydına dokunmaz. Projede zaten bir hata kaydı varsa
  başlığındaki önlem kuralı elle `process.md` "Hata kaydı"na işaretle değiştirilir (ör. "ikinci kez görülen önlem kurala taşınır" satırı).

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
