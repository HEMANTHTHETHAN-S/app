from app.utils import random_string, random_words


def test_random_words():
    s = random_words()
    assert len(s) > 0


def test_random_string():
    s = random_string()
    assert len(s) > 0


def test_parse_environment():
    from app.config import parse_environment

    array = parse_environment('["word_1", "word_2"]')
    assert array == ["word_1", "word_2"]
    env_tuple = parse_environment('("word_1", "word_2")')
    assert env_tuple == ("word_1", "word_2")
    env_list_tuple = parse_environment('[(10, "domain_1")]')
    assert [(10, "domain_1")] == env_list_tuple
    failed_python_object = parse_environment("a")
    assert failed_python_object is None
