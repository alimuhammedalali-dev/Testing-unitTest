from src.main import calculate_total

def test_calculate_total_success():
    assert calculate_total(100, 15) == 115

def test_calculate_total_negative_values():
    expected_error = "error: price and tax cannot be negative"
    
    assert calculate_total(-100, 15) == expected_error
    assert calculate_total(100, -5) == expected_error
