#Chạy hồi quy python trong linear.py từ private_investment.xlsx
#Vẽ biểu đồ hồi quy
#Tính các biến phụ thuộc và độc lập
#Dự đoán và kết luận từ kết quả hồi quy
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# --- Bước 1: Tải dữ liệu từ tệp Excel ---
# Đảm bảo rằng tệp 'private_investment.xlsx' nằm trong cùng thư mục với tệp script này.
try:
    df = pd.read_excel('private_investment.xlsx')
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tệp 'private_investment.xlsx'. Vui lòng đảm bảo tệp nằm trong cùng một thư mục.")
    exit()

# --- Bước 2: Xác định biến phụ thuộc và biến độc lập ---
# BIẾN PHỤ THUỘC (dependent variable - y): Là biến bạn muốn dự đoán.
# BIẾN ĐỘC LẬP (independent variable - X): Là biến bạn sử dụng để dự đoán.
# !!! QUAN TRỌNG: Thay thế 'TEN_COT_BIEN_DOC_LAP' và 'TEN_COT_BIEN_PHU_THUOC' bằng tên cột thực tế trong tệp Excel của bạn.

# Ví dụ, nếu bạn muốn dự đoán 'Đầu tư tư nhân' (y) dựa trên 'GDP' (X)
ten_bien_doc_lap = 'GDP' # <-- THAY THẾ TÊN CỘT CỦA BẠN Ở ĐÂY
ten_bien_phu_thuoc = 'Dau_tu_tu_nhan' # <-- THAY THẾ TÊN CỘT CỦA BẠN Ở ĐÂY

# Kiểm tra xem các cột đã cho có tồn tại trong DataFrame không
if ten_bien_doc_lap not in df.columns or ten_bien_phu_thuoc not in df.columns:
    print(f"Lỗi: Một hoặc cả hai cột '{ten_bien_doc_lap}' và '{ten_bien_phu_thuoc}' không tồn tại trong tệp Excel.")
    print(f"Các cột có sẵn là: {df.columns.tolist()}")
    exit()

y = df[ten_bien_phu_thuoc]
X = df[ten_bien_doc_lap]

# Thêm một hằng số (intercept) vào mô hình. Đây là một bước cần thiết cho hồi quy OLS.
X = sm.add_constant(X)

# --- Bước 3: Chạy mô hình hồi quy ---
# Chúng tôi sử dụng phương pháp Bình phương nhỏ nhất thông thường (Ordinary Least Squares - OLS)
model = sm.OLS(y, X).fit()

# --- Bước 4: In kết quả hồi quy chi tiết ---
print("--- KẾT QUẢ HỒI QUY TUYẾN TÍNH ---")
print(model.summary())
print("------------------------------------")


# --- Bước 5: Vẽ biểu đồ hồi quy ---
plt.figure(figsize=(10, 6))
# Sử dụng seaborn để vẽ biểu đồ phân tán cùng với đường hồi quy và khoảng tin cậy
sns.regplot(x=df[ten_bien_doc_lap], y=df[ten_bien_phu_thuoc], ci=95, scatter_kws={'alpha':0.5})

plt.title(f'Biểu đồ hồi quy: {ten_bien_phu_thuoc} so với {ten_bien_doc_lap}', fontsize=16)
plt.xlabel(ten_bien_doc_lap, fontsize=12)
plt.ylabel(ten_bien_phu_thuoc, fontsize=12)
plt.grid(True)
plt.show()


# --- Bước 6: Dự đoán và kết luận ---
# Lấy các hệ số từ mô hình
intercept, slope = model.params

print("\n--- DIỄN GIẢI VÀ KẾT LUẬN ---")
print(f"Phương trình hồi quy: {ten_bien_phu_thuoc} = {intercept:.4f} + {slope:.4f} * {ten_bien_doc_lap}")

# Diễn giải hệ số
print(f"\nDiễn giải hệ số góc (slope): Khi {ten_bien_doc_lap} tăng 1 đơn vị, {ten_bien_phu_thuoc} được dự đoán sẽ {'tăng' if slope > 0 else 'giảm'} một lượng là {abs(slope):.4f} đơn vị.")

# Diễn giải R-squared
r_squared = model.rsquared
print(f"\nR-squared = {r_squared:.4f}: Khoảng {r_squared*100:.2f}% sự biến thiên của biến phụ thuộc '{ten_bien_phu_thuoc}' có thể được giải thích bởi biến độc lập '{ten_bien_doc_lap}'.")

# Đưa ra dự đoán mới
# !!! QUAN TRỌNG: Thay đổi giá trị `gia_tri_moi` để dự đoán cho một điểm dữ liệu mới.
gia_tri_moi = 1000  # <-- THAY ĐỔI GIÁ TRỊ NÀY ĐỂ DỰ ĐOÁN
gia_tri_du_doan = model.predict([1, gia_tri_moi]) # [1, gia_tri_moi] vì chúng ta cần hằng số (intercept)

print(f"\nDự đoán: Khi {ten_bien_doc_lap} = {gia_tri_moi}, giá trị dự đoán cho {ten_bien_phu_thuoc} là {gia_tri_du_doan[0]:.4f}.")
print("---------------------------------")