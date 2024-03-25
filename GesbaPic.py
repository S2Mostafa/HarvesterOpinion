import streamlit as st
import os
from pathlib import Path

col1,col2 = st.columns(2)
#print(Path.cwd())
#print(os.path())
if 'counter' not in st.session_state: 
    st.session_state.counter = 0

def showPhoto(photo):
    col2.image(photo)#,caption=photo
    col1.write(f"Index as a session_state attribute: {st.session_state.counter}")
    
    ## Increments the counter to get next photo
    st.session_state.counter += 1
    if st.session_state.counter >= len(pathsImages):
        st.session_state.counter = 0

# Get list of images in folder
folderWithImages = r"images"
#pathsImages = [os.path.join(folderWithImages,f) for f in os.listdir(folderWithImages)]

pathsImages = os.listdir(folderWithImages)

col1.subheader("List of images in folder")
col1.write(pathsImages)

# Select photo a send it to button
photo = pathsImages[st.session_state.counter]
show_btn = col1.button("Show next pic ⏭️",on_click=showPhoto,args=([photo]))