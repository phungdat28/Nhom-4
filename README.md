User
# Nhóm 4 :
## Nguyễn Văn Trường
## Phùng Tiến Đạt
## Nguyễn Xuân Chức
## Nguyễn Gia Bảo
## b) Tìm hiểu và giải thích chi tiết giao diện sử dụng của một project.
### Tab "Code" :
- Tab "Code" chứa mã nguồn của dự án. Có thể sao chép URL để clone repository về máy cục bộ của mình.
- Có thể tải về mã nguồn dưới dạng file ZIP.
  Tab Issues:
### Tab "Issues":
- sử dụng để theo dõi, báo cáo lỗi và thảo luận về các vấn đề trong dự án.
### Tab "Pull Requests" :
- Tab "Pull Requests" là nơi bạn có thể tạo và xem các pull request để đề xuất thay đổi vào dự án.
### Tab "Projects" :
- Tab "Projects" có tác dụng giúp bạn quản lý công việc và theo dõi tiến độ của dự án. Nó cung cấp một cách để tổ chức và theo dõi các nhiệm vụ, tính năng, hoặc các mục công việc khác trong dự án.
### Tab "Security" :
- Tab "Security" cung cấp thông tin và công cụ liên quan đến bảo mật của dự án. Nó giúp bạn theo dõi và quản lý các vấn đề bảo mật trong mã nguồn.
### Tab "Insights" :
- Tab "Insights" cung cấp thông tin phân tích và thống kê về dự án của bạn. Giúp hiểu rõ hơn về cách mà người dùng tương tác với mã nguồn của bạn và cung cấp thông tin hữu ích về sự phát triển của dự án.
## c) Tìm hiểu các lệnh được sử dụng trong git.
### Cấu hình Git:
- git config --global user.name "Tên của bạn"
- git config --global user.email "email@example.com"
### Tạo Repository:
- git init
### Clone Repository:
- git clone <URL_repository>
### Kiểm Tra Trạng Thái:
- git status
### Thêm File vào Stage:
- git add <tên_file>
### Commit Thay Đổi:
- git commit -m "Thông điệp commit"
### Xem Lịch Sử Commit:
- git log
### Tạo Nhánh:
- git branch <tên_nhánh>
### Chuyển Đổi Nhánh:
- git checkout <tên_nhánh>
### Hợp Nhất Nhánh:
- git merge <tên_nhánh>
### Xóa Nhánh:
- git branch -d <tên_nhánh>
### Tải Thay Đổi từ Repository Xa:
- git pull origin <tên_nhánh>
### Đẩy Thay Đổi Lên Repository Xa:
- git push origin <tên_nhánh>
### Tạo Nhánh và Chuyển Đến Nhánh Mới:
- git checkout -b <tên_nhánh>
### Hủy Bỏ Các Thay Đổi Chưa Commit:
- git reset --hard
### Khôi Phục File Đã Xóa:
- git checkout -- <tên_file>
### Tạo và Áp Dụng Patch:
- git diff > patchfile
- git apply patchfile
