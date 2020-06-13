from ciphers.caeser_cipher import CaeserCipher


def test_caeser_cipher_encrypt_default_rotation():
    cipher = CaeserCipher()
    input_string = "abc"
    output_string = cipher.encrypt(plain_text=input_string)
    assert output_string == "m.p"


def test_caeser_cipher_decrypt_default_rotation():
    cipher = CaeserCipher()
    input_string = "m.p"
    output_string = cipher.decrypt(encrypted=input_string)
    assert output_string == "abc"


def test_caeser_cipher_encrypt_custom_rotation():
    cipher = CaeserCipher(rotation=1)
    input_string = "abc"
    output_string = cipher.encrypt(plain_text=input_string)
    assert output_string == "~01"


def test_caeser_cipher_decrypt_custom_rotation():
    cipher = CaeserCipher(rotation=1)
    input_string = "~01"
    output_string = cipher.decrypt(encrypted=input_string)
    assert output_string == "abc"

