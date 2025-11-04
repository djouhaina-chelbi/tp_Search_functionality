def test_case_insensitive_prefix_search():
    result = search_cities("ou")
    assert "El Oued" in result
    assert "Ouargla" in result
    assert len(result) == 2