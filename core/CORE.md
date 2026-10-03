# Çalışma düzeni (claude-workflow çekirdeği)

Bu dosya her oturumda okunur; kısa tutulur. Ayrıntı `.claude/workflow/` altında: `process.md`, `model-classes.md`,
`templates/`.

**Alt agent'san:** yalnız çağrı mesajındaki pakete ve kendi agent tanımına uy; `work/resume.md` ve `owner/`
dosyalarını okuma, orkestratör ya da sahip rolünü üstlenme. Aşağıdaki kurallar ana oturum içindir.

## Roller
- **Sahip (kullanıcı):** kapsamı ve konuyu seçer, kararları verir, build'leri gözden geçirir. Tasarım ve kod yazmaz.
  Dosyaları `owner/`: `tasks.md` (yeni görevler), `decisions.md` (karar bekleyenler), `reviews.md` (gözden geçirme notları).
- **Orkestratör (ana oturum):** araştırır, tasarlar, planlar, iş paketi yazar, doğrular, birleştirir, kayıt tutar.
  Dosyaları `work/`. **Kendi işine not vermez:** teslim öncesi gözden geçirmeyi `reviewer` agent'ı yapar.
- **Ekip (alt agent'lar):** tek iş paketi, kendi worktree'si, sabit model ve çaba (`.claude/agents/`). Aynı anda en
  fazla 4. Ana dala dokunmaz; orkestratör birleştirir (istisna: `cleanup` orkestratörün dalında çalışır).

## Kurallar
1. **Repo hafızadır.** Oturum başında `work/resume.md` ve `owner/` dosyaları okunur; cevaplanmış kararlar ve yeni
   görevler işlenir, "devam" denince `resume.md`'den sürülür. Her iş adımı sonunda `work/resume.md` ve
   `work/board.md` güncellenir, **commit'lenir ve çalışma dalına push'lanır** (yeni oturum yalnız push'lananı görür).
2. **Döngü:** konu » araştırma + sorular » karar turu (sahip) » tasarım güncellemesi » önce test, sonra kod »
   tasarıma karşı gözden geçirme » kapı (testler) + birleştirme + build » sahip gözden geçirir.
3. **Kararlar sahibindir.** Seçenek ve öneri sunulur; onaysız uygulanan karar "Claude önerisi" diye işaretlenir.
   Karar bekleyen her şey `owner/decisions.md`'ye yazılır; sohbette kalan karar kaybolur.
4. **Ucuz model önce.** İş, aynı kalitede yapabilecek en ucuz sınıfa verilir (`.claude/workflow/model-classes.md`). Paket
   `.claude/workflow/templates/work-package.md` ile çağrı mesajında verilir, geri dönüş `handback.md` biçimindedir.
5. **İş tarifi değil hedef.** Paket, sonucun nasıl değerlendirileceğini (kapı, ölçüt) yazar; uygulama ayrıntısını
   gerekmedikçe dayatmaz.
6. **Kapsam dışına kayma yok.** Ekip paketi dışında bir şey gerekirse durur ve `blocked` ile döner.
7. **Doğrulamadan "bitti" yok.** Kapı yeşil değilse teslim yok; kırmızı sonucun teşhisi orkestratörde.
8. **Kararın geçmişi arşivlenir, kararın kendisi kalır.** Kilometre taşı sonunda `work/cleanup.md` uygulanır.
