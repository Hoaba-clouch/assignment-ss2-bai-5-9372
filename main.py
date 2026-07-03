from fastapi import FastAPI

app = FastAPI(
    title="API Quản lý Sản phẩm",
    description="API đơn giản để minh họa cấu hình routing với FastAPI cho chủ đề quản lý sản phẩm.",
    version="1.0.0"
)

@app.get("/products", summary="Lấy danh sách tất cả sản phẩm")
async def get_all_products():
    """Trả về danh sách tất cả sản phẩm hiện có."""
    return {"message": "Danh sách tất cả sản phẩm.", "data": [{"id": 1, "name": "Sản phẩm A"}, {"id": 2, "name": "Sản phẩm B"}]}

@app.get("/products/detail", summary="Xem chi tiết một sản phẩm bất kỳ")
async def get_product_detail():
    """Trả về thông tin chi tiết của một sản phẩm."""
    return {"message": "Chi tiết của một sản phẩm cụ thể.", "data": {"id": 1, "name": "Sản phẩm A", "description": "Mô tả chi tiết sản phẩm A", "price": 100}}

@app.post("/products", summary="Thêm sản phẩm mới")
async def create_new_product():
    """Tạo một sản phẩm mới (hiện tại chỉ trả về thông báo thành công)."""
    return {"message": "Sản phẩm mới đã được thêm thành công.", "status": "success"}

@app.put("/products/update", summary="Cập nhật thông tin sản phẩm")
async def update_product_info():
    """Cập nhật thông tin của một sản phẩm hiện có (hiện tại chỉ trả về thông báo thành công)."""
    return {"message": "Thông tin sản phẩm đã được cập nhật thành công.", "status": "success"}

@app.delete("/products/delete", summary="Xóa sản phẩm")
async def delete_product():
    """Xóa một sản phẩm khỏi hệ thống (hiện tại chỉ trả về thông báo thành công)."""
    return {"message": "Sản phẩm đã được xóa thành công.", "status": "success"}

@app.get("/products/statistics", summary="Xem thống kê tổng quan về sản phẩm")
async def get_product_statistics():
    """Cung cấp các số liệu thống kê tổng quan về sản phẩm."""
    return {"message": "Thống kê tổng quan về sản phẩm.", "data": {"total_products": 100, "active_products": 85, "out_of_stock": 15}}

# --- Extended Endpoints (Yêu cầu sáng tạo thêm) ---

@app.get("/products/categories", summary="Lấy danh sách các danh mục sản phẩm")
async def get_product_categories():
    """Trả về danh sách các danh mục mà sản phẩm thuộc về."""
    return {"message": "Danh sách các danh mục sản phẩm.", "data": ["Điện tử", "Thời trang", "Gia dụng", "Sách"]}

@app.get("/products/low_stock", summary="Xem danh sách sản phẩm có số lượng tồn kho thấp")
async def get_low_stock_products():
    """Liệt kê các sản phẩm cần được bổ sung tồn kho."""
    return {"message": "Danh sách sản phẩm có số lượng tồn kho thấp.", "data": [{"id": 3, "name": "Pin AA", "stock": 5}, {"id": 4, "name": "Bàn phím cơ", "stock": 10}]}