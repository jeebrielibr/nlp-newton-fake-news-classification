# Fake News Classification

## Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem klasifikasi berita palsu menggunakan teknik Natural Language Processing (NLP). Sistem akan memproses teks berita, mengekstraksi fitur, melatih beberapa model klasifikasi, dan membandingkan hasilnya.

## Pipeline Proyek
1. Data Collection
   - Kumpulkan dataset dari sumber seperti Kaggle, web scraping, atau open dataset.
   - Dataset minimal berisi lebih dari **10.000 data**.

2. Text Preprocessing
   - Case folding
   - Tokenization
   - Stopword removal
   - Stemming atau lemmatization

3. Feature Extraction (WAJIB 2 jenis)
   - TF-IDF
   - Word embedding seperti Word2Vec, GloVe, atau FastText

4. Modeling (WAJIB 3 model)
   - Contoh model: Naive Bayes, Logistic Regression, SVM, Decision Tree, Random Forest, dll.

5. Comparison Model
   - Bandingkan hasil antara:
     - TF-IDF vs Word Embedding
     - Model A vs Model B
   - Evaluasi menggunakan metrik:
     - Accuracy
     - Precision
     - Recall
     - F1-score

6. Deployment Sederhana
   - Implementasi aplikasi sederhana menggunakan Gradio untuk demo antarmuka.

## Struktur Repository
- `Notebook/` : Notebook eksperimen atau skrip pelatihan
- `Dataset/` : Dataset atau link dataset yang digunakan
- `Model/` : Model terlatih dan file hasil output
- `Laporan/` : Dokumen laporan akhir

## Konten Repository yang Diharapkan
- Notebook atau skrip lengkap untuk preprocessing, ekstraksi fitur, pelatihan model, dan evaluasi
- Dataset atau tautan ke dataset sumber
- File model yang disimpan (misalnya `.pkl`, `.h5`, atau format model lain)
- Aplikasi demonstrasi atau notebook deploy Gradio

## Laporan (Maksimal 10 Halaman)
1. Problem definition
2. Deskripsi dataset
3. Preprocessing
4. Feature extraction
5. Modeling
6. Eksperimen dan perbandingan
7. Insight
8. Conclusion

## Referensi
- [Feature extraction](https://elena.nurulfikri.ac.id/mod/resource/view.php?id=58727)
- [Word embedding](https://elena.nurulfikri.ac.id/mod/resource/view.php?id=59010)
