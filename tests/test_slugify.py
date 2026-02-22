from tvbridge.utils.slugify import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation():
    assert slugify("PLONK: universal SNARK!") == "plonk-universal-snark"


def test_collapses_dashes():
    assert slugify("foo  --  bar") == "foo-bar"


def test_strips_edges():
    assert slugify("  --hi--  ") == "hi"


def test_empty():
    assert slugify("") == ""
    assert slugify(None) == ""



def test_diacritics_pass_through():
    out = slugify("Zürich übung")
    assert "z" in out and "rich" in out
    assert " " not in out
