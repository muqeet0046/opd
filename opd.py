import streamlit as st

st.set_page_config(page_title="Abdul Muqeet Madni's Portfolio", layout="wide")

menu = ["Home", "About Me", "Projects", "Skills", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":

    st.title("Welcome to My Portfolio")
    st.image("profile.png", width= 300)
    st.write("""
    ## Hello! I'm Abdul Muqeet Madni

    A passionate Data Science student eager to make an impact in the tech world. With a strong foundation in data analysis and a keen interest in leveraging data for meaningful insights, I am on a journey to turn complex data into actionable strategies.

    I am currently pursuing my Bachelor's degree in Data Science at the University of Central Punjab. 
    Explore my projects, skills, and get in touch through the navigation menu!
    """)


if choice == "About Me":
    st.header("About Me")
    st.write("""
I am a Data Science student at the University of Central Punjab, currently pursuing my Bachelor's degree. I have a solid foundation in computer skills, including Microsoft Office Suite, email and communication tools, operating systems, Ecommerce, and Marketing . My volunteer experience with Karr-e-Kamal has deepened my commitment to social impact. 
""")
    
    st.subheader("Education")
    st.write("""
    - **University of Central Punjab**: BS in Data Science (in progress)
    - **Government Islamia College**: Intermediate (F.S.C Pre Engineering) (2019-2021)
    - **Brightway Foundation High School**: Matriculation (Science) (2017-2019)
    """)
   
    st.subheader("Skills and Expertise")
    st.write("""
    - Microsoft Office Suite
    - Email and Communication Tools
    - Operating Systems (Windows, Linux)
    - Data Security and Privacy
    - Collaboration and Project Management 
    - Ecommerce
    - Marketing (" Meta, Google, Amazon ")
    """)

if choice == "Projects":
    st.header("Projects")
    st.image("AdobeStock_519767884-1-1024x652.jpeg", width= 250)
    st.subheader("Machine Learning Model")
    st.write("Description: making a accurate model by giving fifa player dataset check the model efficiency .")
    st.write("Language: Python")
    st.write("[View Source Code](https://drive.google.com/drive/folders/1Q9R4sVVPgWmmYu-lQV658Vyi04MPzvxy?usp=sharing)")

    st.image("Screenshot 2025-01-20 193255.png", width= 250)
    st.subheader("AVL Tree ")
    st.write("Description: This project is created on major concept of Data structure and algorithm, About how this AVL tree algorithm work and performed")
    st.write("Language: C++")
    st.write("[View Source Code](https://drive.google.com/drive/folders/1Q9R4sVVPgWmmYu-lQV658Vyi04MPzvxy?usp=sharing)")
    
    st.image("Screenshot 2025-01-20 200609.png", width= 250)
    st.subheader("Online House Renting Management System")
    st.write("Description: In this Project we created a database which include the almost all the concept  of database. To create Online House Renting database for the Client  ")
    st.write("Language: SQL")
    st.write("[View Source Code](https://drive.google.com/drive/folders/1Q9R4sVVPgWmmYu-lQV658Vyi04MPzvxy?usp=sharing)")

if choice == "Skills":
    
    st.subheader("Hobbies and Interests")

    st.write(" - **Hobbies**: Researching about Tech and Dropshipping, PCs, Components, Video Games, Trading, ")
    st.write(" - **Interests**: Tech, IT, Dropshipping, Shopify, Product Hunting, Product Marketing, Esports, Football .")
    
    st.header("Skills")
    st.write("""
    - **Microsoft Office Suite**: 
    - **Email and Communication Tools**: 
    - **Operating Systems (Windows, Linux)**: 
    - **Data Security and Privacy**: 
    - **Collaboration and Project Management Tools**: 
    - **Trading**:
    - **Marketing**:
    """)
 
    st.progress(85)  
    st.progress(80)  
    st.progress(85) 
    st.progress(70)  
    st.progress(75)  
    st.progress(70)
    st.progress(75)

    

if choice == "Contact":
    st.header("Contact Me")
    
    st.write("Feel free to reach out to me via the form below or through my social media profiles.")
    
   
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success("Thank you! Your message has been sent.")
    
    st.write("[LinkedIn](#) | [GitHub](#) | [Twitter](#)")

custom_css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
