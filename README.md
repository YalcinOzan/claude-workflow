# claude-workflow

Projeler arası Claude Code çalışma düzeni. Sahip (kullanıcı) kapsamı ve kararları verir; ana oturum orkestratördür;
işi, aynı kalitede yapabilecek en ucuz modele sabitlenmiş alt agent'lar yapar. Bütün durum repoda, dosyalarda durur.

## İçerik
- `core/CORE.md` — her oturumda okunan kısa çekirdek (projenin CLAUDE.md'si `@.claude/workflow/CORE.md` ile içe aktarır)
- `core/process.md` — döngü, dosyalar, paralel çalışma, periyodik turlar, şablona geri taşıma
- `core/model-classes.md` — hangi iş hangi model ve çabada, yükseltme kuralları
- `templates/` — iş paketi ve geri dönüş biçimi
- `agents/` — reviewer, implementer, test-runner, scout, researcher, cleanup
- `skeleton/` — projeye eklenen `owner/` (sahibin) ve `work/` (orkestratörün) dosyaları

## Kurulum
```sh
git clone https://github.com/YalcinOzan/claude-workflow
./claude-workflow/install.sh /yol/proje            # ilk kurulum
./claude-workflow/install.sh /yol/proje --upgrade  # sürüm güncellemesi
```
Kurulum projenin kodunu, git geçmişini ve CI'ını değiştirmez. `owner/` ve `work/` altındaki mevcut dosyalara dokunmaz;
projede değiştirilmiş bir agent dosyası güncellemede `.bak-<zaman>` olarak yedeklenir.

## Bu repoda çalışmak
Değişiklik önerisi genellikle bir projeden gelir (`core/process.md`, "Şablona geri taşıma"). Her davranış değişikliği
`VERSION` artışı ve `CHANGELOG.md` kaydıyla biter; sahip onaylamadan sürüm çıkmaz.
