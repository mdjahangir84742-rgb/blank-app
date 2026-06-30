import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🤖 महा पाठशाला AI (All Books + AI Answer Bot)")
st.write("चलो भाई, अब कक्षा 8-12 की किताबें भी पढ़ें और एआई (AI) से अपने हर सवाल का जवाब भी पाएं!")

# मुख्य स्क्रीन को दो जादुई भागों में बांटना
tab1, tab2 = st.tabs(["🤖 AI से सवाल पूछें (Ask AI)", "📖 कक्षा 8-12 किताबें (All Books)"])

# ==================== टैब 1: AI जवाब देगा (जैसे ChatGPT देता है) ====================
with tab1:
    st.subheader("💬 आपके दिमाग में जो भी सवाल है, यहाँ एआई से पूछें:")
    user_question = st.text_input("अपना सवाल यहाँ लिखें (जैसे: प्रकाश संश्लेषण क्या है? या टीवी का आविष्कार किसने किया?):", placeholder="यहाँ टाइप करें भाई...")
    
    if st.button("एआई से जवाब पूछें ✨"):
        if user_question:
            with st.spinner("एआई सोच रहा है..."):
                try:
                    # बिना किसी सीक्रेट की (Key) के काम करने वाला एक फ्री एआई लिंक (Free AI API)
                    ai_url = f"https://text.pollinations.ai/{user_question}"
                    response = requests.get(ai_url)
                    
                    if response.status_code == 200:
                        st.success("🤖 एआई का जवाब:")
                        st.write(response.text)
                    else:
                        st.error("भाई, एआई अभी थोड़ा व्यस्त है, कृपया दोबारा बटन दबाएं।")
                except:
                    st.error("इंटरनेट कनेक्शन चेक करें भाई।")
        else:
            st.warning("पहले अपना सवाल ऊपर वाले बॉक्स में लिखें भाई!")

# ==================== टैब 2: कक्षा 8 से 12 तक की सभी किताबें ====================
with tab2:
    st.subheader("📚 कक्षा 8 से 12वीं तक की मुख्य किताबें")
    
    # स्टूडेंट को क्लास और सब्जेक्ट चुनने का पूरा मौका देना
    क्लास = st.selectbox("🎯 कक्षा चुनें:", ["कक्षा 8", "कक्षा 9", "कक्षा 10", "कक्षा 11", "कक्षा 12"])
    सब्जेक्ट = st.selectbox("📖 विषय चुनें:", ["विज्ञान (Science)", "गणित (Maths)", "इतिहास/जीके (History/GK)"])
    
    # डिफ़ॉल्ट बुक का लिंक
    किताब_url = "https://ncert.nic.in/textbook/pdf/jesc101.pdf" 
    
    # अलग-अलग क्लास के हिसाब से असली एनसीईआरटी किताबों को सेट करना
    if क्लास == "कक्षा 10" and सब्जेक्ट == "गणित (Maths)":
        किताब_url = "https://ncert.nic.in/textbook/pdf/jemh101.pdf"
    elif क्लास == "कक्षा 12":
        किताब_url = "https://ncert.nic.in/textbook/pdf/leph101.pdf" # फिजिक्स
    elif क्लास == "कक्षा 11":
        किताब_url = "https://ncert.nic.in/textbook/pdf/keph101.pdf"
    elif क्लास == "कक्षा 9":
        किताब_url = "https://ncert.nic.in/textbook/pdf/jesc101.pdf"
    elif क्लास == "कक्षा 8":
        किताब_url = "https://ncert.nic.in/textbook/pdf/hhsc101.pdf"

    st.write(f"👇 नीचे आपकी **{क्लास} - {सब्जेक्ट}** की पूरी किताब लोड हो गई है:")
    st.markdown(f'<iframe src="{किताब_url}" width="100%" height="800px" type="application/pdf"></iframe>', unsafe_allow_html=True)
    
