from grades import letter_grade

def test_boundary_a_grade():
    assert letter_grade(80) == 'A' #exactly at boundary
    assert letter_grade(79) == 'B' #just below boundary

def test_boundary_pass_fail():
    assert letter_grade(60) == 'C' #lowest pass
    assert letter_grade(59) == 'F' #just failed

def test_minimum_valid():
    assert letter_grade(0) == 'F' #minimum valid score

def test_maximum_valid():
    assert letter_grade(100) == 'A' #maximum valid score

def test_below_minimum_invalid():
    assert letter_grade(-1) == 'Invalid score' #below minimum valid score

