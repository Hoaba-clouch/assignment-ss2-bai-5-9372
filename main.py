from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API Quản Lý Sản Phẩm",
    description="API đơn giản để quản lý thông tin sản phẩm, minh họa các phương thức HTTP cơ bản và cách tổ chức routing trong FastAPI."
)

# Danh sách sản phẩm giả lập để minh họa
# Trong thực tế, dữ liệu này sẽ được lưu trữ trong database
products_db = [
    {"id": 1, "name": "Laptop Dell XPS 15", "price": 1500, "stock": 50, "category": "Electronics"},
    {"id": 2, "name": "Mouse Logitech MX Master 3", "price": 100, "stock": 120, "category": "Accessories"},
    {"id": 3, "name": "Keyboard Mechanical G.Skill", "price": 120, "stock": 30, "category": "Accessories"},
    {"id": 4, "name": "Monitor Samsung Odyssey G9", "price": 1200, "stock": 15, "category": "Electronics"},
    {"id": 5, "name": "Webcam Logitech C920", "price": 70, "stock": 80, "category": "Accessories"},
    {"id": 6, "name": "SSD Samsung 970 EVO Plus 1TB", "price": 150, "stock": 20, "category": "Components"}
]

# --- Main Endpoints ---

@app.get("/products", tags=["Sản Phẩm"])
async def get_all_products():
    """
    Lấy danh sách tất cả các sản phẩm hiện có.
    """
    return {"message": "Danh sách sản phẩm", "data": products_db}

@app.get("/products/detail", tags=["Sản Phẩm"])
async def get_product_detail():
    """
    Xem chi tiết một sản phẩm cụ thể.
    (Hiện tại trả về chi tiết sản phẩm đầu tiên do chưa sử dụng Path Parameter)
    """
    if products_db:
        return {"message": "Chi tiết sản phẩm", "data": products_db[0]}
    raise HTTPException(status_code=404, detail="Không có sản phẩm nào để hiển thị chi tiết.")

@app.post("/products", tags=["Sản Phẩm"])
async def create_product():
    """
    Thêm một sản phẩm mới vào hệ thống.
    (Hiện tại là thêm một sản phẩm giả định do chưa sử dụng Request Body)
    """
    new_id = max([p["id"] for p in products_db]) + 1 if products_db else 1
    new_product = {"id": new_id, "name": f"Sản phẩm mới {new_id}", "price": 99.99, "stock": 100, "category": "General"}
    products_db.append(new_product)
    return {"message": "Sản phẩm đã được thêm thành công", "data": new_product}

@app.put("/products/update", tags=["Sản Phẩm"])
async def update_product():
    """
    Cập nhật thông tin của một sản phẩm hiện có.
    (Hiện tại là cập nhật sản phẩm đầu tiên trong danh sách do chưa sử dụng Request Body)
    """
    if products_db:
        product_to_update = products_db[0]
        original_name = product_to_update["name"]
        product_to_update["name"] = f"Cập nhật - {original_name}"
        product_to_update["price"] = product_to_update["price"] * 1.1
        return {"message": f"Sản phẩm '{original_name}' đã được cập nhật thành công", "data": product_to_update}
    raise HTTPException(status_code=404, detail="Không có sản phẩm nào để cập nhật.")

@app.delete("/products/delete", tags=["Sản Phẩm"])
async def delete_product():
    """
    Xóa một sản phẩm khỏi hệ thống.
    (Hiện tại là xóa sản phẩm cuối cùng trong danh sách do chưa sử dụng Path Parameter)
    """
    if products_db:
        deleted_product = products_db.pop()
        return {"message": f"Sản phẩm '{deleted_product['name']}' đã được xóa thành công", "data": deleted_product}
    raise HTTPException(status_code=404, detail="Không có sản phẩm nào để xóa.")

@app.get("/products/statistics", tags=["Sản Phẩm"])
async def get_product_statistics():
    """
    Xem thống kê tổng quan về các sản phẩm.
    """
    total_products = len(products_db)
    total_stock_value = sum(p["price"] * p["stock"] for p in products_db)
    categories = {}
    for p in products_db:
        categories[p["category"]] = categories.get(p["category"], 0) + 1

    return {
        "message": "Thống kê sản phẩm",
        "data": {
            "total_products": total_products,
            "total_stock_value": round(total_stock_value, 2),
            "product_categories": categories,
            "description": "Đây là thống kê sơ bộ về số lượng sản phẩm và giá trị tồn kho."
        }
    }

# --- Extended Endpoints ---

@app.get("/products/low-stock", tags=["Sản Phẩm Mở Rộng"])
async def get_low_stock_products():
    """
    Lấy danh sách các sản phẩm có số lượng tồn kho thấp (ví dụ: dưới 20).
    """
    low_stock_threshold = 20
    low_stock_products = [p for p in products_db if p["stock"] < low_stock_threshold]
    return {
        "message": f"Danh sách sản phẩm tồn kho thấp (dưới {low_stock_threshold} đơn vị)",
        "data": low_stock_products
    }

@app.get("/products/popular", tags=["Sản Phẩm Mở Rộng"])
async def get_popular_products():
    """
    Lấy danh sách các sản phẩm được coi là phổ biến.
    (Hiện tại là một danh sách giả định, trong thực tế sẽ dựa trên doanh số/lượt xem)
    """
    # Simulate popular products based on some criteria, e.g., high stock, or just a fixed list
    popular_products_sample = [products_db[0], products_db[1]] if len(products_db) >= 2 else products_db
    return {
        "message": "Danh sách sản phẩm phổ biến (ví dụ)",
        "data": popular_products_sample
    }