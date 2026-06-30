import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(layout="wide", page_title="Makro Monthly Scheduler")

st.title("Makro Monthly Scheduler (July 2026)")

# ข้อมูลพนักงาน 24 ท่าน
data = {
    'Emp.Code': ['00015942', '00009251', '00068673', '00003912', '00075745', '00065835', '00039569', '00030761', '00088227', '00005478', '00012929', '00002958', '00073378', '00016020', '00019962', '00048417', '00006174', '00049306', '00002408', '00012965', '00029917', '00002397', '00006800', '00000000'],
    'Name': ['วาทยากร', 'วนิดา', 'นพรัตน์', 'อำพันทอง', 'วราณิษฐ์', 'ศุภิกามณฑ์', 'อุทัย', 'เกียรติศักดิ์', 'กิตทรา', 'เบญจมาศ', 'อัญพัชญ์', 'พรพิสัย', 'จรัส', 'อรพรรณ', 'ศุธิชา', 'ทาริกา', 'ณัชชา', 'สราวุธ', 'กัญญารัตน์', 'รสริน', 'ปฏิวัติ', 'โยธิน', 'วิโรจน์', 'พนักงานใหม่'],
    'Position': ['SGM', 'ASGM', 'ASGM', 'Order Mg', 'Sale Mgr', 'Officer', 'SM-Dry1', 'SM-Dry2', 'SM-Non', 'SM-Cust', 'SM-Cust', 'SM-O2O', 'SM-O2O', 'SM-O2O', 'Sr.Sales', 'SM-HR', 'SM-GR', 'SM-GA', 'Fresh Mgr', 'SM-Butch', 'SM-Fish', 'SM-F&V', 'SM-Bakery', 'Support']
}

df = pd.DataFrame(data)

# สร้างตารางวันในเดือน
days = list(range(1, 32))
for day in days:
    df[day] = ""

st.write("พี่นพสามารถแก้ไขกะงาน (01+, 01++, 19+, 19++, 11) ลงในตารางด้านล่างได้เลยค่ะ:")

# แสดงผลตารางให้แก้ไขได้
edited_df = st.data_editor(df, num_rows="fixed", use_container_width=True)

if st.button("บันทึกตาราง"):
    st.write("ตารางถูกบันทึกชั่วคราวในหน้าจอค่ะ")

st.info("เงื่อนไขกะงานที่รองรับ: 01+, 01++, 19+, 19++, 11")