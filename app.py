import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BiogenX | Academic & Research Care",
    page_icon="🎓",
    layout="wide"
)

# --- CUSTOM CSS (Shifat's Tales Inspired Style) ---
st.markdown("""
<style>
    /* Light Cream Background */
    .stApp {
        background-color: #fdfbf7;
        color: #0d1b2a;
    }
    
    /* Hide Streamlit Default Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Top Announcement Badge */
    .badge {
        background-color: #ffffff;
        color: #1b263b;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 6px 16px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Hero Title */
    .hero-title {
        color: #0a192f;
        font-size: 38px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 10px;
        line-height: 1.2;
    }
    
    .hero-sub {
        color: #475569;
        text-align: center;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* Sidebar Custom Navy Blue */
    section[data-testid="stSidebar"] {
        background-color: #001d3d !important;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Student Dashboard Style) ---
st.sidebar.markdown("<h2 style='color:#ffb703 !important;'>🎓 BiogenX Hub</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:12px; color:#cbd5e1 !important;'>Academic & Research Care</p>", unsafe_allow_html=True)

nav = st.sidebar.radio("Dashboard Navigation", [
    "📊 Dashboard Home",
    "📚 Academic Journey (HSC/SSC)",
    "🧪 3D Bio-Lab & Tools",
    "🇧🇩 Public Health Tracker (2026)",
    "🔬 Simplified Research Papers",
    "👨‍🏫 Founder & Personal Guidance"
])

# ==========================================
# 1. DASHBOARD HOME
# ==========================================
if nav == "📊 Dashboard Home":
    st.markdown("<div style='text-align:center;'><span class='badge'>🟡 Open Access for Biology & Biotech Enthusiasts</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>Personal Guidance & 3D Interactive Care For Better Biology Success</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>অল্প সময়ে গোছানো প্রস্তুতি, সঠিক গাইডলাইন ও ৩D ভিজ্যুয়ালাইজেশন পেতে বায়ো-রিসার্চ জার্নিতে তোমাকে স্বাগতম! 💬</div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📞 Contact Founder"):
            st.info("💬 Connect via Email: contact@biogenx.org")
    with c2:
        if st.button("▶️ Explore 3D Bio-Lab"):
            st.success("👈 বামপাশের মেনু থেকে '3D Bio-Lab & Tools' সিলেক্ট করো!")
    with c3:
        if st.button("👤 Visit Founder Portfolio"):
            st.info("👨‍🔬 Founder Section Active in Dashboard Menu!")

    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; color:#64748b; font-size:14px; font-weight:600;'>
    Interactive 3D Visuals • Disease Epidemiology • Research Digest • 24/7 Problem Solving
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 2. ACADEMIC JOURNEY
# ==========================================
elif nav == "📚 Academic Journey (HSC/SSC)":
    st.subheader("📚 Academic Syllabus Breakdown & 3D Lessons")
    
    topic = st.selectbox("একটি বিষয় সিলেক্ট করো:", [
        "DNA Double Helix Structure (ডিএনএ গঠন)",
        "Human Heart & Blood Circulation",
        "Cell Division & Mitosis"
    ])
    
    if "DNA" in topic:
        st.write("**ব্যাখ্যা:** ওয়াটসন ও ক্রিক এর দ্বিসূত্রক মডেল অনুযায়ী DNA দুটি প্যাঁচানো সূত্রের মতো গঠিত।")
        html_code = """
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div id="container" style="width: 100%; height: 350px; border-radius: 12px; border: 2px solid #ffb703;"></div>
        <script>
            let viewer = $3Dmol.createViewer( document.getElementById('container'), { backgroundColor: '#001d3d' } );
            $3Dmol.download("pdb:1bna", viewer, {}, function() {
                viewer.setStyle({}, {cartoon: {color: 'spectrum'}});
                viewer.zoomTo();
                viewer.render();
            });
        </script>
        """
        components.html(html_code, height=370)

# ==========================================
# 3. 3D BIO-LAB & TOOLS
# ==========================================
elif nav == "🧪 3D Bio-Lab & Tools":
    st.subheader("🧪 Interactive 3D Drug & Molecular Explorer")
    
    pdb = st.text_input("Enter 4-letter PDB Code (e.g. 4ins = Insulin, 1c8u = Paracetamol):", "4ins").lower()
    
    html_code = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div id="container" style="width: 100%; height: 400px; border-radius: 12px; border: 2px solid #001d3d;"></div>
    <script>
        let viewer = $3Dmol.createViewer( document.getElementById('container'), {{ backgroundColor: '#001d3d' }} );
        $3Dmol.download("pdb:{pdb}", viewer, {{}}, function() {{
            viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}, stick: {{}}}});
            viewer.zoomTo();
            viewer.render();
        }});
    </script>
    """
    components.html(html_code, height=420)

# ==========================================
# 4. PUBLIC HEALTH TRACKER
# ==========================================
elif nav == "🇧🇩 Public Health Tracker (2026)":
    st.subheader("🇧🇩 Bangladesh Public Health & Disease Insight")
    
    disease = st.selectbox("Disease Profile:", ["Dengue Virus", "Nipah Virus"])
    if disease == "Dengue Virus":
        st.write("• **উপসর্গ:** তীব্র জ্বর, চোখের পেছনে ব্যথা, রক্তে প্লাটিলেট কমে যাওয়া।")
        st.write("• **প্রতিকার:** মশারি ব্যবহার করা এবং এডিস মশার লার্ভা জমে থাকা পানি পরিষ্কার রাখা।")

# ==========================================
# 5. RESEARCH PAPERS
# ==========================================
elif nav == "🔬 Simplified Research Papers":
    st.subheader("🔬 Simplified Scientific Publications")
    st.write("• **CRISPR-Cas9 Gene Editing:** জিনের সুনির্দিষ্ট অংশ কেটে বা পরিবর্তন করে জটিল বংশগত ব্যাধি নিরাময়ের আধুনিক প্রযুক্তি।")

# ==========================================
# 6. FOUNDER PROFILE
# ==========================================
elif nav == "👨‍🏫 Founder & Personal Guidance":
    st.subheader("👨‍🏫 Founder's Personal Guidance")
    st.write("আমি একজন বায়োটেকনোলজি অনুরাগী ও ডেভেলপার, যে শিক্ষা ও আধুনিক ৩D প্রযুক্তির মেলবন্ধন ঘটিয়ে শিক্ষাব্যবস্থাকে সহজ করতে কাজ করছি।")
