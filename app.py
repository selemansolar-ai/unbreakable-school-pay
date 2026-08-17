import streamlit as st
import pandas as pd
from datetime import datetime
import random
import datetime
from fpdf import FPDF
import io

st.set_page_config(page_title="UNBREAKABLE SCHOOL PAY", page_icon="🏫", layout="wide")

# DATABASE
if 'users' not in st.session_state:
	st.session_state.users = {
		'admin': {'password': 'admin123', 'type': 'Mkuu'}
	}
#----DATA YA DEMO----
if 'df' not in st.session_state:
	st.session_state.df = pd.DataFrame({
	  'namba': ['STD001', 'STD002', 'STD003'],
	  'jina': ['Juma Ali', 'Asha Mohamed' 'Peter John'],
	  'darasa': ['Darasa la 7A', 'Darasa la 3B', 'Darasa la 5C'],
	  'deni': [150000, 750000, 200000],
	  'namba_mzazi': [+255775049026, +255774792548, +255687093070],
	  'malipo_yaliyofanyika': [0, 250000, 0]
	})

df = st.session_state.df

# FUNCTION YA KUTENGENEZA PDF
def tengeneza_risiti(red, jina, kiasi, salio):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_front("Arial", 'B', 16)
	pdf.cell(0, 10, "UNBREAKABLE SCHOOL", 0, 1, 'C')
	pdf.cell(0, 10, f"RISITI # : {ref}", 0, 1, 'C')
	pdf.ln(5)
	pdf.set_font("Arial", size=12)
	pdf..cell(0, 10, f"Tarehe: {datetime.date.today()}", 0, 1)
	pdf.cell(0, 10, f"Mwanafunzi: {jina}", 0, 1)
	pdf.cell(0, 10, f"kiasi: Tsh {kiasi:, }", 0, 1)
	pdf.cell(0, 10, f"Salio Jipya: Tsh {salio:,}", 0,1)
	buffer = io.BytesIO()
	pdf.output(buffer)
	return buffer.getvalues()

# LOG IN PAGE
if 'logged_in' not in st.session_state:
	st.session_state.logged_in = False

if not st.session_state.logged_in:
	st.title("🏫UNBREAKABLE SCHOOL PAY")
	user_type = st.radio("Ingia kama:", ["Mzazi", "Mkuu wa Shule"])
	
	if user_type == "Mzazi":
		namba = st.text_input("Namba ya simu ya Mzazi", " ")
		password = st.text_input("Password", type="password")
		if st.button("Ingia"):
			if namba in st.session_state.users and st.session_state.users[namba]['password']==password:
				st.session_state.logged_in = True
				st.session_state.user = namba
				st.session_state.type = "Mkuu"
				st.rerun()
		   else:
			    st.error("password sio sahihi")

else:
	# 4. PORTAL YA MZAZI
	if st.session_state.type == "Mzazi":
		st.title("Portal ya Mzazi")
		namba_mzazi = st.sesaion.user
		Watoto = df[df['namba_mzazi'] == namba_mzazi]
		
		with st.expander("⚙️ Badili Password yako"):
            pass_mpya = st.text_input("Weka Password Mpya", type="password")
            if st.button("Hifadhi Password"):
                st.session_state.users[namba_mzazi]['password'] = pass_mpya
                st.success("Password imebadilishwa!")

       for idx, mtoto in watoto.iterrows():
           st.subheader(f"{mtoto['jina']} - {mtoto['darasa']}")
           st.metric("Deni la Sasa", f"Tsh {mtoto['deni']:,}")
           amount = st.number_input("kiasi cha kulipa", min_value=1000, max_value=int(mtoto['deni'], key=mtoto['namba']))
           if st.button(f"Lipa Tsh {amount:,} Sasa", key=f"btn {mtoto['namba']}", type="primary"):
               ref = f"RCPT {random.randint(10000,99999)}"
               df.at[idx, 'deni'] -= amount
               df.at[idx, 'malipo_yaliyofanyika'] += amount
			   st.session_state.df = df
			   salio_jipya = df.at[idx, 'deni']
			   st.success(f"✅ Malipo yamefanikiwa! Ref: {ref}")
			   pdf_data = tengeneza_risiti(ref, mtoto['jina'], amount, salio_jipya)
			   st.download_button("📄Pakua Risiti PDF", data=pdf_data, file_name=f"risiti_{ref}.pdf")

      if st.button("Toka"):
		  st.session_state.logged_in = False
		  st.rerun()

    #ADMIN PANEL
	elif:
		st.session_state.type == "Mkuu"
		st.title("🧑‍💼 ADMIN PANEL")
		tab1, tab2, tab3 = st.tabs(["📊 Ripoti", "➕ Ongeza Mzazi", "⚙️ Badili Password"])
		
		with tab1:
			st.metric("Jumla ya Madeni", f"Tsh {df['deni'].sum():,}")
			st.dataframe(df, use_container_width=True)

        with tab2: #Hapa admin anafungulia wazaI
			st.header("Ongeza Mzazi Mpya")
			namba_mpya = st.text_input("Namba ya Mzazi +255..")
			mtoto_namba = st.selectbox("Muunganishe na Mwanafunzi"), df['namba'])
			if st.button("Ongeza Mzazi"):
				st.session_state.users[namba_mpya] = {'password:  '1234', 'type': 'Mzazi'}
				df.loc[df['namba'] ==  mtoto_namba, 'namba_mzazi'] = namba_mpya
				st.session_state.df = df
				st.success(f"Mzazi {namba_mpya} imeongezwa! Mwambie aingie na password: 1234")

        with tab3:
		




st.write("---")
st.caption("System imetengenezwa na UNBREAKABLE TECH. Shule ndio msimamizi wa fedha na data zote")
