# Model sınıfları

İş, aynı kalitede yapabilecek en ucuz sınıfa verilir. Sınıf ve çaba agent tanımında sabittir (`model:`, `effort:`);
pakette farklısı seçilirse nedeni pakete yazılır.

| İş türü | Sınıf | Çaba | Üst sınıfa çıkar, eğer |
|---|---|---|---|
| Salt okunur tarama, dosya bulma, rapor özeti (`scout`) | Haiku | düşük | taramanın kendisi karar vermek zorundaysa |
| Kapı koşturma: testler, lint, build, simülasyon (`test-runner`) | Haiku | düşük | sonuç kırmızıysa: teşhis orkestratörde |
| Tanımı net toplu dönüşüm, mekanik kod, test yazımı (`implementer`) | Sonnet | orta | paket bir tasarım seçimi gerektirirse: dur, `blocked` |
| Web/kütüphane araştırması (`researcher`) | Sonnet | orta | — (taslağı orkestratör son haline getirir) |
| Kilometre taşı sonu temizlik ve arşiv özeti (`cleanup`) | Haiku | orta | silinecek şeyin değeri belirsizse: sor |
| Diff gözden geçirme (`reviewer`) | Sonnet | yüksek | aşağıdaki koşullardan biri: Opus |
| Mimari, tasarım, oyun/ürün kararı önerisi, karar turu, birleştirme, son söz | Orkestratör (Opus) | yüksek | — |

**Gözden geçirmede Opus'a çıkma koşulları** (Claude önerisi, ilk optimizasyon turunda ölçülecek):
tasarım aşaması geçişi; mimari, veri biçimi ya da genel arayüz değişikliği; güvenlik yüzeyi (kimlik, gizli bilgi,
dış girdi); kilometre taşı sonu gözden geçirmesi; Sonnet gözden geçiricinin "emin değilim" ya da çelişkili bulgu demesi.

**Yükseltme mekaniktir:** ekip üyesi şu durumlardan birinde işi durdurur ve `blocked` döner: paketin yazmadığı bir
dosyayı değiştirmesi gerekirse; genel arayüz, veri biçimi ya da tasarım kararı gerekirse; paketin cevaplamadığı bir
soru çıkarsa; kapı iki denemede yeşile dönmezse.
