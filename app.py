#streamlit run app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Mô hình Markov", layout="centered")

st.title("Mô hình Markov")

# Nhập số lượng trạng thái
st.subheader("Nhập số lượng trạng thái")
n = st.number_input("", min_value=2, step=1)
M = np.zeros((n, n))
L0 = np.zeros((n, 1))



# Cho người dùng chọn 1 trong 2 kiểu nhập
st.subheader("Chọn cách nhập ma trận Markov")
mode = st.radio("",["Dạng ma trận", "Dạng tỉ lệ chuyển"])



if mode=="Dạng tỉ lệ chuyển":
    # Tạo ma trận chuyển trạng thái
    st.subheader("Nhập các tỉ lệ chuyển trạng thái")
    for i in range(n):
        for j in range(n):
            if i!=j:
                M[i, j] = st.number_input(
                    f'Tỉ lệ chuyển từ trạng thái {j+1} sang trạng thái {i+1}',
                    min_value=0.0, max_value=1.0, step=0.01, key=f"M_{i}_{j}"
                )
    for i in range(n):
        M[i,i]=1-np.sum(M,axis=0)[i]

else:

    # Tạo ma trận chuyển trạng thái
    for i in range(n):
        cols = st.columns(n)
        for j in range(n):
            M[i, j] = cols[j].number_input(
                rf"$M_{{{i+1}{j+1}}}$",
                min_value=0.0, max_value=1.0, step=0.01,
                key=f"mat_{i}_{j}")
    if (np.sum(M, axis=0) != 1).any():
        st.error("Sai số liệu(tổng mỗi cột phải bằng 1), vui lòng nhập lại")



# Nhập số lượng ban đầu
st.subheader("Nhập số lượng đối tượng ban đầu L")
for i in range(n):
    L0[i, 0] = st.number_input(f'Số lượng trạng thái {i+1}', min_value=0.0, step=0.01, key=f"L0_{i}")


# Nhập số chu kỳ
k = st.number_input("Số chu kỳ k", min_value=1, step=1)

#Kiểm tra tính hợp lệ của ma trận
if (np.sum(M, axis=0) != 1).any() or (M < 0).any():
    hople=False
else:
    hople=True


# Tính kết quả
st.subheader("Kết quả")
hienthi = st.radio("Bạn muốn",
                [f"Chỉ xem số lượng trạng thái sau {k} chu kì", 
                    f"Xem biểu đố biến đổi suốt {k} chu kì"], disabled=not hople)


if hople==True and st.button("Tính toán kết quả"):
    if hienthi==f"Chỉ xem số lượng trạng thái sau {k} chu kì":
        Ln = np.linalg.matrix_power(M, k) @ L0
        st.subheader("Kết quả:")
        for i in range (n):
            st.write(f'Số lượng đối tượng ở trạng thái {i+1} là {Ln[i,0]}')    

    else:
        states_over_time = []
        Ln = L0
        for step in range(k):
            Ln = M@Ln       # tính bước tiếp theo
            states_over_time.append(Ln)  # lưu vào list
        for i in range (n):
            st.write(f'Số lượng đối tượng ở trạng thái {i+1} ở chu kì {k} là {Ln[i,0]}')    

        states_over_time = np.array(states_over_time)  # shape (k, n)

        fig, ax = plt.subplots()
        for i in range(n):
            ax.plot(range(1, k+1), states_over_time[:, i], marker='o', label=f"S{i}")

        ax.set_xlabel("Chu kỳ")
        ax.set_ylabel("Số lượng trạng thái")
        ax.set_title("Số lượng các trạng thái theo chu kỳ")
        ax.legend()
        st.pyplot(fig)

        
            

