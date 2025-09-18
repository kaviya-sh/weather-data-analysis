import pandas as pd
import matplotlib.pyplot as plt
import os

# ✅ Step 1: Check if file exists before loading
filename = "daily-min-temperatures.csv"

if not os.path.exists(filename):
    print(f"❌ File '{filename}' not found!")
    exit()

# ✅ Step 2: Load dataset
df = pd.read_csv(filename)

# ✅ Step 3: Show first 5 rows
print("📊 Sample Data:\n", df.head())

# ✅ Step 4: Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ✅ Step 5: Basic statistics
print("\n📈 Weather Statistics:\n", df.describe())

# ✅ Step 6: Plot temperature trend
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Temp'], color="orange")
plt.title("Daily Minimum Temperatures (Australia 1981–1990)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

# ✅ Step 7: Monthly average temperature
df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['Temp'].mean()

print("\n🌡️ Average Temperature by Month:\n", monthly_avg)

# ✅ Step 8: Bar chart for monthly average temperature
monthly_avg.plot(kind="bar", figsize=(10,5), color="skyblue", edgecolor="black")
plt.title("Average Monthly Temperature (°C)")
plt.xlabel("Month (1=Jan, 12=Dec)")
plt.ylabel("Temperature (°C)")
plt.show()

# ✅ Step 9: Histogram of all temperatures
plt.hist(df['Temp'], bins=20, color="green", edgecolor="black")
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
