with open("/stat129/ghcnd-stations.csv") as f:
    for row in f:
        if "SACRAMENTO" in row:
            print(row, end="")
