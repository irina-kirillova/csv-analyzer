import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Анализатор")

uploaded_file = st.file_uploader("Загрузи CSV файл", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Данные")
    st.dataframe(df)
    
    st.subheader("Статистика")
    st.write(df.describe())
    
    st.subheader("График")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        col = st.selectbox("Выбери колонку", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        st.pyplot(fig)
    else:
        st.write("Нет числовых колонок для графика")