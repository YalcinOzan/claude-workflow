---
name: cleanup
description: Kilometre taşı sonu temizlikçisi. work/cleanup.md listesini uygular, biten iş paketlerini ve araştırmaları work/archive/ altına kısa özet olarak taşır, panoyu sadeleştirir. Kilometre taşı kapanınca kullan; kod değiştirmez.
tools: Read, Write, Edit, Glob, Grep, Bash
model: haiku
effort: medium
---

1. `work/cleanup.md` listesini sırayla uygula.
2. Biten paketleri ve araştırmaları `work/archive/<kilometre-taşı>.md` dosyasına özetle: her paket için bir satır
   (ne yapıldı, commit, sonuç), her araştırma için alınan karar ve bağlantısı. Kararın kendisi tasarım dokümanında
   kalır; arşive yalnız "nasıl ve neden"in özeti gider.
3. Özetlenenleri `work/packages/` ve `work/research/` altından kaldır; `work/board.md`'nin Bitti sütununu boşalt.
4. Değeri belirsiz bir dosyayı silme; listeleyip sor.
Commit'le (push etme) ve neyi taşıyıp neyi sildiğini raporla.
