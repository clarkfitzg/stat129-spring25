# /opt/anaconda/bin/ipython
# ^ run with this ^

import os

from lxml import etree

datadir = "/stat129/tax23/"
all990 = [datadir + p for p in os.listdir(datadir)]

def extract(xmlfile):
    tree = etree.parse(xmlfile)
    result = {}

    try:
        result["mission"] = tree.xpath("/Return/ReturnData/IRS990/ActivityOrMissionDesc/text()")[0]
        result["year"] = int(tree.xpath("/Return/ReturnData/IRS990/FormationYr/text()")[0])
        result["website"] = tree.xpath("/Return/ReturnData/IRS990/WebsiteAddressTxt/text()")[0]
    except:
        return None

    return result


# Change this to True to process the entire data set.
if False: 
    from multiprocessing import Pool
    with Pool(10) as p:
        r = p.map(extract, all990)

    r = [x for x in r if x is not None]

    print("worked on:", len(r))
    print("failed on:", len(all990) - len(r))
    # Just over one third worked.
    # Well, we just have to go in and see why that happens!
