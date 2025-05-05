import streamlit as st

st.title('My First Streamlit App')
st.write('Hello from Streamlit!')

echo "import streamlit as st\nst.title('My First Streamlit App')" > streamlit_app.py
git add streamlit_app.py
git commit -m "Add streamlit_app.py"
git push origin main
