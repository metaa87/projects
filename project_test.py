# importing the useful librariees
import time
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_extras.let_it_rain import rain

# defining the subject of the web-app
st.title('Welcome to Age Prediction Game')
st.markdown('### How old is he? Make your guess.')

# inserting the desired photo
b = Image.open(r"E:\Python exercises\Simon 1.jpg")
st.image(b)

# defining some essential variables
y_true = np.array([54])
y_pred = np.array([st.number_input('Enter Your Guess:')])
score = 100 - (np.sum(np.square(y_pred - y_true)))

# Let's play the game!
if y_pred == y_true:
    st.success('Great Job!')
    rain(emoji = '🎊' , font_size = 60 , falling_speed = 3 , animation_length = 'temporary')
elif y_pred < y_true :
    st.info('Look Carefully!')
elif y_pred > y_true :
    st.info('Is he that old?!')

if st.button('Score'):
    st.text(f'Your Score is {round(score)}')

# The End
if st.button('Bye!'):
    with st.spinner('I\'d love to hear your thoughts on my first project. Please feel free to give feedback! https://t.me/bahare_cs'):
        time.sleep(7)
