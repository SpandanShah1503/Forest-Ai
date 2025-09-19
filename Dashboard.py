import streamlit as st

#st.write("Hello")

st.title("Document Submission")


code_example = """
  def user(name)
      print(Hey User Add your PDF here) 
"""
st.code(code_example, language = "python")

st.divider()

with st.form(key = "Form"):

  st.file_uploader("Upload Your PDF")
  st.form_submit_button() 