# Süreç

## Döngü (her konu, her kilometre taşı)

| Adım | Kim | Çıktı |
|---|---|---|
| 1. Konu seçimi | Sahip | `owner/tasks.md`'ye satır |
| 2. Araştırma + sorular | Orkestratör (geniş tarama ekibe) | `work/research/<konu>/`, sorular `owner/decisions.md`'ye |
| 3. Karar turu | Sahip | `owner/decisions.md`'de cevaplar |
| 4. Tasarım güncellemesi | Orkestratör | Projenin tasarım dokümanı + karar kaydı |
| 5. Önce test, sonra kod | Ekip (iş paketiyle) | Worktree dalı, kapı yeşil |
| 6. Tasarıma karşı gözden geçirme | `reviewer` | Bulgular; kritik bulgu adım 5'e döner |
| 7. Kapı + birleştirme + build | Orkestratör | Ana dala birleşme, build |
| 8. Gözden geçirme ve sürüm | Sahip | `owner/reviews.md` notları » sonraki turun girdisi |

Adım 7'nin build'i sahibin gerçekten kullanabileceği haldedir: commit'lenmiş halden temiz bir kopyada alınır (yerel test
araçları, sürücüler, commit'lenmemiş değişiklik girmez), duman testinden geçer (açılır, hata vermez). Projenin build
betiği bu adımları tek komutta yapar. Sahip build'i gözden geçirirken orkestratör beklemez, sıradaki işe geçer.

Küçük iş döngüyü kısaltır (soru gerektirmeyen düzeltme adım 2–4'ü atlar), ama adım 6–7 atlanmaz.
Sahibe dönen her şey ya `owner/decisions.md`'de bir soru ya da `owner/reviews.md`'de gözden geçirilecek bir build'dir;
acil girdi gerekiyorsa başına **SAHİP GİRDİSİ GEREKLİ** yazılır.

## Dosyalar

`owner/` (sahibin): `tasks.md`, `decisions.md`, `reviews.md`.

`work/` (orkestratörün):
- `resume.md` — yeni oturumun kaldığı yerden sürmesi için: şu anki konu, son durum, sıradaki adım, açık sorular,
  aktif dallar/worktree'ler. Kısa; her adımda üzerine yazılır.
- `board.md` — kanban: Yapılacak / Sürüyor / Gözden geçirmede / Bitti (bu kilometre taşı).
- `packages/` — iş paketleri (`.claude/workflow/templates/work-package.md`), dosya adı `NNN-kisa-ad.md`. Paket metni
  agent çağrısında verilir; geri dönüşü orkestratör aynı dosyanın sonuna ekler.
- `research/<konu>/` — araştırma notları.
- `inbox/` — başka projeden devredilen iş; gelen her öğe bir araştırma + karar turu başlatır.
- `cleanup.md` — kilometre taşı sonu kontrol listesi.
- `archive/` — biten kilometre taşlarının özetleri (paketler ve araştırma buraya özetlenip silinir).
- `timelog.md` — kilometre taşı başına gerçek süre, agent sayısı, yaklaşık token.

Tasarım dokümanı ve karar kaydı projenin kendi yerindedir (projenin CLAUDE.md'si yerlerini yazar); `work/resume.md`
bunlara bağlantı verir.

## Paralel çalışma
- En fazla 4 ekip üyesi aynı anda; her biri kendi worktree'sinde (`implementer` tanımında sabit; başka agent
  dosya değiştirecekse çağrıda `isolation: worktree` verilir). İstisna: `cleanup` orkestratörün dalında çalışır.
- Paket **başlangıç commit'ini** yazar; ekip işe başlamadan `git log -1` ile doğrular, farklıysa o commit'e geçer.
- Paylaşılan dosyalar (ortak tablo, test dosyası) paketlerde sahiplenilir; ortak arayüz gerekiyorsa orkestratör onu
  paketlerden **önce** kurar ve commit'ler.
- Birleştirme sırası: bağımlılığı az olan önce; her birleştirmeden sonra kapı.

## Periyodik turlar
- **Optimizasyon turu** (her 3–4 kilometre taşında): `work/timelog.md`, geri dönüşler ve sohbet üzerinden "neyi
  daha az token, zaman ya da G/Ç ile, kaliteyi düşürmeden yapabilirdik?" araştırması. Öneriler karar turuna gider;
  genellenebilen değişiklik şablona taşınır.
- **Model karşılaştırma turu** (yeni model çıkınca): aynı birkaç iş paketi farklı model ve çaba seviyelerinde yaptırılır,
  kapı sonucu, gözden geçirme bulgusu ve token karşılaştırılır; `model-classes.md` tablosu güncellenir.

## Şablona geri taşıma
Bir projede yapılan süreç değişikliği genellenebiliyorsa orkestratör şablon reposuna öneri olarak yazar
(`CHANGELOG.md`'ye taslak + değişiklik). İskelet dosyalarındaki (`owner/`, `work/`) değişiklikler güncellemeyle mevcut
projelere taşınmaz; gerekiyorsa CHANGELOG kaydı elle geçiş adımını yazar. Diğer projelerde bozmayacağı kontrol edilir; sahip onaylarsa sürüm artar,
projeler `install.sh --upgrade` ile güncellenir.
