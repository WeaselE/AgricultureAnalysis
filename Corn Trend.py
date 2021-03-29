# Source: https://www.ers.usda.gov/data-products/feed-grains-database/feed-grains-yearbook-tables/

import pandas as pd
import matplotlib.pyplot as plt


with open("FeedGrains.csv", "r") as fl:
    df = pd.read_csv(fl)
    #Finding Info for corn
    df_corn = df.query("SC_Commodity_Desc == 'Corn' & SC_Attribute_Desc == 'Prices received by farmers' & SC_Frequency_Desc == 'Annual'")
    df_corn = df_corn.sort_values(by="Year_ID")
    #Plotting corn information
    plt.plot(df_corn["Year_ID"], df_corn["Amount"], label="Corn")
    #Find info for Barley feed
    df_barley = df.query("SC_Commodity_Desc == 'Barley feed' & SC_Attribute_Desc == 'Prices received by farmers' & SC_Frequency_Desc == 'Annual'")
    df_barley = df_barley.sort_values(by="Year_ID")
    #Plotting Barley feed info
    plt.plot(df_barley["Year_ID"], df_barley["Amount"], label="Barley feed")
    #Find info for Oats
    df_oats = df.query("SC_Commodity_Desc == 'Oats' & SC_Attribute_Desc == 'Prices received by farmers' & SC_Frequency_Desc == 'Annual'")
    df_oats = df_oats.sort_values(by="Year_ID")
    #Plotting oats info
    plt.plot(df_oats["Year_ID"], df_oats["Amount"], label="Oats")
    #Final plot setup, then show and save to png
    plt.xlabel("Year")
    plt.ylabel("Dollars per Bushel (Annual)")
    plt.legend()
    plt.xlim([1866, 2020])
    plt.xticks([i for i in range(2020, 1866, -15)])
    plt.savefig("Grain Prices for Farmers, Annually.png", dpi=1000)