import streamlit as st
import html

st.set_page_config(
    page_title="roamie. | AI Travel Planner",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp { background: #F8FAFA; color: #244B62; }
.block-container { max-width: 850px; padding-top: 2rem; padding-bottom: 4rem; }
header[data-testid="stHeader"] { background: transparent; }

h1, h2, h3, p, label { color: #244B62; }
[data-testid="stWidgetLabel"] p {
    color: #244B62 !important;
    font-weight: 650;
}

.brand {
    font-size: 29px;
    font-weight: 900;
    letter-spacing: -1px;
    margin-bottom: 22px;
}
.brand span { color: #244B62; }

.hero {
    background: linear-gradient(120deg, #D8EAF0, #DDEFE9);
    border-radius: 26px;
    padding: 42px 36px;
    margin-bottom: 34px;
}
.eyebrow {
    color: #447F7D;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}
.hero-title {
    font-size: clamp(34px, 5vw, 52px);
    font-weight: 900;
    line-height: 1.2;
    color: #244B62;
    margin: 16px 0;
}
.hero-desc { color: #48636A; line-height: 1.9; }

.section-title {
    font-size: 26px;
    font-weight: 850;
    margin-bottom: 5px;
}
.section-desc {
    color: #71858A;
    font-size: 14px;
    margin-bottom: 20px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 1px solid #E4E6E0 !important;
    border-radius: 13px !important;
}
div[data-baseweb="input"] input {
    color: #244B62 !important;
    -webkit-text-fill-color: #244B62 !important;
}
div[data-baseweb="select"] * { color: #244B62; }

div[data-baseweb="tag"] {
    background: #D9EEEB !important;
}
div[data-baseweb="tag"] span {
    color: #285F63 !important;
}

div.stButton > button {
    background: #244B62 !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 55px;
    font-weight: 800;
    font-size: 17px;
}
div.stButton > button:hover {
    background: #326B80 !important;
    color: white !important;
}

.note {
    background: #E6F1F1;
    border-radius: 14px;
    padding: 18px;
    color: #315F64;
    line-height: 1.8;
    margin: 18px 0;
}
.result-card {
    background: #FFFFFF;
    border: 1px solid #EEE7DE;
    border-radius: 18px;
    padding: 24px;
    line-height: 2.3;
    color: #244B62;
}
.footer {
    text-align: center;
    color: #91A098;
    font-size: 12px;
    margin-top: 45px;
}

/* roamie. Ocean Blue Theme */
.stApp {
    color-scheme: light !important;
}
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background-color: #FFFFFF !important;
    color: #244B62 !important;
    -webkit-text-fill-color: #244B62 !important;
}
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stMultiSelect"] [data-baseweb="select"] > div,
[data-testid="stNumberInput"] [data-baseweb="input"] > div,
[data-testid="stTextInput"] [data-baseweb="input"] > div {
    background-color: #FFFFFF !important;
    color: #244B62 !important;
    border-color: #D5E3E6 !important;
}
[data-testid="stSelectbox"] [data-baseweb="select"] span,
[data-testid="stMultiSelect"] [data-baseweb="select"] span {
    color: #244B62 !important;
}
[data-testid="stWidgetLabel"] p {
    color: #244B62 !important;
}


/* ===== roamie. UI 統一修正版 ===== */

/* Streamlit 整體使用淺色介面 */
.stApp {
    color-scheme: light !important;
}

/* 所有輸入欄位 */
div[data-baseweb="input"],
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border-color: #C9DADD !important;
    color: #244B62 !important;
}

/* 輸入欄位文字 */
div[data-baseweb="input"] input,
div[data-baseweb="select"] input,
div[data-baseweb="select"] span {
    color: #244B62 !important;
    -webkit-text-fill-color: #244B62 !important;
}

/* 下拉選單內的文字與箭頭 */
[data-testid="stSelectbox"] svg,
[data-testid="stMultiSelect"] svg {
    fill: #244B62 !important;
    color: #244B62 !important;
}

/* 興趣選擇標籤 */
[data-baseweb="tag"],
[data-baseweb="tag"][aria-label] {
    background-color: #D9EEEB !important;
    border-radius: 8px !important;
}

[data-baseweb="tag"] span,
[data-baseweb="tag"] svg {
    color: #285F63 !important;
    fill: #285F63 !important;
}

/* 數字輸入的加減按鈕 */
[data-testid="stNumberInput"] button {
    background: #EDF5F5 !important;
    color: #244B62 !important;
    border-color: #C9DADD !important;
}

[data-testid="stNumberInput"] button svg {
    color: #244B62 !important;
    stroke: #244B62 !important;
}

/* 主要按鈕：強制文字永遠顯示白色 */
[data-testid="stButton"] button[kind="primary"],
[data-testid="stButton"] button[kind="secondary"],
div.stButton > button {
    background: #244B62 !important;
    border: 1px solid #244B62 !important;
    color: #FFFFFF !important;
    opacity: 1 !important;
}

/* 修正 Streamlit 按鈕內文字被其他 CSS 覆蓋 */
[data-testid="stButton"] button *,
div.stButton > button *,
[data-testid="stButton"] button p {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    opacity: 1 !important;
}

/* 滑鼠移過去的效果 */
[data-testid="stButton"] button:hover {
    background: #326B80 !important;
    border-color: #326B80 !important;
}

/* 聚焦時的外框 */
input:focus {
    outline-color: #5E9D9A !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="brand">✈️ roamie<span>.</span></div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
    <div class="eyebrow">EXPLORE MORE. PLAN LESS.</div>
    <div class="hero-title">想出去玩？<br>剩下的交給 AI！</div>
    <div class="hero-desc">
        從社群熱門景點到順路行程與旅費規劃。<br>
        你的下一趟旅行，從這裡開始。
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">🌍 你的下一站是哪裡？</div>
<div class="section-desc">告訴我們你的喜好，打造專屬旅行提案。</div>
""", unsafe_allow_html=True)

destination = st.text_input(
    "📍 想去哪裡？",
    value="嘉義、台南"
)

c1, c2 = st.columns(2)

with c1:
    days = st.selectbox(
        "🗓️ 旅遊天數",
        ["1天", "2天1夜", "3天2夜", "4天3夜", "5天4夜"],
        index=1
    )

with c2:
    people = st.number_input(
        "👥 旅遊人數",
        min_value=1,
        max_value=30,
        value=2
    )

c3, c4 = st.columns(2)

with c3:
    budget = st.number_input(
        "💰 整團總預算（NT$）",
        min_value=0,
        value=10000,
        step=1000
    )

with c4:
    transport = st.selectbox(
        "🚗 交通方式",
        ["自駕", "租車", "包車", "訂車", "大眾運輸"]
    )

interests = st.multiselect(
    "✨ 這次想體驗什麼？",
    ["美食", "咖啡廳", "自然風景", "拍照打卡",
     "文化古蹟", "購物", "親子", "夜生活",
     "藝術展覽", "戶外活動"],
    default=["美食", "咖啡廳"]
)

st.markdown("""
<div class="note">
    💡 <b>聰明預算規劃</b><br>
    AI 將先安排合理完整的旅程，再依整團預算調整住宿、
    餐飲與景點，盡量保留你最想去的地方。
</div>
""", unsafe_allow_html=True)

if st.button("✨ 開始我的 AI 旅行", use_container_width=True):
    if not destination.strip():
        st.warning("請輸入旅遊目的地。")
    elif not interests:
        st.warning("請至少選擇一個興趣。")
    else:
        st.success("已成功取得你的旅遊需求！")

        safe_destination = html.escape(destination)
        safe_days = html.escape(days)
        safe_transport = html.escape(transport)
        safe_interests = html.escape("、".join(interests))

        st.subheader("✈️ 你的旅行設定")
        st.markdown(f"""
        <div class="result-card">
            📍 <b>目的地：</b>{safe_destination}<br>
            🗓️ <b>天數：</b>{safe_days}<br>
            👥 <b>人數：</b>{people} 人<br>
            💰 <b>整團總預算：</b>NT${budget:,}<br>
            🚗 <b>交通方式：</b>{safe_transport}<br>
            ✨ <b>興趣：</b>{safe_interests}
        </div>
        """, unsafe_allow_html=True)

        st.info("目前是前端展示版，下一階段將串接 AI 行程生成。")

st.markdown("""
<div class="footer">
    roamie. · Your AI Travel Buddy<br>
    Made for curious travelers ✨
</div>
""", unsafe_allow_html=True)
