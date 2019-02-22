import datetime
import requests
import time
import zipfile
from os import listdir
from os.path import isfile, join

currentDate = datetime.datetime(2018, 12, 10)
zipPath = '/Users/prateeag/Downloads/zips/'
csvPath = '/Users/prateeag/Downloads/csvs/'

zipList = []

def getURL(date):
	day = str(date.day)
	month = date.month
	year = str(date.year)
	if day<10:
		day = '0' + day

	if month==1:
		month = 'JAN'
	elif month==2:
		month = 'FEB'
	elif month==3:
		month = 'MAR'
	elif month==4:
		month = 'APR'
	elif month==5:
		month = 'MAY'
	elif month==6:
		month = 'JUN'
	elif month==7:
		month = 'JUL'
	elif month==8:
		month = 'AUG'
	elif month==9:
		month = 'SEP'
	elif month==10:
		month = 'OCT'
	elif month==11:
		month = 'NOV'
	elif month==12:
		month = 'DEC'

	url = 'https://www.nseindia.com/content/historical/EQUITIES/' + year + '/' + month + '/' + 'cm' + day + month + year + 'bhav.csv.zip'
	print url
	return url

def getDateString(date):
	return str(date.day) + "-" + str(date.month) + "-" + str(date.year) + ".zip"

for i in range(10):
	url = getURL(currentDate)
	r = requests.get(url)
	fileName = getDateString(currentDate)
	open(zipPath + fileName, "wb").write(r.content)
	zipList.append(fileName)
	currentDate+=datetime.timedelta(days=1)

for fl in zipList:
	try:
		zip_ref = zipfile.ZipFile(zipPath + fl, 'r')
		zip_ref.extractall(csvPath)
		print zipPath + fl
	except:
		print 'File not present: ' + fl
