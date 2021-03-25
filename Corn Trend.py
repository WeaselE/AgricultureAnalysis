# Source: https://www.ers.usda.gov/data-products/feed-grains-database/feed-grains-yearbook-tables/

import pandas as pd
from skimage import io as sk
import matplotlib as plt


with open("FeedGrains.csv", "r") as fl:
    df = pd.read_csv(fl)
    print(df.head(1))
    # commodity_t = pd.series(df, index=["SC_GroupCommod_Desc", ""]
    # print(commodity_t)