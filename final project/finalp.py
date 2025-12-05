import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("air.csv")
df["DateTime"] = pd.to_datetime(df["DateTime"])
df = df.set_index("DateTime")


# 1) BAR CHART (Avg PM2.5, PM10, NO2)

plt.figure(figsize=(7,4))
avg_values = [df["PM2.5"].mean(), df["PM10"].mean(), df["NO2"].mean()]
labels = ["PM2.5", "PM10", "NO2"]
plt.bar(labels, avg_values, color=["blue", "orange", "green"])
plt.title("Average Pollution Levels (Bar Chart)")
plt.ylabel("Value")
plt.show()


# 2) LINE CHART (PM2.5)

plt.figure(figsize=(10,5))
plt.plot(df.index, df["PM2.5"], label="PM2.5", color='blue')
plt.title("PM2.5 Over Time (Line Chart)")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.grid()
plt.legend()
plt.show()


# 3) PIE CHART (Pollution distribution)

avg = df[["PM2.5","PM10","NO2"]].mean()
plt.figure(figsize=(6,6))
plt.pie(avg, labels=avg.index, autopct="%1.1f%%", startangle=90)
plt.title("Pollution Composition (Pie Chart)")
plt.show()


# 4) HISTOGRAM (Temperature)

plt.figure(figsize=(8,5))
plt.hist(df["Temperature"], bins=10, color='purple', edgecolor='black')
plt.title("Temperature Distribution (Histogram)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()


# 5) LINE CHART (PM10)

plt.figure(figsize=(10,5))
plt.plot(df.index, df["PM10"], label="PM10", color='orange')
plt.title("PM10 Over Time")
plt.xlabel("Date")
plt.ylabel("PM10")
plt.grid()
plt.legend()
plt.show()


# 6) LINE CHART (NO2)

plt.figure(figsize=(10,5))
plt.plot(df.index, df["NO2"], label="NO2", color='green')
plt.title("NO2 Over Time")
plt.xlabel("Date")
plt.ylabel("NO2")
plt.grid()
