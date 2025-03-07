
# Build up a CSV file to make all the subsequent steps easy.
.ONESHELL:
station-day-tmin.csv: 
	echo "station,year,TMIN" > $@
	zcat /stat129/200[0-2].csv.gz |
	    grep -E "USW00023271|USW00093225" |
	    grep "TMIN" |
	    cut -d, -f1,2,4 |
	    cut -c 17-20 --complement |
	    sed "s/USW00023271/Sacramento/" |
	    sed "s/USW00093225/airport/" >> $@
