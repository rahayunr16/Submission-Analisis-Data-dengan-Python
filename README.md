# Submission-Analisis-Data-dengan-Python
Ini merupakan salah satu submission pada course yang diadakan oleh program beasiswa Laskar AI dengan menggunakan dataset dari Bike-Sharing Rental. Analisis ini juga menyediakan dashboard sebagai hasil visualisasi Data Wrangling, EDA, dan Visualization to Get An Insight

# BIKE-SHARING RENTAL 
##**Tentang Bike-Sharing Rental**
Bike-sharing rental adalah inovasi dari penyewaan sepeda tradisional dengan proses otomatis, mencakup keanggotaan, penyewaan, dan pengembalian. Pengguna dapat menyewa dan mengembalikan sepeda di lokasi yang berbeda. Saat ini, terdapat lebih dari 500 program penyewaan sepeda berbagi di seluruh dunia, dengan total lebih dari 500.000 sepeda. Inovasi ini berkontribusi terhadap lalu lintas, lingkungan, dan kesehatan.

##**Pertanyaan Analisi yang Dijawab**
Bagaimana pola musiman memengaruhi jumlah penyewaan sepeda?
Apakah jumlah penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan?
Apakah kondisi cuaca memengaruhi tren penyewaan sepeda?
Pada hari apa penyewaan sepeda mencapai jumlah tertinggi?
Di bulan apa jumlah penyewaan sepeda paling tinggi?
Mana yang lebih banyak: pengguna terdaftar atau pengguna kasual?
Bagaimana tren total penyewaan sepeda dari waktu ke waktu?

##**Detail Proyek**
Proyek data ini terdiri dari data wrangling yaitu gathering data, assesing data, dan cleaning data; exploratory data analysis (EDA); serta data vizualisation.
Pada proyek data ini tujuan pengolahan adalah menjawab pertanyaan yang muncul sebagai analisis dan insight untuk dapat menerapkan strategi bisnis atau pengembangan bike-sharing rental.

##**Dataset**
Adapun dataset yang digunakan adalah Bike-sharing rental dengan detail label tentang index, tahun, bulan, jam, kondisi cuaca, musim, temperatur udara dalam celsius, temperatur yang dirasakan, kelembaban, kecepatan angin, banyaknya pengguna kasual dan terdaaftar, total penyewaan sepeda.
Dataset merupakan rekam dari 2 tahun dari Januari 2011 hingga Desember 2012 dari Capital Bikeshare system, Washington D.C., USA yang dipublikasikan http://capitalbikeshare.com/system-data. 
Kondisi cuaca didapatkan dari informasi http://www.freemeteo.com.
| Kolom                 | Deskripsi |
|----------------------|-----------|
| `season`            | Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin) |
| `year`              | Tahun (0: 2011, 1: 2012) |
| `month`             | Bulan (1 - 12) |
| `hour`              | Jam dalam sehari (0 - 23) |
| `holiday`           | Hari libur (0: Tidak, 1: Ya) |
| `weekday`           | Hari dalam seminggu (0: Minggu, 6: Sabtu) |
| `working_day`       | Hari kerja (0: Tidak, 1: Ya) |
| `weather_condition` | Kondisi cuaca (1: Cerah, 2: Berawan, 3: Hujan, 4: Badai) |
| `temperature_celsius` | Suhu dalam Celsius |
| `humidity`          | Kelembaban (%) |
| `windspeed`        | Kecepatan angin |
| `casual_users`      | Jumlah pengguna tidak terdaftar |
| `registered_users`  | Jumlah pengguna terdaftar |
| `total_rentals`     | Total jumlah penyewaan sepeda |

##**Instalasi**
###**1. Install Library yang Dibutuhkan**
Jalankan perintah berikut untuk menginstal library yang diperlukan:
'pip install numpy'
'pip install pandas'
'pip install scipy'
'pip install matplotlib''
'pip install seaborn'
'!pip install streamlit pyngrok
from pyngrok import ngrok'

###**2.  Jika Menggunakan Google Colab**

mount Google Drive untuk membaca dataset:
'from google.colab import drive'
'drive.mount('/content/drive')'

Kemudian, file dataset day.csv dan hour.csv diakses dari Google Drive:
'daydataset = "/content/drive/MyDrive/LASKAR AI/SUBMISSION/day.csv"'
'day_df = pd.read_csv(daydataset)'
'hourdataset = "/content/drive/MyDrive/LASKAR AI/SUBMISSION/hour.csv"'
'hour_df = pd.read_csv(hourdataset)'

###**3.  Menjalankan Streamlit''
Jika di Google Colab
'!pip install streamlit pyngrok'
'from pyngrok import ngrok'

'!streamlit run dashboardbikesharing.py &>/dev/null &'
'url = ngrok.connect(port='8501')'
'print(f"🎯 Buka dashboard di: {url}")'

Jika di PC/Laptop:
streamlit run dashboardbikesharing.py

##**Struktur Proyek**

📂 SUBMISSION
 ┣ 📂 dataset (raw)
 ┃ ┣ 📄 day.csv
 ┃ ┣ 📄 hour.csv
 ┣ 📂 dataset (cleaning)
 ┃ ┣ 📄 day1.csv
 ┃ ┣ 📄 hour1.csv
 ┃ 📄 SubmissionLAI.ipynb  
 ┃ 📄 submissionlai2_(dashboard).py  
 ┣ 📄 requirements.txt  
 ┣ 📄 README.md  

##**Library yang digunakan**

'numpy == (1.26.4)'
'pandas == (2.2.2)'
'scipy == (1.13.1)'
'matplotlib == (3.10.0)'
'seaborn == (0.13.2)'
'pyngrok == (7.2.3)'
'streamlit == (1.43.1)'

##**Kontak**

Jika memiliki pertanyaan, hubungi saya di a229xbm406@devacademy.id
