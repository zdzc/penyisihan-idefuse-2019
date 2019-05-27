# Pembahasan Soal Penyisihan Ideafuse 2019

## Soal A
**Tags**: ad-hoc  
Soal ini bisa disebut soal bonus. Soal ini dikerjakan dengan mengurangkan 100 dengan jumlah dua bilangan input. Jika hasilnya kurang dari sama dengan 0 maka jawabannya adalah 0, selain itu jawabannya adalah hasil pengurangan tersebut.


## Soal B
**Tags**: searching, graph-traversal  
Untuk pendekatan ini mungkin ada kesalahan karena kelompok kami belum sempat menyelesaikan soal ini saat lomba berlangsung. Soal ini dapat diselesaikan dengan *binary search* yang dikombinasikan dengan *breadth-first search*. Pada soal ini didefinisikan jarak sebagai jarak *euclidean*, dimana jarak dapat dihitung sebagai
    
    sqrt((x1-x2)² + (y1-y2)²)

Tetapi untuk soal ini kita diminta hasil kuadrat dari jarak tersebut, sehingga rumus jaraknya menjadi

    (x1-x2)² + (y1-y2)²

Kita dapat mencari radius minimal yang diperlukan dengan *binary search*. Untuk batas bawahnya adalah 1, karena tidak ada tower yang berada di tempat yang sama dan jumlah tower minimal ada 2. Pada soal terdapat *constraint* -1.000.000 <= xi, yi <= 1.000.000. Oleh karena itu batas atasnya adalah jarak terjauh dari 2 titik, yaitu titik di sebelah kiri bawah dan kanan atas. Dengan begitu, jarak terjauhnya adalah

    (-1.000.000 - 1.000.000)² + (-1.000.000 - 1.000.000)²
    = 2 (-2 * 10⁶)²
    = 2 (4 * 10¹²)
    = 8 * 10¹²

Pada setiap tahap binary search, akan dihasilkan nilai tengah *mid*. Nilai *mid* tersebut kita tes dengan *breadth-first search*, apakah dapat mengcover seluruh area. Jika iya, maka jawaban yang optimal lebih kecil sama dengan nilai *mid*. Jika tidak, maka jawaban yang optimal lebih besar dari nilai *mid*. Ulangi proses ini sampai nilai bawah sama dengan nilai atas. Jawaban dari soal ini adalah nilai bawah atau atas. Kompleksitas dari solusi ini adalah O(n² log(I)), dimana n adalah jumlah tower, dan I adalah panjang interval batas bawah dan batas atas.


## Soal C
**Tags**: ad-hoc  
Soal ini sebenarnya mudah, tetapi agak panjang kode yang diperlukan. Pertama-tama kita pisah string menjadi kumpulan karakter-karakter. Pada soal ini 'ng' juga dianggap sebagai sebuah karakter. 

Setelah itu, kita mengecek karakter-karakter tersebut dari kiri sampai kanan. Untuk karakter yang paling kiri, sebelahnya hanya ada di kanan. Untuk karakter yang paling kanan, sebelahnya hanya ada di kiri. Hati-hati dengan string yang hanya memiliki satu karakter, karena karakter tersebut tidak memiliki sebelah. Selain itu, sebuah karakter memiliki dua karakter yang ada di sebelahnya, yaitu di bagian kiri dan kanan.

Apabila ada karakter sebelah yang memiliki tipe yang sama dengan karakter sekarang, maka karakter sekarang akan diubah menjadi huruf besar. Jika tidak, maka karakter akan didiamkan saja.


## Soal D
**Tags**: ad-hoc  
Untuk soal ini sebenarnya mudah, asalkan sudah ketemu aturan untuk meletakkan batunya. Kita lihat status setiap batu dari kiri sampai kanan. Jika batu di petak tersebut dan kanannya hilang, maka kita taruh batu di petak sebelah kanan. Jawaban dari soal ini adalah berapa banyak batu yang diletakkan.


## Soal E
**Tags**: data-structure, min-heap  
Pada soal ini kita disuruh menyimulasi jalan proses di *environment* yang memiliki banyak prosesor. Kita diberikan input berupa jumlah prosesor, dan lama dari setiap proses untuk dikerjakan CPU. Kita hanya diminta untuk menyebutkan waktu yang diperlukan agar semua proses selesai dikerjakan. Aturan no 5 tidak relevan karena kita tidak diharuskan menyebut kapan dan prosesor mana yang mengerjakan proses apa.

Pada pendekatan pertama, kita inisialisasi array sebesar jumlah prosesor. Kita isi array tersebut dengan nilai 0, karena setiap CPU belum menjalankan proses apapun. Untuk setiap proses kita pilih indeks yang memiliki nilai paling kecil, lalu kita tambahkan nilai di indeks tersebut dengan berapa lama proses berjalan. Untuk pendekatan ini kompleksitas waktunya adalah O(N K), dimana N adalah banyaknya prosesor dan K adalah banyaknya proses. Tetapi pendekatan ini tidak cukup, karena *constraint* dari soal ini adalah 1 <= N, K <= 100000.

Struktur data yang dapat mendukung operasi mengambil bilangan terkecil, dan mengubah datanya adalah *priority queue*. *Priority queue* dapat diimplementasikan dengan *heap*. Harga dari operasi mengambil bilangan terkecil adalah O(log n), dan harga dari operasi mengubah key adalah O(log n). Dengan *heap*, kompleksitas waktu dari algoritma ini menjadi O(n log n).

## Soal F
**Tags**: math, geometry  
Kami menyelesaikan soal ini dengan menemukan korelasi input dan output. Untuk jumlah segitiga, hasilnya dapat dihitung dengan:

    input - 2

Dan untuk sisi dapat dihitung dengan:

    2 * (jumlah_segitiga) + 1


## Soal H
**Tags**: math, geometry  
Pada soal ini diberikan titik tengah lingkaran, radius lingkaran, dan kumpulan titik. Tujuan dari soal ini adalah mencari jarak terdekat untuk memindahkan semua titik agar berada di dalam lingkaran. Kita dapat menghitung jarak tersebut dengan menghitung jarak dari titik tersebut ke tepi lingkaran yang terdekat. Cara mencari jarak terdekat dapat dilihat di link [berikut](https://www.varsitytutors.com/hotmath/hotmath_help/topics/shortest-distance-between-a-point-and-a-circle). Untuk rumus yang ada di link sebelumnya, hasil akhirnya tidak perlu di absolutkan.

Jika jarak tersebut negatif berarti titik tersebut berada di dalam lingkaran, sehingga kita abaikan saja. Jika jaraknya positif, kita tambahkan jarak tersebut ke total jaraknya.
