from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_input_format():
    try:
        convert("2/0")
        assert False, "ZeroDivisionError"
    except ZeroDivisionError:
        pass

    try:
        convert("-1/4")
        assert False, "ValueError"
    except ValueError:
        pass
