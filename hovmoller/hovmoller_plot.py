import os, datetime
import datetime
from datetime import timedelta, date
import numpy as np
from numpy import newaxis
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid
import mpl_toolkits.basemap
from collections import deque
from matplotlib.mlab import griddata
import netCDF4 as nc
import sys
import gc
import time
import math
from scipy import interpolate

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#User defined area ******************
threshold = 0.25 #threshold for ETS in inches
lower_lon = -105.0
upper_lon = -80.0
lower_lat = 30.0
mid_lat = 40.0
upper_lat = 50.0
lons_interval = 0.2
lats_box_lower = [lower_lat,mid_lat]
lats_box_upper = [mid_lat,upper_lat]
lons_box = [lower_lon,upper_lon]
lons_list = np.arange(lower_lon,upper_lon+(lons_interval/2.),lons_interval)
hours = (range(13,24)+range(0,13))
hourly_samples = [0.0]*len(hours)
