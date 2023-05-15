def func(val):
    return val + 5

def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper()

class A:
    field = 5
    def test1(self):
        return self.field-5

    @staticmethod
    def static_test1():
        return A.field

class B:
    message="I'm class B"

    def test2(self):
        return B.message

class C(A, B):
    pass