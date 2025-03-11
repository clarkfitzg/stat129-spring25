# Prepare the interesting subset of data
echo "station,year,TMIN" > station-day-tmin.csv
bash prep-data.sh >> station-day-tmin.csv

# Use the data to make the plot
# /opt/anaconda/bin/ipython accepts a file name to run, just like python3
/opt/anaconda/bin/ipython plot-year-temp.py
