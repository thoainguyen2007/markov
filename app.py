#streamlit run app.py



import streamlit as st
import numpy as np
st.set_page_config(page_title="Mô hình Markov")

st.title("Mô hình Markov")

# Nhập số lượng trạng thái
n = st.number_input("Nhập số lượng trạng thái", min_value=2, step=1)

# Tạo ma trận chuyển trạng thái
st.subheader("Nhập các tỉ lệ chuyển trạng thái")
M = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i!=j:
            M[i, j] = st.number_input(
                f'Tỉ lệ chuyển từ trạng thái {j+1} sang trạng thái {i+1}',
                min_value=0.0, max_value=1.0, step=0.01, key=f"M_{i}_{j}"
            )
for i in range(n):
    M[i,i]=1-np.sum(M,axis=0)[i]


# Nhập số lượng ban đầu
st.subheader("Nhập số lượng đối tượng ban đầu L")
L = np.zeros((n, 1))
for i in range(n):
    L[i, 0] = st.number_input(
        f'Số lượng trạng thái {i+1}', min_value=0.0, step=1.0, key=f"L_{i}"
    )

# Nhập số chu kỳ
k = st.number_input("Số chu kỳ k", min_value=1, step=1)

# Kiểm tra tính hợp lệ của ma trận và tính kết quả

if st.button(f"Tính trạng thái sau {k} chu kỳ"):
    if (np.sum(M, axis=0) != 1).any() or (M < 0).any():
        st.error("Sai số liệu, vui lòng nhập lại")


    Ln = np.linalg.matrix_power(M, k) @ L
    st.subheader("Kết quả:")
    for i in range (n):
        st.write(f'Số lượng đối tượng ở trạng thái {i+1} là {Ln[i,0]}')

