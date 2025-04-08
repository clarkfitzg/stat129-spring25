cut --fields=4-6 /stat129/complaints/* |
    grep -E "CHRYSLER\s+PACIFICA" > minivans.txt

cut --fields=4-6 /stat129/complaints/* |
    grep -E "HONDA\s+ODYSSEY" >> minivans.txt

cut --fields=4-6 /stat129/complaints/* |
    grep -E "TOYOTA\s+SIENNA" >> minivans.txt


sort minivans.txt | uniq --count | sort --numeric > minivan-counts.txt
