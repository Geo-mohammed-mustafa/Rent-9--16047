import streamlit as st 
import math 


st.header("Welcome Muhammed16047 to Rent9 - 16047")

col_1 , col_2 =st.columns(2)

with col_1 :
    lls=st.number_input(label="Enter the value of LLS")
    lld=st.number_input(label="Enter the value of LLD")
    ms=st.number_input(label="Enter the value of Micro spherical")


if lls and lls and ms is not None :
    
    m=lls/lld
    q=lls/ms
    rt=(lls-(lls/100*ms))/(1-lls/100)
    di=(math.log10(rt)-math.log10(lls))*300
    if m==1 and q==1 :
        di=10
        rxo=lls/rt
    else :
        rxo=lls/rt
    Rt=st.write("RT value ")
    Rt_1=st.write(rt)
    depth=st.write("Depth of investigation")
    depth_1=st.write(di)
    rxoot=st.write("RXO value")
    rxoot_1=st.write(rxo)

    m_out=st.write("LLS / LLD")
    m_out_1=st.write(m)
    rxoot=st.write("LLS / microspherical")
    rxoot=st.write(q)
