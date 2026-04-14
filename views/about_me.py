import streamlit as st

from forms.contact import contact_form

# --- CSS for specific elements ---
st.markdown(
    """
    <style>
    /* Target only the profile picture in the hero section */
    .hero-img img {
        border-radius: 50%;
    }
    
    /* Force all certification columns to be identical */
    .cert-section [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
    }

    /* Style the certification cards to have a strict fixed height and "Card" look */
    .cert-section [data-testid="stVerticalBlockBorderWrapper"] {
        height: 350px !important;      /* Fixed height for all boxes - Reduced to be less "long" */
        min-height: 350px !important;
        max-height: 350px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        padding: 15px !important;      /* Reduced padding */
        box-sizing: border-box !important;
        border: 1px solid #333333 !important; /* Subtle dark border */
        border-radius: 12px !important;
        background-color: #111111 !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    /* Hover effect for cards */
    .cert-section [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 120, 212, 0.2) !important; /* Blue glow */
        border-color: #0078d4 !important;
    }

    /* Standardize certification image containers */
    .cert-img-container {
        height: 100px !important;      /* Standardized height for logo area */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-bottom: 10px !important;
    }
    
    .cert-img-container img {
        max-height: 80px !important;   /* Standardized logo size */
        width: auto !important;
        object-fit: contain !important;
    }

    /* Ensure text area is consistent */
    .cert-text {
        height: 80px;                  /* Consistent height for titles */
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        margin-bottom: 5px !important;
        font-size: 1.0em;
    }

    /* Button style for "View Certification" */
    .cert-link {
        background-color: #0078d4; 
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
        transition: background-color 0.3s;
        font-weight: bold;
        width: 100%; 
        text-align: center;
        box-sizing: border-box;
    }

    .cert-link:hover {
        background-color: #005a9e; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Hero section ---
col1, col2 = st.columns([1, 1], gap = "medium", vertical_alignment = "center")

with col1:
    st.markdown('<div class="hero-img">', unsafe_allow_html=True)
    st.image("assets/profile_v2.png", width = 500)
    st.markdown('</div>', unsafe_allow_html=True)

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

with col2:
    st.title("Jun Song", anchor = False)
    st.write(
        "Data Scientist | Assisting enterprises in making data-driven decisions through insightful analysis and visualization."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- Experience & Qualifications ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor = False )
st.write("""
         - Over 4 years of experience as a Data Analyst and Data Scientist
         - Proficient in Python, SQL, and Power BI for data analysis and visualization
         """
         )

# --- Skills ---
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Data Analysis & Visualization: Python (Pandas, Matplotlib, Seaborn), SQL, Power BI
    - Statistical Analysis: Hypothesis Testing, Regression Analysis, A/B Testing
    """
)

# --- Certifications ---
st.write("\n")
st.subheader("Certifications", anchor=False)

# Certification data
certs = [
    {
        "title": "Azure Fundamentals (AZ-900)",
        "image": "assets/azure_fund.png",
        "link": "https://learn.microsoft.com/api/credentials/share/en-us/JunSong-5041/786AEB5C9A3CF009?sharingId=45F5A439DD34DA79"
    },
    {
        "title": "Machine Learning Specialization - DeepLearning.AI",
        "image": "assets/deepLearning.jpeg",
        "link": "https://coursera.org/share/9d072142a12734248b81b4aaf64e20a6"
    },
    {
        "title": "Google Data Analytics Professional Certificate",
        "image": "assets/google_logo_v2.png",
        "link": "https://coursera.org/share/6954042ae7c1941480899e8a50f0ad79"
    },
    {
        "title": "IBM Data Science Professional Certificate",
        "image": "assets/IBM_LOGO.png",
        "link": "https://coursera.org/share/33d001c7b204eb3d05c72447b0ecef38"
    },
    {
        "title": "IBM Data Analyst Professional Certificate",
        "image": "assets/IBM_LOGO.png",
        "link": "https://coursera.org/share/0ccbc6368cf1e00b3603ab1f33f13eef"
    }
]

# Carousel logic using session state
if "cert_index" not in st.session_state:
    st.session_state.cert_index = 0

def next_cert():
    if st.session_state.cert_index < len(certs) - 3:
        st.session_state.cert_index += 1

def prev_cert():
    if st.session_state.cert_index > 0:
        st.session_state.cert_index -= 1

# Display 3 at a time with side arrows
st.markdown('<div class="cert-section">', unsafe_allow_html=True)
col_prev, col_content, col_next = st.columns([0.5, 9, 0.5], gap="small", vertical_alignment="center")

with col_prev:
    st.button("❮", key="prev", on_click=prev_cert, disabled=(st.session_state.cert_index == 0))

with col_content:
    cert_cols = st.columns(3)
    for i in range(3):
        idx = st.session_state.cert_index + i
        if idx < len(certs):
            cert = certs[idx]
            with cert_cols[i]:
                import base64, os
                # Load image as base64 so it works inline in HTML
                with open(cert["image"], "rb") as f:
                    ext = os.path.splitext(cert["image"])[1].lstrip(".")
                    if ext == "svg":
                        mime = "image/svg+xml"
                    elif ext in ("jpg", "jpeg"):
                        mime = "image/jpeg"
                    else:
                        mime = f"image/{ext}"
                    img_b64 = base64.b64encode(f.read()).decode()

                st.markdown(f"""
                    <div style="
                        height: 350px;
                        border: 1px solid #333333;
                        border-radius: 12px;
                        background-color: #111111;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: space-between;
                        padding: 20px 15px;
                        box-sizing: border-box;
                        transition: transform 0.3s ease, box-shadow 0.3s ease;
                    ">
                        <div style="
                            height: 100px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">
                            <img src="data:{mime};base64,{img_b64}"
                                 style="max-height: 110px; max-width: 120%; object-fit: contain;" />
                        </div>
                        <div style="
                            flex: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            text-align: center;
                            padding: 10px 0;
                            font-size: 1.0em;
                            font-weight: bold;
                            color: white;
                        ">
                            {cert["title"]}
                        </div>
                        <a href="{cert["link"]}" target="_blank" style="
                            background-color: #0078d4;
                            color: white;
                            padding: 8px 16px;
                            border-radius: 6px;
                            text-decoration: none;
                            font-weight: bold;
                            width: 100%;
                            text-align: center;
                            box-sizing: border-box;
                            display: block;
                        ">View Certificate</a>
                    </div>
                """, unsafe_allow_html=True)

with col_next:
    st.button("❯", key="next", on_click=next_cert, disabled=(st.session_state.cert_index >= len(certs) - 3))
st.markdown('</div>', unsafe_allow_html=True)
