import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red','green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

love = []
y = []
for i in range(-20, 21, 3):
    love.append(i)
    y.append(-2*i*i + 3*i + 5)

# plt.plot(x, y, 'r:^')
plt.plot(love, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)

import sys
sys.exit()






























# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# col1, col2, col3 = st.columns(3)

# with col1:
#     c1 = st.radio('선택 색을 선택하시오',('red', 'green', 'blue', 'orange'))
# with col2:
#     s1 = st.radio('선택 형태를 선택하시오', ('-', ':', '-.', '--'))
# with col3:
#     m1 = st.radio('마커의 형태를 선택하시오', ('o', '^', 's', 'p'))

# fig, ax = plt.subplot()

# x = []
# y = []
# for i in range (-20, 21,1):
#     x.append(i)
#     y.append (-2*i*i + 3*i + 5)

# plt.plot(x, y, color=c1, linestyle= s1, marker= 'h')

# # st.pyplot(fig)
# plt.plot(x, y, color=c1, linestyle=s1, marker=m1)




# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots()

# x = []
# y = []
# ysin = []
# for i in range (-20, 21,1):
#     x.append(i)
#     y.append(3*i*i - 5*i + 2)
#     ysin.append(1200*np,sin(i))

# plt.plot(x, y, 'rs-', lineidth = '2nd Function')
# plt.plot(x, ysin,'go--', label = 'sin Function')
# plt.legend()
# st.pyplot(fig)

# import sys
# sys.exit()


# import streamlit as st
# # import random
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# x=[]
# for i in range(-100, 100):
#     x.append(i/10.0)

# col = st. columns(3)
# with col[0]:
#     a = st.number_input('insert a', step = 10)
# with col[1]:
#     b = st.number_input('insert b', step = 10)
# with col[2]:
#     c = st.number_input('insert c', step = 10)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x,y)

# st. pyplot(fig)



# import time
# import random as r

# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# t.pensize(5)

# while True:
#     for i in range(20):
#         t.circle(1+5*i)
#         t.color(r.random, r.random, r.random)
#         t.goto(i*20, 0)
#     t.clear()
     
# # t.forward(100)

# turtle.done()



# import turtle
# screen = turtle. Screen()
# im1 = 'rabbit.gif'
# im2 = 'turtle.gif'
# im3 = 'moon.gif'
# im4 = 'Kim.gif'
# im5 = 'yoon.gif'
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()

# screen.addshape(im3)
# screen.addshape(im4)
# screen.addshape(im5)
# t1.shape(im3)
# t2.shape(im4)
# t3.shape(im5)

# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1. goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2. goto(-300,-100)

# t3.penup()
# t3.shapesize(3)
# t3.pensize(5)
# t3. goto(-300,-200)

# t1.pendown()
# t2.pendown()
# t3.pendown()
# t1.speed(1)
# t2.speed(1)
# t3.speed(1)

# for i in range(50):
#     d1 = r.randint(1,30)
#     t1.forward(d1)
#     d2 = r.randint(1,30)
#     t2.forward(d2)
#     d3 = r.randint(1,30)
#     t3.forward(d3)

# # t.speed(1)


# turtle.done()





# for _ in range(6):
#     a1= r.randint(1, 45)
#     a2= r.random()
#     a1, a2

# a = 0
# for i in range(100):
#     c = r.choice('abcdef')
#     if c == 'a':
#     a= a + 1

# a/n, %



# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)

# def rec(x, y, lx, ly):
#     turtle.bgcolor('yellow')
#     t.up()
#     t.goto(x,y)
#     t.down()
#     for i in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)


# rec(-200, 0, 100, 50)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 100)


# turtle.done()


# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)

# import random
# t = turtle.Turtle
# t.shape("turtle")

# for i in range(10)
# x = random.randint(-200,200)
# y = random.randint(-200,200)
# r = random.randint(1,100)
# t.penup()
# t.goto(x,y)
# t.pendown()
# t.circle(r)




# turtle.done()






# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)

# # color = ["red", "purple", "blue", "green", "yellow", "orange", "magenta" ]

# t.width(2)
# # turtle.bgcolor('black')

# length= 5

# for i in range(100):
#     t.forward(length)
#     # t.pencolor(color[length%7])
#     t.right(89)
#     length += 5

# turtle.done()


# for i in range(1, 10):
#     if 1%3 == 1:
#     i



# s = 70
# if s >= 90:
#     '당신의 점수는'+ str(s) + '점으로 :blue[A등급]입니다 축하드립니다'
# elif s >= 80:
#     '당신의 점수는'+ str(s) + '점으로 :green[B등급]입니다'
# elif s >= 70:
#     '당신의 점수는'+ str(s) + '점으로 :orange[C등급]입니다'
# elif s >= 60:
#     '당신의 점수는'+ str(s) + '점으로 :blue[D등급]입니다'
# else:
#     '당신의 점수는'+ str(s) + '점으로 :red[F등급]입니다'



# s = 0 #초기값
# for i in range(1,101,2):
#      's =', s, 'i =', i
#      s= s + i
#      s+= i
#     's + i= ', s

# s



# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# #여기에코드입력
# turtle.done()


# a = 3.141592*10*10.0
# b = (1/100)*1234

# print(a,b)
# a,b

# print('hello')

# st.write('hello')
# st.write('강아지+고양이')
# st.write('1+1')

# st.write('스트림릿.....')
# st.write('streamlit Image')
# st.image('images.jpg')
