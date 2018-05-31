import random
import numpy
import matplotlib.pyplot as plt



x = [ 1, 2, 3, 4, 5]
#NB of TXed frames  for hostA
y1= [30,32,28,15,5]
#NB of RXed frames  for hostA
y2= [29,31,25,15,5]
#NB of dropped frames  for hostA
y3= [55,50,40,19,11]

#NB of TXed frames  for hostX
y4= [29,27,32,17,11]
#NB of RXed frames  for hostX
y5= [28,26,29,17,11]
#NB of dropped frames  for hostX
y6= [0,4,6,1,0]

# #NB of TXed frames  for hostX
# y7= [38]
# #NB of RXed frames  for hostX
# y8= [37]
# #NB of dropped frames  for hostX
# y9= [21]
#
# #NB of TXed frames  for hostA
# y10= [37]
# #NB of RXed frames  for hostA
# y11= [19]
# #NB of dropped frames  for hostA
# y12= [23]
#




plt.figure(figsize=(16,6))
plt.plot(x,y1,color='red')
plt.plot(x,y2,color='red',dashes=(2,4))
#plt.plot(x,y3,color='blue')

plt.plot(x,y4,color='green')
plt.plot(x,y5,color='green',dashes=(2,4))
#plt.plot(x,y6,color='blue',dashes=(2,4))

# plt.plot(x,y7,'r--')
# plt.plot(x,y8,'g^')
# plt.plot(x,y9,'bs')
#
# plt.plot(x,y10,'r--')
# plt.plot(x,y11,'g^')
# plt.plot(x,y12,'bs')

plt.xticks([1,2,3,4,5], ['exp(2ms)','exp(5ms)','exp(10ms)','exp(30ms)','exp(60ms)'])
plt.title('CSMA protocol - SCENERIO 3')
plt.xlabel('Interval Time')
plt.ylabel('Packet Number')
plt.ylim((0,40))
plt.legend(['TXed frames by hostA','TXed frames by hostC','RXed frames of hostC','RXed frames of hostD'])
plt.show()

