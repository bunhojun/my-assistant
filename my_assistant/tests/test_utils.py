from ..utils import is_keyword


def test_is_keyword():
    assert is_keyword('OKブンブン') is True
    assert is_keyword('OK ブンブン') is True
    assert is_keyword('OKぶんぶん') is True
    assert is_keyword('OK ぶんぶん') is True
    assert is_keyword('ok ぶんぶん') is True
    assert is_keyword('ok ブンブン') is True
    assert is_keyword('OK') is False
    assert is_keyword('ブンブン') is False
    assert is_keyword('ぶんぶん') is False
    assert is_keyword('こんにちは') is False
