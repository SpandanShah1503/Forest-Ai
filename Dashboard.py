import streamlit as st

#st.write("Hello")

st.title("Document Submission")


code_example = """
  def user(name)
      print(Hey User Add your PDF here) 
"""
st.code(code_example, language = "python")

st.divider()

st.button("Submit Document")