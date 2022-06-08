import serial
import math
import time
import json

port = "/dev/ttyAMA4"
sonuc={}
def parseGPS(data):
	if data[0:6]==b"$GPRMC":
		s=data.split(b",")
		if s[7]=='0':
			print("Uydu verisine erisilemiyor")
			return
		time=str(s[1][0:2]) + ":" + str(s[1][2:4]) + ":" + str(s[1][4:6])
		lat=(str(s[3]).lstrip('b'))#Latitude
		a=(lat[1:3]).lstrip("")
		b=(lat[3:10]).rstrip("'")
		#c=int(a+b/60)
		d=lat[:2]
		DD=float(a)
		MM=float(b)
		LatDec=DD+MM/60
		
		lon=(str(s[5]).lstrip('b'))#Longitude
		a2=(lon[1:4]).lstrip("'")
		b2=(lon[4:10]).rstrip("'")
		DD2=float(a2)
		MM2=float(b2)
		LonDec=DD2+MM2/60
		
		print("Latitude:" + str(LatDec)[:10],"Longitude:" + str(LonDec)[:10])
		#print("Latitude: %s -- Longitude:%s" %((lat),((lon))))
		
		new_json={"Latitude":str(LatDec)[:10],"Longitude":str(LonDec)[:10]}
		sonuc=json.dumps(new_json)
		file=open('gps.json','w+')
		file.write(sonuc)
		file.close()
def decdegNmea2(dd):
    num =abs(float(dd))
    d=float(math.floor(num))
    m=num - d
    sign= '-' if dd < 0 else ''
    return sign+ '%03i%02.5f' %(int(d),m *60.00)
# def decode(coord):
# 	
# 	v= coord.split(",")
# 	head=v[0]
# # 	tail=v[2]
# 	deg=head[0:2]
# 	min=head[-2:]
# 	return deg + min + "," + tail
	
ser = serial.Serial(port,9600,timeout = 0.5)
ser.flushInput() #Cakısan veri olmaması icin yazılır
while True:
	data=ser.readline()
	#data=data2.decode("utf-8")
#	print(data)
	parseGPS(data)
	time.sleep(0.8)
	
			
