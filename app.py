import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="BioLab Hub | Biotech & Drug Research Suite",
    page_icon="🧪",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button {
        background: linear-gradient(135deg, #2ea043, #238636);
        color: white; border: None; border-radius: 8px;
        padding: 0.6rem 1.2rem; font-weight: bold; width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #3fb950, #2ea043);
        box-shadow: 0 4px 12px rgba(46, 160, 67, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🧪 BioLab All-in-One Research Hub")
st.caption("Genomics, Molecular Drug Design, Sequence Alignment & Lab Calculators")
st.markdown("---")

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧬 Genomics & Protein", 
    "💊 3D Drug & Chemical Viewer", 
    "🔗 Gene Similarity Matcher", 
    "🧪 Biotech Lab Calculators", 
    "📖 Science Wiki"
])

# --- TAB 1: GENOMICS ---
with tab1:
    st.subheader("🧬 DNA to Protein Sequence Analyzer")
    dna_input = st.text_area("Enter DNA Sequence:", "ATGCGATATGACTGATCATAGATGC").upper().replace(" ", "")
    
    if st.button("🚀 Analyze Genome"):
        if any(c not in "ATGC" for c in dna_input):
            st.error("Invalid DNA! Only A, T, C, G bases allowed.")
        elif dna_input:
            rna = dna_input.replace('T', 'U')
            gc = round(((dna_input.count('G') + dna_input.count('C')) / len(dna_input)) * 100, 2)
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Sequence Length", f"{len(dna_input)} bp")
            c2.metric("GC Content Ratio", f"{gc}%")
            c3.metric("RNA Transcribed", f"{len(rna)} bases")
            
            st.code(f"RNA: {rna}")
            
            # Nucleotide Chart
            counts = {b: dna_input.count(b) for b in "ATGC"}
            fig = px.pie(values=list(counts.values()), names=list(counts.keys()), hole=0.4, title="Base Distribution")
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: 3D DRUG & MOLECULE VIEWER ---
with tab2:
    st.subheader("💊 Interactive 3D Drug & Molecule Explorer")
    st.caption("Inspect 3D structures of medicines, viruses, and DNA.")
    
    col_a, col_b = st.columns([1, 3])
    with col_a:
        mol_type = st.radio("Choose Input Type:", ["Preset Drugs", "Custom PDB ID"])
        if mol_type == "Preset Drugs":
            drug = st.selectbox("Select Compound:", ["Paracetamol (1C8U)", "Insulin (4INS)", "DNA Helix (1BNA)", "Hemoglobin (1A3N)"])
            pdb_id = drug.split("(")[-1].replace(")", "").lower()
        else:
            pdb_id = st.text_input("Enter 4-letter PDB Code:", "1bna").lower()
            
    with col_b:
        html_code = f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div id="container" style="width: 100%; height: 450px; position: relative; border-radius: 10px; border: 1px solid #30363d;"></div>
        <script>
            let element = document.getElementById('container');
            let viewer = $3Dmol.createViewer( element, {{ backgroundColor: '#161b22' }} );
            $3Dmol.download("pdb:{pdb_id}", viewer, {{}}, function() {{
                viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}, stick: {{}}}});
                viewer.zoomTo();
                viewer.render();
            }});
        </script>
        """
        components.html(html_code, height=470)

# --- TAB 3: GENE ALIGNMENT ---
with tab3:
    st.subheader("🔗 DNA Sequence Similarity Matcher")
    st.caption("Compare two gene sequences to calculate percentage similarity (e.g., Species Comparison).")
    
    seq1 = st.text_input("Sequence 1 (e.g. Human Gene):", "ATGCGATCGATCG").upper()
    seq2 = st.text_input("Sequence 2 (e.g. Chimpanzee Gene):", "ATGCGATCCATCG").upper()
    
    if st.button("🔍 Compare Sequences"):
        min_len = min(len(seq1), len(seq2))
        matches = sum(1 for i in range(min_len) if seq1[i] == seq2[i])
        similarity = round((matches / max(len(seq1), len(seq2))) * 100, 2) if seq1 else 0
        
        st.success(f"Genetic Match Similarity: **{similarity}%**")
        st.progress(similarity / 100)

# --- TAB 4: LAB CALCULATORS ---
with tab4:
    st.subheader("🧪 Virtual Biotech Lab Calculators")
    
    calc_type = st.selectbox("Select Calculator:", ["Solution Dilution (C1V1 = C2V2)", "Molarity Calculator"])
    
    if calc_type == "Solution Dilution (C1V1 = C2V2)":
        st.markdown("#### Solution Dilution Calculator")
        c1 = st.number_input("Initial Concentration (C1):", value=10.0)
        v1 = st.number_input("Initial Volume Needed (V1):", value=0.0)
        c2 = st.number_input("Target Concentration (C2):", value=2.0)
        v2 = st.number_input("Target Total Volume (V2):", value=500.0)
        
        if v1 == 0 and c1 > 0:
            req_v1 = (c2 * v2) / c1
            st.info(f"💡 You need **{req_v1:.2f} mL** of Stock Solution (V1).")
            
    elif calc_type == "Molarity Calculator":
        st.markdown("#### Molarity Calculator (M = mol / L)")
        moles = st.number_input("Solute Amount (Moles):", value=0.5)
        liters = st.number_input("Volume (Liters):", value=1.0)
        if liters > 0:
            molarity = moles / liters
            st.info(f"💡 Molarity = **{molarity:.3f} M (Mol/L)**")

# --- TAB 5: WIKI ---
with tab5:
    st.subheader("📖 Quick Biotech Reference")
    st.write("• **Genomics:** Study of entire genomes including sequence and mutation analysis.")
    st.write("• **Drug Design:** Using 3D molecular structures to fit chemicals into human proteins.")
    st.write("• **Sequence Alignment:** Finding evolutionary links between different organisms.")
