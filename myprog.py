
# coding: utf-8

# In[3]:

import random
wrname_wrn_list = ['Wrong name!' , 'Are you sure?' , 'Sorry we can\'t find you in the database!']
def myname_get():
    myname = raw_input('Input your name: ')
    if myname=="Evgeny":
        print ("Hi ", myname)
    else:
        print(wrname_wrn_list[0], "Try again!")
        myname_get()
myname_get()


# In[ ]:



