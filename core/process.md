# Süreç

## Döngü (her konu, her kilometre taşı)

| Adım | Kim | Çıktı |
|---|---|---|
| 1. Konu seçimi | Kullanıcı | `owner/tasks.md`'ye satır |
| 2. Araştırma + sorular | Orkestratör (geniş tarama ekibe) | `work/research/<konu>/`, sorular `owner/decisions.md`'ye |
| 3. Karar turu | Kullanıcı | `owner/decisions.md`'de cevaplar |
| 4. Tasarım güncellemesi | Orkestratör | Projenin tasarım dokümanı + karar kaydı |
| 5. Önce test, sonra kod | Ekip (iş paketiyle) | Worktree dalı, kapı yeşil |
| 6. Tasarıma ve pano ölçütüne karşı gözden geçirme | `reviewer` | Bulgular + ölçüt tablosu; kritik bulgu ya da tutmayan ölçüt adım 5'e döner |
| 7. Kapı + birleştirme + build | Orkestratör | Ana dala birleşme, build |
| 8. Gözden geçirme ve sürüm | Kullanıcı | `owner/reviews.md` notları » sonraki turun girdisi |

Adım 7'nin build'i kullanıcının gerçekten kullanabileceği haldedir: commit'lenmiş halden temiz bir kopyada alınır (yerel test
araçları, sürücüler, commit'lenmemiş değişiklik girmez), duman testinden geçer (açılır, hata vermez). Projenin build
betiği bu adımları tek komutta yapar. Kullanıcı build'i gözden geçirirken orkestratör beklemez, sıradaki işe geçer.

Küçük iş döngüyü kısaltır (soru gerektirmeyen düzeltme adım 2–4'ü atlar), ama adım 6–7 atlanmaz.
Kullanıcıya dönen her şey ya `owner/decisions.md`'de bir soru ya da `owner/reviews.md`'de gözden geçirilecek bir build'dir;
acil girdi gerekiyorsa başına **KULLANICI GİRDİSİ GEREKLİ** yazılır.

## Dosyalar

`owner/` (kullanıcının): `tasks.md`, `decisions.md`, `reviews.md`.

`work/` (orkestratörün):
Her bilginin tek yeri: pano = ne yapılıyor / ne bitti; karar kaydı = kesinleşen karar ve neden; `owner/decisions.md` = yalnız kullanıcının
cevabını bekleyen; `owner/reviews.md` = kullanıcının build notları; `owner/tasks.md` = kullanıcının gelen kutusu.
- `resume.md` — oturum girişi, ~10 satır: durum, panoya işaret, kalıcı kurallar. Her adımda üzerine yazılır.
- `handout.md` — "nasıl" el kitabı: kapı ve build komutları, bağlar, tuzaklar, bilinen notlar, Sürüyor işin ayrıntılı planı.
  Biten işlerin hikâyesi buraya yazılmaz (git + karar kaydı).
- `board.md` — tek iş listesi (CORE kural 10): Şu anki taş (ad, satırlar, taşın bitti ölçütü) / Sürüyor (en fazla 1) / Yapılacak / Açık (ölçütü tutmadı) / Sonra (yan yollar, kullanıcı onayı
  bekler) / Gözden geçirmede / Bitti (kanıtlı). Her satırda amaç ve önceden yazılmış bitti ölçütü; Bitti'de kanıt (commit, kapı, ölçüm).
  Üç ve daha çok adımlı satır pano satırı çoğaltmadan kendi altında `- Alt görevler:` ve `- [ ] metin · Yapan: <kim, model>` satırlarına
  bölünür. Biten alt görevde Yapan zorunlu: ana oturumun modeli, alt agent adı ve modeli, başka araç kullanıldıysa aracı, modeli ve çabası;
  commit mesajında aynı bilgi `Uygulayıcı:` satırıyla. İş tahtası alt görevi bu biçimden okur.
- `packages/` — iş paketleri (`.claude/workflow/templates/work-package.md`), dosya adı `NNN-kisa-ad.md`. Paket metni
  agent çağrısında verilir; geri dönüşü orkestratör aynı dosyanın sonuna ekler.
- `research/<konu>/` — araştırma notları.
- `inbox/` — başka projeden devredilen iş; gelen her öğe bir araştırma + karar turu başlatır.
- `cleanup.md` — kilometre taşı sonu kontrol listesi.
- `hatalar.md` — hata kaydı, her hata bir satır (aşağıda "Hata kaydı"). Kalıcı araç tuzağı `handout.md`'dedir.
- `archive/` — biten kilometre taşlarının özetleri (paketler ve araştırma buraya özetlenip silinir).

Tasarım dokümanı ve karar kaydı projenin kendi yerindedir (projenin CLAUDE.md'si yerlerini yazar); `work/resume.md`
bunlara bağlantı verir.

İş tahtası (isteğe bağlı görünüm): `python .claude/workflow/tools/pano_sayfa.py <çıktı.html> <repo>[=<Ad>[=<Etiket>]] ...`
bir ya da birkaç reponun panosunu ve `owner/decisions.md` Bekleyen'ini tek HTML sayfada gösterir. Kaynak md'dir, sayfa elle düzenlenmez.
İskeletin bölümlerine ek olarak `## Fikirler` ve `## Bekleyen` (kullanıcıyı bekleyen iş) tanınır; başka adlı bölüm sayfaya girmez.

## Hata kaydı
Yakalanan her hata aynı turda `work/hatalar.md`'ye bir satır olur: tarih · ne oldu · ne yakaladı · önlem.
**Sabit desenli ihlal kural metnine değil denetime bağlanır.** Bir dosyanın yanlış yere girmesi, yasak komut ya da API, unutulan yer
tutucu gibi makinenin görebileceği ihlal ilk görüldüğünde projenin kapısına ya da bir kancaya denetim olarak eklenir; satır denetimin
yerini yazar. Kural metni hatırlanmayı bekler, kapı beklemez. Kural metni yalnız yargı isteyen hataya kalır: aynı tür ikinci kez
yazılıyorsa önlem projenin CLAUDE.md'sine ya da teste taşınır. Kapıya eklenen denetim kapının kendi sınamasıyla gelir (bilerek bozulmuş
girdide kırmızı verdiği görülür).

## Paralel çalışma
- En fazla 4 ekip üyesi aynı anda; her biri kendi worktree'sinde (`implementer` tanımında sabit; başka agent
  dosya değiştirecekse çağrıda `isolation: worktree` verilir). İstisna: `cleanup` orkestratörün dalında çalışır.
- Paket **başlangıç commit'ini** yazar; ekip işe başlamadan `git log -1` ile doğrular, farklıysa o commit'e geçer.
- Paylaşılan dosyalar (ortak tablo, test dosyası) paketlerde sahiplenilir; ortak arayüz gerekiyorsa orkestratör onu
  paketlerden **önce** kurar ve commit'ler.
- Birleştirme sırası: bağımlılığı az olan önce; her birleştirmeden sonra kapı.

## Periyodik turlar
- **Kota kaydı:** taş sonunda kullanım ölçümü (`get_usage`) panonun Bitti satırına tek satır.
- **Optimizasyon turu** (her 3–4 kilometre taşında): panodaki kota satırları, geri dönüşler ve sohbet üzerinden "neyi
  daha az token, zaman ya da G/Ç ile, kaliteyi düşürmeden yapabilirdik?" araştırması. Öneriler karar turuna gider;
  genellenebilen değişiklik şablona taşınır.
- **Model karşılaştırma turu** (yeni model çıkınca): aynı birkaç iş paketi farklı model ve çaba seviyelerinde yaptırılır,
  kapı sonucu, gözden geçirme bulgusu ve token karşılaştırılır; `model-classes.md` tablosu güncellenir.

## Şablona geri taşıma
Bir projede yapılan süreç değişikliği genellenebiliyorsa orkestratör şablon reposuna öneri olarak yazar
(`CHANGELOG.md`'ye taslak + değişiklik). İskelet dosyalarındaki (`owner/`, `work/`) değişiklikler güncellemeyle mevcut
projelere taşınmaz; gerekiyorsa CHANGELOG kaydı elle geçiş adımını yazar. Diğer projelerde bozmayacağı kontrol edilir; kullanıcı onaylarsa sürüm artar,
projeler `install.sh --upgrade` ile güncellenir.
