import pandas as pd
# -----------------------
# Task 1: Load CSV
# -----------------------
data = pd.read_csv("temperature.csv")
print("\n--- First 10 Rows ---")
print(data.head(10))

# -----------------------
# Task 2: Data Cleaning
# -----------------------
print("\nMissing values before cleaning:")
print(data.isnull().sum())

# Fill missing values with mean
data["temperature"] = data["temperature"].fillna(data["temperature"].mean())

print("\nMissing values after cleaning:")
print(data.isnull().sum())

# Convert date column to datetime
data["date"] = pd.to_datetime(data["date"])

# -----------------------
# Task 3: Line Plot
# -----------------------
plt.plot(data["date"], data["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_plot.png")
print("\nSaved: line_plot.png")

# -----------------------
# Task 4: Bar Chart (Month Wise)
# -----------------------
data["month"] = data["date"].dt.month
month_avg = data.groupby("month")["temperature"].mean()

month_avg.plot(kind="bar")
plt.xlabel("Month")
plt.ylabel("Average Temp")
plt.title("Average Temperature by Month")
plt.tight_layout()
plt.savefig("bar_chart.png")
print("Saved: bar_chart.png")

print("\nProgram completed!")



