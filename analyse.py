import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Data.csv")
print (data)
print (data.columns.values)
gb = data.groupby("Протокол")
print (gb.groups)
data["cis_trans"] = data["cis"] / data["trans"]
def f(x):
    if x.find("Ma ") != -1:
        return "Ma et al."
    elif x.find("Ramani") != -1:
        return "Ramani et al."

def f2(x):
    try:
        x = int(x)
    except:
        x = -1
    if x==4:
        print ("----------")
        print(x)
        print (0<x<9)
    if 0<x<9:
        return "1st batch"
    elif 41<=x<=48:
        return "2nd batch"
    elif 55<=x<=66:
        return "3rd batch"
    elif 67<=x<=77:
        return "4th batch"
    elif 78<=x<=89:
        return "5th batch"
    else:
        return 0

data["group"] = data["Код сиквенса (S)"].apply(f2)
data.query("group != 0", inplace=True)
print (data["group"].values)
sns.set(font_scale = 2)
sns.boxplot(x = "group", y = "Enrichment Average", data = data)
sns.swarmplot(x = "group", y = "Enrichment Average", data = data)

plt.show()