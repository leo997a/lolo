import streamlit as st
import requests

st.title("نسبة انتقال اللاعب 🔁")

player_name_ar = st.text_input("اكتب اسم اللاعب بالعربي:")
club_name_ar = st.text_input("اكتب اسم النادي الذي تريد معرفة نسبة انتقال اللاعب إليه:")

if st.button("جلب النسبة"):
    if player_name_ar and club_name_ar:
        with st.spinner("جارٍ البحث..."):
            response = requests.post(
                "https://n8n.yourserver.com/webhook/transfer-check",  # غيره لمسار Webhook الخاص بك
                json={
                    "player": player_name_ar,
                    "club": club_name_ar
                }
            )
            if response.ok:
                data = response.json()
                st.success(f"النسبة: {data.get('percentage', 'غير متوفرة')}")
                st.write("البيانات الكاملة:", data)
            else:
                st.error("حدث خطأ أثناء جلب البيانات")
