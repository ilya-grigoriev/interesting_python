class A(dict):
    def __getitem__(self, __key) -> int:
        return 52


a = A(b=100)
print(a)
print(a['b'])   # There is 52
print(a.get('b'))   # There is no 52
print(a.pop('b'))   # There is no 52
