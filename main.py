import streamlit as st
from streamlit_option_menu import option_menu

# st.title("hello world")
# st.header("this is a header")
# st.subheader("this isa subheader")
# st.write("this is a text")
# st.text("this isa text")
# st.code("""
# num1 = float(input("enter first number:"))
# num2 = float(input("enter second number:"))

# Add two numbers
# sum = num1 + num2

#  """, language="python")

# st.latex(r"E=mc^2")
# st.metric(label="Temperate",value="70 degree F")
# st.progress(0.5,text="50%")
# st.text_input("Enter your name")
# st.number_input("enter your age")
# st.date_input("enter your date of birth")
# st.checkbox("I agree")
# st.radio("select your gender",["male","female","other"])
# st.mu;tiselect("select your country",["united states","canada","united kingdom"])
# st.slider(label="select your age",min_value=0,max_value=100,value=23)

with st.sidebar:

    select = option_menu(
        menu_title="vinsup",
        options=['Home','About','Services'],
        icons=['house','file-person','gear']


    )
if select=="Home":
    st.title("welcome to Home")
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        a= st.text_input("Name")
        if st.button("Click"):
         st.write(a)
         st.balloons()
    with col2: 
        st.text_input("Email")     
elif select=="About": 
    st.title("Welcome to about")
elif select=="Services":
    st.title("welcome to Services")                    