import streamlit as st
import streamlit.components.v1 as components

# Set page title and configuration
st.set_page_config(
    page_title="IntelliScan AI | About",
    page_icon=":brain:",
    initial_sidebar_state="expanded",
)

# --- HIDE STREAMLIT STYLE ---
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

# --- DEVELOPER INFORMATION ---
mayank = {
    'name': 'Mayank Shukla',
    'bio': 'I am a passionate AI developer and machine learning enthusiast dedicated to leveraging technology to solve real-world problems. My expertise lies in computer vision and developing intelligent systems that can make a tangible impact. This project is a culmination of my dedication to creating accessible and innovative technological solutions.',
    'email': 'mayankshukla270903@gmail.com',
}

# --- PAGE HEADER ---
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            left: 0px;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#20D2FE, #5292FE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">About</p>
    """,
    height=69,
)

# --- ABOUT THE DEVELOPER ---
st.markdown("## About the Developer")

# You can add your image here if you have one.
# For example: st.image("path/to/your/photo.jpg", width=200)

st.markdown(f"### {mayank['name']}")
st.write(mayank['bio'])
st.write(f"**Contact Email:** {mayank['email']}")
st.divider()

# --- ABOUT THE PROJECT ---
st.markdown("## IntelliScan AI")
st.write("IntelliScan AI is an application that uses artificial intelligence and machine learning to analyze and detect anomalies from images uploaded by users. Our goal is to make advanced analysis more accessible by providing a fast, accurate, and reliable tool. We believe that technology can revolutionize the way we approach image analysis, and we're excited to be at the forefront of this innovation.")