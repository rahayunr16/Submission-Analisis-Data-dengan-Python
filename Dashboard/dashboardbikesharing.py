import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
day1_df = pd.read_csv("Dashboard/day1_data.csv")

# Konversi kolom tanggal
day1_df["date"] = pd.to_datetime(day1_df["date"])

# Pastikan kolom season tidak ada error
# Jika memang perlu mapping, tambahkan dictionary mapping
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}  # Contoh mapping
day1_df["season"] = day1_df["season"].map(season_mapping)

# Fungsi untuk agregasi data berdasarkan season
def create_user_v_season_df(df):
    return df.groupby("season", as_index=False)["total_rentals"].sum()

# Ambil rentang tanggal dari dataset
min_date = day1_df["date"].min().date()
max_date = day1_df["date"].max().date()

# Sidebar untuk filter tanggal
with st.sidebar:
    st.title("Filter Tanggal")
    
    start_date, end_date = st.date_input(
        "Pilih Rentang Tanggal",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    
    st.write(f"Tanggal yang dipilih: {start_date} sampai {end_date}")

# Filter data berdasarkan rentang tanggal
main_df = day1_df[(day1_df["date"].dt.date >= start_date) & 
                  (day1_df["date"].dt.date <= end_date)]

# Judul Dashboard
st.title("Dashboard Bike Sharing")

st.subheader("Informasi Data")
st.write(f"Jumlah data: {len(main_df)} baris")
st.write(f"Periode data: {start_date} sampai {end_date}")

# Filter berdasarkan season
st.subheader("Jumlah Total Rentals berdasarkan Season")

selected_seasons = st.multiselect(
    "Pilih Season yang ingin ditampilkan:",
    options=day1_df["season"].unique().tolist(),
    default=day1_df["season"].unique().tolist()
)

if selected_seasons:
    filtered_df = main_df[main_df["season"].isin(selected_seasons)]
else:
    filtered_df = main_df  

# Buat dataframe untuk visualisasi
season_df = create_user_v_season_df(filtered_df)

# Plot data jika tidak kosong
if not season_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="total_rentals", data=season_df, ax=ax)
    ax.set_title("Jumlah Total Rentals per Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Total Rentals")
    plt.xticks(rotation=0)
    st.pyplot(fig)

    # Insight
    st.subheader("*Insight*")
    if not season_df.empty:
        st.write(f"Season dengan rentals tertinggi: {season_df.loc[season_df['total_rentals'].idxmax(), 'season']}")
        st.write(f"Season dengan rentals terendah: {season_df.loc[season_df['total_rentals'].idxmin(), 'season']}")
else:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")
