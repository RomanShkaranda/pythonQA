class A:
    var = 'A'

    def method(self):
        print('Method A')


class B:
    var = 'B'

    def method(self):
        print('Method B')


class C(A, B):
    # def method(self):
    #     print('Method C')
    pass


class D(C):
    pass

# d = D()
# d.method()

c = C()
c.method()