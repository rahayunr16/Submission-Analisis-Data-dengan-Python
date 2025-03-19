import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
day1_df = pd.read_csv("Dashboard/day1_data.csv")

# Konversi kolom tanggal ke tipe datetime
day1_df["date"] = pd.to_datetime(day1_df["date"])

# Mapping season dari angka ke nama (asumsi data season dalam bentuk angka)
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day1_df["season_name"] = day1_df["season"].map(season_mapping)

# Fungsi untuk membuat dataframe season vs total rentals
def create_user_v_season_df(df):
    user_v_season_df = df.groupby("season_name", as_index=False)["total_rentals"].sum()
    return user_v_season_df

# Setup sidebar untuk filter tanggal
min_date = day1_df["date"].min().date()
max_date = day1_df["date"].max().date()

with st.sidebar:
    st.title("Filter Data")
    
    start_date, end_date = st.date_input(
        label='Filter Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    st.write("Tanggal yang dipilih:", start_date, "sampai", end_date)

# Filter data berdasarkan tanggal yang dipilih
main_df = day1_df[(day1_df["date"].dt.date >= start_date) & 
                 (day1_df["date"].dt.date <= end_date)]

# Mulai tampilan utama
st.title("Dashboard Bike Sharing")
st.write("Data rentals sepeda berdasarkan season")

# Menampilkan informasi data
st.subheader("Informasi Data")
st.write(f"Jumlah data: {len(main_df)} baris")
st.write(f"Periode data: {start_date} sampai {end_date}")

# Judul untuk bagian visualisasi
st.subheader("Jumlah Total Rentals berdasarkan Season")

# Daftar season yang tersedia
all_seasons = ["Spring", "Summer", "Fall", "Winter"]

# Filter season dengan multiselect
selected_seasons = st.multiselect(
    "Pilih Season yang ingin ditampilkan:",
    options=all_seasons,
    default=all_seasons
)

# Filter dataframe berdasarkan season yang dipilih
if selected_seasons:
    filtered_df = main_df[main_df["season_name"].isin(selected_seasons)]
else:
    filtered_df = main_df  # Jika tidak ada yang dipilih, tampilkan semua

# Mendapatkan data yang dikelompokkan berdasarkan season yang sudah difilter
season_df = create_user_v_season_df(filtered_df)

# Visualisasi dengan seaborn
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season_name", y="total_rentals", data=season_df, ax=ax)
    ax.set_title("Jumlah Total Rentals per Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Total Rentals")
    plt.xticks(rotation=0)  # Memastikan label tidak dirotasi
    st.pyplot(fig)
else:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")

# Menampilkan insight
st.subheader("*Insight*")
if not filtered_df.empty:
    st.write(f"Season dengan rentals tertinggi: {season_df.loc[season_df['total_rentals'].idxmax(), 'season_name']}")
    st.write(f"Season dengan rentals terendah: {season_df.loc[season_df['total_rentals'].idxmin(), 'season_name']}")
    st.write(f"Total rentals dari semua season yang dipilih: {filtered_df['total_rentals'].sum()}")
else:
    st.write("Tidak ada data untuk menampilkan insight.")
