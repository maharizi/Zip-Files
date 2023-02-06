import os
import pytest as pytest
from dotenv import load_dotenv
import log_manage
from tools.numbers import simp
from tools.numbers.comp import Comp

load_dotenv()
l = log_manage.Log_manage()
l.open_file()


@pytest.fixture
def comp():
    """Author: Maor Maharizi,
            Created: 01.02.2023,
            Detail: init comp class
            Return: Null"""
    return Comp()


@pytest.mark.test_sum_of_digits
def test_sum_of_digits(comp):
    """Author: Maor Maharizi,
                Created: 01.02.2023,
                Detail: test sum of digits function
                Return: Null"""
    simp.Simp.flag = True
    try:
        assert comp.sum_of_digits(int(os.getenv('ARG_SUM_OF_DIGITS'))) == int(os.getenv('RESULT_SUM_OF_DIGITS'))
        l.write_to_log(os.getenv('SUM_OF_DIGITS'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('SUM_OF_DIGITS'), str(e))


@pytest.mark.test_subtracting
def test_subtracting(comp):
    """Author: Maor Maharizi,
                Created: 01.02.2023,
                Detail: test is pal function
                Return: Null"""
    simp.Simp.flag = True
    try:
        assert comp.is_pal(int(os.getenv('ARG_IS_PAL'))) == True
        l.write_to_log(os.getenv('IS_PAL'), os.getenv('PASS_MESSAGE'))
    except Exception as e:
        l.write_to_log(os.getenv('IS_PAL'), str(e))
