import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BiogenX | Crop & Public Health Pathogen Repository",
    page_icon="🔬",
    layout="wide"
)

# --- CUSTOM CSS (Clean, Modern & Spaced UI) ---
st.markdown("""
<style>
    /* Global Page Background & Font */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Header, Footer & Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Header Section Banner */
    .header-box {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        padding: 35px 25px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(2, 132, 199, 0.2);
    }
    .header-box h1 {
        font-size: 38px !important;
        font-weight: 800 !important;
        margin-bottom: 8px !important;
        color: #ffffff !important;
    }
    .header-box p {
        font-size: 16px;
        color: #e0f2fe;
        margin: 0;
    }

    /* Pathogen Disease Card */
    .pathogen-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Disease Title Badge */
    .disease-title {
        color: #0369a1;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .sci-name {
        color: #64748b;
        font-style: italic;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* Tab Design */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #ffffff;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        padding: 0 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0284c7 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
<div class='header-box'>
    <h1>BiogenX 🔬</h1>
    <p>Bangladesh Crop Pathology & Public Health Pathogen Repository</p>
</div>
""", unsafe_allow_html=True)

# --- MAIN NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs([
    "🌾 Agricultural Pathology (কৃষি রোগতত্ত্ব)", 
    "🦠 Public Health Pathogens (জনস্বাস্থ্য রোগতত্ত্ব)",
    "📖 Scientific Methodology & Impact"
])

# ==========================================
# TAB 1: AGRICULTURAL PATHOLOGY
# ==========================================
with tab1:
    st.subheader("🌾 Crop Pathogens & Disease Manifestations in Bangladesh")
    st.caption("বাংলাদেশে ফসলের ফলন ধ্বংসকারী প্রধান ভাইরাস, ছত্রাক ও ব্যাকটেরিয়া ঘটিত রোগের সায়েন্টিফিক ক্যাটালগ।")
    
    crop_disease = st.selectbox("Select Crop Disease:", [
        "Rice Tungro Disease (ধানের টুংরো ভাইরাস)",
        "Wheat Blast Disease (গমের ব্লাস্ট ছত্রাক)",
        "Late Blight of Potato & Tomato (আলু ও টমেটোর লেট ব্লাইট)",
        "Papaya Ring Spot Virus (পেঁপের রিং স্পট ভাইরাস)",
        "Banana Bunchy Top Virus (কলার বাঞ্চি টপ ভাইরাস)"
    ])
    
    st.markdown("---")
    
    if crop_disease == "Rice Tungro Disease (ধানের টুংরো ভাইরাস)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Rice_tungro_spherical_virus.jpg/640px-Rice_tungro_spherical_virus.jpg", caption="Rice Tungro Affected Field & Plants", use_container_width=True)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🌾 ধানের টুংরো রোগ (Rice Tungro Disease)</div>
                <div class='sci-name'>Pathogen: Rice Tungro Bacilliform Virus (RTBV) & RTSV</div>
                <p><b>সংক্রমণের মাধ্যম:</b> সবুজ পাতাফড়িং (Nephotettix virescens) পোকার মাধ্যমে এই ভাইরাস ছড়ায়।</p>
                <p><b>উপসর্গ ও লক্ষণ:</b></p>
                <ul>
                    <li>ধান গাছের কচি পাতা হলুদ বা গাঢ় কমলা রঙ ধারণ করে।</li>
                    <li>গাছের বৃদ্ধি একদম থমকে যায় (Stunted growth) এবং শিকড় দুর্বল হয়ে পড়ে।</li>
                    <li>শীষে ধান আংশিক বা সম্পূর্ণ চিটা হয়।</li>
                </ul>
                <p><b>প্রতিকার ও প্রতিরোধমূলক ব্যবস্থা:</b></p>
                <ul>
                    <li>সবুজ পাতাফড়িং দমনে অনুমোদিত কিটনাশক ব্যবহার করা।</li>
                    <li>টুংরো প্রতিরোধী ধানের জাত (যেমন: বিআর-২২, বিআর-২৩) চাষ করা।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif crop_disease == "Wheat Blast Disease (গমের ব্লাস্ট ছত্রাক)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Magnaporthe_oryzae.jpg", caption="Wheat Blast Symptoms on Head", use_container_width=True)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🌾 গমের ব্লাস্ট রোগ (Wheat Blast)</div>
                <div class='sci-name'>Pathogen: Magnaporthe oryzae pathotype Triticum (Fungus)</div>
                <p><b>সংক্রমণের মাধ্যম:</b> বাতাস এবং দূষিত বীজের মাধ্যমে দ্রুত এক মাঠ থেকে অন্য মাঠে ছড়ায়।</p>
                <p><b>উপসর্গ ও লক্ষণ:</b></p>
                <ul>
                    <li>গমের শিষের গোড়ায় ধূসর বা কালো দাগ পড়ে এবং পুরো শিষ শুকিয়ে সাদা হয়ে যায়।</li>
                    <li>বীজ কুঁচকে যায় বা একেবারেই গঠিত হয় না।</li>
                </ul>
                <p><b>প্রতিকার ও প্রতিরোধমূলক ব্যবস্থা:</b></p>
                <ul>
                    <li>ব্লাস্ট প্রতিরোধী জাত (যেমন: বারি গম-৩৩) চাষ করা।</li>
                    <li>বীজ বপনের আগে ছত্রাকনাশক (Fungicide) দিয়ে শোধন করে নেওয়া।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif crop_disease == "Late Blight of Potato & Tomato (আলু ও টমেটোর লেট ব্লাইট)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/Phytophthora_infestans_01.jpg", caption="Late Blight Infection on Leaf & Tuber", use_container_width=True)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🥔 আলু ও টমেটোর মড়ক বা লেট ব্লাইট</div>
                <div class='sci-name'>Pathogen: Phytophthora infestans (Oomycete)</div>
                <p><b>উপসর্গ ও লক্ষণ:</b></p>
                <ul>
                    <li>পাতার কিনারে ছাই বা পানিভেজা গাঢ় বাদামি দাগ দেখা দেয়।</li>
                    <li>আর্দ্র আবহাওয়া বা কুয়াশায় দ্রুত পুরো মাঠ পচে কালো হয়ে যায়।</li>
                </ul>
                <p><b>প্রতিকার:</b> আক্রান্ত গাছে ম্যানকোজেব সমৃদ্ধ ছত্রাকনাশক স্প্রে করা এবং রোগমুক্ত বীজ ব্যবহার করা।</p>
            </div>
            """, unsafe_allow_html=True)

    elif crop_disease == "Papaya Ring Spot Virus (পেঁপের রিং স্পট ভাইরাস)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Papaya_ringspot_virus_on_fruit.jpg/640px-Papaya_ringspot_virus_on_fruit.jpg", caption="Papaya Fruit with Ring Spot Symptoms", use_container_width=True)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🍈 পেঁপের রিং স্পট ভাইরাস (PRSV)</div>
                <div class='sci-name'>Pathogen: Papaya Ringspot Virus (Potyvirus)</div>
                <p><b>উপসর্গ:</b> পেঁপের ফল এবং পাতায় রিং বা আংটির মতো গোল বাদামি দাগ পড়ে, পেঁপে মিষ্টি হয় না এবং ছোট থাকে।</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# TAB 2: PUBLIC HEALTH PATHOGENS
# ==========================================
with tab2:
    st.subheader("🦠 Major Public Health & Zoonotic Pathogens in BD")
    st.caption("বাংলাদেশের প্রধান জনস্বাস্থ্য হুমকি এবং সংক্রামক ভাইরাসের আণবিক পর্যবেক্ষণ।")
    
    health_disease = st.selectbox("Select Public Health Threat:", [
        "Dengue Virus (ডেঙ্গু ভাইরাসের প্রাদুর্ভাব)",
        "Nipah Virus (নিপা ভাইরাস সংক্রমণ)",
        "Rabies Lyssavirus (জলাতঙ্ক রোগ)"
    ])
    
    st.markdown("---")
    
    if health_disease == "Dengue Virus (ডেঙ্গু ভাইরাসের প্রাদুর্ভাব)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Aedes_aegypti_biting_human_vector.jpg/640px-Aedes_aegypti_biting_human_vector.jpg", caption="Aedes aegypti Vector", use_container_width=True)
            st.caption("3D Envelope Protein Structure Below:")
            html_code = """
            <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
            <div id="container" style="width: 100%; height: 260px; border-radius: 12px; border: 1px solid #0284c7;"></div>
            <script>
                let viewer = $3Dmol.createViewer( document.getElementById('container'), { backgroundColor: '#f8fafc' } );
                $3Dmol.download("pdb:1k4r", viewer, {}, function() {
                    viewer.setStyle({}, {cartoon: {color: 'spectrum'}});
                    viewer.zoomTo();
                    viewer.render();
                });
            </script>
            """
            components.html(html_code, height=270)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🦟 ডেঙ্গু ভাইরাস (Dengue Virus - DENV)</div>
                <div class='sci-name'>Pathogen: Flaviviridae Family (DENV-1, DENV-2, DENV-3, DENV-4)</div>
                <p><b>সংক্রমণ চক্র:</b> এডিস মশাবাহিত ভাইরাস। বর্ষার মৌসুমে এর বিস্তার তীব্র হয়।</p>
                <p><b>উপসর্গ:</b> তীব্র জ্বর, চোখের পেছনে ব্যথা, প্লাটিলেট কমে যাওয়া এবং অভ্যন্তরীণ রক্তপাত।</p>
                <p><b>প্রতিকার ও প্রতিরোধ:</b></p>
                <ul>
                    <li>জমে থাকা পানি ৩ দিনের মধ্যে ফেলে দেওয়া।</li>
                    <li>এনএস১ (NS1) অ্যান্টিজেন পরীক্ষা করানো এবং ওরাল স্যালাইন গ্রহণ।</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif health_disease == "Nipah Virus (নিপা ভাইরাস সংক্রমণ)":
        c1, c2 = st.columns([1, 1.2])
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pteropus_vampyrus.jpg/640px-Pteropus_vampyrus.jpg", caption="Fruit Bat (Pteropus) Host", use_container_width=True)
        with c2:
            st.markdown("""
            <div class='pathogen-card'>
                <div class='disease-title'>🦇 নিপা ভাইরাস (Nipah Virus)</div>
                <div class='sci-name'>Pathogen: Henipavirus genus</div>
                <p><b>সংক্রমণ:</b> কাঁচা খেজুরের রস এবং বাদুড়ের লালা/প্রস্রাব দ্বারা দূষিত ফলমূল খেলে মানুষে ছড়ায়।</p>
                <p><b>উপসর্গ:</b> তীব্র জ্বর, মস্তিষ্কে প্রদাহ (Encephalitis) এবং শ্বাসকষ্ট। মৃত্যুর হার প্রায় ৭০%।</p>
                <p><b>প্রতিরোধ:</b> শীতকালে কাঁচা খেজুরের রস না খাওয়া এবং পাখির খাওয়া ফল পরিহার করা।</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# TAB 3: METHODOLOGY & IMPACT
# ==========================================
with tab3:
    st.markdown("""
    <div class='pathogen-card'>
        <h3>🎯 Project Vision & Scientific Rigor</h3>
        <p><b>BiogenX</b> exists to centralize open-access pathology data for agricultural sustainability and public health awareness in Bangladesh.</p>
        <h4>Key Impact Areas:</h4>
        <ul>
            <li><b>Crop Security:</b> Educating farmers and agricultural students on early identification of viral/fungal plant threats.</li>
            <li><b>Epidemiology Awareness:</b> Providing data-driven insights into vector-borne diseases to reduce public health risks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
