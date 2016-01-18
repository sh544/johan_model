#Move into the directory on the network drive we copied the files to (assuming Diane has given you access)
cd /data/NAS-geo01/ph290/sarah/50_year_hindcast_v2/annual_av

#Launch python (once you've installed iris - https://wiki.exeter.ac.uk/display/HalloranResearchMain/Installing+Python+Iris+Cartopy+on+Ubuntu)
python2.7

#Import the required modules:
import iris
import iris.quickplot as qplt
import matplotlib.pyplot as plt

#Specify the file you want to look at
file = 'ns_bfm_annual_ave.3d.nc'

#Load all of the metadata from that file so you can see what variables there are
metadata_cube = iris.load(file)

#Display those variables:
print metadata_cube

#Find the variables you want, and load them in and plot them:
filter_feeder_cube = iris.load_cube(file,'net filterfeeder produc.')

#Average the data through time:
filter_feeder_cube_avg = filter_feeder_cube.collapsed('time',iris.analysis.MEAN)

#Plot the data
qplt.contourf(filter_feeder_cube_avg,51)
plt.show() 
