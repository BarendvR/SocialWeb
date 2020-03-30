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
  * [Quickstart](#Quickstart)
  * [Data](#data)
  * [The network](#the-network)
  * [Research question](#rq)
  * [The Results](#results)
  * [Thesis](#thesis)    
<!--te-->
# Quickstart

Install [Jupyter notebook](https://jupyter.org/install) `pip install jupyterlab`

Install [Plotly](https://github.com/plotly/plotly.py) `pip install "notebook>=5.3" "ipywidgets>=7.2"`

Put the data folder in the same folder as the notebooks.

If you only have the source data run the [Data notebook](Data.ipynb) first.

If you have the full processed data you can start by running the other notebooks.

# Data 
We gathered our Twitter data via scrapting using a slightly modified version of the scraper found at: https://github.com/Jefferson-Henrique/GetOldTweets-python

Because of the Twitter ToS we can not make our data publicly available, but if you want acces to the data please contact us at barendvanrooij@gmail.com and we will see what we can do.

The COVID-19 statistics used in this project came from https://github.com/CSSEGISandData/COVID-19/
The file 'casesDeathRecoveries.py' contains the Python script that gets the data provided by that git repository. It outputs the current total number of confirmed coronavirus cases, deaths and recoveries. It also exports the number of confirmed cases, deaths and recoveries per day to CSV files and plots this data on a graph.

The data is further processed and explored in:
[Data notebook](Data.ipynb)  

# Data visualization

[Plotly](https://github.com/plotly/plotly.py) was used for an interactive plot design. Unfortunately github does not show these plots. Therefore, a .PNG file for each plot can be found in the [Plots](Plots) folder.

To see the the interactive graphs in action a local run of the notebooks is needed. 

The [data visualization notebook](Data-visualization.ipynb) visualizes the data gathered.

# Hype

The [Hype notebook](Hype.ipynb) calculates and visualizes the twitter hype. 

# Tweet analysis

The [Tweet analysis notebook](Tweet-analysis.ipynb) looks at the content of tweets and their populairity. Certain part take over an hour to run and everything should be visible on github. Therefore, it is not recommanded to run this notebook


