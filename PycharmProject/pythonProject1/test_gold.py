from unittest import TestCase


class trytesting (TestCase) :
    def fun(self):
        a=3
        b=5
        c=a+b
        if c==15 :
            print('good working')
        else:
             print('fail')
