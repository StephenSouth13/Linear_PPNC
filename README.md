Phân Tích Hồi Quy Tuyến Tính bằng Python
Đây là một dự án đơn giản để thực hiện phân tích hồi quy tuyến tính bằng Python. Script sử dụng các thư viện khoa học dữ liệu phổ biến như pandas, statsmodels, và matplotlib để mô hình hóa và trực quan hóa mối quan hệ giữa các biến số được cung cấp trong một tệp Excel.
Lưu ý: Bạn có thể thay thế hình ảnh trên bằng ảnh chụp màn hình biểu đồ kết quả của chính bạn.
Tính Năng Chính
Đọc Dữ liệu Động: Tự động đọc dữ liệu từ tệp private_investment.xlsx.
Mô hình Hồi quy OLS: Sử dụng phương pháp Bình phương nhỏ nhất thông thường (Ordinary Least Squares) từ thư viện statsmodels.
Báo cáo Thống kê: In ra bảng tóm tắt hồi quy chi tiết, bao gồm R-squared, hệ số, sai số chuẩn, và giá trị P.
Trực quan hóa Dữ liệu: Vẽ biểu đồ phân tán của các điểm dữ liệu cùng với đường hồi quy tuyến tính và khoảng tin cậy 95%.
Diễn giải và Dự đoán: Cung cấp phương trình hồi quy, diễn giải ý nghĩa của các hệ số và cho phép dự đoán giá trị mới.
Công Nghệ Sử Dụng
Ngôn ngữ: Python 3
Thư viện:
pandas: Để xử lý và thao tác dữ liệu.
openpyxl: Để pandas có thể đọc được tệp .xlsx.
statsmodels: Để xây dựng mô hình thống kê và thực hiện hồi quy.
matplotlib & seaborn: Để trực quan hóa dữ liệu.
Hướng Dẫn Cài Đặt và Sử Dụng
1. Chuẩn bị
Clone kho chứa này về máy tính của bạn:
Generated bash
git clone https://github.com/TEN-CUA-BAN/TEN-KHO-CHUA.git
cd TEN-KHO-CHUA
Use code with caution.
Bash
(Hãy thay thế TEN-CUA-BAN/TEN-KHO-CHUA bằng URL kho chứa của bạn)
2. Thiết lập Môi trường
Khuyến khích sử dụng một môi trường ảo để quản lý các gói thư viện một cách độc lập.
Generated bash
# Tạo một môi trường ảo có tên là 'venv'
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows:
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate```

### **3. Cài đặt các Thư viện**

Cài đặt tất cả các thư viện cần thiết bằng lệnh sau:
```bash
pip install pandas openpyxl statsmodels matplotlib seaborn
Use code with caution.
Bash
4. Cấu hình và Chạy Script
Đặt tệp dữ liệu: Đảm bảo tệp private_investment.xlsx của bạn nằm trong thư mục gốc của dự án.
Chỉnh sửa file linear.py: Mở file và tùy chỉnh các biến sau cho phù hợp với dữ liệu của bạn:
Generated python
# Thay thế bằng tên cột thực tế trong tệp Excel của bạn
ten_bien_doc_lap = 'TEN_COT_BIEN_DOC_LAP'
ten_bien_phu_thuoc = 'TEN_COT_BIEN_PHU_THUOC'

# (Tùy chọn) Thay đổi giá trị này để dự đoán
gia_tri_moi = 1000
Use code with caution.
Python
Thực thi script: Chạy lệnh sau trong terminal của bạn:
Generated bash
python linear.py
Use code with caution.
Bash
5. Xem Kết quả
Bảng tóm tắt hồi quy và phần diễn giải sẽ được in ra trực tiếp trong terminal.
Một cửa sổ biểu đồ sẽ tự động bật lên để hiển thị kết quả trực quan.
Giấy Phép
Dự án này được cấp phép theo Giấy phép MIT. Xem tệp LICENSE để biết thêm chi tiết (nếu có).
