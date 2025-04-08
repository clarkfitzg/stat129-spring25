# /opt/anaconda/bin/ipython
# ^ run with this ^

# If you're using this script, please clean it up and delete whatever is not essential.

import os
import random

from lxml import etree

datadir = "/stat129/tax23/"

all990 = [datadir + p for p in os.listdir(datadir)]

# Working with a small sample is easier
# Setting the seed here guarantees the same random sample
random.seed(286349) 
n = 10
s990 = random.sample(all990, n)

# Develop a function by starting with just one.
xmlfile = s990[0]

tree = etree.parse(xmlfile)

mission = tree.xpath("//ActivityOrMissionDesc/text()")


# Take the little experiment we had above and build it into a function
def findbikes(xmlfile, pattern = r"bicycl| bike "):
    """
    Find nonprofits related to bicycles, returning None for failures
    """
    tree = etree.parse(xmlfile)
    # A dictionary holding all the results
    result = {}

    try:
        # Here we ONLY return text and data, NOT the actual nodes.
        # If you return nodes in the tree, then it will break when
        # we run this in parallel.
        result["mission"] = tree.xpath("/Return/ReturnData/IRS990/ActivityOrMissionDesc/text()")[0]
        result["year"] = int(tree.xpath("/Return/ReturnData/IRS990/FormationYr/text()")[0])
        result["website"] = tree.xpath("/Return/ReturnData/IRS990/WebsiteAddressTxt/text()")[0]
    except:
        # xpath fails for some reason, so just give up!
        # A better way to handle this is to actually *look* 
        # at this XML file, which may have a different structure.
        # None below functions as a *sentinel value* indicating
        # failure
        return None

    return result

# Test our function.
findbikes(s990[0])

# Apply our function to the small sample of files
rn = map(findbikes, s990)

# Convert it to a list, because map is lazy
# It only evaluates when we force it.
rn = list(rn)

# Now run it on... EVERYTHING ALL AT ONCE IN PARALLEL!
# Change this to True to process the entire data set.
if False: 
    from multiprocessing import Pool
    # See https://docs.python.org/3/library/multiprocessing.html
    # 10 parallel workers
    with Pool(10) as p:
        # Parallel map is not lazy
        r = p.map(findbikes, all990)

    # Remove all these None values
    r = [x for x in r if x is not None]

    len(r) # found 

    # Sort in place based on the value of year
    r.sort(key = lambda x: x["year"])

    # Now we can plot the top 5 using another program.
