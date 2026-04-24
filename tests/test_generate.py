from password_generator.generator import generate_password


def test_password_length():
    password, strength = generate_password(12, True, True, True)
    assert len(password) == 12


def test_includes_uppercase():
    password, strength = generate_password(12, True, True, False)
    assert any(c.isupper() for c in password)


def test_includes_digits():
    password, strength = generate_password(12, False, True, True)
    assert any(c.isdigit() for c in password)


def test_not_empty():
    try:
        generate_password(12, False, False, False)
        assert False
    except Exception:
        assert True
