import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


# download the image
img_url = 'https://www.bing.com/images/search?view=detailV2&ccid=fuCb7wnv&id=69A2BF09FC9E5B1F83B4B24AE32858ABC900C7F1&thid=OIP.fuCb7wnvVw2X9W2AMP2wwwHaFj&mediaurl=https%3a%2f%2faichinavi.jp%2fupload%2fspot_images%2f59452062a560b2d7dcd24dfc7c8c4622.jpg&exph=900&expw=1200&q=%e7%8a%ac%e5%b1%b1%e5%9f%8e&simid=607996562979506165&FORM=IRPRST&ck=7E9A88D4CDA001D82CAF2723D112A91A&selectedIndex=6&ajaxhist=0&ajaxserp=0'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    df_hist = pd.DataFrame(hist_red)
    st.bar_chart(df_hist)
if color == 'G':
    df_hist = pd.DataFrame(hist_green)
    st.bar_chart(df_hist)
if color == 'B':
    df_hist = pd.DataFrame(hist_blue)
    st.bar_chart(df_hist)
