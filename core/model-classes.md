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
| Mimari, tasarım, ürün kararı önerisi, karar turu, birleştirme, son söz | Orkestratör (Opus) | yüksek | — |

Gözden geçirici, işi yazandan düşük sınıfta olmamalı: Sonnet'in yazdığını Sonnet ya da Opus, orkestratörün kendi
yazdığını (altyapı, tasarım) Opus gözden geçirir. `effort` desteklemeyen modelde alan yok sayılır.

**Gözden geçirmede Opus'a çıkma koşulları** (Ozan onayı 2026-10-03; ilk optimizasyon turunda ölçüldü, 2026-10-04 güncellendi):
tasarım aşaması geçişi; mimari, veri biçimi ya da genel arayüz değişikliği; güvenlik yüzeyi (kimlik, gizli bilgi,
dış girdi); kilometre taşı sonu gözden geçirmesi; Sonnet gözden geçiricinin "emin değilim" ya da çelişkili bulgu demesi.

**Yükseltme mekaniktir:** ekip üyesi şu durumlardan birinde işi durdurur ve `blocked` döner: paketin yazmadığı bir
dosyayı değiştirmesi gerekirse; genel arayüz, veri biçimi ya da tasarım kararı gerekirse; paketin cevaplamadığı bir
soru çıkarsa; kapı iki denemede yeşile dönmezse.

**Doğrulama turları Sonnet'te** (Ozan onayı 2026-10-04, koşullu: "Sonnet Opus kadar faydalıysa"): yukarıdaki koşullardan biri için yapılan
**ilk** gözden geçirme Opus'tur; aynı değişikliğin düzeltmelerini kontrol eden doğrulama turları Sonnet'le (yüksek çaba) yapılır. Sonnet
"emin değilim", çelişkili bulgu ya da tasarım düzeyinde sorun derse Opus'a çıkılır. Ölçüm: ayrı Sonnet–Opus karşılaştırma koşusu yapılmaz (Ozan, 2026-10-04: yayımlanmış
5.5 karşılaştırmaları yeterli; kod incelemesinde Sonnet daha az bulur ve daha gürültülü, dar doğrulamada kabul edilebilir); panonun ilgili Bitti satırında Sonnet doğrulamasının kaçırdığı ve sonradan bulunan her
sorun "kaçırılan" diye yazılır. Kaçırılan önemli bulgu çıkarsa doğrulama yeniden Opus'a döner.

**Bütçe kontrolü (Ozan, 2026-10-15: "token kritik kaynak, limitli hesaplar").** Her dağıtımdan önce Claude için `get_usage` (5 saat + haftalık).
Claude haftalık %80'i geçtiyse alt agent çağrılmaz; orkestratör büyük dosya/rapor okumaz, özetini ister. Araştırma paketleri dar tutulur
(tek bir geniş araştırma yüz binlerce token yiyebilir): soru sayısı ve okunacak dosya sınırlanır.
