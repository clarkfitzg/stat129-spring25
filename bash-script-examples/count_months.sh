# count_months.sh
# Modify with a text editor such as nano
#
zcat /stat129/1763.csv.gz |
	cut --delimiter=, --fields=2 |
	cut --characters=5-6 |
	sort --numeric |
	uniq --count > months.txt

