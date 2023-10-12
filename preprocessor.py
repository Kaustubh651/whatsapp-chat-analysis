import re
import pandas as pd
import numpy as np

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\s[ap]m\s-\s'
    messages = re.split(pattern,data)[1:]
    dates = re.findall(pattern,data)
    

    df = pd.DataFrame({'user_messgae':messages,'message_date':dates})
    # convert message_data type

    df['message_date'] = df['message_date'].str.replace('\u202f', ' ')
    df['message_date'] = df['message_date'].str.strip()

    # Convert the date to datetime
    df['message_date']=pd.to_datetime(df['message_date'], format="%d/%m/%y, %I:%M %p -", errors='coerce')
    
    
    df.rename(columns={'message_date':'date'},inplace=True)



    user_list = []  # Rename the list to user_list to avoid naming conflicts
    message_list = []  # Rename the list to message_list to avoid naming conflicts

    for message in df['user_messgae']:
        message = message.strip()
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # User name
            user_list.append(entry[1])
            message_list.append(entry[2])
        else:
            user_list.append('group_notification')
            message_list.append(entry[0])
  
    df['user'] = user_list  # Rename the list to user_list here
    df['message'] = message_list  # Rename the list to message_list here
    df.drop(columns=['user_messgae'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()


    period= []
    for hour in df[['day_name','hour']]['hour']:
        if hour == 23:
            period.append(str(hour)+ "-"+ str("00"))
        elif hour==0:
            period.append(str("00")+ "-"+str(hour+1))
        else:
            period.append(str(hour)+ "-"+str(hour+1))
    df['period'] = period
    return df