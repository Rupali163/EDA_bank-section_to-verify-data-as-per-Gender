#!/usr/bin/env python
# coding: utf-8

# In[20]:


# import required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# read the data from file
df=pd.read_csv("bank_marketing.csv")


# In[3]:


# check the data is read properly or not
df


# In[5]:


#check the column of data
df.columns


# In[6]:


# check the size of data
df.shape


# In[7]:


#check is any data missing in in paticular or not!
df.info()


# In[8]:


# check arbitrary description upon all data
df.describe()


# In[9]:


# extract first 5 recored from  data(just to check data read properly or not)
df.head()


# In[10]:


# extract last 5 records from data.
df.tail()


# In[11]:


#check is any  null/missing value is present in data set or not
df.isna().sum()
#other option to check the missing value is present or not
#df.isnull().sum()


# In[13]:


#start to analysis of column wise data
# use mariatal status column
#Q. How many Married pepole is took the loan ?
#Q. How many unmarried pepole is took the loan ?
#Q. How many divorced pepole is took the loan ?
# Q what is the Marital status of people with sub cataeogory
df.marital.value_counts()


# # summary of Mariatal status

# In[ ]:


# as per above result total 3134 married people, 1816  unmarieed  and 631 divorced people are present in our data set
# divorced people are very less  who took loan
# marroed people count is more as compare to unmaried and divorced people 
# it will represent with the help of  different visualization technique..please check below 


# In[14]:


M_status=df['marital'].value_counts()


# In[86]:


m = M_status.index


# In[89]:


m1 = M_status.values


# In[91]:


plt.bar(m, m1, color= ('c','g','b'))


# In[41]:


plt.figure(figsize=(10,10))
plt.pie(M_status, autopct='%.2f%%', labels=M_status.index)
plt.title='Complete Maratial Status'
plt.show()


# In[43]:


plt.figure(figsize=(10,10))
plt.pie(M_status, explode=[0,0,0.2],autopct='%.2f%%', labels=M_status.index)
plt.title='Complete Maratial Status'
plt.show()


# In[52]:


#now we work on Education column
#Q. what kind of education is had taken loan?
# Q what is loan status od=f secondary education people?
E_status=df.education.value_counts()


# In[53]:


E_status


# In[68]:


s = E_status.index


# In[69]:


s1 = E_status.values


# In[85]:


plt.figure(figsize=(10,10))
plt.bar(s,s1, color=('g','c','r','b'), width = .4, align = 'center', label= 'Educational details')
plt.legend()


# In[ ]:


# as per above visualization we summarize -secondary people have highest rate to 
#taken loan as compare to tertiary and primary


# In[ ]:


#Q how many people had taken loan in month of feb


# In[92]:


df[:2]


# In[93]:


df.month.value_counts()


# In[106]:


Month_count = df.month.value_counts()


# In[107]:


Month_count


# In[108]:


plt.plot(Month_count)


# In[110]:


plt.bar(Month_count.index, Month_count.values)


# In[ ]:


# as per above visualization we summarize is that:- in month of MAY Maximum people had taken loan
# as well as in month of DECEMBER  very few /minimum people had taken loan


# In[122]:


a =Month_count.describe()
a


# In[100]:


Month_feb=df.groupby('month').get_group('feb')


# In[119]:


Month_feb.shape


# In[126]:


# if you check the maximum. count of  loan taken month
a.max()


# In[137]:


# check how many people had taken loan
z =df.loan.value_counts()
z


# In[139]:


#as per above details 718 people had taken loan
# as per above details 4863 people had not taken loan 
plt.bar(z.index, z.values, color = ('c', 'g'))


# In[142]:


df[:2]


# In[145]:


df.groupby('job').get_group('technician')['balance'].mean()


# In[152]:


df.groupby('deposit').get_group('yes')['age'].mean()


# In[161]:


o = df.age.value_counts()


# In[163]:


o1= df['age'].value_counts()


# In[174]:


Top_Ten_age_category=o1.head(10)


# In[175]:


plt.bar(Top_Ten_age_category.index, Top_Ten_age_category.values)


# In[186]:


# as per above visualizatoin we summarize that::-Max age group of 31 to 36 people had taken loan
#31 age's peolple taken maximum loan

plt.figure(figsize= (15,8))
plt.bar(Top_Ten_age_category.index, Top_Ten_age_category.values)
plt.show()


# In[167]:


plt.bar(o1.index, o1.values)


# In[188]:


sns.scatterplot(o1.index, o1.values)

