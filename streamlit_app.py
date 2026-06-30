import streamlit as st

st.title("📚 डिजिटल पाठशाला (Study App)")
st.write("चलो भाई, आज कुछ नया सीखते हैं!")

subject = st.selectbox("अपना सब्जेक्ट चुनें:", ["सामान्य ज्ञान (GK)", "विज्ञान (Science)", "गणित (Maths)"])

st.subheader(f"📝 {subject} का टेस्ट")

if subject == "सामान्य ज्ञान (GK)":
    q1 = st.radio("भारत की राजधानी क्या है?", ["मुंबई", "दिल्ली", "कोलकाता", "चेन्नई"])
    if st.button("उत्तर चेक करें 🎯"):
        if q1 == "दिल्ली":
            st.success("बिल्कुल सही जवाब भाई! 🎉")
        else:
            st.error("गलत जवाब, फिर से कोशिश करो।")

elif subject == "विज्ञान (Science)":
    q2 = st.radio("पानी का रासायनिक सूत्र (Formula) क्या है?", ["CO2", "H2O", "O2"])
    if st.button("उत्तर चेक करें 🎯"):
        if q2 == "H2O":
            st.success("अरे वाह! सही उत्तर है। 🧪")
        else:
            st.error("गलत जवाब भाई।")

elif subject == "गणित (Maths)":
    q3 = st.radio("5 + 7 कितना होता है?", ["10", "12", "15"])
    if st.button("उत्तर चेक करें 🎯"):
        if q3 == "12":
            st.success("जीनियस! सही जवाब। 🔢")
        else:
            st.error("जोड़ दोबारा चेक करो भाई।")
            
