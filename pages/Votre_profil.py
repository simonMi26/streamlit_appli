from math import nan
import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

header = st.container()
graphique = st.container()
dataset = st.container()
test = st.container()
test2 = st.container()



with header : 
    st.title( "L'assurance tourisme")
    st.subheader("Visualisation des données selon certains critères")
    df = pd.read_csv("TravelInsurancePrediction.csv", delimiter= ";")


with graphique :
    
    col1, col2 = st.columns(2)
    with col1 :
        st.selectbox("Age", np.sort(df["Age"].unique()), key= "age")
        filtre_age = df[df["Age"] == (st.session_state.age) ]    
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="Age",hue = "TravelInsurance", data = filtre_age)
        st.pyplot(fig)     

        st.selectbox("GraduateOrNot", df["GraduateOrNot"].unique(), key = "graduate")
        filtre_graduate = df[df["GraduateOrNot"] == (st.session_state.graduate) ]
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="GraduateOrNot",hue = "TravelInsurance", data = filtre_graduate)
        st.pyplot(fig)

        st.selectbox("FamilyMembers", np.sort(df["FamilyMembers"].unique()), key = "family")
        filtre_family = df[df["FamilyMembers"] == (st.session_state.family) ]
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="FamilyMembers",hue = "TravelInsurance", data = filtre_family)
        st.pyplot(fig)

        st.selectbox("FrequentFlyer", df["FrequentFlyer"].unique(), key = "fly")
        filtre_fly = df[df["FrequentFlyer"] == (st.session_state.fly) ]
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="FrequentFlyer",hue = "TravelInsurance", data = filtre_fly)
        st.pyplot(fig)

    with col2:
        st.selectbox("Employment Type", df["Employment Type"].unique(),key = "employment")
        filtre_employment = df[df["Employment Type"] == (st.session_state.employment) ]
        fig2 = plt.figure(figsize=(8,6))
        sns.countplot(x="Employment Type",hue = "TravelInsurance", data = filtre_employment)
        st.pyplot(fig)

        st.selectbox("AnnualIncome", np.sort(df["AnnualIncome"].unique()), key = "income")
        filtre_income = df[df["AnnualIncome"] == (st.session_state.income) ]
        fig = plt.figure(figsize=(8,6))
        ax = sns.countplot(x="AnnualIncome",hue = "TravelInsurance", data = filtre_income)
        ax.set_xticklabels(ax.get_xticklabels(),rotation = 70)   
        st.pyplot(fig)

        st.selectbox("ChronicDiseases", np.sort(df["ChronicDiseases"].unique()), key = "disease")
        filtre_disease = df[df["ChronicDiseases"] == (st.session_state.disease) ]
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="ChronicDiseases",hue = "TravelInsurance",data = filtre_disease)
        st.pyplot(fig)

        st.selectbox("EverTravelledAbroad", df["EverTravelledAbroad"].unique(), key = "abroad")
        filtre_abroad = df[df["EverTravelledAbroad"] == (st.session_state.abroad) ]
        fig = plt.figure(figsize=(8,6))
        sns.countplot(x="EverTravelledAbroad",hue = "TravelInsurance",data = filtre_abroad)
        st.pyplot(fig)

    with dataset : 
        final = df[(df["EverTravelledAbroad"] == (st.session_state.abroad)) & (df["ChronicDiseases"] == (st.session_state.disease) ) & (df["AnnualIncome"] == (st.session_state.income)) & (df["Employment Type"] == (st.session_state.employment)) & (df["FrequentFlyer"] == (st.session_state.fly)) & (df["FamilyMembers"] == (st.session_state.family) ) & (df["GraduateOrNot"] == (st.session_state.graduate) ) & (df["Age"] == (st.session_state.age))]
        st.table(final)
        assurance = round(final["TravelInsurance"].sum() / final["TravelInsurance"].count() * 100,2) 
        if np.isnan(assurance):
            st.write("Il n'y a aucun profil qui correspond au votre")
        else:
            st.write(f"Il y a {assurance} % personnes au même profil que vous qui prend une assurance voyage")

    with test :
        EverTravelled, Disease, Income, Employment  = st.columns(4)
        colonnes = ["Column1", "TravelInsurance"]
        data = df[colonnes]
        with EverTravelled:
            if st.checkbox("EverTravelledAbroad", True):
                data = pd.concat([data,df["EverTravelledAbroad"]], axis = 1)
                data = data[(data["EverTravelledAbroad"] == (st.session_state.abroad))]
        with Disease : 
            if st.checkbox("ChronicDiseases", True):
                data = pd.concat([data,df["ChronicDiseases"]], axis = 1)
                data = data[(data["ChronicDiseases"] == (st.session_state.disease))]
        with Income : 
            if st.checkbox("AnnualIncome", True):
                data = pd.concat([data,df["AnnualIncome"]], axis = 1)
                data = data[(data["AnnualIncome"] == (st.session_state.income))]
    
    with test2 :
        Flyer, Family, Graduate, Age = st.columns(4)
        with Employment :
            if st.checkbox("Employment Type", True):
                data = pd.concat([data,df["Employment Type"]], axis = 1)
                data = data[(data["Employment Type"] == (st.session_state.employment))]
        with Flyer :
            if st.checkbox("FrequentFlyer",True):
                data = pd.concat([data,df["FrequentFlyer"]], axis = 1)
                data = data[(data["FrequentFlyer"] == (st.session_state.fly))]
        with Family :
            if st.checkbox("FamilyMembers", True):
                data = pd.concat([data,df["FamilyMembers"]], axis = 1)
                data = data[(data["FamilyMembers"] == (st.session_state.family))]
        with Graduate :
            if st.checkbox("GraduateOrNot", True):
                data = pd.concat([data,df["GraduateOrNot"]], axis = 1)
                data = data[(data["GraduateOrNot"] == (st.session_state.graduate))]
        with Age :
            if st.checkbox("Age", True):
                data = pd.concat([data,df["Age"]], axis = 1)
                data = data[(data["Age"] == (st.session_state.age))]

        if np.nan not in data: 
            st.dataframe(data)

        assurance2 = round(data["TravelInsurance"].sum() / data["TravelInsurance"].count() * 100,2) 
        if np.isnan(assurance2):
            st.write("Il n'y a aucun profil qui correspond au votre")
        else:
            st.write(f"Il y a {assurance2} % personnes au même profil que vous qui prend une assurance voyage")