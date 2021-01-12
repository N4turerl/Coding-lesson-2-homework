#!/usr/bin/env python
# coding: utf-8

# In[3]:


number = input('insert a number: ')
converted_number = int(number)
number_calculator = converted_number%2

if number_calculator == 0 and converted_number > 100:
    print('the number was even and greater then 100')

else:
    print('the number was either odd, less then 100, or both.')


# In[ ]:




