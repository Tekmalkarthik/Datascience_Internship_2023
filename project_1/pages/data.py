import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt
df=pd.read_csv(r"F:\innomatics_internship2023\project_1\resources\car_data.csv")

st.subheader(":red[Dataset Sample of CarDekhoo.com]")
info=st.selectbox("",("Head","Tail","unique","body_style"))

if info=="Head":
    st.dataframe(df.head())
elif info=="Tail":
    st.dataframe(df.tail())
elif info == "unique":
        st.dataframe(df['body_style'].unique())
        st.bar_chart(df["body_style"].value_counts())
else:
     st.dataframe(df["make"].unique())  
     st.line_chart(df["make"].value_counts())

st.subheader(":blue[Detailed Visulization of Some Columns]")

info=st.selectbox("",("setter","engine_type","horse_power","fuel_type"))

if info=="fuel_type":
    st.bar_chart(df.fuel_type.value_counts())
elif info=="horse_power":
    st.subheader(":green[The average horse speed of the cardekho.com is: 154]")
elif info=="engine_type":
     st.bar_chart(df.engine_type.value_counts())
else:
     st.subheader(":green[Number of door vechiles available for sale] ")
     st.bar_chart(df.num_of_doors.value_counts())     
     
