# Paket NNN: <kısa ad>

- **Agent:** <implementer | scout | test-runner | researcher | cleanup | reviewer>  (model/çaba farklıysa nedeni)
- **Başlangıç commit'i:** `<hash>` (dal `<ad>`); işe başlamadan `git log -1` ile doğrula, farklıysa bu commit'e geç.
  Paket metni çağrı mesajında verilir; dosyası (`work/packages/`) yalnız orkestratörde durur.
- **Hedef:** <ne elde edilecek, kim için; uygulama ayrıntısı değil sonuç>

## Bilgiler
<Paketi yapmak için gereken gerçekler: ilgili dosyalar, mevcut API, sözlük/kurallar, önceki kararlar. Okunacak
dosyaları ve satır aralıklarını adıyla ver; ajan bunların dışını okumak zorunda kalmasın.>

## Sahiplik
- Değiştirebileceğin dosyalar: <liste>
- Dokunmayacağın: <liste / "geri kalan her şey">
- Hazır kullanılacak arayüzler: <liste>

## Nasıl değerlendirilecek
- Kapı: `<komut>` » beklenen çıktı `<...>`
- Ek ölçüt: <ör. "çevrilmemiş metin 0", "denge raporu ±2 puan içinde">

## Durma koşulları
Paketin dışında bir dosya, bir tasarım/arayüz kararı ya da cevaplanmamış bir soru gerekirse dur ve `blocked` dön.
Kapı iki denemede yeşile dönmezse dur ve çıktıyı aynen getir.

## Bitirme
Commit'le (push etme), mesaj: `<önek>: <özet>` + projenin atıf satırları. Geri dönüşü
`.claude/workflow/templates/handback.md` biçiminde yalnız son mesajına yaz; orkestratör onu bu dosyanın sonuna ekler.
