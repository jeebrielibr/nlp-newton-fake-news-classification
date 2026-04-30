# Laporan Analisis Performa Model & Rekomendasi Peningkatan

Laporan ini menyajikan analisis mendalam terhadap pipeline klasifikasi berita bohong (Fake News) yang diimplementasikan dalam tiga notebook utama: `1. Textporcessing.ipynb`, `2. Feature_extraction.ipynb`, dan `3. Model_Trainning.ipynb`.

## 1. Ringkasan Proses Saat Ini

### A. Preprocessing (`1. Textporcessing.ipynb`)
- **Pipeline:** Case folding (lowercasing, URL removal, non-alphabetic cleaning), Tokenization, Stopword removal, dan Lemmatization.
- **Hasil:** Dataset bersih disimpan dalam `fake_news_dataset_cleaned.csv`.
- **Observasi:** Lemmatization dilakukan tanpa POS tagging, yang dapat mengurangi efektivitas reduksi kata ke bentuk dasarnya.

### B. Feature Extraction (`2. Feature_extraction.ipynb`)
- **Teknik:** Implementasi TF-IDF (N-gram 1-3), Metadata Encoding (Source & Category), Word2Vec, FastText, dan GloVe.
- **Hasil:** Matriks fitur gabungan (TF-IDF + Metadata) dan embedding matrices.
- **Observasi:** Penggunaan N-gram dan Metadata merupakan langkah yang sangat baik untuk menangkap konteks.

### C. Model Training (`3. Model_Trainning.ipynb`)
- **Model:** Random Forest, XGBoost, CNN, dan Bi-LSTM.
- **Hasil:** Akurasi semua model tertahan di kisaran **49% - 50.5%**.
- **Observasi:** Meskipun menggunakan arsitektur canggih seperti Bi-LSTM dengan Pre-trained GloVe, model tidak mampu melampaui performa tebakan acak (*random guessing*).

---

## 2. Analisis Akar Masalah (Root Cause)

Mengapa akurasi masih ~50% meskipun sudah menggunakan teknik advanced?

1.  **Kualitas Dataset (Masalah Utama):**
    Berdasarkan sampel data di Notebook 1, teks berita tampak seperti kumpulan kata acak (*synthetic/scrambled text*). Contoh: *"more tax development both store agreement lawyer hear out..."*. 
    - Jika teks tidak memiliki struktur semantik yang nyata, model NLP tidak akan menemukan pola yang membedakan antara "real" dan "fake".
2.  **Ketiadaan Korelasi Label:**
    Ada kemungkinan label "real" dan "fake" pada dataset saat ini diberikan secara acak atau tidak berkorelasi dengan isi teks.
3.  **Embeddings vs Synthetic Text:**
    Pre-trained embeddings (GloVe) dilatih pada bahasa manusia yang terstruktur (Wikipedia). Jika dataset berisi kata-kata acak, vektor GloVe tidak akan membentuk representasi dokumen yang bermakna.

---

## 3. Langkah Strategis Meningkatkan Skor (>80%)

Untuk mencapai target akurasi yang kompetitif, langkah-langkah berikut **wajib** dilakukan:

### Tahap 1: Validasi & Penggantian Data
- **Audit Dataset:** Periksa apakah berita dalam `fake_news_dataset.csv` memiliki kalimat yang koheren. Jika tidak, ganti dengan dataset berita nyata.
- **Rekomendasi Dataset:**
    - [WELFake Dataset](https://www.kaggle.com/datasets/saurabhshahane/welfake-dataset) (72k records).
    - [ISOT Fake News Dataset](https://www.kaggle.com/datasets/emineotuzbir/isot-fake-news-dataset).

### Tahap 2: Optimasi Preprocessing
- **POS-Tagged Lemmatization:** Gunakan library `spaCy` untuk lemmatization yang memahami konteks (Noun, Verb, Adj).
- **Retention of Punctuation:** Berita bohong seringkali menggunakan tanda seru (`!`) atau tanda tanya (`?`) secara berlebihan. Jangan hapus karakter ini sepenuhnya; jadikan sebagai fitur.

### Tahap 3: Perbaikan Arsitektur Model
- **Hybrid Deep Learning:** Integrasikan fitur Metadata (Source, Author, Category) ke dalam model Deep Learning menggunakan *Concatenate Layer* (menggabungkan output LSTM dengan output Dense layer metadata).
- **Transformer Models (SOTA):** Gunakan **BERT** atau **DistilBERT** melalui library `transformers` (Hugging Face). Model ini jauh lebih kuat daripada Bi-LSTM dalam memahami konteks bahasa.

### Tahap 4: Hyperparameter Tuning
- Gunakan **Optuna** untuk mencari parameter optimal pada XGBoost dan Random Forest (misalnya: `max_depth`, `n_estimators`, `learning_rate`).

---

## 4. Kesimpulan
Proses saat ini sudah secara teknis benar dalam hal alur kerja (pipeline), namun terhambat oleh kualitas data input. Dengan menggunakan dataset yang memiliki struktur bahasa alami dan mengadopsi model Transformer, akurasi >80% sangat mungkin dicapai.
