import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import textwrap

st.set_page_config(
    page_title="Эхлэл",
    page_icon="📌",
)

st.sidebar.header("Mongolian SDG Tracker App Demo")

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def create_clickable_icon(image_path, alt_text, title, index):
    page_route = f"./{title.replace(' ', '_')}"
    encoded_image = image_to_base64(Image.open(image_path))

    wrapped_title = '<br>'.join(textwrap.wrap(title, width=20))

    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="display: inline-block; text-align: center;">
                <a href="{page_route}" style="text-decoration: none;">
                    <img src="data:image/png;base64,{encoded_image}" alt="{alt_text}" style="width:150px;">
                </a>
                <p style="max-width: 50px; margin-top: 5px; margin-left:50px; text-align: center; font-weight: bold;">{wrapped_title}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)



#text here
st.title('Sustainable Development Goals')
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

cols_per_row = 4 
rows = (17 + cols_per_row - 1) // cols_per_row 

english_titles = [
    "No Poverty",
    "Zero Hunger",
    "Good Health and Well-being",
    "Quality Education",
    "Gender Equality",
    "Clean Water and Sanitation",
    "Affordable and Clean Energy",
    "Decent Work and Economic Growth",
    "Industry Innovation and Infrastructure",
    "Reduced Inequalities",
    "Sustainable Cities and Communities",
    "Responsible Consumption and Production",
    "Climate Action",
    "Life Below Water",
    "Life on Land",
    "Peace Justice and Strong Institutions",
    "Partnerships for the Goals"
]


st.markdown(
    """
    <style>
    .block-container>div>div>div>div {
        padding: 2px 4px; 
    }
    .block-container>div>div>div>div img {
        display: block;
        justify-content: space-between;
        margin: 0 auto; 
        width: 15px;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

for row_num in range(rows):
    cols = st.columns(cols_per_row)
    for col_num in range(cols_per_row):
        index = row_num * cols_per_row + col_num
        if index < 17: 
            icon_path = f'assets/sdg-goals-icons/{str(index+1).zfill(2)}.png'
            alt_text = f'SDG Goal {index+1}'
            title = english_titles[index]  #use eng title (can be substituted for mongolian)
            page_file_path =  f"./{title.replace(' ', '_')}"

            
            with cols[col_num]:
                encoded_image = image_to_base64(Image.open(icon_path))
                link_content = f'<a href="{page_file_path}" style="text-decoration: none;"><img src="data:image/png;base64,{encoded_image}" alt="{alt_text}" style="width:150px;"></a>'
                st.markdown(link_content, unsafe_allow_html=True)

