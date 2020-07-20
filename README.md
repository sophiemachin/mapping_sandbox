# Mapping sandbox project

## General information

A sandbox environment for testing folium chloropleth maps

The folium project can be viewed here:

https://python-visualization.github.io/folium/

## Usage

This project takes CSV data and json map files and combines them into html that can be used to visualise data. 

### As a server

To run the server:

  python flaskapp.py
  
You can then make calls to http://127.0.0.1:5000

### To generate one-off html files

The project also has files to generate one-off html files for static sites. To generate an html file you will need

* some json map data
* some csv data to plot

#### Json cleaner

`json_cleaner.py` cleans files from http://geoportal.statistics.gov.uk/search 

Each type of file is slightly different. It is currently set up to clean European Electoral Regions December 2018 Boundaries UK.

#### CSV file

The CSV data should have the same regions as the map regions, and a possible data point for each region. 

#### Generate the html

Run `folium_chloropleth.py` to generate an html file. It is currently set up to read the output from the json cleaner above. The html is not centred or zoomed perfectly on the UK, rather it is a compromise between showing the mainland in as much detail as possible while also included as many islands as possible. 


The output html file can be used, for example, in an iframe in a static website. 
