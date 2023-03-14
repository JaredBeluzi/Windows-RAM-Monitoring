import pandas as pd


# 1. Import data
# load logging.csv into a pandas dataframe with Microsoft cmd encoding and no header
df = pd.read_csv('logging.csv', encoding='cp852', header=None)
# name first column "Prozess"
df.columns = ['process',
              'loop_number_of_date',
              'logging_date',
              'logging_time',
              'RAM_usage_KB',
              'user']

# 2. Data transformation
# remove last 2 characters from date
df['logging_date'] = df['logging_date'].str[:-2]
# remove last 2 characters from Ram usage
df['RAM_usage_KB'] = df['RAM_usage_KB'].str[:-2]
# remove dot in ram usage
df['RAM_usage_KB'] = df['RAM_usage_KB'].str.replace('.', '')
# cast ram usage to int
df['RAM_usage_KB'] = df['RAM_usage_KB'].astype(int)

# 3 grouping data
# group by process and user
df_grouped = df.groupby(['user',
                         'process',
                         'loop_number_of_date',
                         'logging_date'])
df_grouped = df_grouped.agg({'logging_time':'min',
                            'RAM_usage_KB':'sum'})

# 4. Export data
# check if file exists
try:
    # if file exists, append data to existing csv file with ansi encoding
    df_grouped.to_csv('logging_hist.csv', mode='a', encoding='utf-8', header=False)
except FileNotFoundError:
    # if file does not exist, create file and write data to it
    df_grouped.to_csv('logging_hist.csv', mode='w', encoding='utf-8', header=True)

