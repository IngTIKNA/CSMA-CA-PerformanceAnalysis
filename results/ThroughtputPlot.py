import pandas as pd
from matplotlib import pyplot
from matplotlib import colors

df = pd.read_csv('CSMA.csv', sep=',')

res = df.query('name == "rcvdPk:sum(packetBytes)"')

a = ['WirelessA2.hostB.udpApp[0]', 'WirelessA2.hostPU2.udpApp[0]']
c = res[res['module'].isin(a)]['value'].dropna()
time=0.5   # 0.5 sec
throughput1 = c*time

asd = pyplot.hist2d( [0,1], throughput1, ])


pyplot.show(asd)

