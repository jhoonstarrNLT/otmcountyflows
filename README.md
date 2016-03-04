# otmcountyflows

This package includes a few scripts and zip files from onthemap.ces.census.gov for use in creating a county to county flows matrix.

Produced for a tutorial at the 2016 LEHD workshop.

## What does this do?

A county to county flow matrix will show a large table of the relationships between home and work locations in the LODES dataset. For example, how many persons travel from county A to county B for work? From county B to county A? What if there are 100 counties in my region, what then? This process is a way to run analyses and organize the data so that an area with 100 counties can be boiled down into a single csv or excel table. 

## What is this example?

This specific example takes all counties in the state of Maryland and creates a single table. This table shows the home-work employment relationship for workers in all counties, to all counties across the entire state. Here  is a small subset of the output:

    +--------------+------------+--------------+-----------+
    |              |  Alleganey | Anne Arundel | Baltimore |
    +--------------+------------+--------------+-----------+
    | Alleganey    |  15655     |   226	       |  361      |
    | Anne Arundel |  673       |   95352      |  28330    |
    | Baltimore    |  574       |   19084      |  148749   |
    +--------------+------------+--------------+-----------+
  
In this case, our left column will be the  user selected home or work county. So for this example, using the default OnTheMap settings, the left column is the 'Work' county and the top is the 'Home'. So approximately 15k people live and work in Alleganey county. Only 226 work in Allegany and live in Anne Arundel. On the flip side, 673 work in Anne Arundel and live in Alleganey. 

## Purpose

A number of users have requested the ability to get county to county home-work job flow matrices using OnTheMap. This is not currently possible in the existing version. It is straightforward to create the data necessary and the manually or programmatically organize the results into a flows table. Included in this package are:
- Unmanipulated Destination Analysis results directly from OnTheMap (in the folder county_to_county_data/)
- Collection of example modules to perform specific actions (in the folder otmcountypy/)
- A control module (run.py)

## Source data

All zip files in the county_to_county data were created using a Destination Analysis in OnTheMap. It isn't necessary to create any additional data for this tutorial but the steps are below. 


Steps to produce source data:
- Navigate to http://onthemap.ces.census.gov/
- Zoom into a region until county boundaries and names appear
- Use the selection tab to "Draw Point(s)" and place a single dot in a county
- Change the 'Add Layer Selection' dropdown to Counties and click 'Confirm Selection'
- Run a Destination Analysis with the Destination Type set to Counties
- Change the number of results to Top 50 (Can run with 'Top 100' or 'All' as well)
- Select 'Export Geography' and then 'CSV (results, all years)'
- Save the zip file to a directory

## Running the process
- Download python 2.7 (https://www.python.org/downloads/)
- Run IDLE or your preferred editor
- Open (File -> Open in IDLE) run.py from the base directory of this package
- Note the default settings at the top (jobtype s000 - all jobs, year 2013)
- Run the program (Run -> Run Module in IDLE)
- Examine the new CSV file in the base directory of your folder called output.csv

## Limitations
Currently this script is setup to produce a square matrix - in other words, every county selected and run as a Destination Analysis will appear in the output. Counties not selected in this first step do not appear. Minor modifications can be made to change this. 

## Can this be used on Tracts, Block Groups, Places, etc?
Yes, but running more than a handfull of Destination Analyses (see steps to create source data) in OnTheMap will be tiresome. Processing all tracts in a county would be time consuming but is very much possible. 

## What is the job type in run.py? 
There are a few different job types in the LODES Origin-Destination data. The options can be found in otmcountypy/constants.py and are listed here:

's000': 'Total number of jobs'
'sa01': 'Number of jobs of workers age 29 or younger'
'sa02': 'Number of jobs for workers age 30 to 54'
'sa03': 'Number of jobs for workers age 55 or older'
'se01': 'Number of jobs with earnings $1250/month or less'
'se02': 'Number of jobs with earnings $1251/month to $3333/month'
'se03': 'Number of jobs with earnings greater than $3333/month'
'si01': 'Number of jobs in Goods Producing industry sectors'
'si02': 'Number of jobs in Trade, Transportation, and Utilities industry sectors'
'si03': 'Number of jobs in All Other Services industry sectors'

## What are the NaN values seen in the output file?
Because this example limited the results of the OnTheMap output to the top 50 results there are some occasions where a county will fall outside this threshold. In these cases, a 'NaN' value appears in the output table. If the source OnTheMap data was set to return 'All' result then these values could be set to 0 as there are no workers who live in county A and work in county B.
