import streamlit as st
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="UNBREAKABLE SCHOOL PAY", page_icon="🏫", layout="wide")

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

#---MENU YA JUU---
menu = st.sidebar.sidebarbox("Chagua Sehemu", ["Mlango wa Mzazi", "Mlango wa Mkuu wa shule"])

#===SEHEMU 1: MLANGO WA MZAZI===
if menu == "Mlango wa Mzazi":
	st.title("🏫UNBREAKABLE SCHOOL PAY")
	st.subheader("Lipa Ada yako Mtandaoni")
	st.write("---")
	
	student_id = st.text_input("Ingiza Namba ya Mwanafunzi", " ")
	
	if student_id:
		student = df[df['namba'] == student_id]
		if not student.empty:
			st.success("Mwanafunzi amepatikana!")
			col1, col2 = st.columns(2)
			with col1:
				st.write(f"**Jina:** {student['jina'].values[0]}")
				st.write(f"**Darasa:** {student['darasa'].values[0]}")
			with col2:
				st.write(f"**Deni la Sasa:** Tsh {student['deni'].values[0]:, }")
				st.write(f"**Alishalipa:** Tsh {student['malipo_yaliyofanyika'].values[0]:, }")
			
			amount = st.number_input("Weka Kiasi cha Kulipa", min_value=1000, max_value=int(student['deni'].values[0]), step=5000)
			
			if st.button(f"Lipa Tsh {amount:, } Sasa", type="primary"):
				with st.spinner("Tafadhali Lipia kwa simu yako..."):
					import time; time.sleep(2)#Hapa API itaingia
				#SASISHA DATA
				idx = df[df['namba'] == stident_id].index[0]
				df.at[idx, 'deni'] -= amount
				df.at[idx, 'malipo_yaliyofanyika'] += amount
				st.session_state.df = df
				
				st.balloons()
				st.success("Malipo yamefanikiwa!✅")
				st.write("### RISITI: RCPT{random.randint(10000,99999)}")
				st.write(f"**Kiasi:** Tsh {amount:, } | **Salio Jipya:** Tsh {df.at[idx, 'deni']:, }")
				st.info(f"Risiti imetumwa kwa WhatsApp: {student['namba_mzazi'].values[0]}")
				
	else: st.error("Namba ya Mwanafunzi haipatikani.")
	
#====SEHEMU 2: MLANGO WA MKUU====
elif menu == "Mlango wa Mkuu wa Shule":
	st.title("🧑‍💼ADMIN PANEL - Mkuu wa Shule")
	
	password = st.text_input("Weka Password yako Mkuu", type="password")
	if password == "admin123":
		st.success("Karibu Mkuu!")
		tab1, tab2, tab3 = st.tabs(["📊Ripot", "🔍Tafuta Mwanafinzi", "✏️Hariri Data"])
		
		with tab1:
			st.header("Ripoti ya Jumla")
			total_deni = df['deni'].sum()
			total_lipwa = df['malipo_yaliyofanyika'].sum()
			col1, col2, col3 = st.columns(3)
			col1.metric("Jumla ya Madeni", f"Tsh {total_deni:, }")
			col2.metric("Jumla Imelipwa", f"Tsh {total_lipwa:, }")
			col3.metric("Wanafunzi", len(df))
			st.DataFrame(df)
			
		with tab2:
			st.header("Tafuta Mwanafunzi")
			search = st.text_input("Tafuta kwa Jina au Namba")
			if search:
				result = df[df['jina'].str.contains(search, case=False)]
				st.dataframe(result)
				
	   with tab3:
	   	st.header("Badili Deni la Mwanafunzi")
	   	student_to_edit = st.selectbox("Chagua Mwanafunzi", df['namba'])
	   	new_debt = st.number_input("Weka Deni Jipya", value=int(df[df['namba']==student_to_edit]['deni'].values[0]))
	   	if st.button("Hifadhi Mabadiliko"):
	   		df.loc[df['namba'] == student_to_edit, 'deni'] = new_debt
	   		st.session_state.df = df
	   		st.success("Imesasishwa!")

   else password:
   	st.error  ("password sio Sahihi")

st.write("---")
st.caption("System imetengenezwa na UNBREAKABLE TECH. Shule ndio msimamizi wa fedha na data zote")
