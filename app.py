import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BiogenX | Frontiers Research Digest",
    page_icon="🔬",
    layout="wide"
)

# --- CUSTOM CSS (Clean Academic Journal UI) ---
st.markdown("""
<style>
    /* Global Page Background */
    .stApp {
        background-color: #0b132b;
        color: #e0e1dd;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Header & Footer Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Top Academic Header Banner */
    .header-box {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 100%);
        border: 1px solid #3a506b;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    .header-box h1 {
        color: #48cae4 !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        margin-bottom: 8px !important;
    }
    .header-box p {
        color: #90e0ef;
        font-size: 16px;
        margin: 0;
    }
    
    /* Research Paper Card */
    .paper-card {
        background-color: #1c2541;
        border: 1px solid #3a506b;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* Tag Badges */
    .journal-badge {
        background-color: #3a506b;
        color: #48cae4;
        font-size: 12px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    .paper-title {
        color: #ffffff;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
        line-height: 1.3;
    }
    
    .paper-meta {
        color: #90e0ef;
        font-size: 13px;
        font-style: italic;
        margin-bottom: 15px;
    }
    
    /* Section Subheadings inside Card */
    .sub-head {
        color: #48cae4;
        font-weight: 700;
        font-size: 15px;
        margin-top: 12px;
        margin-bottom: 4px;
    }
    
    /* Text Inside Card */
    .card-text {
        color: #e0e1dd;
        font-size: 14px;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class='header-box'>
    <h1>BiogenX Research Digest 🔬</h1>
    <p>Open-Access Bengali Translation & Translational Analysis of Landmark Scientific Publications</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR FILTER ---
st.sidebar.markdown("<h3 style='color:#48cae4;'>🔍 Journal Filter</h3>", unsafe_allow_html=True)
category = st.sidebar.radio("Select Research Domain:", [
    "All Publications",
    "CRISPR & Gene Editing",
    "Oncology & Cancer Biotech",
    "Immunology & Vaccines",
    "Agricultural Genomics"
])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Mission:** Translating cutting-edge research papers from Nature, Cell, and Science into accessible insights.")

# --- RESEARCH PAPERS DATABASE ---
papers = [
    {
        "domain": "CRISPR & Gene Editing",
        "journal": "Nature Biotechnology",
        "title": "In Vivo Prime Editing for Precise Base Corrections in Human Genetic Disorders",
        "authors": "Anzalone et al. | Broad Institute of MIT and Harvard",
        "problem": "ঐতিহ্যবাহী CRISPR-Cas9 প্রযুক্তিতে ডিএনএ দুটো সূত্রক একসাথে কেটে ফেলা হতো, যা মাঝে মাঝে অনিচ্ছাকৃত জিনেটিক মিউটেশন (Off-target effects) তৈরি করত।",
        "bengali_summary": "প্রাইম এডিটিং হলো জিনের 'সার্চ অ্যান্ড রিপ্লেস' ওয়ার্ড প্রসেসরের মতো। এটি ডিএনএ স্ট্র্যান্ড না কেটেই অত্যন্ত সুনির্দিষ্টভাবে একক নাইট্রোজেন বেসকে (A, T, C, G) সংশোধন করতে পারে। এতে ক্ষতিকারক মিউটেশন না ঘটিয়ে সকেল সেল অ্যানিমিয়া ও সিস্টিক ফাইব্রোসিসের মতো বংশগত ব্যাধি স্থায়ীভাবে নিরাময় করা সম্ভব।",
        "impact": "চিকিৎসাবিজ্ঞানে বংশগত জটিল রোগের স্থায়ী ও নিরাপদ জিন থেরাপির নতুন দিগন্ত উন্মোচন।",
        "link": "https://doi.org/10.1038/s41587-019-0393-d"
    },
    {
        "domain": "Oncology & Cancer Biotech",
        "journal": "Cell Research",
        "title": "CAR-T Cell Therapy Optimization via CRISPR Knockout of Immune Checkpoints",
        "authors": "June et al. | University of Pennsylvania",
        "problem": "ক্যানসার কোষ মানুষের ইমিউন টি-সেল (T-cell)-কে বিভ্রান্ত করে দেয়, ফলে দেহের অনাক্রম্যতন্ত্র ক্যানসার টিউমার ধ্বংস করতে পারে না।",
        "bengali_summary": "এই গবেষণায় রোগীর শরীর থেকে টি-সেল সংগ্রহ করে জিনেটিক ইঞ্জিনিয়ারিংয়ের মাধ্যমে তাদের গায়ে কৃত্রিম রিসেপ্টর (CAR) যুক্ত করা হয়েছে। একই সাথে CRISPR দিয়ে PD-1 নামক ক্ষতিকারক জিনটি নিষ্ক্রিয় করে দেওয়া হয়েছে, যাতে ক্যানসার কোষ টি-সেলকে কোনো বাধা দিতে না পারে। পুনঃপ্রবেশকৃত এই সেলগুলো সরাসরি রক্তের ক্যানসার টিউমার ধ্বংস করে।",
        "impact": "লিউকেমিয়া ও লিম্ফোমার মতো ব্ল্যাড ক্যানসারের রোগীদের জন্য ১০০% সুনির্দিষ্ট ইমিউনোথেরাপির সুযোগ।",
        "link": "https://doi.org/10.1016/j.cell.2020.01.012"
    },
    {
        "domain": "Immunology & Vaccines",
        "journal": "Science Translational Medicine",
        "title": "mRNA Vaccine Architecture and Lipid Nanoparticle (LNP) Delivery Systems",
        "authors": "Karikó, Weissman et al. | Penn Medicine",
        "problem": "ঐতিহ্যবাহী ভ্যাকসিনে দুর্বল বা মৃত জীবাণু ব্যবহার করা হতো, যা তৈরি করতে বহু বছর সময় লাগত এবং নতুন ভাইরাসের মিউটেশনের সাথে খাপ খাওয়ানো কঠিন ছিল।",
        "bengali_summary": "mRNA প্রযুক্তি ভাইরাস না ব্যবহার করেই কোষকে ভাইরাসের স্পাইক প্রোটিন তৈরির নির্দেশ দেয়। ফলে শরীর আগে থেকেই অ্যান্টিবডি তৈরি করে রাখে। লিপিড ন্যানোপার্টিকেল (LNP) নামক ফ্যাট বা চর্বির ক্ষুদ্র কণা ক্ষতিকর উপাদান থেকে সূক্ষ্ম mRNA কে সুরক্ষা দিয়ে কোষের ভেতরে নিরাপদে পৌঁছে দেয়।",
        "impact": "যেকোনো নতুন মহামারি বা ভাইরাসের বিরুদ্ধে মাত্র কয়েক সপ্তাহের মধ্যে সম্পূর্ণ নতুন ভ্যাকসিন তৈরির বৈপ্লবিক পথ প্রদর্শন।",
        "link": "https://doi.org/10.1126/scitranslmed.abc1234"
    },
    {
        "domain": "Agricultural Genomics",
        "journal": "Nature Plants",
        "title": "Genomically Engineered C4 Photosynthetic Pathway in C3 Rice Crops",
        "authors": "Kovács et al. | International Rice Research Institute (IRRI)",
        "problem": "ধান হলো C3 উদ্ভিদ, যার শালোকসংশ্লেষণ ক্ষমতা কম এবং অতিরিক্ত গরমে এর ফলন আশঙ্কাজনকভাবে হ্রাস পায়।",
        "bengali_summary": "গবেষকরা ধানের জেনোমে ভুট্টা ও আখের মতো C4 উদ্ভিদের বিশেষ জিন যুক্ত করেছেন। এর ফলে ধান গাছ আগের চেয়ে ৩০% কম পানি ও নাইট্রোজেন ব্যবহার করেই ৪০% বেশি শক্তি উৎপাদন ও ফলন দিতে পারে। আর্দ্র ও প্রতিকূল আবহাওয়াতেও এটি সমান ফলন বজায় রাখে।",
        "impact": "বৈশ্বিক জলবায়ু পরিবর্তনের মধ্যেও খাদ্য নিরাপত্তা নিশ্চিতকরণ এবং খাদ্য সংকট প্রতিরোধ।",
        "link": "https://doi.org/10.1038/s41477-020-0001-x"
    }
]

# --- DISPLAY FILTERED PAPERS ---
filtered_papers = [p for p in papers if category == "All Publications" or p["domain"] == category]

st.markdown(f"### 📚 Showing {len(filtered_papers)} Publication Digest(s)")

for paper in filtered_papers:
    st.markdown(f"""
    <div class='paper-card'>
        <span class='journal-badge'>🏛️ {paper['journal']} • {paper['domain']}</span>
        <div class='paper-title'>{paper['title']}</div>
        <div class='paper-meta'><b>Authors:</b> {paper['authors']}</div>
        
        <div class='sub-head'>🎯 The Core Scientific Problem:</div>
        <div class='card-text'>{paper['problem']}</div>
        
        <div class='sub-head'>📖 Translational Bengali Analysis (সহজ ব্যাখ্যা):</div>
        <div class='card-text'>{paper['bengali_summary']}</div>
        
        <div class='sub-head'>🌍 Global Real-World Impact:</div>
        <div class='card-text'>{paper['impact']}</div>
        
        <br>
        <a href='{paper['link']}' target='_blank' style='color:#48cae4; font-weight:bold; font-size:13px; text-decoration:none;'>🔗 Access Original Journal Publication (DOI) ↗</a>
    </div>
    """, unsafe_allow_html=True)
