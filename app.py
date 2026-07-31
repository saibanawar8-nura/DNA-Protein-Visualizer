import streamlit as st

# পেজের শিরোনাম ও সেটিংস
st.set_page_config(page_title="Biotech DNA Visualizer", page_icon="🧬")

st.title("🧬 DNA to RNA & Protein Converter")
st.write("Welcome! Enter a DNA sequence below to convert it into RNA and Protein amino acids.")

# ইউজার ইনপুট বক্স
dna_input = st.text_input("Enter DNA Sequence (A, T, C, G):", "ATGCGATAT").upper()

# প্রসেসিং বাটন
if st.button("Convert Sequence"):
    # শুধুমাত্র সঠিক DNA লেটার আছে কিনা তা চেক করা
    valid_dna = set("ATCG")
    if set(dna_input).issubset(valid_dna) and len(dna_input) > 0:
        # ১. DNA to RNA (T পরিবর্তন হয়ে U হবে)
        rna_sequence = dna_input.replace('T', 'U')
        
        st.success("Conversion Successful!")
        st.subheader("1. RNA Sequence:")
        st.code(rna_sequence)
        
        # ২. RNA to Protein Amino Acids (কোডন টেবিল)
        codon_table = {
            'AUG': 'Methionine (Start)', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
            'UUA': 'Leucine', 'UUG': 'Leucine', 'GCU': 'Alanine', 'GCC': 'Alanine',
            'GCA': 'Alanine', 'GCG': 'Alanine', 'GAU': 'Aspartate', 'GAC': 'Aspartate',
            'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
        }
        
        # ৩টি করে লেটার (Codon) আলাদা করা
        codons = [rna_sequence[i:i+3] for i in range(0, len(rna_sequence)-2, 3)]
        amino_acids = [codon_table.get(codon, "Unknown") for codon in codons]
        
        st.subheader("2. Protein Sequence (Amino Acids):")
        st.write(" ➔ ".join(amino_acids))
        
    else:
        st.error("Please enter a valid DNA sequence containing only A, T, C, and G.")
