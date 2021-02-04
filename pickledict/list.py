# Read-only methods are commented out

class SerializedList(list):
    # def __add__(self, *args, **kwargs):
    #     super().__add__(*args, **kwargs)
    #     self.checked_serialize()

    # def __class__(self, *args, **kwargs):
    #     super().__class__(*args, **kwargs)
    #     self.checked_serialize()

    # def __contains__(self, *args, **kwargs):
    #     super().__contains__(*args, **kwargs)
    #     self.checked_serialize()

    # def __delattr__(self, *args, **kwargs):
    #     super().__delattr__(*args, **kwargs)
    #     self.checked_serialize()

    def __delitem__(self, *args, **kwargs):
        r = super().__delitem__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __dir__(self, *args, **kwargs):
    #     super().__dir__(*args, **kwargs)
    #     self.checked_serialize()

    # def __doc__(self, *args, **kwargs):
    #     super().__doc__(*args, **kwargs)
    #     self.checked_serialize()

    # def __eq__(self, *args, **kwargs):
    #     super().__eq__(*args, **kwargs)
    #     self.checked_serialize()

    # def __format__(self, *args, **kwargs):
    #     super().__format__(*args, **kwargs)
    #     self.checked_serialize()

    # def __ge__(self, *args, **kwargs):
    #     super().__ge__(*args, **kwargs)
    #     self.checked_serialize()

    # def __getattribute__(self, *args, **kwargs):
    #     super().__getattribute__(*args, **kwargs)
    #     self.checked_serialize()

    # def __getitem__(self, *args, **kwargs):
    #     super().__getitem__(*args, **kwargs)
    #     self.checked_serialize()

    # def __gt__(self, *args, **kwargs):
    #     super().__gt__(*args, **kwargs)
    #     self.checked_serialize()

    # def __hash__(self, *args, **kwargs):
    #     super().__hash__(*args, **kwargs)
    #     self.checked_serialize()

    def __iadd__(self, *args, **kwargs):
        r = super().__iadd__(*args, **kwargs)
        self.checked_serialize()
        return r

    def __imul__(self, *args, **kwargs):
        r = super().__imul__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.checked_serialize()

    # def __init_subclass__(self, *args, **kwargs):
    #     super().__init_subclass__(*args, **kwargs)
    #     self.checked_serialize()

    # def __iter__(self, *args, **kwargs):
    #     super().__iter__(*args, **kwargs)
    #     self.checked_serialize()

    # def __le__(self, *args, **kwargs):
    #     super().__le__(*args, **kwargs)
    #     self.checked_serialize()

    # def __len__(self, *args, **kwargs):
    #     super().__len__(*args, **kwargs)
    #     self.checked_serialize()

    # def __lt__(self, *args, **kwargs):
    #     super().__lt__(*args, **kwargs)
    #     self.checked_serialize()

    def __mul__(self, *args, **kwargs):
        r = super().__mul__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __ne__(self, *args, **kwargs):
    #     super().__ne__(*args, **kwargs)
    #     self.checked_serialize()

    # def __new__(self, *args, **kwargs):
    #     super().__new__(*args, **kwargs)
    #     self.checked_serialize()

    # def __reduce__(self, *args, **kwargs):
    #     super().__reduce__(*args, **kwargs)
    #     self.checked_serialize()

    # def __reduce_ex__(self, *args, **kwargs):
    #     super().__reduce_ex__(*args, **kwargs)
    #     self.checked_serialize()

    # def __repr__(self, *args, **kwargs):
    #     super().__repr__(*args, **kwargs)
    #     self.checked_serialize()

    # def __reversed__(self, *args, **kwargs):
    #     super().__reversed__(*args, **kwargs)
    #     self.checked_serialize()

    def __rmul__(self, *args, **kwargs):
        r = super().__rmul__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __setattr__(self, *args, **kwargs):
    #     super().__setattr__(*args, **kwargs)
    #     self.checked_serialize()

    def __setitem__(self, *args, **kwargs):
        r = super().__setitem__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __sizeof__(self, *args, **kwargs):
    #     super().__sizeof__(*args, **kwargs)
    #     self.checked_serialize()

    # def __str__(self, *args, **kwargs):
    #     super().__str__(*args, **kwargs)
        # self.checked_serialize()

    # def __subclasshook__(self, *args, **kwargs):
    #     super().__subclasshook__(*args, **kwargs)
    #     self.checked_serialize()

    def append(self, *args, **kwargs):
        r = super().append(*args, **kwargs)
        self.checked_serialize()
        return r

    def clear(self, *args, **kwargs):
        r = super().clear(*args, **kwargs)
        self.checked_serialize()
        return r

    # def copy(self, *args, **kwargs):
    #     super().copy(*args, **kwargs)
    #     self.checked_serialize()

    def count(self, *args, **kwargs):
        r = super().count(*args, **kwargs)
        self.checked_serialize()
        return r

    def extend(self, *args, **kwargs):
        r = super().extend(*args, **kwargs)
        self.checked_serialize()
        return r

    def index(self, *args, **kwargs):
        r = super().index(*args, **kwargs)
        self.checked_serialize()
        return r

    def insert(self, *args, **kwargs):
        r = super().insert(*args, **kwargs)
        self.checked_serialize()
        return r

    def pop(self, *args, **kwargs):
        r = super().pop(*args, **kwargs)
        self.checked_serialize()
        return r

    def remove(self, *args, **kwargs):
        r = super().remove(*args, **kwargs)
        self.checked_serialize()
        return r

    def reverse(self, *args, **kwargs):
        r = super().reverse(*args, **kwargs)
        self.checked_serialize()
        return r

    def sort(self, *args, **kwargs):
        r = super().sort(*args, **kwargs)
        self.checked_serialize()
        return r
