**W205_Exercise2 Twitter feed wordcount**      
**By Manish Shah**  
**Date:12/03/2017**  

# Project  

This project uses a constant twitter feed and parses the tweets and for valid words, it creates a wordcount of the words used in the tweets.  
The words and corresponding word counts are stored in a postgress database and queries can be used. 

# Run Environment

The analysis has been tested on AWS hosted EC2 instance with 100 GB of diskspace, 8 GB of Ram and 2 processors and using Linux operating system.  
The AMI used is "UCB W205 Spring 2016 (ami-be0d5fd4)"  

Postgres version: 8.4  
Python version : 2.7

# Folders and Files  

The project directory contains the following files and folders. Remaining files  
were provided as part of the exercise.  


Files | Description
------|-------------
create_database.py | Python program to create the postgres database tcount.  
extweetwordccount | The directory to define the storm components created by sparse quickstart command  
final_results.py | Python program to query the keywords from the postgres database tcount    
histogram.py | Python program to query the words with frequency >= k and <= 1. k,l are command lines.  
main.sh | The main program to run this exercise.  
output | This folder has the results from running the main.sh file  
screenshots | This folder has the screenshots from this exercise  
top20_plot.py | Python program to plot top 20 words. This program has been run on windows python.  
top_20.py | Python program to query top 20 words from the database  

# Run Instructions   

The program is run with w205 as the user. Start the postgres server with the start_postgres script /data/start_postgres.   

To run the program, run main.sh from the bash command prompt. 



