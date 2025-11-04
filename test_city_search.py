def test_query_is_star_returns_all_cities():
    result = city_search("*")
    assert result == CITIES

