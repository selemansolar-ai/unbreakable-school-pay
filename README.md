### 🏫 UNBREAKABLE SCHOOL PAY

**School Fee Management & Payment Tracking System for Tanzanian School**

A simple and secure web application that allows parents to check school fees balance and make payments, while school administrators can manages all student and payment data. All data is stored in Google Sheets - no database needed!

### DEMO LIVE
🔗[https://unbreakable-school-pay.streamlit.app](https://unbreakable-school-pay.streamlit.app)

### **FEATURES**

#### **For Parents / Wazazi**
- Login with phone number and password
- View all children linked to the parent
- Check fee balance, total paid and payment
- Mobile friendly design

#### **For School Admin / Mkuu wa Shule**
- Add new student and link to parent phone number
- View all student and payment status
- Add payments manually
- Dashboard with total collected fees
- All data syncs with Google Sheets in real-time

#### **TECH STACK**
- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **Database**: Google Sheets API via gspread
- **Hosting**: Streamlit cloud
- **PDF**: FPDF for receipts

### **HOW TO SETUP LOCALLY**
1. Clone this repo
2. Install requirements
3. Add your 'credentials.json' for Google Sheets API
4. Run the app

### **GOOGLE SHEET STRUCTURE**
The app uses 2 sheets: 'users' and 'wanafunzi'
1.'users': namba, password, role

2.'wanafunzi': jina, namba_mzazi, darasa, jumla_madeni, malipo

### **BUILT BY**
**UNREAKABLE TECH** - Building solutions for Tanzanian Schools

Contact: [+255687093070 WhatsApp]
