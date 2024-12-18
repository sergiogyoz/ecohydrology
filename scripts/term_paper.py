#%%
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
sb.set_style("whitegrid")
#%%
pathBAR = "../term paper/AMF covariance station Barataria/AMF_US-LA3_BASE-BADM_1-5/AMF_US-LA3_BASE_HH_1-5.csv"
pathSAL = "../term paper/AMF covariance station Salvador/AMF_US-LA2_BASE-BADM_3-5/AMF_US-LA2_BASE_HH_3-5.csv"

Barataria = pd.read_csv(pathBAR, skiprows=2, na_values=[-9999])
Barataria["datetime"] = pd.to_datetime(Barataria["TIMESTAMP_START"] ,format="%Y%m%d%H%M")

Salvador = pd.read_csv(pathBAR, skiprows=2, na_values=[-9999])
Salvador["datetime"] = pd.to_datetime(Barataria["TIMESTAMP_START"] ,format="%Y%m%d%H%M")
#%%
Vars=["datetime", "NETRAD_1_1_1", "SWC_1_1_1", "RH_1_1_1", "TA_1_1_1", "TS_1_1_1"]
Barataria = Barataria[Vars]
Salvador = Salvador[Vars]
rename = {
    "datetime":"time",
    "NETRAD_1_1_1":"radiation",
    "SWC_1_1_1":"soil moisture",
    "RH_1_1_1":"relative humidity",
    "TA_1_1_1":"air temperature",
    "TS_1_1_1":"soil temperature"}
Barataria.rename(columns = rename, inplace=True)
Salvador.rename(columns = rename, inplace=True)
Vars = ["radiation", "soil moisture", "relative humidity", "air temperature", "soil temperature"]

#%%
Colors = ["#ffbe0b","#fb5607","#ff006e","#8338ec","#3a86ff"]
Sizes = [1,10,1,1,10]
for var, color, size in zip(Vars, Colors, Sizes):
    Barataria.plot.scatter(x="time", y = var, c=color, s=size, figsize=(10, 4))

#%%
fig2, axes2 = plt.subplots(nrows=5, ncols=1)
for i in range(len(Vars)):
    Salvador.plot.scatter(x="time", y = Vars[i], ax = axes2[i], s = 1)

# %%

Barataria["time"][pd.notna(Barataria["soil temperature"])]



# %%
