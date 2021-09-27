# SPARKIFY

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 


## Motivation

The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

To complete this work an ETL pipeline needed to be created with a database schema to optimize queries on song play analysis.


## Tech used

Built with

- [Python](https://www.python.org/)
- PostgreSQL database


## Arcitechure

An ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.
Fact and dimension tables have been used for a star schema for a particular analytic focus.  
Using this model enables end users to query their data simply ( this is because we can denormalise the data making joining on tables easier) and do aggregations on the data at pace.


# Running the Process

To run it manually you can launch the create_tables.py and then etl.py process from the command line by typing 'python create_tables.py' then 'python etl.py'.
This process could be set up to execute on a task scheduler. 


## Script Files

- sql_queries.py
This script specifies what database tables we need dropped, created and inserted into.    

- create_tables.py
This script sets up the database connection and executes several functions defined in the sql_queries.py. 

- etl.py
This is the main script which processes the song and log data preparing data for insert into created tables.

- test.ipynb
This tests the database and ETL pipeline by running queries given by the analytics team from Sparkify to compare produced results with their expected results.