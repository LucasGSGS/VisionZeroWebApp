import numpy
import pytz
import os
import multiprocessing
import pandas
import importlib
import sys

tz="America/New_York"
region=pytz.timezone(tz)

N_trips=500 #set to None if use all trips.
outdir="TEMP/"
# in case of mistake, don't overwrite data.p;
# manuall move from TEMP to desired directory
dataFile=outdir+"data.p"
statsFile=outdir+"stats.txt"
#put curves in desired directory
curveFile="curve.png" #put curve in data directory

scatterFile="scatter.png" #put curve in data directory
accident_HTML=outdir+"accidents.html"
origins_HTML=outdir+"origins.html"
destinations_HTML=outdir+"destinations.html"

alphaList=numpy.arange(0,1,step=0.1)

dirnames=[#"", #current directory
	"FINAL_Manhattan_All",
	"FINAL_Manhattan_EveningMorning",
	"FINAL_Manhattan_Morning_RushHour",
	"FINAL_Manhattan_Midday",
	"FINAL_Manhattan_Evening_RushHour"]

def windower(d=0):
	try:
		d=int(d)
		return importlib.import_module(dirnames[d]+".windower")
	except Exception as e:
		print("directory name index should be 0-4")
		print(e)
		sys.exit()
	

accident_directory="DATA_Accidents"
traveltime_directory="DATA_Traveltimes"
trip_directory="DATA_Trips"


class accidents:
	@staticmethod
	def processor(full_input):
		(fname,windower)=full_input
		data=pandas.read_pickle(fname)
		if windower is not None:
			flags=data["datetime"].apply(windower)
			data=data[flags]
		return data

	def __new__(cls,windower=None):
		directory=accident_directory
		fnames=[directory+"/"+fname for fname in 
			os.listdir(directory+"/") if 
				fname.endswith(".p")]

		inputList=[(fname,windower) for fname in fnames]
		p=multiprocessing.Pool()
		out=p.map(cls.processor,inputList)
		return pandas.concat(out,axis="index")

class trips:
	@staticmethod
	def processor(full_input):
		(fname,windower)=full_input
		data=pandas.read_pickle(fname)
		if windower is not None:
			flags=data["origin_datetime"].apply(windower)
			data=data[flags]
		return data

	def __new__(cls,windower=None):
		directory=trip_directory
		fnames=[directory+"/"+fname for fname in 
			os.listdir(directory+"/") if 
				fname.endswith(".p")]

		inputList=[(fname,windower) for fname in fnames]
		p=multiprocessing.Pool()
		out=p.map(cls.processor,inputList)
		return pandas.concat(out,axis="index")

class traveltimes:
	@staticmethod
	def processor(full_input):
		(fname,windower)=full_input
		data=pandas.read_pickle(fname)
		if windower is not None:
			flags=data["datetime"].apply(windower)
			data=data[flags]
		return data

	def __new__(cls,windower=None):
		directory=traveltime_directory
		fnames=[directory+"/"+fname for fname in 
			os.listdir(directory+"/") if 
				fname.endswith(".p")]

		inputList=[(fname,windower) for fname in fnames]
		p=multiprocessing.Pool()
		out=p.map(cls.processor,inputList)
		out= pandas.concat(out,axis="index")
		return out