from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("password", "0")

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(235813, 0)

    invalid_index = encrypt_message("password", -1)
    even = encrypt_message("password", 2)
    odd = encrypt_message("password", 3)

    assert invalid_index == "drowssap"
    assert even == "drowss_ap"
    assert odd == "sap_drows"
