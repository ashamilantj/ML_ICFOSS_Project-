import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import altair as alt
#%matplotlib inline
#from wordcloud import WordCloud
#import string
#import nltk
#import squarify
#import pygal

#Github repository
#https://github.com/ashamilantj/ML_ICFOSS_Project-

# from /kaggle/input/data-analyst-jobs/DataAnalyst.csv
df=pd.read_csv('DataAnalyst.csv')
#df=df.dropna(axis=1)
df=df.dropna(axis=0)
df=df.drop(['Unnamed: 0'], axis = 1)
df=df.drop(['Easy Apply'], axis = 1)
df=df.drop(['Competitors'], axis = 1)
def load_data(nrows):
    data = pd.read_csv('DataAnalyst.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
data = load_data(2200)
@st.cache

def load_data(nrows):
    data_load_state.text("Done! (using st.cache)")
    st.subheader('Raw data')
    st.write(data)
st.title("Data Analyst Job Opportunities")
st.subheader(' to find the job opportunities available for a Data Analyst, the top companies, average salary provided by the companies')
df['Revenue'].unique()
df=df.replace({'Revenue':'-1'}, {'Revenue':'Unknown'})
df['Revenue'].unique()
df['Location'].value_counts().sort_values(ascending=False).head(n=10).plot.bar(figsize=(25,5),ylabel="Size");
df.head(3)


df['Salary_From']=df["Salary Estimate"].str.extractall(r"[$](\d+)").xs(0,level='match')
df['Salary_To']=df["Salary Estimate"].str.extractall(r"[$](\d+)").xs(1,level='match')
df.fillna(-1,inplace=True)
df['Salary_From']=df['Salary_From'].astype(int)
df['Salary_To']=df['Salary_To'].astype(int)
df['Average_Salary']=(df['Salary_To']+df["Salary_From"]/2)
df['Salary_From'] = df['Salary_From'].astype(float)
df['Salary_To'] = df['Salary_To'].astype(float)
df['Average_Salary'] = df['Average_Salary'].astype(float)
st.header("The Data Frame Contents")
st.write(df)


#add_selectbox = st.sidebar.selectbox(
 #   'Select an option?',
  #  ('Data Frame View','Top Companies', 'Average Salary and Job Sector', 'Job Opportunities')
#)
#print("You Selected", add_selectbox)


my_button = st.sidebar.radio("Select an option: ", ('Data Frame View', 'Location, employee Size , Job Sector', 'Job Sector, Average Salary')) 

if my_button == 'Data Frame View':
     #do some stuff
    df_jobs = df.Location.value_counts().sort_values(ascending=False).head(n=15)
    fig, axs=plt.subplots(nrows=1, ncols=1, figsize=(10,10))
    df_jobs.plot.pie(autopct="%.1f%%",ylabel="",   colors = ["green","orange", "brown",'red', 'pink',"blue" ])


elif my_button == 'Location, employee Size , Job Sector':
    #arr1=df['Average_Salary'].unique()
    #sns.distplot([arr1],color='r')
    #plt.show()
    st.header('VISUALISATION - AREA CHART - LOCATION, SIZE AND SECTOR')
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['Location','Size','Sector'])

st.area_chart(chart_data)


df['Location'].value_counts().sort_values(ascending=False).head(n=10).plot.bar(figsize=(25,5),ylabel="Size");
#VISUALISATION - LINE CHART 
if my_button=='Job Sector, Average Salary':
    st.write('Visualisation - Line Chart - Job Sector and Average Salary')
    chart_data=pd.DataFrame(np.random.randn(20,2),columns=['Sector','Average_Salary'])
    st.line_chart(chart_data)



#   other other things

# WORD CLOUD



#read first column of csv file to string of words seperated
#by tab

your_list = []
with open('DataAnalyst.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = '\t'.join([i[11] for i in reader])


plt.figure()

df['Location'].value_counts().sort_values(ascending=False).head(n=10).plot.bar(figsize=(25,5),ylabel="Size");
#VISUALISATION - AREA CHART
#st.header('VISUALISATION - AREA CHART - LOCATION, SIZE AND SECTOR')
#chart_data=pd.DataFrame(np.random.randn(20,3),columns=['Location','Size','Sector'])

#st.area_chart(chart_data)


df['Location'].value_counts().sort_values(ascending=False).head(n=10).plot.bar(figsize=(25,5),ylabel="Size");

#VISUALISATION - LINE CHART 
#st.write('Visualisation - Line Chart - Job Sector and Average Salary')
#chart_data=pd.DataFrame(np.random.randn(20,2),columns=['Sector','Average_Salary'])
#st.line_chart(chart_data)


#st.subheader(‘Job Locations')
#st.write(df)#Bar Chart
#st.bar_chart(df[‘Location’])


# VISUALISATION - - - TOP 15 JOB LOCATIONS
import altair as alt

 #df = pd.DataFrame(np.random.randn(200, 1), columns=['Location'])

 #c = alt.Chart(df).mark_circle().encode(
  #   x='a' color='c', tooltip=['a'])


 #st.write(c)