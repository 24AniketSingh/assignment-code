#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabula
file1=tabula.read_pdf("100100502_AES01267KY_ORG_Financial-Statement_2020.pdf",pages="5",stream=True)[0]
file2=tabula.read_pdf("100100502_AES01267KY_ORG_Financial-Statement_2020.pdf",pages="4",stream=True)[0]
tabula.convert_into("100100502_AES01267KY_ORG_Financial-Statement_2020.pdf", "profit loss sheet.csv", output_format="csv", pages='5',stream=True)
tabula.convert_into("100100502_AES01267KY_ORG_Financial-Statement_2020.pdf", "consolidated balance sheet.csv", output_format="csv", pages='4',stream=True)
print(file1)
print(file2)


# In[ ]:




