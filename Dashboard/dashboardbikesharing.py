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

weekday_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def create_weekday_df(day1_df):
    weekday_df = day1_df.groupby('weekday', as_index=False)['total_rentals'].sum()
    weekday_df['weekday'] = pd.Categorical(weekday_df['weekday'], categories=weekday_order, ordered=True)
    weekday_df = weekday_df.sort_values('weekday')
    return weekday_df

month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Desember"]
def create_month_df(day1_df):
    month_df = day1_df.groupby('month', as_index=False)['total_rentals'].sum()
    month_df['month'] = pd.Categorical(month_df['month'], categories=month_order, ordered=True)
    month_df = month_df.sort_values('month')
    return month_df

def create_user_counts_df(day1_df):
    user_counts_df = [day1_df['registered_users'].sum(), day1_df['casual_users'].sum()]
    return user_counts_df

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
sns.barplot(x="season", y="total_rentals", data=season_df, ax=ax, palette="viridis")
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Season dengan rentals tertinggi: {season_df.loc[season_df['total_rentals'].idxmax(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")
st.write(f"Season dengan rentals terendah: {season_df.loc[season_df['total_rentals'].idxmin(), 'season' if 'season_name' not in season_df.columns else 'season_name']}")

st.subheader("Perbandingan Total Rentals berdasarkan Hari Kerja dan Akhir Pekan")

working_sf = create_workingday_summary_df(main_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="working_day", y="total_rentals", data=working_sf, ax=ax, palette="viridis")
ax.set_xlabel("Hari Kerja (False = Akhir Pekan, True = Hari Kerja)")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.subheader("Insight")
st.write("Total rentals pada hari kerja lebih banyak dibandingkan akhir pekan.")

st.subheader("Pengaruh Kondisi Cuaca pada Total Penyewaan Sepeda")

condition_sf=create_condition_day_df(main_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weather_condition",y="total_rentals", data=condition_sf, ax=ax, palette="viridis")
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Total Penyewaan')
st.pyplot(fig)

st.subheader("Total Penyewaan Sepeda per Hari")

weekday_sf = create_weekday_df(main_df)  

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="weekday", y="total_rentals", data=weekday_sf, ax=ax, palette="viridis")
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Hari dengan rentals tertinggi: {weekday_sf.loc[weekday_sf['total_rentals'].idxmax(), 'weekday' if 'weekday_name' not in weekday_sf.columns else 'weekday_name']}")
st.write(f"Hari dengan rentals terendah: {weekday_sf.loc[weekday_sf['total_rentals'].idxmin(), 'weekday' if 'weekday_name' not in weekday_sf.columns else 'weekday_name']}")

st.subheader("Total Penyewaan Sepeda per Bulan")

month_sf = create_month_df(day1_df)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="month", y="total_rentals", data=month_sf, ax=ax, palette="viridis")
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan")
plt.tight_layout()
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Bulan dengan rentals tertinggi: {month_sf.loc[month_sf['total_rentals'].idxmax(), 'month' if 'month_name' not in month_sf.columns else 'month_name']}")
st.write(f"Bulan dengan rentals terendah: {month_sf.loc[month_sf['total_rentals'].idxmin(), 'month' if 'month_name' not in month_sf.columns else 'month_name']}")

st.subheader("Perbandingan Pengguna Terdaftar dan Pengguna Kasual")

user_counts = create_user_counts_df(day1_df)
labels = ['Registered Users', 'Casual Users']
colors = ['#3A1B6D', '#C1D32F']

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    user_counts,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

ax.axis('equal')
st.pyplot(fig)

st.subheader("Insight")
st.write(f"Banyaknya Pengguna Terdaftar: {user_counts[0]:,}")
st.write(f"Banyaknya Pengguna Kasual: {user_counts[1]:,}")
