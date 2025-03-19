import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day1_df = pd.read_csv("Dashboard/day1_data.csv")

day1_df["date"] = pd.to_datetime(day1_df["date"])

def create_user_v_season_df(df):
    user_v_season_df = df.groupby("season", as_index=False)["total_rentals"].sum()
    return user_v_season_df

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

main_df = day1_df[(day1_df["date"].dt.date >= start_date) & 
                 (day1_df["date"].dt.date <= end_date)]

st.title("Dashboard Bike Sharing")
st.write("Data rentals sepeda berdasarkan season")

st.subheader("Informasi Data")
st.write(f"Jumlah data: {len(main_df)} baris")
st.write(f"Periode data: {start_date} sampai {end_date}")

st.subheader("Jumlah Total Rentals berdasarkan Season")

season_df = create_user_v_season_df(main_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="total_rentals", data=season_df, ax=ax)
ax.set_title("Jumlah Total Rentals per Season")
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Statistik Total Rentals")
st.write(f"Total seluruh rentals: {main_df['total_rentals'].sum()}")
st.write(f"Season dengan rentals tertinggi: {season_df.loc[season_df['total_rentals'].idxmax(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")
st.write(f"Season dengan rentals terendah: {season_df.loc[season_df['total_rentals'].idxmin(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")
