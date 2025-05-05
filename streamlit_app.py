cd DSCP

# Create the Python file with valid content
echo "import streamlit as st\nst.title('My First Streamlit App')\nst.write('Hello from Streamlit!')" > streamlit_app.py

# Push it to GitHub
git add streamlit_app.py
git commit -m "Add working Streamlit app"
git push origin main

