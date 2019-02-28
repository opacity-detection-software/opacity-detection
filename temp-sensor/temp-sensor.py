
import pigpio
from time import sleep
# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()
print("run")

import Adafruit_DHT as dht
h,t = dht.read_retry(dht.DHT22, 4)
print ('Temp1={0:0.1f}*C Humidity1={1:0.1f}%'.format(t, h))
h2,t2 = dht.read_retry(dht.DHT22, 22)
print ('Temp2={0:0.1f}*C Humidity2={1:0.1f}%'.format(t2, h2))