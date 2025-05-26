import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 구글 드라이브 CSV Plotly 시각화 웹앱")

# 구글 드라이브 CSV 파일 URL
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("데이터 미리보기")
st.dataframe(df)

# 사용자에게 X축과 Y축 선택 기능 제공
x_col = st.selectbox("X축 컬럼 선택", df.columns)
y_col = st.selectbox("Y축 컬럼 선택", df.columns)

# X축이 날짜면 datetime 변환 시도
try:
    df[x_col] = pd.to_datetime(df[x_col])
except Exception:
    pass

# Plotly 선 그래프 그리기
fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
st.plotly_chart(fig, use_container_width=True)
