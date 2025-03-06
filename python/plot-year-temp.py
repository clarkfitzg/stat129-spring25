# Plot the year temperature

# Data frames
import pandas as pd

d = pd.read_csv("station-year-temp.csv")


# Plotting interface for data frames
# similar to R's ggplot2
import seaborn as sns


# Returns an axis to plot
ax = sns.lineplot(x = "year",
                  y = "temperature",
                  hue = "station",
                  data = d)

# Save the resulting figure
ax.figure.savefig("year-temp.pdf")
