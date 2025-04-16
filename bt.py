import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st



st.markdown("2321050066:Bùi Mai Hương, 23215043:Khổng Thị Hòa, 2321050084:Đinh Thùy Linh")
@st.cache_data
def loaddata():
    df=pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")
    return df
df=loaddata()
st.dataframe(df)

st.sidebar.header("Chọn Rating")
# Giả sử cột điểm rating tên là 'score' trong dataset
min_rating = float(df['score'].min())
max_rating = float(df['score'].max())

rating_range = st.sidebar.slider(
    "Chọn khoảng điểm đánh giá:",
    min_value=min_rating,
    max_value=max_rating,
    value=(min_rating, max_rating),
    step=0.1
)

# Lọc dữ liệu theo rating
filtered_df = df[(df['score'] >= rating_range[0]) & (df['score'] <= rating_range[1])]
st.subheader(f"Danh sách phim có điểm từ {rating_range[0]:.1f} đến {rating_range[1]:.1f}")
st.dataframe(filtered_df)

##
st.subheader("📊 Biểu đồ phân bố điểm đánh giá (Histogram)")
fig=plt.figure(figsize=(5,5))
plt.hist(filtered_df["score"],bins=20)
plt.title("Phân bố đánh giá các phim")
plt.xlabel("Điểm đánh giá")
plt.ylabel("Số lượng phim")
st.pyplot(fig)
    
