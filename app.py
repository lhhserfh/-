import streamlit as st
st.title('나는 송은호')
st. write('나는 윤희승')
# app.py

import streamlit as st
import random

st.set_page_config(page_title="무서운 랜덤 그림", page_icon="👻")

st.title("👻 랜덤 무서운 그림 앱")
st.write("버튼을 누르면 랜덤으로 무서운 그림이 나옵니다 😱")

# 사용할 이미지 주소들
images = [
    "https://images.unsplash.com/photo-1509248961158-e54f6934749c",
    "https://images.unsplash.com/photo-1518709268805-4e9042af2176",
    "https://images.unsplash.com/photo-1507149833265-60c372daea22"
]

# 버튼
if st.button("무서운 그림 보기 👁️"):
    random_image = random.choice(images)
    st.image(random_image, use_container_width=True)
