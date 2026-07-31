import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="3D Bio-Visualizer", page_icon="🧬", layout="wide")

st.title("🧬 Advanced 3D DNA, RNA & Protein Interactive Visualizer")
st.write("Analyze biological sequences and interact with real 3D Protein & DNA structures!")

# --- SIDEBAR ---
st.sidebar.header("1. Sequence Analysis")
dna_seq = st.sidebar.text_area("Enter DNA Sequence:", "ATGCGATATGACTGATCATAG").upper()
dna_seq = "".join(dna_seq.split())

st.sidebar.header("2. 3D Structure Viewer")
pdb_code = st.sidebar.text_input("Enter PDB ID for 3D Animation:", "1BNA").strip().lower()
st.sidebar.caption("Try examples: **1bna** (DNA Double Helix), **1cag** (Collagen), **4ins** (Insulin)")

# --- TAB SETUP ---
tab1, tab2, tab3 = st.tabs(["📊 Sequence Converter", "🧊 3D Molecular Animation", "📖 Biotech Terms Simplified"])

# TAB 1: CONVERTER
with tab1:
    if st.button("Run Sequence Analysis"):
        invalid = [c for c in dna_seq if c not in "ATGC"]
        if invalid:
            st.error("Invalid DNA sequence! Only A, T, C, G allowed.")
        elif not dna_seq:
            st.warning("Please enter sequence.")
        else:
            with st.spinner("Analyzing..."):
                time.sleep(0.5)
            
            rna_seq = dna_seq.replace('T', 'U')
            
            codon_table = {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
                'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
            }

            protein_seq = ""
            for i in range(0, len(dna_seq), 3):
                codon = dna_seq[i:i+3]
                if len(codon) == 3:
                    aa = codon_table.get(codon, 'X')
                    if aa == '_': break
                    protein_seq += aa

            st.success("Analysis Complete!")
            st.subheader("Results:")
            st.code(f"DNA:     {dna_seq}")
            st.code(f"RNA:     {rna_seq}")
            st.code(f"Protein: {protein_seq}")
            
            counts = {n: dna_seq.count(n) for n in "ATGC"}
            st.bar_chart(counts)

# TAB 2: 3D ANIMATION (Pure HTML/JS Embed - Error Free)
with tab2:
    st.subheader("🧊 Interactive 3D Molecular Structure View")
    st.info("You can spin, drag, and zoom in/out of the 3D model below using your touch screen or mouse!")
    
    if pdb_code:
        html_code = f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div id="container" style="width: 100%; height: 500px; position: relative; border: 1px solid #ccc; border-radius: 8px;"></div>
        <script>
            let element = document.getElementById('container');
            let config = {{ backgroundColor: 'white' }};
            let viewer = $3Dmol.createViewer( element, config );
            $3Dmol.download("pdb:{pdb_code}", viewer, {{}}, function() {{
                viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
                viewer.zoomTo();
                viewer.render();
            }});
        </script>
        """
        components.html(html_code, height=520)

# TAB 3: BIOTECH TERMS
with tab3:
    st.header("🔬 Biotech & Bioinformatics Concepts")
    with st.expander("🧬 DNA (Deoxyribonucleic Acid)"):
        st.write("জীবদেহের মূল ব্লু-প্রিন্ট যা A, T, C, G নামক নিউক্লিওটাইড দিয়ে গঠিত।")
    with st.expander("🧪 RNA (Ribonucleic Acid)"):
        st.write("DNA থেকে সংকেত বহন করে প্রোটিন তৈরির মেসেঞ্জার হিসেবে কাজ করে।")
    with st.expander("🍔 Protein & Amino Acids"):
        st.write("শরীরের পেশি, এনজাইম এবং অন্যান্য অঙ্গ তৈরীর মূল কারিগর।")
    with st.expander("🧊 PDB (Protein Data Bank) ID"):
        st.write("বিশ্বব্যাপী বায়োইনফর্মেটিক্স গবেষণাগারে আবিষ্কৃত ৩D মলিকিউলের অনন্য কোড (যেমন DNA 3D Structure = 1bna)।")
