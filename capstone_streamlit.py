# import package 


import streamlit as st

import pandas as pd 

#import matplotlib
#from matplotlib import pyplot as plt
#import seaborn as sns

from sklearn.utils import estimator_html_repr
from streamlit_option_menu import option_menu

import plotly.express as px  
import numpy as np
import plotly.figure_factory as ff
import chart_studio.plotly as py
from plotly.offline import init_notebook_mode,iplot



# setting page layout 
st.set_page_config(layout="wide")
st.title('Analysis of Jobs and Skills')

# dataset
df = pd.read_csv("C:\\Users\\BC\\Documents\\MSBA Summer 2022\\Ghida Raydan_Capstone\\Data\\bahrain_new_1.csv", encoding='latin1')

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #eeeeeeee;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(0, 162, 208);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: black;
}
</style>
"""
, unsafe_allow_html=True)

#Menu Bar
selected = option_menu(
        menu_title = None,
        options = ["Home", "Kpis", "Requirments", 'Comapnies',"Skills"],
        default_index=0,
        orientation ='horizontal',
        styles={
        "container": {"padding": "0!important", "background-color": "#ededed94"},
        #"icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": '#00a2d0'},
    }
)
        
# SideBar 
# Upload dataset
st.sidebar.write('<p style="font-size:130%">Import Dataset 👇</p>', unsafe_allow_html=True)
uploaded_data= st.sidebar.file_uploader('Upload dataset', type='csv')
if uploaded_data is not None:
    df = pd.read_csv(uploaded_data, encoding = 'latin1')

st.cache(persist=True)

if selected == "Home":

    st.title("Welcome...")
    st.write('<p style="font-size:130%"> Hello and welcome to the job analysis application ! </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:130%"> The aim of this application is to keep the user updated with latest job offers and skills required </p>', unsafe_allow_html=True)


# Load dataset
    if st.checkbox("Preview Dataset"):
        data =df
        if st.button ("ALL Dataset"):
            st.dataframe(data)
        elif st.button("Head"):
            st.write(data.head())
        elif st.button("Tail"):
            st.write(data.tail())

# Show Column Name
    if st.checkbox ("Show Column Name"):
        data=df
        st.write(data.columns)

## EDA
if selected == "Kpis":
    st.title(f"{selected}")

    
    kpi1, kpi2, kpi3 = st.columns(3)


    wch_colour_box = (237, 237, 237, 0.582)
    wch_colour_font = (0,162,208)
    fontsize = 25
    valign = "right"
    iconname1 = "fas fa-briefcase"
    iconname2 = "fas fa-city"
    iconname3= "fas fa-industry"
    iconname4='fas fa-users'
    iconname5='fas fa-cogs'
    iconname6='fas fa-user-cog'
    
    sline1 = "Job Offers"
    sline2 = "Companies"
    sline3 = "Company Industries"
    sline4 = "Job Roles"
    sline5 = "Hard Skills"
    sline6 = "Soft Skills"
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i1 = (df["Position"].nunique())
    i2= (df["Company"].nunique()) 
    i3= (df["Company Industry"].nunique())
    i4= (df["Job Role"].nunique())
    i5= (df["Hard_Skills"].nunique())
    i6= (df["Soft_Skills"].nunique())

    htmlstr1 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname1} fa-xl'></i> {i1}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline1}</style></span></p>"""

    htmlstr2 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname2} fa-xl'></i> {i2}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline2}</style></span></p>"""

    htmlstr3 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname3} fa-xl'></i> {i3}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline3}</style></span></p>"""
    htmlstr4 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname4} fa-xl'></i> {i4}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline4}</style></span></p>"""

    htmlstr5 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname5} fa-xl'></i> {i5}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline5}</style></span></p>"""
    htmlstr6 = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname6} fa-xl'></i> {i6}
                            </style><BR><span style='font-size: 20px; 
                            margin-top: 0;'>{sline6}</style></span></p>"""

    kpi1.markdown(lnk + htmlstr1, unsafe_allow_html=True)
    kpi2.markdown(lnk + htmlstr2, unsafe_allow_html=True)
    kpi3.markdown(lnk + htmlstr3, unsafe_allow_html=True)
    kpi1.markdown(lnk + htmlstr4, unsafe_allow_html=True)
    kpi2.markdown(lnk + htmlstr5, unsafe_allow_html=True)
    kpi3.markdown(lnk + htmlstr6, unsafe_allow_html=True)

if selected == 'Requirments':
    
    df2=df[['Position', 'Company',  'Posted', 'Company Industry', 'JobText',
       'Job Role', 'Career Level', 'Years of Experience', 'Degree']]
    df3=df2.drop_duplicates()
    
    col1, col2= st.columns([4,4])

    val_count11  = df3['Degree'].value_counts(normalize=True, ascending=False)
    #fig11 = plt.figure()
    fig11=px.pie(val_count11, values= val_count11.values , names= val_count11.index, title="Education")
    fig11.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    fig11.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
    #fig.update_layout(xaxis_visible=Fa, xaxis_showticklabels=True)
    #fig11.update_traces(marker_color='#00a2d0')
    col1.plotly_chart(fig11, use_container_width=True)

    val_countt  = df['Years of Experience'].value_counts(normalize=True, ascending=False)
    #fig17 = plt.figure()
    fig17=px.pie(val_countt, values= val_countt.values , hole=0.3,  names= val_countt.index, title="Years of Experience")
    fig17.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)'})
    fig17.update_traces(hoverinfo='label+percent+name', textinfo='none')
    fig17.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
    col2.plotly_chart(fig17, use_container_width=True)

if selected == 'Comapnies':

    df2=df[['Position', 'Company',  'Posted', 'Company Industry', 'JobText',
       'Job Role', 'Career Level', 'Years of Experience', 'Degree']]
    df3=df2.drop_duplicates()

    col1, col2= st.columns(2)

    val_count1  = df3['Company'].value_counts(normalize=True, ascending=False).head(5)
    #fig1= plt.figure()
    fig1=px.bar(val_count1, x=(val_count1.values)*100, y=val_count1.index, title='Top Hiring Companies', labels=dict(x=" percentage(%)", y=" "))
    fig1.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    fig1.update_layout(yaxis=dict(autorange="reversed"))
    fig1.update_traces(marker_color='#00a2d0')
    col1.plotly_chart(fig1, use_container_width=True)

    val_count  = df3['Company Industry'].value_counts(normalize=True, ascending=False).head(6)
    #fig = plt.figure()
    fig=px.bar(val_count, x= (val_count.values)*100, y= val_count.index, title="Top Hiring Industries", labels=dict(x=" percentage(%)", y=" "))
    fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    fig.update_layout(yaxis=dict(autorange="reversed"))
    
    fig.update_traces(marker_color='#00a2d0')
    col2.plotly_chart(fig,use_container_width=True)

    val_count2  = df3['Job Role'].value_counts(normalize=True, ascending=False).head(6)
    #fig2 = plt.figure()
    fig2=px.bar(val_count2,  x= (val_count2.values)*100, y= val_count2.index, title="Most Required Job Roles", labels=dict(x=" percentage(%)", y=" "))
    fig2.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    
    fig2.update_layout(xaxis_visible=True, xaxis_showticklabels=True)
    fig2.update_layout(yaxis=dict(autorange="reversed"))
    fig2.update_traces(marker_color='#00a2d0')
    col1.plotly_chart(fig2,use_container_width=True)

if selected == 'Skills':
    
    col1, col2= st.columns([5,5])
    role = df['Job Role'].unique()
    industry = df['Company Industry'].unique()

    
     # Most Required Soft Skills

    val_count3 = df['Soft_Skills'].value_counts(normalize=True, ascending=False).head(6)
    #fig3 = plt.figure()
    fig3=px.bar(val_count3, x= (val_count3.values)*100, y= val_count3.index,  title="Top Soft Skills", labels=dict(x=" percentage(%)", y=" "))
    fig3.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    #fig.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
    #fig3.update_layout(xaxis_visible=False, xaxis_showticklabels=True)
    fig3.update_layout(yaxis=dict(autorange="reversed"))
    fig3.update_traces(marker_color='#00a2d0')
    col1.plotly_chart(fig3,use_container_width=True)

    # Most Required Hard Skills
    val_count4 = df['Hard_Skills'].value_counts(normalize=True, ascending=False).head(6)
    #fig4 = plt.figure()
    fig4=px.bar(val_count4, x= (val_count4.values)*100, y= val_count4.index,  title="Top Hard Skills", labels=dict(x=" percentage(%)", y=" "))
   
    fig4.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
    #fig.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
    #fig4.update_layout(xaxis_visible=False, xaxis_showticklabels=True)
    fig4.update_layout(yaxis=dict(autorange="reversed"))
    fig4.update_traces(marker_color='#00a2d0')
    col2.plotly_chart(fig4, use_container_width=True)