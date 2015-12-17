
# coding: utf-8

# In[1]:

import datetime


# In[3]:

today = datetime.date.today()
print "today: ", today
#yesterday = today - datetime.timedelta(days=1) tomorrow = today + datetime.timedelta(days=1) print yesterday, today, tomorrow
#emits: 2004-11-17 2004-11-18 2004-11-19


# In[7]:

yesterday = today - datetime.timedelta(days=1)
print "yesterday: ",  yesterday


# In[9]:

def date_func():
    # Prints time lapse
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1) 
    tomorrow = today + datetime.timedelta(days=1) 
    print yesterday, today, tomorrow

date_func()


# In[11]:

def date_func_2():
    # Returns time lapse
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1) 
    tomorrow = today + datetime.timedelta(days=1) 
    return yesterday

date_1, date_2, date_3 = date_func_2()

print "date_1: ", date_1
print "date_2: ", date_2
print "date_3", date_3


# In[14]:

# Data Structures: 
list_ds = [1, 2, 3, 4, 5]
for num in list_ds:
    if num >= 3:
        print num


# In[21]:

TIME_TICKER = 0
GREATER_THAN_NUM = 2
LIST_DS = [1, 2, 3, 4, 5]

def print_greater_func(num_greater, list_ds):
    global TIME_TICKER
    for num in list_ds:
        TIME_TICKER += 1
        if num > num_greater:
            print num
    print 'TICKER: ', TIME_TICKER

print_greater_func(GREATER_THAN_NUM, LIST_DS)


# In[23]:

dict = {'one': 1, 'two': 2, 'three': 3}

plate_names = {'plate_1': [3, 4, 2.3, 4.5], 'plate_2': [3, 1.2, 4, 5]}

# col_1, col_2, col_3
#  1      2.3     3.4
#  4.3    5.1     1.6

# file_1 = {'col_1': [1, 4.3], 'col_2': [2.3, 5.1]}

for key, value in dict.iteritems():
    print "key: ", key, "  ", "value: ", value
    

for plate_name, values in plate_names.iteritems():
    if plate_name == 'plate_1':
        print values

