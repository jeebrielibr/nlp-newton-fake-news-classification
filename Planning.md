# Panduan Pembuatan Model Fake News Classification

File ini mendefinisikan panduan langkah demi langkah (pipeline) dan instruksi kerja yang harus dilakukan untuk menyelesaikan proyek klasifikasi berita palsu (Fake News Classification) sesuai dengan spesifikasi di repository ini.

## 1. Persiapan Data (Data Collection)
- **Tujuan:** Mendapatkan dataset yang memadai untuk pelatihan model.
- **Kriteria:** Dataset harus berisi lebih dari **10.000** data.
- **Lokasi Simpan:** Folder `Data/` (jika dataset terlalu besar, simpan tautannya di dalam file text di folder ini).
- **Tindakan:** Load data menggunakan library seperti `pandas` dan lakukan pengecekan awal (missing values, duplikat, dan distribusi kelas Fake/Real).

## 2. Text Preprocessing
- **Tujuan:** Membersihkan teks berita agar dapat diproses oleh algoritma Machine Learning dengan optimal.
- **Langkah Wajib:**
  1. **Case Folding:** Mengubah seluruh teks menjadi huruf kecil (lowercase) dan menghapus karakter khusus/angka.
  2. **Tokenization:** Memecah teks utuh menjadi sekumpulan token (kata).
  3. **Stopword Removal:** Menghapus kata-kata umum yang tidak memberikan konteks signifikan (misalnya: 'dan', 'di', 'ke', 'the', 'is').
  4. **Stemming / Lemmatization:** Mengembalikan kata ke bentuk dasarnya (misalnya: 'berjalan' -> 'jalan'). Gunakan library `Sastrawi` jika berbahasa Indonesia, atau `NLTK`/`Spacy` jika berbahasa Inggris.

## 3. Ekstraksi Fitur (Feature Extraction)
- **Tujuan:** Mengonversi teks yang sudah bersih menjadi vektor angka.
- **Teknik yang Harus Digunakan:**
  - **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - **Word Embedding:** Implementasikan ketiga teknik berikut:
    - Word2Vec
    - GloVe
    - FastText
- **Catatan Eksekusi:** Pastikan proses ekstraksi dilakukan secara terpisah agar performa masing-masing representasi teks dapat dibandingkan.

## 4. Pemodelan (Modeling)
- **Tujuan:** Melatih model klasifikasi untuk membedakan kelas Fake dan Real.
- **Algoritma yang Harus Dilatih:**
  1. LSTM
  2. XGBoost
  3. CNN
- **Catatan Eksekusi:** Lakukan pembagian data (Train-Test Split) yang konsisten (misalnya 80:20) untuk semua model agar perbandingan adil.

## 5. Evaluasi dan Perbandingan Model (Comparison Model)
- **Tujuan:** Menentukan model dan teknik ekstraksi fitur mana yang memberikan kinerja terbaik.
- **Metrik Evaluasi yang Diukur:**
  - Accuracy
  - Precision
  - Recall
  - F1-score
- **Skenario Perbandingan:**
  - Analisis hasil **TF-IDF vs Word Embedding (Word2Vec, GloVe, FastText)** pada masing-masing model.
  - Analisis **Model A vs Model B** untuk mencari algoritma yang paling unggul secara keseluruhan.
- **Tindakan Lanjutan:** Simpan model terbaik ke dalam folder `Model/` dalam format seperti `.pkl` atau `.joblib`.

## 6. Deployment Sederhana
- **Tujuan:** Membuat purwarupa agar pengguna dapat menguji model secara interaktif.
- **Teknologi:** Gunakan framework `Gradio` untuk membuat antarmuka berbasis web sederhana.
- **Cara Kerja:** Antarmuka harus menyediakan textbox di mana pengguna bisa memasukkan teks berita, lalu sistem mengeluarkan hasil prediksi apakah berita tersebut **Fake** atau **Real** berdasarkan model terbaik yang telah disimpan.

## 7. Penyusunan Laporan
- **Tujuan:** Mendokumentasikan seluruh alur kerja proyek dari awal hingga akhir.
- **Lokasi Simpan:** Folder `Laporan/` (Maksimal 10 Halaman).
- **Struktur Laporan Wajib:**
  1. Problem Definition (Definisi Masalah)
  2. Deskripsi Dataset
  3. Preprocessing (Proses pembersihan teks)
  4. Feature Extraction (Metode ekstraksi fitur)
  5. Modeling (Algoritma yang digunakan)
  6. Eksperimen dan Perbandingan (Hasil analisis metrik)
  7. Insight (Temuan menarik)
  8. Conclusion (Kesimpulan)

---
**Catatan untuk Developer/Eksekutor:** Pastikan setiap progres kode (preprocessing, ekstraksi fitur, modeling) didokumentasikan dengan baik di dalam Jupyter Notebook dan disimpan dalam folder `Notebook/`.
