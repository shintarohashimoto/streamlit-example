import streamlit as st
import qrcode
import tempfile
import os
from PIL import Image


sei = st.text_input('姓')
mei = st.text_input('名')
seinengappi = st.text_input('生年月日')
value = sei+mei+seinengappi
if value:
    with tempfile.TemporaryDirectory() as folder:
        img = qrcode.make(value)
        path = os.path.join(folder, "test.png")
        img.save(path)
        with Image.open(path) as f:
            st.image(f, caption='Sunrise by the mountains')
