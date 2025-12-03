Docker_Project
Mô tả Ứng dụng Flask đơn giản. Chạy trong Docker, dễ deploy trên bất kỳ máy nào có Docker.
📦 Cách chạy dự án:

1️⃣ Kiểm tra Docker:

docker --version
2️⃣ Clone repository:

git clone https://github.com/TIEUPHUONG1711/Docker_Project.git
cd Docker_Project
3️⃣ Build Docker image:

docker build -t quoteapp:latest .
4️⃣ Chạy container:

docker run -d -p 5000:5000 --name quoteapp quoteapp:latest
Truy cập ứng dụng tại:

http://127.0.0.1:5000/web
🔁 Rebuild khi cập nhật code:

Nếu bạn thay đổi nội dung project, hãy build lại image:

docker build -t quoteapp:latest .
docker run -d -p 5000:5000 --name quoteapp quoteapp:latest
🛑 Dừng & Xóa container Liệt kê container đang chạy:

docker ps
Dừng container:

docker stop <container_id>
container_id lấy từ cột CONTAINER ID trong docker ps.
Xóa container:

docker rm <container_id>
Xóa image (tùy chọn):

docker rmi docker_flask_app
