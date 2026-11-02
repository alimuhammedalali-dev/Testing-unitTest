# Simple function 1: calculate_total
def calculate_total(price, tax):
    if price < 0 or tax < 0:
        return "error: price and tax cannot be negative"
    total = price + tax
    return total



print(calculate_total(100, 15))      # المتوقع: 115
print(calculate_total(50.5, 5.25))   # المتوقع: 55.75
print(calculate_total(0, 0))   # المتوقع: 0


print(calculate_total(-50, 10))    # المتوقع: رسالة الخطأ
print(calculate_total(100, -5))    # المتوقع: رسالة الخطأ
print(calculate_total(-5.0, -1.0))   # المتوقع: رسالة الخطأ


# Simple function 2: is_secure_password
def is_secure_password(password):
    #  تحقق من الطول
    if len(password) < 8:
        return "password must be at least 8 characters long"
    
    #  تحقق من وجود رقم
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break  
            
    if not has_digit:
        return "password must contain at least one digit"
        
    return password  


# Complex function: check_user_access
def check_user_access(db_collection, username, password=None, role=None):

    # 1. جلب المستخدم من الداتابيز
    user = db_collection.find_one({"username": username})
    if not user:
        return "User not found"
    
    # 2. التحقق من كلمة السر إذا تم تمريرها
    if password is not None:
        if user.get("password") == password:
            return "Authenticated successfully"
        return "Invalid password"
        
    # 3. التحقق من الدور/الصلاحية إذا تم تمريرها
    elif role is not None:
        if user.get("role") == role:
            return f"Authorized as {role}"
        return "Role mismatch"
        
    return "Missing password or role"


