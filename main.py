from tools.col import Col
from tools.numbers.comp import Comp
from tools.numbers.simp import Simp

if __name__ == '__main__':
    s = Simp()
    print(s.adding(2, 4))
    print(s.subtracting(2, 4))
    c = Comp()
    print(c.sum_of_digits(1234))
    print(c.is_pal(123321))
    c2 = Col()
    files = ['comp.py', 'simp.py']
    c2.compress(files)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
