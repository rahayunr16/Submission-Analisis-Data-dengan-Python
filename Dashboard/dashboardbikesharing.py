import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day1_df = pd.read_csv("Dashboard/day1_data.csv")

day1_df["date"] = pd.to_datetime(day1_df["date"])

def create_user_v_season_df(day1_df):
    user_v_season_df = day1_df.groupby("season", as_index=False)["total_rentals"].sum()
    return user_v_season_df

def create_workingday_summary_df(day1_df):
    workingday_summary_df = day1_df.groupby("working_day", as_index=False)["total_rentals"].sum()
    return workingday_summary_df

def create_condition_day_df(day1_df):
    condition_day_df = day1_df.groupby('weather_condition', as_index=False)['total_rentals'].sum()
    return condition_day_df

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

st.title("DASHBOARD BIKE-SHARING RENTALS")

st.subheader("Informasi Data")
st.write(f"Jumlah data: {len(main_df)} baris")
st.write(f"Periode data: {start_date} sampai {end_date}")

st.subheader("Total Rentals berdasarkan Season")

season_df = create_user_v_season_df(main_df)
    
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="season", y="total_rentals", data=season_df, ax=ax)
ax.set_title("Jumlah Total Rentals per Season")
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Season dengan rentals tertinggi: {season_df.loc[season_df['total_rentals'].idxmax(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")
st.write(f"Season dengan rentals terendah: {season_df.loc[season_df['total_rentals'].idxmin(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")

st.subheader("Perbandingan Total Rentals berdasarkan Hari Kerja dan Akhir Pekan")

working_sf = create_workingday_summary_df(main_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="working_day", y="total_rentals", data=working_sf, ax=ax)
ax.set_title("Hari Kerja vs Akhir Pekan")
ax.set_xlabel("Hari Kerja (False = Akhir Pekan, True = Hari Kerja)")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Insight")
st.write("Total rentals pada hari kerja lebih banyak dibandingkan akhir pekan.")

st.subheader("Pengaruh Kondisi Cuaca pada Total Penyewaan Sepeda")

condition_sf=create_condition_day_df(main_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weather_condition",y="total_rentals", data=condition_sf, ax=ax)
ax.set_title('Hubungan Cuaca & Total Penyewaan')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Penyewaan')
st.pyplot(fig)


order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def weekday_df(day1_df):
    weekday_df = day1_df.groupby('weekday', as_index=False)['total_rentals'].sum()
    weekday_df['weekday'] = pd.Categorical(weekday_df['weekday'], categories=order, ordered=True)
    weekday_df = weekday_df.sort_values('weekday')
    return weekday_df

st.subheader("Total Penyewaan Sepeda per Hari dalam Seminggu")

weekday_sf = weekday_df(main_df)  

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weekday", y="total_rentals", data=weekday_sf, ax=ax, palette="viridis")
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Sepeda per Hari")
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Hari dengan rentals tertinggi: {weekday_sf.loc[weekday_sf['total_rentals'].idxmax(), 'weekday' if 'weekday_name' not in weekday_sf.columns else 'weekday_name']}")
st.write(f"Hari dengan rentals terendah: {weekday_sf.loc[weekday_sf['total_rentals'].idxmin(), 'weekday' if 'weekday_name' not in weekday_sf.columns else 'weekday_name']}")
