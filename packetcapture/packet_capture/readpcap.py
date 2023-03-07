import pandas as pd
df=pd.read_csv('/home/thirupathi/PycharmProjects/networkpython/analysethepacket/capturedpacket.csv')
print(df.columns)
print(df.groupby('Protocol').sum())