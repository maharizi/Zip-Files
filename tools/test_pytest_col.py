import os
import pytest as pytest
from dotenv import load_dotenv
from tools.col import Col
import log_manage

load_dotenv("C:\\Users\\User\\PycharmProjects\\Files\\tools\\numbers\\.env")
l = log_manage.Log_manage()
l.open_file()


@pytest.fixture
def col():
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: init simp class
            Return: Null"""
    return Col()


@pytest.mark.test_compress
def test_compress(col):
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: test adding function
            Return: Null"""
    try:
        assert col.compress(os.getenv('FILES').split(',')) == True
        l.write_to_log(os.getenv('COMPRESS'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('COMPRESS'), str(e))
