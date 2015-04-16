from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt


# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)

# Drop null rows
 
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print freq

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())
print chi
print p
 
