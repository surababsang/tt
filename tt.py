import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red','green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

col = st. columns(4)
with col[0]:
    a = st.number_input('a의 값을 입력하시오', value = 2.0, step = 1.0)
with col[1]:
    b = st.number_input('b의 값을 입력하시오', value = -1.0, step = 1.0)
with col[2]:
    c = st.number_input('c의 값을 입력하시오', value = 15.0, step = 1.0)
with col[3]:
    d = st.number_input('d의 값을 입력하시오', value = 2000.0, step = 100.0)


x = []
y = []
for i in range(-29, 30, 3):
    x.append(i)
    y.append(-2*i*i + 3*i + 5)

# plt.plot(x, y, 'r:^')
plt.plot(x, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)

import sys
sys.exit()
