from hex_converter.converter import get_conversions

def test_float32():
    # 42BB6E98 = 93.71600341796875 (float32 big-endian)
    conv = get_conversions("42BB6E98")
    f_big, f_mid, f_little = conv["Float 32-bit"]
    print("Valori obținute:", f_big, f_mid, f_little)
    assert abs(f_big - 93.71600341796875) < 1e-5
    assert isinstance(f_mid, float)
    assert isinstance(f_little, float)

def test_ascii():
    conv = get_conversions("48656C6C6F")
    assert conv["ASCII"][0].endswith("Hello") or conv["ASCII"][2].startswith("o")

if __name__ == "__main__":
    test_float32()
    test_ascii()
    print("All tests passed.")
    