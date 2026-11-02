import pytest
from src.main import *
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


