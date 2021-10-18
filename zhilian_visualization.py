#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import pandas as pd 
import pandas.util.testing as tm 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import folium
from folium.plugins import FastMarkerCluster
from wordcloud import WordCloud
from nltk.corpus import stopwords
import operator
import string   

import warnings
warnings.filterwarnings('ignore')

from bubbly.bubbly import bubbleplot
import squarify


# In[15]:


df = pd.read_excel('D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\zhilian.xlsx')
df.head()


# In[16]:


print("There are {} rows and {} columns in our data".format(df.shape[0], df.shape[1]))


# In[17]:


df.info()


# In[18]:


for column in df.columns:
    if df[column].isnull().any(): 
       print('{0} has {1} null values'.format(column, df[column].isnull().sum()))


# In[23]:


df[df['Job Category'].isnull().values]


# In[19]:


df[df['Jobtype'].isnull().values]


# In[25]:


df["Job Category"] = df["Job Category"].fillna("Constituent Services & Community Programs")


# In[28]:


## here we gave the data specific index and range information into the panda dataframe
df = pd.read_excel("D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\zhilian.xlsx",index_col='Posting Date', parse_dates=['Posting Date'])
df[["Jobtype"]].resample('M').count().plot(figsize=(20,10), linewidth=3, fontsize=20)
plt.xlabel('Year', fontsize=20)


# In[29]:


df[["# Of Positions"]].resample('M').sum().plot(figsize=(20,10), linewidth=3, fontsize=20)
plt.xlabel('Year', fontsize=20)


# In[44]:


#Highest Average Starting Salary Job?
salaries = df.groupby('Jobname')['Salary Range From'].sum().sort_values(ascending=False).head(15)

trace1 = go.Bar(x=salaries.values, 
                y=salaries.index, 
                width=0.6,
                marker=dict(
                    color='#54d1f7', 
                    line=dict(
                        color='#54d1f7', 
                        width=1.5)
                ),
                orientation='h', name='Highest Average Starting Salary')

layout = dict(showlegend=False,
              title='Highest Average Starting Salaries',
              yaxis=dict(
                  showgrid=False,
                  showline=False,
                  showticklabels=True,
              ),
             xaxis=dict(
                  title='Salaries',
                  zeroline=False,
                  showline=False,
                  showticklabels=True,
                  showgrid=False,
             ),
             margin = dict(l=300, r=20, t=50, b=50),
            )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig)


# In[46]:


#Highest Salary Job?
import plotly_express as px
high_sal_range = (df.groupby('Jobtype')['Salary Range To'].mean().nlargest(10)).reset_index()

fig = px.bar(high_sal_range, y="Jobtype", x="Salary Range To", orientation='h', title = "Highest High Salary Range",color=  "Salary Range To", color_continuous_scale= px.colors.qualitative.G10).update_yaxes(categoryorder="total ascending")
fig.show()


# In[47]:


high_sal_range = (df.groupby('Jobtype')['Salary Range From'].mean().nlargest(10)).reset_index()

fig = px.bar(high_sal_range, y="Jobtype", x="Salary Range From", orientation='h', title = "Highest (Low) Salary Ranges",color=  "Salary Range From", color_continuous_scale= px.colors.qualitative.T10).update_yaxes(categoryorder="total ascending")

fig.show()


# In[42]:


#Top 10 Job Openings via Category
job_categorydf = df['Jobname'].value_counts(sort=True, ascending=False)[:10].rename_axis('Jobname').reset_index(name='Counts')
job_categorydf = job_categorydf.sort_values('Counts')


# In[43]:


trace = go.Scatter(y = job_categorydf['Jobname'],x = job_categorydf['Counts'],mode='markers',
                   marker=dict(size= job_categorydf['Counts'].values/2,
                               color = job_categorydf['Counts'].values,
                               colorscale='Viridis',
                               showscale=True,
                               colorbar = dict(title = 'Opening Counts')),
                   text = job_categorydf['Counts'].values)

data = [(trace)]

layout= go.Layout(autosize= False, width = 1000, height = 750,
                  title= 'Top 10 Job Openings Count',
                  hovermode= 'closest',
                  xaxis=dict(showgrid=False,zeroline=False,
                             showline=False),
                  yaxis=dict(title= 'Job Openings Count',ticklen= 2,
                             gridwidth= 5,showgrid=False,
                             zeroline=True,showline=False),
                  showlegend= False)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[54]:


#The most busy locations
locations = df['Cityname'].value_counts().sort_values(ascending=False).head(15)

trace1 = go.Bar(x=locations.values, 
                y=locations.index, 
                width=0.6,
                marker=dict(
                    color='#8ddcf4', 
                    line=dict(
                        color='#54d1f7', 
                        width=1.5)
                ),
                orientation='h', name='Cityname')

layout = dict(showlegend=False,
              title='Most Busy Locations',
              yaxis=dict(
                  showgrid=False,
                  showline=False,
                  showticklabels=True,
              ),
             xaxis=dict(
                  title='Jobs',
                  zeroline=False,
                  showline=False,
                  showticklabels=True,
                  showgrid=False,
             ),
             margin = dict(l=300, r=20, t=50, b=50),
            )
fig = go.Figure(data=[trace1], layout=layout)
py.iplot(fig)


# In[59]:


# Word clouds
# encoding:utf-8
from PIL import Image
import random
from palettable.colorbrewer.sequential import Greens_9, Greys_9, Oranges_9, PuRd_9


Qual_mask  = np.array(Image.open(('D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\Qual_mask.png')))
skill_mask = np.array(Image.open(('D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\skill_mask.png')))
residency_mask = np.array(Image.open(('D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\residency_mask.png')))
job_mask = np.array(Image.open(('D:\\博士课程\\讲座——Machine Learning\\家教数据机器学习\\家教数据机器学习\\job_mask.png')))


# In[82]:


df['Min_req']=df['Welfare'].apply(lambda x : x.split(',') if type(x)==str else [''])
df['Job_desc'] = df['Jobtype'].apply(lambda x : x.split(',') if type(x)==str else [''])
df['res_req']=df['Cityname'].apply(lambda x : x.split(',') if type(x)==str else [''])
df['Pref_skill'] = df['Jobname'].apply(lambda x : x.split(',') if type(x)==str else [''])


# In[79]:


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Greys_9.colors[random.randint(2,8)])


def green_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Greens_9.colors[random.randint(2,8)])

def orange_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Oranges_9.colors[random.randint(2,8)])

def PuRd_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(PuRd_9.colors[random.randint(2,8)])

def produce_wordcloud(dataframe, title, mask, color):
    
    path="C:\Windows\Fonts\SimHei.ttf"
    plt.figure(figsize=(10, 10))
    corpus=dataframe.values.tolist()
    corpus=','.join(x  for list_words in corpus for x in list_words)
    wordcloud = WordCloud(max_font_size=None, background_color='white',font_path=path,collocations=False, height=1500,
                 mask = mask).generate(corpus)
    wordcloud.recolor(color_func=color)
    plt.axis("off")
    plt.title(title)    
    return plt.imshow(wordcloud)


# In[80]:


produce_wordcloud(df['Min_req'], "Welfare", job_mask, orange_color_func)


# In[77]:


produce_wordcloud(df['Job_desc'], "Jobtype", Qual_mask, grey_color_func)


# In[74]:


produce_wordcloud(df['Pref_skill'], "Jobname", residency_mask, PuRd_color_func)


# In[83]:


produce_wordcloud(df['res_req'], "Cityname", skill_mask, green_color_func)


# In[ ]:




