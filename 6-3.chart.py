import streamlit as st
import altair as alt
import pandas as pd
pip install plotly
import plotly.express as px

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv 읽어오기 
# 한글 encoding='CP949'
st.title("Advanced")

def financial():
    st.subheader('1. Altair Scatter chart- 재무 분석')
    fi = pd.read_csv("https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv", encoding='CP949')

    # 체크박스 버튼을 선택하여 데이터 확인
    tab1, tab2 = st.tabs(["재무분석 데이터", "Scatter"])
    box = tab1.checkbox("재무분석 데이터 조회", value=True)
    if box:
        tab1.dataframe(fi)

    # radio button을 사용하여 판매량/매출원가/수익을 선택
    radio = tab2.radio("총 매출 대비 분석을 원하는 항목을 선택하세요.",("판매량", "매출원가", "수익"))

    chart = alt.Chart(fi).mark_circle().encode(x="총매출", y=radio, color="상품", size=radio)
    tab2.altair_chart(chart, use_container_width=True)


def titanic():
    st.subheader('2. Plotly Pie chart- 타이타닉 생존 분석')
    titanic = pd.read_csv("https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv")

    # 체크박스 버튼을 선택하여 데이터 확인
    tab1, tab2 = st.tabs(["타이타닉 데이터", "Pie & Bar"])

    box = tab1.checkbox("타이타닉 데이터 조회", value=True)
    if box:
        tab1.dataframe(titanic)
    
    # select box를 사용하여 탑승지역-Embarked/객실등급-Pclass 선택
    tit = tab2.selectbox("생존자 분석을 위한 항목을 선택하세요.", ('탑승지역별 분석', '객실등급별 분석'))

    if tit == "탑승지역별 분석":
        sel = "Embarked"
    else:  
        sel = "Pclass"

    # columns 함수를 이용하여 좌-pie chart, 우-bar chart 그리기
    # 차트 크기 조정- fig.update_layout(height=400, width=400)
    col1, col2 = tab2.columns(2)

# # 범례 표시 제거 : fig.update(layout_showlegend=False) 
    with col1:
        # pie chart 그리기: values='Survived'
        fig = px.pie(titanic, values = "Survived", names = sel, title=f"{sel}", hole=.2)
        fig.update_traces(textposition='inside', textinfo = 'percent+label+value')
        fig.update_layout(font = dict(size = 16))
        fig.update_layout(height=400, width=400)
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
    with col2:
        # bar chart 그리기: y="Survived", color="Sex"
        fig = px.bar(titanic, x=sel, y="Survived", color="Sex", text_auto=True, title="Survived")
        fig.update_layout(height=400, width=400)
        st.plotly_chart(fig)    

page_names_to_funcs = {'재무분석': financial, '타이타닉': titanic}
selected_page = st.sidebar.selectbox("어떤 데이터를 조회하시나요?", page_names_to_funcs.keys())

if selected_page == "재무분석":
    st.sidebar.title("💲")
else :
    st.sidebar.title("🚢")

page_names_to_funcs[selected_page]()


# # select box를 사용하여 탑승지역-Embarked/객실등급-Pclass 선택
# tit = (
#      '생존자 분석을 위한 항목을 선택하세요.',
#      ('탑승지역별 분석', '객실등급별 분석') )
# if tit == 
#     sel = 
# else:  
#     sel = 

# # columns 함수를 이용하여 좌-pie chart, 우-bar chart 그리기
# # 차트 크기 조정- fig.update_layout(height=400, width=400)

# with col1:
#     # pie chart 그리기: values='Survived'
#     fig = 
#     fig.update_traces(
#     fig.update_layout(
#     fig.update(layout_showlegend=False)
#     st.
# with col2:
#     # bar chart 그리기: y="Survived", color="Sex"
#     fig = 
#     fig.update_layout(height=400, width=400)
#     st.
    
# # 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-3.chart.py
