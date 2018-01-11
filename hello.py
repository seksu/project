
############### CONFIG ##############

ftpAddr 	= '161.246.5.152'
ftpUser		= 'root'
ftpPass	 	= '123456'
ftpDir		= 'ipcam'
token		= 'a121'

#####################################

import pylab
import cv2
#import imageio
from time import gmtime
from ftplib import FTP
from urllib import urlretrieve
import os

ftp = FTP(ftpAddr)     							
ftp.login(ftpUser,ftpPass)

minStore 	 	= ''
listFileName 	= [] 

while 1:
	year 	= str(gmtime().tm_year)
	month 	= str(gmtime().tm_mon)
	day 	= str(gmtime().tm_mday)
	hour 	= str((gmtime().tm_hour+7)%24)
	minute 	= str((gmtime().tm_min-1)%60)
	sec 	= str(gmtime().tm_sec)

	minStore = minute

	ftp.cwd("/ipcam/"+year+""+month+""+day+"/"+hour+"00/")
	currentVideo = ftp.nlst()

	for filename_video in currentVideo:
		if(filename_video.startswith(token+year+month+day+hour+minStore) and filename_video.endswith(".avi")):
			non = True
			for name in listFileName:
				if(filename_video == name):
					non = False
			if(non == True):
				listFileName.append(filename_video)
				print(filename_video)
			if(minStore != minute):
				minStore = minute
				listFileName = []

#urlretrieve("ftp://"+ftpUser+":"+ftpPass+"@"+ftpAddr+"/ipcam/"+year+""+mouth+""+day+"/"+hour+"00/"+token+""+year+""+mouth+""+hour+,"source/input.avi")

#filename = '/home/pansek/workspace/source/input.avi'
#vid = imageio.get_reader(filename,  'ffmpeg')

#image = vid.get_data(100)

#rgbImg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# print(year)
# print(month)
# print(day)
# print(hour)
# print(minute)
# print(sec)


#cv2.waitKey(0)
#cv2.destroyAllWindows()