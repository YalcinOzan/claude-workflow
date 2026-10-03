# claude-workflow (şablon reposu)

Bu repo projelere kurulan çalışma düzeninin kaynağıdır; kendisi bir proje değildir. Dil Türkçe.
- `core/CORE.md` her projede her oturumda okunur: kısa tut, ayrıntıyı `process.md` / `model-classes.md`'ye koy.
- Her davranış değişikliği: `VERSION` artışı + `CHANGELOG.md` kaydı (yalnız eklenir). Sahip onaylamadan sürüm çıkmaz.
- Değişiklik `install.sh`'ı etkiliyorsa geçici bir dizine kurup (`install.sh /tmp/x` ve `--upgrade`) doğrula.
