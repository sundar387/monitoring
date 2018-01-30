import psutil
import math
import os

class monitor():
	cpu_per=psutil.cpu_percent(interval=None, percpu=False)
	val=psutil.virtual_memory()
	totphys, availphys, percent, used, free = val
	per=percent
	total=cpu_per+(per)/10
	average=round((total/2)*10)
	print("Load Balancing" ,average,"%")
	
