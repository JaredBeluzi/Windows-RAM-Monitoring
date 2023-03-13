## What does it do?

![alt text](https://github.com/JaredBeluzi/Windows-RAM-Monitoring/blob/main/logging_hist%20example.png?raw=true)

The program creates a logging_hist.csv as above with data about the RAM usage of a Windows PC.
The data shown in the picture above shows from left to right:
- process name
- logging number of the day (useful for grouping on logging entries)
- logging date
- logging time
- RAM usage in KB
- user

This data can then be used to create any dashboard you like.

## How to use

- copy whole folder to the machine, where you want to monitor the RAM usage
- install python on that machine
- install pandas package in Python (in cmd:
```batch
py -m pip install pandas
```
- add a task in task scheduler on Windows that starts the START.bat in the downloaded folder
- let the Server do its thing and wait at least 2 days. Then there should be a logging_hist.csv in this folder, that you can use however you want


## How does it work?

1. START.bat

Started via Task Scheduler (Aufgabenplanung) every day in the morning at 06:00.
Starts logging.bat.

2. logging.bat

Retrieves list of all processes with users and RAM usage once every minute and writes it into logging.csv.
Runs until 20:00. After that process stops and data_transformation.py starts.

3. data_transformation.py

Loads logging.csv in python, corrects some mistakes in the data and aggregates them to save disk space.
Aggregated data is added to logging_hist.csv.
