import sys
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
from datetime import date
import csv

#List of countries in the EU
euCountriesList = ["austria","belgium","bulgaria","croatia","cyprus","czech republic","denmark","estonia","finland","france","germany","greece","hungary","ireland",
"italy","latvia","lithuania","luxembourg","malta","netherlands","poland","portugal","romania ","slovakia","slovenia","spain","sweden"]

#List of countries in Europe
euroCountriesList = ["andorra","armenia","austria","azerbaijan","belarus","belgium","bosnia and herzegovina","bulgaria","croatia","cyprus","czech republic","denmark",
"estonia","finland","france","georgia","germany","greece","hungary","iceland","ireland","italy","kazakhstan","kosovo","latvia","liechtenstein","lithuania","luxembourg",
"malta","moldova","monaco","montenegro","netherlands","north macedonia","norway","poland","portugal","romania","russia","san marino","serbia","slovakia","slovenia",
"spain","sweden","switzerland","turkey","ukraine","united kingdom","vatican city"]

#Plots the cases/deaths/recoveries to a graph
def plotCases(columns, europe, EU, nonEurope, yTag):
    dates = []
    numberOfCasesInEurope = []
    numberOfCasesOutside = []
    totalCases = []

    #Set the counter to 0 for all the given dates
    for i in range(len(columns) - 4):
        dates.append(columns[i + 4])
        numberOfCasesInEurope.append(0)
        numberOfCasesOutside.append(0)
        totalCases.append(0)

    #Loop through all the european countries
    for location in europe:
        #Loop through this location's cases
        for i in range(len(columns) - 4):
            #Add up the number of cases
            numberOfCasesInEurope[i] = int(numberOfCasesInEurope[i]) + int(location[i + 4])
            totalCases[i] = int(totalCases[i]) + int(location[i + 4])

    #Loop through all the non-european countries
    for location in nonEurope:
        #Loop through this location's cases
        for i in range(len(columns) - 4):
            #Add up the number of cases
            numberOfCasesOutside[i] = int(numberOfCasesOutside[i]) + int(location[i + 4])
            totalCases[i] = int(totalCases[i]) + int(location[i + 4])

    # plotting the points
    plt.plot(dates, numberOfCasesInEurope, label="europe")
    plt.plot(dates, numberOfCasesOutside, label="non-europe")
    plt.plot(dates, totalCases, label="total")

    # naming the x axis
    plt.xlabel('timeline')
    # naming the y axis
    plt.ylabel(yTag)

    # giving a title to my graph
    plt.title('Confirmed cases over time')

    #Rotate the x-axis labels
    plt.xticks(rotation=90, fontsize='x-small')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

#Get the number of cases/deaths/recoveries from Github
def getCases(printWord, csvUrl, yTag):
    #Get the page HTML
    url = urllib.request.urlopen(csvUrl)
    bytes = url.read()
    html = bytes.decode("utf8")

    columns = []

    #Get the column names from the page HTML
    for row in BeautifulSoup(html, features="html.parser")("th"):
        columnText = re.sub("<th>", "", str(row))
        columnText = re.sub("</th>", "", columnText)
        columns.append(columnText)

    #Get the table data from the page HTML
    table_data = [[cell.text for cell in row("td")]
        for row in BeautifulSoup(html, features="html.parser")("tr")]

    #The first value of the table data is empty, so we toss it
    table_data.pop(0)

    europe = []
    EU = []
    nonEurope = []
    NL = []

    euroCountList = []
    euCountList = []
    nonEuroCountList = []

    #Create the correct number of indices (one for each recorded day)
    for column in range(4, (len(columns))):
        euroCountList.append(0)
        euCountList.append(0)
        nonEuroCountList.append(0)

    #Look through the rows
    for row in table_data:
        #The first item is empty
        row.pop(0)

        #[0] = province/state
        #[1] = country/region
        #[2] = lattitude
        #[3] = longitude
        #The rest of the columns are columns containing the number of confirmed cases on a specific date
        #So in order to get the total number of confirmed cases we look at the last column

        #If this is a European country
        if (row[1].lower() in euroCountriesList):
            #Add it to the Europe list
            europe.append(row)

            #Add the number of cases on this
            for index in range(0, len(row) - 4):
                euroCountList[index] += int(row[index + 4])

            #If this country is in the EU
            if (row[1].lower() in euCountriesList):
                #Add it to the EU list
                EU.append(row)

                #For each recorded day
                for index in range(0, len(row) - 4):
                    #Add the cases from this country to the counter of that day
                    euCountList[index] += int(row[index + 4])

                #Save the Netherlands as a separate row
                if (row[1].lower() == "netherlands"):
                    NL = row
        #If this is not a European country
        else:
            #Save it to the non-European list
            nonEurope.append(row)

            #For each recorded day
            for index in range(0, len(row) - 4):
                #Add the cases from this country to the counter of that day
                nonEuroCountList[index] += int(row[index + 4])

    #Write the data to CSV
    csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Location'] + columns[4:(len(columns))])
    csv_writer.writerow(['Netherlands'] + NL[4:(len(NL))])
    csv_writer.writerow(['Europe'] + euroCountList)
    csv_writer.writerow(['EU'] + euCountList)
    csv_writer.writerow(['Non-Europe'] + nonEuroCountList)

    #Add up the total counts for each day
    totalCountList = [];
    for index in range(0, len(euroCountList)):
        totalCountList.append(int(euroCountList[index]) + int(nonEuroCountList[index]))

    csv_writer.writerow(['Worldwide'] + totalCountList)

    euroCounter = 0
    euCounter = 0

    #Loop through the locations in Europe
    for location in europe:
        #Add the total count of the current location to the Europe counter
        euroCounter += int(location[len(location) - 1])
        #Do the same for the EU counter
        if (location[1].lower() in euCountriesList):
            euCounter += int(location[len(location) - 1])

    otherCounter = 0

    #Loop through the locations outside of Europe
    for location in nonEurope:
        #Add the total count of the current location to the counter
        otherCounter += int(location[len(location) - 1])

    #Print the results
    print("Confirmed " + printWord + " in Europe: " + str(euroCounter))
    print("Of which EU member states: " + str(euCounter))
    print("Confirmed " + printWord + " outside of Europe: " + str(otherCounter))
    print("Total " + printWord + " worldwide: " + str(otherCounter + euroCounter))
    print(" ")

    #Plot the confirmed cases
    plotCases(columns, europe, EU, nonEurope, 'confirmed cases')

#Get the confirmed cases
with open('confirmedCases.csv', mode='w') as csv_output:
    getCases('cases', "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv", 'confirmed cases')

#Get the confirmed deaths
with open('confirmedDeaths.csv', mode='w') as csv_output:
    getCases('deaths', "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv", 'confirmed deaths')

#Get the confirmed recoveries
with open('confirmedRecoveries.csv', mode='w') as csv_output:
    getCases('recoveries', "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv", 'confirmed recoveries')
