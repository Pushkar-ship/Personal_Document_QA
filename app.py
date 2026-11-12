import streamlit as st

st.set_page_config(
    page_title='Personal Document Q&A',
    page_icon='📚'
)

st.title("Personal Document Q&A")

st.write(
    "Upload your PDF documents"
    "and ask questions about them"
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=['pdf']
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

