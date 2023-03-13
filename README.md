## What does it do?

**Example result:**

![alt text](https://github.com/JaredBeluzi/Windows-RAM-Monitoring/blob/main/logging_hist.png?raw=true)

The program creates a logging_hist.csv as above with data about the RAM usage of a Windows PC.
The data shown in the picture above shows from left to right:
- user (with domain)
- process name
- number of logging attempt of the day (useful for grouping data on each logging process)
- logging date (German Format)
- logging time
- RAM usage in KB

Since each user will be monitored seperately, this program can be used on a machine to track RAM usage per user on a multi-user PC.
This data can then be used to create any dashboard you like.

## How to use

1. Copy the whole folder to the machine, where you want to monitor the RAM usage.
2. Install python on that machine (I used python 3.11.1)
3. Install the pandas package in Python (in cmd you can type:
```batch
python -m pip install pandas
```
4. Add a task in the task scheduler on Windows that starts the START.bat in the downloaded folder each day in the morning, e.g. at 06:00 
(please check the box in the task scheduler that starts the script even if you are not logged in on that machine!)
5. Let the Server do its thing and wait at least 2 days. Then there should be a logging_hist.csv like the one in the picture above in this folder


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
