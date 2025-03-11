# Run as follows:
# make year-temp.pdf

# Build up a CSV file to make all the subsequent steps easy.
station-day-tmin.csv: 
	echo "station,year,TMIN" > $@
	bash prep-data.sh >> $@

year-temp.pdf: plot-year-temp.py station-day-tmin.csv
	/opt/anaconda/bin/ipython $<
