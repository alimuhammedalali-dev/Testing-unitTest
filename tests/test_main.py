import pytest
from src.main import *
from unittest.mock import MagicMock
# Simple function 1
def test_calculate_total_success():
    assert calculate_total(100, 15) == 115

def test_calculate_total_negative_values():
    expected_error = "error: price and tax cannot be negative"
    
    assert calculate_total(-100, 15) == expected_error
    assert calculate_total(100, -5) == expected_error
    
# Simple function 2
@pytest.mark.parametrize(
    "password, expected_output",
    [
        #حالة ناجحة
        ("password123", "password123"), 
        #حالة طول قصير
        ("pass", "password must be at least 8 characters long"), 
        #حالة غياب أرقام
        ("password", "password must contain at least one digit"), 
        #حالة ناجحة
        ("12345678", "12345678"), 
        #حالة ناجحة
        ("pass1234", "pass1234"), 
        #حالة طول قصير
        ("short1", "password must be at least 8 characters long"), 
        #حالة غياب أرقام  
        ("longpasswordwithoutdigit", "password must contain at least one digit"), 
    ]
)
def test_is_secure_password(password, expected_output):
    assert is_secure_password(password) == expected_output

# Complex function 1
# create a facke user collection to simulate the database
@pytest.fixture
def mock_collection():
    collection = MagicMock()
    collection.find_one.return_value = {
        "username": "ali", 
        "password": "secure123", 
        "role": "admin"
    }
    return collection

@pytest.mark.parametrize(
    "username_in, password_in, role_in, expected_output",
    [
        # باسوورد صح
        ("ali", "secure123", None, "Authenticated successfully"), 
        # باسوورد غلط
        ("ali", "wrong_pwd", None, "Invalid password"), 
        # دور صح
        ("ali", None, "admin", "Authorized as admin"),
        # دور غلط
        ("ali", None, "user", "Role mismatch"), 
        # ناقص
        ("ali", None, None, "Missing password or role") 
    ]
)
def test_check_user_access_cases(mock_collection, username_in, password_in, role_in, expected_output):
    
    result = check_user_access(mock_collection, username_in, password=password_in, role=role_in)
    assert result == expected_output

def test_user_not_found():
    no_user_collection = MagicMock()
    no_user_collection.find_one.return_value = None 
    
    result = check_user_access(no_user_collection, "unknown_user", password="123")
    assert result == "User not found"