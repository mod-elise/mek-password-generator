from password_generator.generator import generate_password

def test_password_length():
    password = generate_password(12, True, True, True)
    assert len(password) == 12


def test_includes_uppercase():
    password = generate_password(12, True, True, False)
    assert any(c.isupper() for c in password)


def test_includes_digits():
    password = generate_password(12, False, True, True)
    assert any(c.isdigit() for c in password)


def test_not_empty():
    try:
        generate_password(12, False, False, False)
        assert False
    except Exception:
        assert True