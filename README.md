# Klasifikasi Gambar CIFAR-10 dengan CNN Teroptimasi dan Streamlit

Team Assignment 2, Artificial Intelligence (COSC6023036), BINUS University
Kelompok 5

| Anggota | NIM |
|---|---|
| Abzachrie Defghi Ferdyan | 2902741953 |
| Kezia Anandita | 2802662216 |
| Muhammad Thareq Iqbal Rayyan | 2902670313 |
| Daffa Fathur Rahman | 2902692586 |
| Aziz Dimas Pradana | 2902742956 |

## Deskripsi

Proyek ini mengoptimalkan model CNN untuk klasifikasi gambar dataset CIFAR-10 (10 kelas, 32x32 piksel), lalu mengintegrasikannya ke aplikasi web Streamlit yang menerima input gambar dan menampilkan prediksi beserta tiga kelas teratas (Top-3).

**Aplikasi (live):** https://cifar10-classifier-aigroup5.streamlit.app

## Hasil Utama

| Metrik | Baseline | Teroptimasi |
|---|---|---|
| Akurasi test (10.000 gambar) | 71,45% | 91,61% |
| Selisih akurasi latih dan validasi | 16,97 poin | 1,35 poin |
| Test loss | 1,1240 | 0,2850 |

- Pengujian 20 gambar baru di luar dataset: 19 benar (95%).
- Pasangan kelas paling sering tertukar: cat dan dog.

## Teknik Optimasi

- Hyperparameter tuning: Keras Tuner Random Search (8 trial)
- Data augmentation (RandomFlip, RandomTranslation)
- Batch Normalization
- Dropout bertingkat
- Blok konvolusi ganda
- Global Average Pooling
- Callbacks: EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

Konfigurasi terbaik: filter awal 64, dropout konvolusi 0,2, dropout dense 0,4, dense 128 neuron, learning rate 0,001.

## Pembagian Data

| Partisi | Jumlah |
|---|---|
| Train | 45.000 |
| Validation | 5.000 |
| Test | 10.000 |

Test set hanya digunakan satu kali pada evaluasi akhir.

## Struktur Folder

```
.
├── README.md
├── app.py                          # Aplikasi Streamlit
├── requirements.txt                # Dependensi aplikasi
├── cnn_cifar10_optimized.keras     # Model teroptimasi
├── model_info.json                 # Info model dan hyperparameter terbaik
├── notebook/
│   └── TK2_AI.ipynb                # Notebook pelatihan dan tuning
├── hasil/
│   ├── perbandingan_model.csv
│   ├── kurva_pelatihan.png
│   └── confusion_matrix.png
└── gambar_uji/                     # 20 gambar uji di luar dataset
```

## Cara Menjalankan Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Versi TensorFlow pada `requirements.txt` disesuaikan dengan `model_info.json`.

## Catatan Preprocessing

Normalisasi piksel (`Rescaling(1./255)`) sudah berada di dalam model. Karena itu, aplikasi hanya mengonversi gambar ke RGB, resize ke 32x32, dan mengirim array float32 dengan nilai 0 sampai 255. Jangan membagi dengan 255 lagi di sisi aplikasi.

## Dokumen Terkait

- Laporan teknis (Laporan_Teknis_TA_2_Group_5-AI.pdf)
- Video demo: [isi link]

## Deklarasi Penggunaan AI

Penggunaan AI dalam pengerjaan tugas ini dicantumkan pada form deklarasi yang dikumpulkan bersama tugas.
