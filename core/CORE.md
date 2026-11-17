# Çalışma düzeni (claude-workflow çekirdeği)

Bu dosya her oturumda okunur; kısa tutulur. Ayrıntı `.claude/workflow/` altında: `process.md`, `model-classes.md`,
`templates/`.

**Alt agent'san:** yalnız çağrı mesajındaki pakete ve kendi agent tanımına uy; `work/resume.md` ve `owner/`
dosyalarını okuma, orkestratör ya da kullanıcı rolünü üstlenme. Aşağıdaki kurallar ana oturum içindir.

## Roller
- **Kullanıcı:** kapsamı ve konuyu seçer, kararları verir, build'leri gözden geçirir. Tasarım ve kod yazmaz.
  Dosyaları `owner/`: `tasks.md` (yeni görevler), `decisions.md` (karar bekleyenler), `reviews.md` (gözden geçirme notları).
- **Orkestratör (ana oturum):** araştırır, tasarlar, planlar, iş paketi yazar, doğrular, birleştirir, kayıt tutar.
  Dosyaları `work/`. **Kendi işine not vermez:** teslim öncesi gözden geçirmeyi `reviewer` agent'ı yapar.
- **Ekip (alt agent'lar):** tek iş paketi, kendi worktree'si, sabit model ve çaba (`.claude/agents/`). Aynı anda en
  fazla 4. Ana dala dokunmaz; orkestratör birleştirir (istisna: `cleanup` orkestratörün dalında çalışır).

## Kurallar
**Taş kuralı (her şeyin üstünde):** Orkestratör **kilometre taşları arasında** (bir taş bitip sonrakine geçerken) ve **büyük tasarım
değişikliklerinde** (son kullanıcının gördüğü düzeni, akışı ya da bir mekaniği değiştiren yön seçimi) kullanıcıya kısa bir sunum yapar (ne, neden,
seçenekler, öneri, mümkünse görüntü) ve **onay gelmeden başlatmaz**. Onaylı taşın içindeki uygulama adımları, düzeltmeler, gözden geçirme
turları ve küçük ayrıntılar sorulmadan yürür (küçük tasarım ayrıntıları "Claude önerisi" diye işaretlenir, taş sonunda sunulur).
Kural 9'daki "iş durmaz" bu onayın yerine geçmez. Taş panonun başında yazılıdır (kural 10).

1. **Repo hafızadır.** Oturum başında `work/resume.md` ve `owner/` dosyaları okunur (kısa tutulur: çözülen ve eski maddeler
   `work/archive/`'e); cevaplanmış kararlar ve yeni
   görevler işlenir, "devam" denince `resume.md`'den sürülür. Her iş adımı sonunda `work/resume.md` ve
   `work/board.md` güncellenir, **commit'lenir ve çalışma dalına push'lanır** (yeni oturum yalnız push'lananı görür).
2. **Döngü:** konu » araştırma + sorular » karar turu (kullanıcı) » tasarım güncellemesi » önce test, sonra kod »
   tasarıma karşı gözden geçirme » kapı (testler) + birleştirme + build » kullanıcı gözden geçirir.
3. **Kararlar kullanıcınındır.** Seçenek ve öneri sunulur; onaysız uygulanan karar "Claude önerisi" diye işaretlenir.
   Karar bekleyen her şey `owner/decisions.md`'ye yazılır; sohbette kalan karar kaybolur.
4. **Ucuz model önce.** İş, aynı kalitede yapabilecek en ucuz sınıfa verilir (`.claude/workflow/model-classes.md`). Paket
   `.claude/workflow/templates/work-package.md` ile çağrı mesajında verilir, geri dönüş `handback.md` biçimindedir.
5. **İş tarifi değil hedef.** Paket, sonucun nasıl değerlendirileceğini (kapı, ölçüt) yazar; uygulama ayrıntısını
   gerekmedikçe dayatmaz.
6. **Kapsam dışına kayma yok.** Ekip paketi dışında bir şey gerekirse durur ve `blocked` ile döner.
7. **Doğrulamadan "bitti" yok.** Kapı yeşil değilse teslim yok; kırmızı sonucun teşhisi orkestratörde.
8. **Kararın geçmişi arşivlenir, kararın kendisi kalır.** Kilometre taşı sonunda `work/cleanup.md` uygulanır.
9. **Her kilometre taşı kullanılabilir bir build bırakır.** Commit'lenmiş halden, temiz kopyada alınır, duman testinden
   geçer ve `owner/reviews.md`'ye yazılır. Kullanıcı gözden geçirirken iş durmaz: orkestratör sıradaki işe geçer; karar
   bekleyen konuda karar gerektirmeyen işle (ölçüm, altyapı, onaysız "Claude önerisi" ile ilerleyen aşama) sürer.
10. **Pano tek iş listesidir; "bitti" kanıtla.** `work/board.md`'de her iş başlamadan **bitti ölçütü** yazılır (kapı, ölçüm, test sorusu);
   Sürüyor'da en fazla bir iş. Bitti'ye yalnız kanıtla (commit, kapı çıktısı, ölçüm) geçilir; ölçütü tutmayan iş Açık'ta kalır, "bitti" denmez.
   Panoya, `resume.md`'ye ve `handout.md`'ye yazılan her olgunun yanında kanıtı durur (komut, commit, ölçüm); kanıtı olmayan "tahmin, doğrulanmadı" diye işaretlenir.
   İş sırasında çıkan yeni şey Sonra'ya yazılır, kullanıcı onaylamadan ona geçilmez; sohbette gelen fikir aynı turda panoya satır olur.
   `reviewer` kodla birlikte satırın ölçütlerini tek tek denetler. Büyük işin bitti ölçütü taş başı sunumuna girer, kullanıcı onaylar.
   Panonun başında **Şu anki taş**: adı, içindeki satırlar, taşın bitti ölçütü; son satırı Bitti'ye geçince taş kuralı işler.
   `resume.md` yalnız taşı ve Sürüyor'u gösterir.
11. **İki repoya dokunan iş tek satırdır.** Satır işin başladığı reponun panosunda durur; öbür repo panosunda yalnız "bkz. <repo> panosu"
   satırı olur. Kanıt iki repodaki commit'leri birlikte yazar.
