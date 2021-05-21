# Polonom Challenge
Challenge verilmiş olan [sorular](./POLONOM_TEKNOLOJİ_MÜLAKAT_SORULARI_2021.pdf).

## 1. Soru çözümü 2 farklı yöntem ile CmakeLists.txt oluşturulmuştır.
Çözümlerni deneybilmek için GCC/G++ derleyicinin ve cmake kurulu olması lazım.

Hangi çözümü denemek isteseniz cozum_# içinden soru_1 klasör içine CmakeLists.txt dosyayı çıkartmanız lazım.

Terminalden aşakdakı bash komutlarını çalıştırarak çözümleri bakabilirsiniz.

[source,bash]
----
~$ mkdir build
~$ cd build
~$ cmake ..
~$ make
~$ ./added.out
----

## 1. Soru çözümü hız açısından C de yazılmıştır.

Terminalden aşakdakı bash komutlarını çalıştırarak 2. sorunın çözmünü kontrol edilebilir.

[source,bash]
----
~$ gcc find_point.c
~$ ./a.out
----
