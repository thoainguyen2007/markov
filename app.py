import streamlit as st
import numpy as np
st.set_page_config(page_title="Mô hình Markov")

st.title("Mô hình Markov")

# Nhập số lượng trạng thái
n = st.number_input("Nhập số lượng trạng thái", min_value=1, step=1)

# Tạo ma trận chuyển trạng thái
st.subheader("Nhập ma trận chuyển trạng thái M (n x n)")
M = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        M[i, j] = st.number_input(
            f'Tỉ lệ chuyển từ trạng thái {j} sang trạng thái {i}',
            min_value=0.0, max_value=1.0, step=0.01, key=f"M_{i}_{j}"
        )


# Nhập số lượng ban đầu
st.subheader("Nhập số lượng đối tượng ban đầu L")
L = np.zeros((n, 1))
for i in range(n):
    L[i, 0] = st.number_input(
        f'Số lượng trạng thái {i}', min_value=0.0, step=1.0, key=f"L_{i}"
    )

# Nhập số chu kỳ
k = st.number_input("Số chu kỳ k", min_value=1, step=1)

# Kiểm tra tính hợp lệ của ma trận
if st.button("Kiểm tra ma trận và nhập số lượng ban đầu"):
    if (np.sum(M, axis=0) != 1).any() or (M < 0).any():
        st.error("Sai số liệu, vui lòng nhập lại")
    else:
        st.success("Ma trận hợp lệ! Nhập số lượng đối tượng ban đầu.")
        


if st.button("Tính trạng thái sau k chu kỳ"):
    Ln = np.linalg.matrix_power(M, k) @ L
    st.subheader("Kết quả:")
    st.write(Ln)
