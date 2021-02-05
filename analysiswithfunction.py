#import modules
import matplotlib.pyplot as plt
import pandas as pd

#read the csv file
coviddata = pd.read_csv("national_trends.csv", header=0)

#this section is the first chart. It is a blue line that represents the total confirmed cases in Italy.
#this section also labels the x and y axis as well as the chart title
plt.plot(coviddata['date'], coviddata['total_confirmed_cases'], color='blue')
plt.ylabel('Total Confirmed Cases (Blue) | Total Deaths (Red)')
plt.xlabel('Date')
plt.title('Covid-19 Trends in Italy')

#this section makes the second line in the same graph as the one above. This line is read and represents the total deaths in Italy.
plt.plot(coviddata['date'], coviddata['deaths'], color='red')
plt.show()

#this section makes a new (2nd) graph. It represents the new cases confirmed each day in Italy.
plt.plot(coviddata['date'], coviddata['new_total_confirmed_cases'], color='green')
plt.ylabel('Cases')
plt.xlabel('Date')
plt.title('New Cases Confirmed Each Day')
plt.show()

#this function finds the minimum, maximum, and average for different parts of the data.
def minmaxavg(column, description):
    #set up variables
    mini = coviddata[column][0]
    maxi = coviddata[column][0]
    mindate = coviddata['date'][0]
    maxdate = coviddata['date'][0]
    sum_ = 0
    avg = 0

    for i in range(0, len(coviddata[column])):
        if (coviddata[column][i] < mini):
            mini = coviddata[column][i]
            mindate = coviddata['date'][i]
        if (coviddata[column][i] > maxi):
            maxi = coviddata[column][i]
            maxdate = coviddata['date'][i]
            sum_ = sum_ + coviddata[column][i]
        
    avg = sum_/len(coviddata[column])
    print("The minimum", description, "is:", mini, "which occured in", mindate)
    print("The maximum", description, "is:", maxi, "which occured in", maxdate)
    print("The average", description, "is:", avg)

print("MIN/MAX/AVG FOR DEATHS")
minmaxavg('deaths', 'deaths')

print("MIN/MAX/AVG FOR TOTAL CONFIRMED CASES")
minmaxavg('total_confirmed_cases', 'total confirmed cases')

print("MIN/MAX/AVG FOR CONFIRMED CASES PER DAY")
minmaxavg('new_total_confirmed_cases', 'confirmed cases per day')