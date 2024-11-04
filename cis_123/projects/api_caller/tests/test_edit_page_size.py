from classes.sites import Site
site = Site("test")


def test_edit_page_size_integer(monkeypatch):
    inputs = iter(["y",10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    site.edit_page_size()
    assert site.page_size == 10
    
# def test_edit_page_size_integer(monkeypatch):
#     inputs = iter(["y", 't', 5])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
#     site.edit_page_size()
#     assert site.page_size == 5

# def test_edit_page_size_integer(monkeypatch):
#     inputs = iter(["y",10])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
#     site.edit_page_size()
#     assert site.page_size == 10

# def test_edit_page_size_integer(monkeypatch):
#     inputs = iter(["y",10])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
#     site.edit_page_size()
#     assert site.page_size == 10