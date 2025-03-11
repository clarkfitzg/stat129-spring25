# Plot the year temperature

# Data frames
import pandas as pd

# Plotting interface for data frames
# similar to R's ggplot2
import seaborn as sns


d0 = pd.read_csv("station-day-tmin.csv")

# convert TMIN from 10ths celsius to Fahrenheit
d0["temperature"] = (d0["TMIN"]/10) * 1.8 + 32


# preparing to calculate statistics 
# for each group of station and year
grouped = d0.groupby(["station", "year"])

# Calculate the median for each group
d = grouped.median()
d = d.reset_index()

def add_anomaly(group):
    mintemp = group["temperature"].min()
    group["anomaly"] = group["temperature"] - mintemp
    return group

# Add an anomaly column by applying the add_anomaly
# function to each station group
d2 = d.groupby("station").apply(add_anomaly)

# Returns an axis to plot
ax = sns.lineplot(x = "year",
                  y = "anomaly",
                  hue = "station",
                  data = d2)

# Save the resulting figure
ax.figure.savefig("year-temp.pdf")
