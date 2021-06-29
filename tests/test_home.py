import pytest
@pytest.mark.nondestructive
def test_title(selenium, base_url):
    selenium.get(base_url)
    assert selenium.title == "Python Barranquilla"

@pytest.mark.nondestructive
def test_main_heading(selenium, base_url):
    selenium.get(base_url)
    assert selenium.find_element_by_tag_name('h1').text == "Python Barranquilla."

