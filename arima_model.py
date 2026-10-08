import pandas as pd
import matplotlib.pyplot as plt

#  Load the dataset
data = pd.read_csv('euriborkorot_pv_chrt_fi.csv')
print(data.head())
#data['date'] = pd.to_datetime(data['date'])
#data.set_index('date', inplace=True)
#Plot the time series
#plt.plot(data['euribor'])
#plt.title('Daily Euribor Rates')
#plt.xlabel('date')
#plt.ylabel('Euribor Rate')
#plt.show()