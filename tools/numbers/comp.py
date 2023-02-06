import os
from dotenv import load_dotenv
import log_manage
from tools.numbers.simp import Simp


class Comp(object):
    load_dotenv("C:\\Users\\User\\PycharmProjects\\Files\\.env")
    l = log_manage.Log_manage()
    l.open_file()

    def sum_of_digits(self, number):
        """Author: Maor Maharizi,
                Created: 01.02.2023,
                Detail: calc sun of digits number if user use at least 1 Simp function
                Return: sum of digits numbers"""
        if Simp.flag == True:
            if number == 0:
                return 0
            return number % int(os.getenv('TEN')) + self.sum_of_digits(int(number / int(os.getenv('TEN'))))
        else:
            Comp.l.write_to_log(os.getenv('SUM_OF_DIGITS'), os.getenv('LEAST_1_SIMP_FUNC_MESSAGE'))

    def is_pal(self, number):
        """Author: Maor Maharizi,
                Created: 01.02.2023,
                Detail: check if number is palindrome
                Return: True or False"""
        if Simp.flag == True:
            rev = 0
            temp = number
            while number != 0:
                dig = number % int(os.getenv('TEN'))
                rev = rev * int(os.getenv('TEN')) + dig
                number = number // int(os.getenv('TEN'))
            if temp == rev:
                return True
            else:
                return False
        else:
            Comp.l.write_to_log(os.getenv('IS_PAL'), os.getenv('LEAST_1_SIMP_FUNC_MESSAGE'))
