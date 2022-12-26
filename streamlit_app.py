import streamlit as st

from PIL import Image
import glob, os
import sys

st.file_uploader(label="画像をアップロードしてください",type=["jpeg","png"],accept_multiple_files=True)
