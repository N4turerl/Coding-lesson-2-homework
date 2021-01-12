#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = input('insert a number: ')
converted_number = int(number)
number_calculator = converted_number%2

if number_calculator == 0:
    print('the number was even')
else:
    print('the number was odd')

