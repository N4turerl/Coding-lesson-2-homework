#!/usr/bin/env python
# coding: utf-8

# In[ ]:


score = input('what is your score?:  ')
converted_score = int(score)
if converted_score >= 90:
    print('you got an A!')
elif converted_score >= 80 and converted_score < 90:
            print('you got a B!')
elif converted_score >= 70 and converted_score < 80:
            print('you got a C!')
elif converted_score >= 60 and converted_score < 70:
            print('you got a D!')
elif converted_score <60:
            print('you got a F... try harder next time!')


# In[ ]:




