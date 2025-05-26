import streamlit as st
import pandas as pd
import plotly.express as px

st.title("데이터 시각화 웹앱")

url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

st.write("데이터 미리보기")
st.dataframe(df)

x_col = st.selectbox("X축 선택", df.columns)
y_col = st.selectbox("Y축 선택", df.columns)

try:
    df[x_col] = pd.to_datetime(df[x_col])
except:
    pass

fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
st.plotly_chart(fig)
