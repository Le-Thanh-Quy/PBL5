# PBL5

- Thư mục DataBase chứa các thư mục con: mỗi thư mục con là tên của người nhận diện và 4-5 ảnh khuôn mặt bên trong (1)

- chạy file initDB trước để tạo CSDL lưu vào CSDL.xlsx (nếu không có thay đổi DB gì thì không cần chạy lại) (2)

- file main.py sẽ khởi chạy camera (mặc định) của máy tính, nhận diện mặt đưa ra tên (3)
![image](https://user-images.githubusercontent.com/80233271/165322217-985d3069-7c1f-464f-825f-7cb1fbc9a134.png)

26/04/2022:
+ đang còn lỗi và chưa test nhiều, mấy bạn chưa cần tạo exception 😥
+ mục (1) mấy pạn có thêm, sửa dữ liệu ảnh thì mỗi thư mục (của mỗi người) thì thêm 4-5 ảnh vô ha 🙉
+ file main.py có cmt vài thư viện cần tải với import

05/05/2022:
+ file main.py: duyệt nhiều ảnh của 1 người (4 ảnh thay vì dùng 1 cái như trước), tính trung bình tỷ lệ nhận dạng rồi so sánh với những người khác.
+ CSDL thêm cái quyền truy cập, thằng nào true là có quyền cạy két, thằng nào false thì là không quyền. 
+ configAllowed.py để cho thằng nào có quyền, chạy file csdl trước rùi mới tới file này (chạy file, nhấn 'y', rồi ghi stt bắt đầu từ 0 vào, ví dụ muốn cho 3 thằng đầu thì '0 1 2')
+ history.log để lưu lịch sử nhận dạng mặt