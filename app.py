from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#---CONFIG URL
st.set_page_config(page_title="Welcome Homie", page_icon="🤘", layout="wide")


#---ANIMATIONS
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


#---HEADER---
with st.container():
    st.markdown(
        """
        <div style="text-align: right;">
            <img src="https://c.tenor.com/S3cTWxIvxj0AAAAC/tenor.gif" style="height: 200px;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style='text-align: center; color: #000000; background-color: #E6E6FA; padding: 10px; font-size: 100;'>WELCOME TO DREAMCRAFT FX MEDIA</h2>
        """,
        unsafe_allow_html=True
    )
    st.write("##")
    st.subheader("Crafting Cinematic Magic for the World")
    st.write("At Dreamcraft FX Media, we're dedicated to turning your creative visions into reality. Our passion is to enhance your workflows by integrating advanced pipeline tools and crafting custom solutions.")
    st.write("[Click here for more info >](https://in.linkedin.com/in/suraj-sinha-54b07b1a8)")


#---ANIMATION
lottie_animation = load_lottie_url("https://lottie.host/1e6f6b90-d56b-41ed-a14d-626e96925da0/7nJHYmT7hI.json")


#---INTERESTING FACTS---
with st.container():
    st.write("---")
    leftColumn, rightColumn = st.columns(2)
    with leftColumn:
        st.header("Discover Our Magic")
        st.write("##")
        st.write(
            '''
            At Dreamcraft FX Media, we breathe life into your creative projects with cutting-edge VFX techniques. Here's a peek into what we do:
            - **Visual Effects Design:** Crafting stunning effects that bring your visuals to life.
            - **Pipeline Integration:** Seamlessly integrating tools to streamline your VFX workflow.
            - **Custom Gizmos:** Building tools tailored to your needs to enhance your creative process.
            - **Code Snippets:** Providing powerful, reusable code solutions for your VFX needs.
            
            Explore our work and see how we can elevate your projects to new heights!
            '''
            )
    with rightColumn:
        st_lottie(lottie_animation, height=500, key="coding")
        
#---WE DIG
with st.container():
    st.write("---")
    st.markdown(
        """
        <h2 size=50 style='text-align: center;'>A Quick Breakdown of Our VFX Work</h2>
        """,
        unsafe_allow_html=True
    )
    st.write("##")
    videoColumn, videoColumn2, videoColumn3 = st.columns((1, 1, 1))
    with videoColumn:
        video_file = open("videos/vfx.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
    with videoColumn2:
        video_file = open("videos/vfx.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
    with videoColumn3:
        video_file = open("videos/vfx.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        
#---PORTFOLIO---
with st.container():
    st.write("---")
    st.subheader("Portfolio Highlights")
    st.write("##")
    st.write(
    '''
    Our VFX services cover a wide range of applications to suit your project needs. Whether you're working on film, TV, gaming, or digital media, we offer comprehensive solutions:
    - **Compositing:** Combining visual elements from different sources into single images.
    - **Motion Graphics:** Creating dynamic graphics that enhance storytelling.
    - **3D Animation:** Bringing characters and objects to life with 3D animation.
    - **Special Effects:** Adding dramatic effects that captivate audiences.
    '''
)
    st.image("images/portfolio_preview.gif", caption="Portfolio Preview")



#---CONTACT ME
with st.container():
    st.write("---")
    st.header("Reach Out")
    
    contact_me = """
    <form action="https://formsubmit.co/farjiwalaid02@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Write your hearts out" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    # Inline CSS for background image
    st.markdown("""
    <style>
    .stApp {
        background-image: url('https://steamuserimages-a.akamaihd.net/ugc/299860700355542580/CCEC3381062DCE1DC215DC7D55442850C90E1EEE/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false');
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    leftColumn, rightColumn = st.columns(2)
    with leftColumn:
        st.markdown(contact_me, unsafe_allow_html=True)
    with rightColumn:
        st.empty()