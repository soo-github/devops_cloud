from . import revrse_string

def test_reverse_string():
    assert revrse_string.check_available("거꾸로 : 안녕")
    assert revrse_string.make_response("거꾸로 : 안녕") == "녕안"