import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Genomic Data Analytics Pro", layout="wide")

st.title("🧬 Genomic Data Analytics & Mutation Visualizer")
st.markdown("Automated sequence metrics and mutation frequency profiling for genomic datasets.")

# Tabbed Layout
tab1, tab2, tab3 = st.tabs(["📊 Mutation Analysis", "🧬 Sequence Analyzer", "📁 FASTA Upload"])

with tab1:
    st.subheader("Gene Mutation Frequency Profile")
    df = pd.DataFrame({
        'Gene Symbol': ['TP53', 'BRCA1', 'EGFR', 'KRAS', 'PIK3CA', 'BRAF'],
        'Mutation Rate (%)': [12.5, 8.3, 15.1, 9.7, 11.2, 14.0],
        'Chromosome Location': ['Chr17', 'Chr17', 'Chr7', 'Chr12', 'Chr3', 'Chr7'],
        'Consequence Class': ['Missense', 'Frameshift', 'Missense', 'Missense', 'Synonymous', 'Nonsense']
    })
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(df, use_container_width=True)
    with col2:
        fig = px.bar(df, x='Gene Symbol', y='Mutation Rate (%)', color='Consequence Class',
                     title="Gene Variant Rates by Consequence Type", text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Interactive DNA Base Composition")
    seq_input = st.text_area("Input DNA Sequence", "ATGCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG")
    if seq_input:
        clean_seq = seq_input.strip().upper()
        gc_count = clean_seq.count('G') + clean_seq.count('C')
        gc_pct = (gc_count / len(clean_seq)) * 100 if len(clean_seq) > 0 else 0
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Bases", len(clean_seq))
        c2.metric("GC Content", f"{gc_pct:.2f}%")
        c3.metric("A/T Count", clean_seq.count('A') + clean_seq.count('T'))
        c4.metric("G/C Count", gc_count)

with tab3:
    st.subheader("Upload FASTA Dataset")
    uploaded = st.file_uploader("Upload genomic FASTA file", type=['fasta', 'fa', 'txt'])
    if uploaded:
        content = uploaded.getvalue().decode("utf-8")
        st.success("File uploaded successfully!")
        st.code(content[:300] + "...", language="text")