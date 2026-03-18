import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Junsong Chen - Personal Profile",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.image("Chen junsong.jpg", width=120)  # 替换为你的本地照片
    st.markdown("## Junsong Chen")

    st.markdown("### Education")
    st.markdown("""
    - Bachelor (2021): Panzhihua University, Electronic Information Engineering  
    - Master (2024): Central South University of Forestry and Technology, School of Computer and Information Engineering
    - Ph.D. (2025–Present): National University of Defense Technology, School of Computer Science
    """)

    st.markdown("### Research Interests")
    st.markdown("""
    - Incomplete Multimodal Sentiment Analysis
    - High-Resolution Remote Sensing Image Classification  
    - Semantic Segmentation
    """)

    st.markdown("### Contact")
    st.markdown("[📧 chenjunsong257@163.com](mailto:chenjunsong257@163.com)")

    st.markdown("### Social Links")
    st.markdown("[GitHub ★](https://github.com/js257)")  # 替换为你的 GitHub

# ---------------- Main Content ----------------
st.header("News")
news = [
     {"date": "2025.11", "content": "One paper has been accepted by AAAI (CCF Rank A)"},
    {"date": "2023.11", "content": "One paper has been accepted by TGRS (CCF Rank B)"},
    {"date": "2023.04", "content": "One paper has been accepted by TGRS (CCF Rank B)"}
]

for item in news:
    st.markdown(f"- [{item['date']}] {item['content']}")

st.header("Awards")
awards = [
    {"date": "2025.11", "content": "Outstanding Master's Thesis of Hunan Artificial Intelligence Society."},
    {"date": "2024.5", "content": "Outstanding Graduate of Hunan Province."},
    {"date": "2023.11", "content": "Awarded the National Scholarship."},
    {"date": "2023.03", "content": "Rated as an Excellent Graduate Student."},
    {"date": "2018.11", "content": "Awarded the National Inspirational Scholarship."}
]

for item in awards:
    st.markdown(f"- [{item['date']}] {item['content']}")

st.header("Selected Publications")
st.markdown("(*: corresponding author, [C]: Conference, [J]: Journal.)")

publications = [
           { "year": "2025", 
            "entries": [ 
                { "info": "[C] **Junsong Chen**, Jiyuan Liu*, Suyuan Liu, Wei Zhang, Ao Li*, En Zhu*, Xinwang Liu. Sample-specific Modality Diagnosis and Cross-modal Enhancement for Incomplete Multimodal Representations.", 
                   "Conference": "Proceedings of the 40th AAAI Conference on Artificial Intelligence (AAAI-26).", 
                   "details": "(CCF Rank A, Accepted Nov 2025)", 
                   "paper_url": "", "code_url": "" } 
                ] 
           },
        {
        "year": "2023",
        "entries": [
            {
                "info": "[J] **Junsong Chen**, Jizheng Yi*, Aibin Chen, Hui Lin. SRCBTFusion-Net: An efficient Fusion Architecture via Stacked Residual Convolution Blocks and Transformer for Remote Sensing Image Semantic Segmentation.",
                "journal": "IEEE Transactions on Geoscience and Remote Sensing (TGRS).",
                "details": "(CCF Rank B, IF=8.2, Accepted Nov 2023)",
                "paper_url": "https://ieeexplore.ieee.org/document/10328787",
                "code_url": "https://github.com/js257/SRCBTFusion-Net"
            },
            {
                "info": "[J] **Junsong Chen**, Jizheng Yi*, Aibin Chen, Ke Yang, Ze Jin. SMFE‑Net: a saliency multi‑feature extraction framework for VHR remote sensing image classification.",
                "journal": "Multimedia Tools and Applications.",
                "details": "(CCF Rank C, IF=3.6, Accepted May 2023)",
                "paper_url": "https://link.springer.com/article/10.1007/s11042-023-15759-2",
                "code_url": None
            },
            {
                "info": "[J] **Junsong Chen**, Jizheng Yi*, Aibin Chen, Ze Jin. EFCOMFF-Net: A Multiscale Feature Fusion Architecture With Enhanced Feature Correlation for Remote Sensing Image Scene Classification.",
                "journal": "IEEE Transactions on Geoscience and Remote Sensing (TGRS).",
                "details": "(CCF Rank B, IF=8.2, Accepted Mar 2023)",
                "paper_url": "https://ieeexplore.ieee.org/abstract/document/10065518",
                "code_url": None
            }
        ]
    },
    {
        "year": "2022",
        "entries": [
            {
                "info": "[J] Jizheng Yi*, **Junsong Chen**, Mengna Zhou, Chao Hou, Aibin Chen, Guoxiong Zhou. Analysis of stock market public opinion based on web crawler and deep learning technologies including 1DCNN and LSTM.",
                "journal": "Arabian Journal for Science and Engineering.",
                "details": "(IF=2.9, Accepted Oct 2022)",
                "paper_url": "https://link.springer.com/article/10.1007/s13369-022-07444-7",
                "code_url": None
            }
        ]
    }
]

# ---------------- Display Publications with blue clickable links ----------------
for pub_year in publications:
    st.subheader(pub_year["year"])
    
    for idx, entry in enumerate(pub_year["entries"], 1):
        # 统一期刊/会议字段
        venue = entry.get("journal") or entry.get("Conference") or ""
        
        # 获取链接
        paper_url = entry.get("paper_url")
        code_url = entry.get("code_url")
        
        # 构建蓝色链接
        paper_link = f"<a href='{paper_url}' target='_blank' style='color:blue'>[Paper]</a>" if paper_url else ""
        code_link = f"<a href='{code_url}' target='_blank' style='color:blue'>[Code]</a>" if code_url else ""
        
        # 显示
        st.markdown(
            f"{idx}. {entry.get('info','')}  {venue}  {entry.get('details','')} {paper_link} &nbsp; {code_link}",
            unsafe_allow_html=True
        )
