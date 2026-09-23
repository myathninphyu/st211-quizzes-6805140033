def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]
def test_list_contents(): 
    result = [3, 1, 2, 4]
    assert sorted(result) == [1, 2, 3, 4]
def test_dict_equality():
    expected = {"name": "Alice", "age": 30}
    actual = {"age": 30, "name": "Alice"} 
    assert actual == expected
def test_set_operations():
    assert {1, 2, 3, 7, 8} & {2, 3, 4, 7} == {2, 7, 3}