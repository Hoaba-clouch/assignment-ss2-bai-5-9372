# HNKS25CNTT1_FastAPI_Session01_Ex01 - Quản lý sản phẩm

## Giới thiệu

Bài tập này nhằm mục đích xây dựng một hệ thống API routing cơ bản bằng FastAPI, tập trung vào việc tạo các endpoint rõ ràng, sử dụng đúng HTTP methods và tổ chức theo nhóm tài nguyên. Chủ đề được chọn là **Quản lý sản phẩm**.

Hệ thống minh họa cách tạo các endpoint cho các hành động CRUD (Create, Read, Update, Delete) cơ bản, cùng với các endpoint để xem thống kê và các tính năng mở rộng khác. Dữ liệu được sử dụng là dữ liệu giả lập trong bộ nhớ để đơn giản hóa, không yêu cầu kết nối cơ sở dữ liệu hoặc sử dụng Path/Query Parameters hay Request Body trong giai đoạn này.

## Chức năng đã làm

API được thiết kế với các endpoint sau:

### Chủ đề API đã chọn: Quản lý sản phẩm

### Bảng thiết kế routing:

| Method   | Endpoint               | Mục đích                                                               |
| :------- | :--------------------- | :--------------------------------------------------------------------- |
| `GET`    | `/products`            | Lấy danh sách tất cả các sản phẩm hiện có.                               |
| `GET`    | `/products/detail`     | Xem chi tiết một sản phẩm cụ thể (hiện tại là sản phẩm đầu tiên).      |
| `POST`   | `/products`            | Thêm một sản phẩm mới vào hệ thống (thêm sản phẩm giả định).           |
| `PUT`    | `/products/update`     | Cập nhật thông tin của một sản phẩm hiện có (cập nhật sản phẩm đầu tiên). |
| `DELETE` | `/products/delete`     | Xóa một sản phẩm khỏi hệ thống (xóa sản phẩm cuối cùng).               |
| `GET`    | `/products/statistics` | Xem thống kê tổng quan về các sản phẩm (số lượng, giá trị tồn kho, phân loại). |
| `GET`    | `/products/low-stock`  | Xem danh sách các sản phẩm có số lượng tồn kho thấp (dưới 20 đơn vị). |
| `GET`    | `/products/popular`    | Xem danh sách các sản phẩm được coi là phổ biến (danh sách giả định). |

## Hướng dẫn chạy chương trình

Để chạy ứng dụng FastAPI này, bạn cần cài đặt Python và FastAPI cùng với Uvicorn.

1.  **Cài đặt các thư viện cần thiết:**
    Mở terminal hoặc command prompt và chạy lệnh sau:
    ```bash
    pip install fastapi uvicorn
    ```

2.  **Lưu mã nguồn:**
    Lưu nội dung của file `main.py` vào một file có tên `main.py` trong thư mục làm việc của bạn.

3.  **Chạy ứng dụng:**
    Từ thư mục chứa file `main.py`, chạy lệnh sau:
    ```bash
    uvicorn main:app --reload
    ```
    *   `main`: Tên module Python (file `main.py`).
    *   `app`: Tên đối tượng FastAPI trong `main.py`.
    *   `--reload`: Tùy chọn để tự động tải lại server khi có thay đổi trong mã nguồn.

4.  **Kiểm tra API:**
    Sau khi server chạy, bạn có thể truy cập các endpoint thông qua trình duyệt hoặc công cụ như Postman/Insomnia:
    *   **Trang tài liệu Swagger UI:** Mở trình duyệt và truy cập: `http://127.0.0.1:8000/docs`
    *   **Trang tài liệu ReDoc:** Mở trình duyệt và truy cập: `http://127.0.0.1:8000/redoc`

    Bạn có thể thử gọi các endpoint được liệt kê trong bảng thiết kế ở trên từ Swagger UI.