import streamlit as st
import webbrowser

# 页面配置
st.set_page_config(
    page_title="陈俊松 (Junsong Chen) - 个人简介",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- 左侧栏 ----------------
with st.sidebar:
    st.image("Chen junsong.jpg", width=120)  # 本地头像
    st.markdown("## 陈俊松 (Junsong Chen)")

    st.markdown("### 教育背景")
    st.markdown("""
    - 学士 (2021): 攀枝花大学 电子信息工程专业  
    - 硕士 (在读): 中南林业科技大学 计算机与信息工程学院
    """)

    st.markdown("### 研究兴趣")
    st.markdown("""
    - 计算机视觉  
    - 高分辨率遥感图像分类  
    - 语义分割
    """)

    st.markdown("### 联系方式")
    st.markdown("[📧 chenjunsong257@163.com](mailto:chenjunsong257@163.com)")

    st.markdown("### 社交链接")
    st.markdown("[GitHub ★](https://github.com/username)")  # 替换为你的 GitHub

# ---------------- 右侧内容 ----------------
st.title("📄 Selected Publications")
st.markdown("(*: corresponding author, [C]: Conference, [J]: Journal.)")

publications = [
    {
        "year": "2023",
        "entries": [
            {
                "info": "[J] Junsong Chen, Jizheng Yi*, Aibin Chen, Hui Lin. SRCBTFusion-Net: An efficient Fusion Architecture via Stacked Residual Convolution Blocks and Transformer for Remote Sensing Image Semantic Segmentation.",
                "journal": "IEEE Transactions on Geoscience and Remote Sensing (TGRS).",
                "details": "(CCF Rank B, IF=8.2, Accepted in Nov. 2023)",
                "paper_url": "https://ieeexplore.ieee.org/document/XXXXXXX",  # 替换真实链接
                "code_url": "https://github.com/username/SRCBTFusion-Net"
            },
            {
                "info": "[J] Junsong Chen, Jizheng Yi*, Aibin Chen, Ke Yang, Ze Jin. SMFE‑Net: a saliency multi‑feature extraction framework for VHR remote sensing image classification.",
                "journal": "Multimedia Tools and Applications.",
                "details": "(CCF Rank C, IF=3.6, Accepted in May. 2023)",
                "paper_url": "https://link.springer.com/article/XXXXXXX",
                "code_url": None
            },
            {
                "info": "[J] Junsong Chen, Jizheng Yi*, Aibin Chen, Ze Jin. EFCOMFF-Net: A Multiscale Feature Fusion Architecture With Enhanced Feature Correlation for Remote Sensing Image Scene Classification.",
                "journal": "IEEE Transactions on Geoscience and Remote Sensing (TGRS).",
                "details": "(CCF Rank B, IF=8.2, Accepted in Mar. 2023)",
                "paper_url": "https://ieeexplore.ieee.org/document/YYYYYYY",
                "code_url": None
            }
        ]
    },
    {
        "year": "2022",
        "entries": [
            {
                "info": "[J] Jizheng Yi*, Junsong Chen, Mengna Zhou, Chao Hou, Aibin Chen, Guoxiong Zhou. Analysis of stock market public opinion based on web crawler and deep learning technologies including 1DCNN and LSTM.",
                "journal": "Arabian Journal for Science and Engineering.",
                "details": "(IF=2.9, Accepted in Oct. 2022)",
                "paper_url": "https://link.springer.com/article/ZZZZZZZ",
                "code_url": None
            }
        ]
    }
]

# 显示论文
for pub_year in publications:
    st.subheader(pub_year["year"])
    for idx, entry in enumerate(pub_year["entries"], 1):
        st.markdown(f"{idx}. {entry['info']}  {entry['journal']}  {entry['details']}")
        col1, col2 = st.columns([1, 1])
        if entry.get("paper_url"):
            with col1:
                if st.button(f"[paper]", key=f"paper_{pub_year['year']}_{idx}"):
                    webbrowser.open(entry['paper_url'])
        if entry.get("code_url"):
            with col2:
                if st.button(f"[Code]", key=f"code_{pub_year['year']}_{idx}"):
                    webbrowser.open(entry['code_url'])
