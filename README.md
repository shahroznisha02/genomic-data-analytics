# Genomic Data Analytics & Mutation Visualizer

An interactive bioinformatics dashboard built with **Python, Streamlit, Pandas and Plotly**. It shows gene mutation profiles, calculates DNA sequence metrics and lets you upload FASTA files, all from the browser with no coding needed.

## Features

The app has 3 tabs:

**1. Mutation Analysis**
- Mutation frequency profile for **6 cancer-related genes**: TP53, BRCA1, EGFR, KRAS, PIK3CA and BRAF.
- Table with mutation rate, chromosome location and consequence class (missense, frameshift, nonsense, synonymous).
- Interactive Plotly bar chart of variant rates, coloured by consequence type.

**2. Sequence Analyzer**
- Paste any DNA sequence to get **total bases, GC-content (%), A/T count and G/C count** instantly.

**3. FASTA Upload**
- Upload a genomic file (`.fasta`, `.fa` or `.txt`) and preview its contents.

## Tech Stack

| Tool | Use |
|------|-----|
| Python | Core logic |
| Streamlit | Web app with tabs and metric cards |
| Pandas | Data tables |
| Plotly | Interactive charts |

## How to Run

```bash
git clone https://github.com/shahroznisha02/genomic-data-analytics.git
cd genomic-data-analytics
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Note

The mutation rates in the Mutation Analysis tab are sample values for demonstration. The Sequence Analyzer works on any real DNA sequence you enter.

## Why This Project

Raw genomic data is hard to read. This dashboard shows how simple data tools can help biologists quickly check sequence quality (GC-content) and compare mutation patterns across key cancer genes.

## Author

**Shahroz Nisha**, B.Sc. (Hons.) Biotechnology: [LinkedIn](https://linkedin.com/in/shahroz-nisha-093957432) · [Portfolio](https://shahroznisha02.github.io) · [GitHub](https://github.com/shahroznisha02)
