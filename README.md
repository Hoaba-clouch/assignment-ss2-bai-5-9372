# HNKS25CNTT1_FastAPI_Session01_Ex01

## Giới thiệu
Bài tập này yêu cầu xây dựng một ứng dụng API sử dụng FastAPI để cấu hình routing cho các endpoint quản lý tài nguyên. Mục tiêu là tạo ra các API endpoint rõ ràng, dễ hiểu, sử dụng đúng HTTP method và được tổ chức theo nhóm tài nguyên.

## Chủ đề API
**Quản lý sản phẩm**

## Bảng thiết kế Routing
Dưới đây là danh sách các endpoint được thiết kế cho hệ thống quản lý sản phẩm, bao gồm các chức năng cơ bản và các chức năng mở rộng.

| Method | Endpoint               | Mục đích                                           |
| :----- | :--------------------- | :------------------------------------------------- |
| GET    | `/products`            | Lấy danh sách tất cả sản phẩm                      |
| GET    | `/products/detail`     | Xem chi tiết của một sản phẩm bất kỳ (ví dụ: sản phẩm đầu tiên) |
| POST   | `/products`            | Thêm một sản phẩm mới (chỉ trả về thông báo thành công) |
| PUT    | `/products/update`     | Cập nhật thông tin của một sản phẩm (chỉ trả về thông báo thành công) |
| DELETE | `/products/delete`     | Xóa một sản phẩm (chỉ trả về thông báo thành công) |
| GET    | `/products/statistics` | Xem thống kê tổng quan về sản phẩm                 |
| **Mở rộng** |                        |                                                    |
| GET    | `/products/categories` | Lấy danh sách các danh mục sản phẩm                |
| GET    | `/products/low_stock`  | Xem danh sách sản phẩm có số lượng tồn kho thấp     |

## Các chức năng đã làm
*   **Xem danh sách sản phẩm**: Endpoint `/products` (GET).
*   **Xem chi tiết sản phẩm**: Endpoint `/products/detail` (GET).
*   **Thêm sản phẩm mới**: Endpoint `/products` (POST).
*   **Cập nhật thông tin sản phẩm**: Endpoint `/products/update` (PUT).
*   **Xóa sản phẩm**: Endpoint `/products/delete` (DELETE).
*   **Xem thống kê sản phẩm**: Endpoint `/products/statistics` (GET).
*   **Xem danh mục sản phẩm (mở rộng)**: Endpoint `/products/categories` (GET).
*   **Xem sản phẩm tồn kho thấp (mở rộng)**: Endpoint `/products/low_stock` (GET).

## Hướng dẫn chạy chương trình
Để chạy ứng dụng FastAPI này, bạn cần cài đặt `FastAPI` và `uvicorn`.

1.  **Cài đặt các thư viện cần thiết**:
    ```bash
    pip install fastapi uvicorn
    ```

2.  **Lưu mã nguồn**:
    Lưu nội dung của file `main.py` vào một file có tên `main.py`.

3.  **Chạy ứng dụng**:
    Mở terminal hoặc command prompt, điều hướng đến thư mục chứa file `main.py` và chạy lệnh sau:
    ```bash
    uvicorn main:app --reload
    ```
    *   `main`: Tên của file Python (main.py).
    *   `app`: Tên của đối tượng FastAPI trong file đó.
    *   `--reload`: Tùy chọn này giúp ứng dụng tự động tải lại khi bạn thay đổi mã nguồn.

4.  **Truy cập API**:
    Ứng dụng sẽ chạy mặc định trên `http://127.0.0.1:8000`.
    Bạn có thể kiểm tra các endpoint bằng cách sử dụng các công cụ như Postman, curl, hoặc truy cập trực tiếp qua trình duyệt:
    *   **Tài liệu Swagger UI**: `http://127.0.0.1:8000/docs`
    *   **Tài liệu ReDoc**: `http://127.0.0.1:8000/redoc`

    Bạn có thể thử các endpoint đã định nghĩa trong bảng thiết kế routing ở trên.