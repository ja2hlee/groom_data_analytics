### 본 앱은 Streamlit 컴포넌트 학습 및 데모 목적입니다.
### 실행 결과 확인용입니다!!
### =========================
### =========================
### =========================

import streamlit as st
import pandas as pd
import numpy as np
import time

# =========================
# Page config
# =========================
st.set_page_config(layout="wide")

st.title("Streamlit 기능 시현 페이지")


# =========================
# Layout
# =========================
st.header("📐 Streamlit Layout")

with st.expander('이 앱에 대하여'):
  st.write('이 앱은 Streamlit 앱을 구성하는 다양한 방법을 보여줍니다.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header("입력 영역")
user_name = st.sidebar.text_input("이름")
user_color = st.sidebar.selectbox(
    "좋아하는 색상", ["", "파랑", "빨강", "초록"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("이름")
    st.write(user_name if user_name else "입력 필요")

with col2:
    st.subheader("색상")
    st.write(user_color if user_color else "선택 필요")

with col3:
    st.subheader("상태")
    st.write("정상 작동 중")

# =========================
# Basic Components
# =========================
st.header("🔷 Streamlit 기본 문법")

st.subheader("st.write")
st.write("streamlit")
st.write(pd.DataFrame({"a": [1, 2], "b": [3, 4]}))

st.subheader("st.slider")
age = st.slider("나이", 0, 100, 25)
st.write(age)

st.subheader("st.line_chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)

st.subheader("st.selectbox")
option = st.selectbox(
    "색상 선택?",
    ("파랑", "빨강", "초록")
)
st.write("가장 좋아하는 색상은", option)

st.subheader("st.multiselect")
options = st.multiselect(
    "가장 좋아하는 색상은?",
    ["초록", "노랑", "빨강", "파랑"],
    ["노랑", "빨강"]
)
st.write("선택:", options)

st.subheader("st.checkbox")
icecream = st.checkbox("아이스크림")
coffee = st.checkbox("커피")

if icecream:
    st.write("아이스크림 선택")
if coffee:
    st.write("커피 선택")

st.subheader("st.latex")
st.latex(r"""
a^2 + b^2 = c^2
""")

st.subheader("st.file_uploader")
uploaded_file = st.file_uploader("파일 선택")
if uploaded_file:
    st.write(uploaded_file.name)

st.subheader("st.progress")
my_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.01)
    my_bar.progress(percent + 1)
#st.balloons() #자꾸 새로고침되는 거 없앰

# =========================
# Form
# =========================
st.header("📝 st.form")

with st.form("my_form"):
    st.subheader("커피 주문하기")

    coffee_bean_val = st.selectbox(
        "커피콩", ["아라비카", "로부스타"]
    )
    coffee_roast_val = st.selectbox(
        "커피 로스팅", ["라이트", "미디엄", "다크"]
    )

    submitted = st.form_submit_button("제출")

if submitted:
    st.write(coffee_bean_val, coffee_roast_val)
else:
    st.write("주문하세요!")
