Goal: Create year-temp.pdf that contains the plot we want

Relevant files:

0. create-plot.sh is a bash script that controls and calls everything else.
1. prep-data.sh is the bash script needed to pick out the subset of interest from the entire data set.
    This takes a long time, so you'll make it run in parallel.
2. station-day-tmin.csv is the prepared subset of interest, an intermediate result.
3. plot-year-temp.py is the Python script that reads in station-day-tmin.csv and makes the plot (year-temp.pdf).
