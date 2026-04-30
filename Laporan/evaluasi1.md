Analisis terhadap proses yang kamu lakukan menunjukkan bahwa model saat ini terjebak di angka **~50%**, yang secara statistik berarti model hanya menebak secara acak (random guessing)[cite: 3]. Hal ini terjadi karena dataset yang digunakan memiliki karakteristik teks yang tampak seperti kata-kata acak (*synthetic/filler text*), sehingga pola bahasa tidak terbentuk[cite: 1, 3].

Berikut adalah analisis mendalam dan solusi teknis untuk mencapai akurasi di atas **80%**:

---

## 1. Analisis Masalah Utama
Berdasarkan data yang kamu lampirkan, ada beberapa *bottleneck* yang menghambat performa:

*   **Kualitas Dataset:** Teks seperti *"more tax development both store agreement..."* tidak memiliki struktur semantik berita nyata[cite: 1]. Jika data ini adalah hasil *generate* acak, model tidak akan pernah belajar pola "hoax".
*   **Representasi Fitur DL yang Keliru:** Pada model CNN dan LSTM, kamu melakukan *reshape* pada vektor rata-rata (mean vector)[cite: 3]. Cara ini menghilangkan informasi urutan kata yang merupakan kekuatan utama Deep Learning.
*   **Vocabulary Terbatas:** Hasil TF-IDF hanya menghasilkan 839 fitur[cite: 2], yang sangat kecil untuk tugas klasifikasi teks kompleks.
*   **Preprocessing Terlalu Agresif:** Menghapus semua angka dan tanda baca terkadang menghilangkan ciri khas berita palsu (misalnya penggunaan tanda seru berlebih atau angka yang tidak masuk akal)[cite: 1].

---

## 2. Solusi Strategis untuk Akurasi >80%

### A. Perbaikan Preprocessing & Feature Engineering
Alih-alih hanya menggunakan kata dasar, tambahkan konteks yang lebih kaya:
*   **N-Gram (TF-IDF):** Gunakan `ngram_range=(1, 2)` atau `(1, 3)` pada `TfidfVectorizer` untuk menangkap frase (misalnya: "pemerintah mengumumkan" vs "pemerintah mengklaim").
*   **Jangan Hapus Semua Karakter:** Simpan tanda tanya (`?`) dan tanda seru (`!`) sebagai fitur, karena berita palsu sering kali bersifat provokatif.
*   **Gunakan Metadata:** Jangan hanya teks. Masukkan kolom `source` dan `category` sebagai fitur tambahan menggunakan *One-Hot Encoding*.

### B. Transformasi Arsitektur Deep Learning (CNN/LSTM)
Untuk mendapatkan hasil terbaik dari LSTM/CNN, jangan gunakan vektor rata-rata. Gunakan **Word Embedding Layer**:
1.  Ubah teks menjadi urutan indeks kata (*sequences*).
2.  Gunakan `pad_sequences` agar panjang input seragam.
3.  Masukkan ke layer `Embedding` (bisa menggunakan pre-trained GloVe/FastText sebagai bobot awal).

### C. Gunakan Model Transformer (Saran Terbaik)
Jika dataset kamu adalah berita nyata, cara tercepat menembus 80-90% adalah menggunakan **Transfer Learning** dengan **BERT** atau **DistilBERT**. Model ini sudah memahami struktur bahasa manusia dengan sangat baik.

---

## 3. Rekomendasi Alur Kerja Baru

| Tahap | Solusi Teknis | Alasan |
| :--- | :--- | :--- |
| **Data** | Pastikan dataset memiliki pola semantik yang valid. | Model tidak bisa belajar dari data acak. |
| **Preprocessing** | Ganti Stemming dengan **Lemmatization**. | Lemmatization menjaga makna kata lebih baik daripada memotong sembarang akhiran. |
| **Model ML** | Gunakan **Random Forest** atau **XGBoost** dengan TF-IDF N-gram. | Algoritma ini sangat tangguh untuk data tabular/vektor. |
| **Model DL** | Gunakan arsitektur: `Embedding` -> `Bidirectional LSTM` -> `Dense`. | Menangkap konteks kata dari dua arah (depan & belakang). |
| **Evaluasi** | Gunakan **Stratified K-Fold Cross Validation**. | Memastikan hasil >80% konsisten dan bukan karena keberuntungan *split* data. |

---