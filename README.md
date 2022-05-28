# PBL5

28/05/2022:
+ Đổi cách làm, qua thư mục v2.
+ Chủ yếu dùng 3 file: PhatHienVaLayDuLieuKhuonMat, NhanDien, trainingFace.
+ PhatHienVaLayDuLieuKhuonMat.py: hiện tại dùng webcam để lấy trực tiếp (hơi cồng kềnh để fix sau). Khi chạy thì hỏi <tên> để tạo thư mục và định danh mặt của thằng nào, lấy 52 ảnh lưu vào thư mục DuLieuKhuonMat/<tên>. Lấy xong có hỏi tuỳ chọn train lại dữ liệu.
+ NhanDien.py: mở lên dùng webcam để nhận diện.
+ trainingFace.py: Có hàm training, file này không cần chạy (chạy ở tuỳ chọn PhatHienVaLayDuLieuKhuonMat.py). Training lấy 52 ảnh đã lưu, như cũng train tầm 7-10 tấm.
+ Thư mục cascade: lưu các file kiểu giống thư viện.
+ Thư mục recognizers: lưu dữ liệu training.