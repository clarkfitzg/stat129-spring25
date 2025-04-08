
# Open ipython with /opt/anaconda/bin/ipython3
#
# And then: %run /stat129/


# After extracting what we need from the XML files we'll have 
# something like this:
d = [
        {"year":"2024", "revenue":"2500", "name":"alpha"},
        {"year":"2023", "revenue":"2300", "name":"alpha"},
        {"year":"2022", "revenue":"2400", "name":"alpha"},
        {"year":"2024", "revenue":"1500", "name":"bravo"},
        {"year":"2023", "revenue":"1400", "name":"bravo"},
        {"year":"2022", "revenue":"1700", "name":"bravo"},
        {"year":"2023", "revenue":"900", "name":"charlie"},
    ]

# Predict the type and value of the following:
d[0]
d[1]["revenue"]


# Necessary so we don't modify d in place.
from copy import deepcopy
d2 = deepcopy(d)

for x in d2:
    for k, v in x.items():
        if k in {"year", "revenue"}:
            x[k] = int(v)  # convert to integer


# Filtering
d23 = [x for x in d2 if x["year"] == "2023"]

# Sorting based on the value of revenue
d23.sort(key = lambda x: x["revenue"])


#import pandas as pd

#d4 = pd.DataFrame(d3)

# import seaborn as sns
