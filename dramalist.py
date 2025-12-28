import streamlit as st
import joblib

st.set_page_config(
    page_title="Rekomendasi Drama Korea",
    page_icon="🎬",
    layout="centered"
)

st.markdown("""
<style>
.main { background-color: #0e1117; }
h1, h2, h3 { text-align: center; color: #ffffff; }
.subtitle { text-align: center; color: #c7c7c7; font-size: 16px; }
.recommend-box {
    background-color: #1f2933;
    padding: 15px;
    border-radius: 14px;
    margin: 10px 0;
    font-size: 18px;
    color: #ffffff;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
}
.footer {
    text-align: center;
    font-size: 14px;
    color: #aaaaaa;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


data = joblib.load("data.pkl")       
cosine_sim = joblib.load("cosine_sim.pkl")


def recommend(title, n=10):
    if title not in data["Title"].values:
        return []

    idx = data[data["Title"] == title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top = scores[1:n+1]
    return [data.iloc[i[0]]["Title"] for i in top]

st.title("🎬 Sistem Rekomendasi Drama Korea")
st.markdown(
    "<div class='subtitle'>Temukan drama Korea serupa berdasarkan cerita & deskripsi 💕</div>",
    unsafe_allow_html=True
)

selected_title = st.selectbox(
    "📺 Pilih Drama Korea Favoritmu:",
    data["Title"].values
)

if st.button("✨ Rekomendasikan"):
    st.subheader("🍿 Drama yang Mungkin Kamu Suka")
    results = recommend(selected_title)

    for i, r in enumerate(results, start=1):
        st.markdown(
            f"<div class='recommend-box'>💜 <b>{i}. {r}</b></div>",
            unsafe_allow_html=True
        )

st.markdown(
    "<div class='footer'>💻 Dibuat dengan Streamlit | Sistem Rekomendasi K-Drama 🎥</div>",
    unsafe_allow_html=True
)
