import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

header = st.container()
dataset = st.container()
graphique = st.container()

with header : 
    st.title( "L'assurance tourisme")

with dataset : 
    st.subheader ("Visualisation du dataset") 
    df = pd.read_csv("TravelInsurancePrediction.csv", delimiter= ";")
    st.table(df.head())


with graphique :
    st.subheader("Visualisation des données générales")
    col1, col2 = st.columns(2)
    with col1 :

        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="Age",hue = "TravelInsurance", data = df)
        st.pyplot(fig)

        
        sns.countplot(x="GraduateOrNot",hue = "TravelInsurance", data = df)
        st.pyplot(fig)

        
        sns.countplot(x="FamilyMembers",hue = "TravelInsurance", data = df)
        st.pyplot(fig)

        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="FrequentFlyer",hue = "TravelInsurance", data = df)
        st.pyplot(fig)

    with col2:
        fig2 = plt.figure(figsize=(8,6))
        sns.countplot(x="Employment Type",hue = "TravelInsurance", data = df)
        st.pyplot(fig)

        fig = plt.figure(figsize=(8,6))
        ax = sns.countplot(x="AnnualIncome",hue = "TravelInsurance", data = df)
        ax.set_xticklabels(ax.get_xticklabels(),rotation = 70)   
        st.pyplot(fig)

        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="ChronicDiseases",hue = "TravelInsurance",data = df)
        st.pyplot(fig)

        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="EverTravelledAbroad",hue = "TravelInsurance",data = df)
        st.pyplot(fig)