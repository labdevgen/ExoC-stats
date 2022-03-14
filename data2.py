import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("Data2.ods", engine="odf")
print (data)
print (pd.melt(data))

sns.boxplot(x="variable", y="value", data=pd.melt(data))
plt.xlabel("Pool")
plt.ylabel("Average enrichment")
plt.savefig("enrichment.png", dpi=600)
plt.show()