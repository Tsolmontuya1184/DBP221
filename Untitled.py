#!/usr/bin/env python
# coding: utf-8

# In[2]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("APF221.json",scope)

client = gspread.authorize(creds)
sheet = client.open('APF221Seminar11').sheet1

sheet.insert_row(["b20fa1184","Tsolmontuya",403],2)
#result = sheet.get_all_records()
row = sheet.row_value(2)
print(row)


# In[ ]:





# In[ ]:




