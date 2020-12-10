#
# Example from StackOverflow: 
# https://stackoverflow.com/questions/23219218/formatting-x-axis-with-dates-format-matplotlib
#
# Formatting X axis with dates format Matplotlib. You have a list of floats representing dates, i.e.:
# [20140421.0, 20140417.0, 20140416.0, 20140415.0]. How do you do to plot these floats as dates in
# the X-axis
#
import numpy as np
import pdb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime as dt

# Original data

raw_x = [20140421.0, 20140417.0, 20140416.0, 20140415.0, 20140414.0, 20140411.0, 20140410.0]
y = [531.17, 524.94, 519.01, 517.96, 521.68, 519.61, 523.48]

# Convert your x-data into an appropriate format.

# date_fmt is a string giving the correct format for your data. In this case
# we are using 'YYYYMMDD.0' as your dates are actually floats.
date_fmt = '%Y%m%d.0'

# Use a list comprehension to convert your dates into datetime objects.
# In the list comp. strptime is used to convert from a string to a datetime
# object.
dt_x = [dt.datetime.strptime(str(i), date_fmt) for i in raw_x]

# Finally we convert the datetime objects into the format used by matplotlib
# in plotting using matplotlib.dates.date2num
x = [mdates.date2num(i) for i in dt_x]

# Now to actually plot your data.
fig, ax = plt.subplots()

# Use plot_date rather than plot when dealing with time data.
ax.plot_date(x, y, 'bo-')

# Create a DateFormatter object which will format your tick labels properly.
# As given in your question I have chosen "YYMMDD"
date_formatter = mdates.DateFormatter('%y%m%d')

# Set the major tick formatter to use your date formatter.
ax.xaxis.set_major_formatter(date_formatter)

# This simply rotates the x-axis tick labels slightly so they fit nicely.
fig.autofmt_xdate()

plt.show()
print("h\n")