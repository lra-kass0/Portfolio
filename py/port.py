import streamlit as st
from PIL import Image


#####################
# Header 
st.write('''
# Lahoucine Aitattaleb
##### *Resume* 
''')


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)



#####################
st.markdown('''
## Education
''')

txt('**Student** , *`eWA Ecole de digital`*, Morocco',
'2022-2023')
st.markdown('''
- I Get `Baccalaureate` SVT in 2021/2022
''')

#####################
st.markdown('''
## Work Experience
''')
st.markdown('''
- `Blockchain` NFT & Crypto Currency
- Print on Demand
- Video's `Editing`
''')
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 `Programming`: html, CSS, Wordpress
- 🗄️ `LOGIECIAL` : photoshop, Editing vedios
- 📚 `Collab Manager` "Nft Ecosystem"
"""
)
#####################
st.markdown('''
## Social Media
''')
txt2('Twitter', 'https://twitter.com/Hpm_25')
txt2('GitHub', 'https://github.com/hosainaittaleb')
txt2('Instagram', 'https://www.instagram.com/aittaleb_hosain')
