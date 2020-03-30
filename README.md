# SocialWeb: Final Report - Project Group 26

|Name|Student ID|Email|
|---	|---	|---	|
|Barend van Rooij|2563934|b.w.vanrooij@student.vu.nl|
|Jakob Kyselica|2593776|j.m.kyselica@student.vu.nl|
|Noah Voogd|2666711|s.n.voogd@student.vu.nl|
|Mark Limudjianto|2687882|m.o.limudjianto@student.vu.nl|
|Mees Bulder|2682775|m.r.j.bulder@student.vu.nl|

## How Does Hype Surrounding a Viral Epidemic Evolve Over Its Lifespan?

Vrije universiteit Information science Social web course project about coronavirus.

# Table of contents


<!--ts-->
  * [Table of contents](#table-of-contents)
  * [Data](#data)
  * [How to run](#how-to-run)
  * [The network](#the-network)
  * [Research question](#rq)
  * [The Results](#results)
  * [Thesis](#thesis)    
<!--te-->

# Data 
We gathered our Twitter data via scrapting using a slightly modified version of the scraper found at: https://github.com/Jefferson-Henrique/GetOldTweets-python

Because of the Twitter ToS we can not make our data publicly available, but if you want acces to the data please contact us at barendvanrooij@gmail.com and we will see what we can do.

The COVID-19 statistics used in this project came from https://github.com/CSSEGISandData/COVID-19/
The file 'casesDeathRecoveries.py' contains the Python script that gets the data provided by that git repository. It outputs the current total number of confirmed coronavirus cases, deaths and recoveries. It also exports the number of confirmed cases, deaths and recoveries per day to CSV files and plots this data on a graph.

The data is further processed and explored in:
[Data notebook](Data.ipynb)  

# The network  
[The network notebook](CreatingNetwork.ipynb)
  
# RQ
How do hyper-parameters like a weight threshold for authors impact the measures of a network for ranking data science conferences and journals?

# Results
[The results notebook](Results.ipynb)  

# Thesis
[Thesis pdf](Thesis_Barend_van_Rooij.pdf)

