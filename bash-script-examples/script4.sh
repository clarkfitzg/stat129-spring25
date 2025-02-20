# A bash script is just a sequence of bash commands

# Let's test and make sure this histogram program works.

# We can create variables in a bash program 
TEMPCOUNT="temp_counts.txt"

# Generate some example data to work with
seq -50 200 | sed "p;p;p;" | uniq --count > $TEMPCOUNT

Rscript /stat129/stat129-spring24/uniq_to_hist.R $TEMPCOUNT
