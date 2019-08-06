###########################################################################
# MainRead001002.py

# Description: An example of how to import wave drifter observations from
# xx001/002 to python3 and plot the observations on the global map
###########################################################################
#
# User Defined Variables
filename='../test/b001/xx102' #Complete path of the dataset location and filename
varname='SGWH' #Variable name to be imported; user can define more than one but they should belong to the same replication.

print('Data corresponding to the following mnemonic(s):', varname, 'will be imported' \
      ' from the ', filename)

# import observations
import importbufr
values = importbufr.read_001002(varname, filename)

# plot imported observations
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
plt.scatter(values['longitude'], values['latitude'],values[varname],cmap='afmhot')
plt.colorbar()
plt.show()
