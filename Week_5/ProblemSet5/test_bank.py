from Week_5.ProblemSet5.bank import value

def test_h():
    assert value("H") == 20
    assert value("hh") == 20
    assert value("hiwhatsup") == 20

def test_hello():
    assert value("hellooooo") == 0
    assert value("HELLOO") == 0

def test_other():
    assert value("yo12323") == 100
    assert value("100") == 100
    assert value("yuh") == 100
