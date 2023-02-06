import os
import pytest as pytest
from dotenv import load_dotenv
from log_manage import Log_manage
from tools.numbers.simp import Simp

load_dotenv()
l = Log_manage()
l.open_file()


@pytest.fixture
def simp():
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: init simp class
            Return: Null"""
    return Simp()


@pytest.mark.test_adding
def test_adding(simp):
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: test adding function
            Return: Null"""
    try:
        assert simp.adding(int(os.getenv('A')), int(os.getenv('B'))) == int(os.getenv('RESULT_ADDING'))
        l.write_to_log(os.getenv('ADDING'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('ADDING'), str(e))


@pytest.mark.test_subtracting
def test_subtracting(simp):
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: test subtracting function
            Return: Null"""
    try:
        assert simp.subtracting(int(os.getenv('A')), int(os.getenv('B'))) == int(os.getenv('RESULT_SUBTRACTING'))
        l.write_to_log(os.getenv('SUBTRACTING'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('SUBTRACTING'), str(e))

