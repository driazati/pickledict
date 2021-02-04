# Read-only methods are commented out

class SerializedDict(dict):
    # def __class__(self, *args, **kwargs):
    #     r = super().__class__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __contains__(self, *args, **kwargs):
    #     r = super().__contains__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    def __delattr__(self, *args, **kwargs):
        r = super().__delattr__(*args, **kwargs)
        self.checked_serialize()
        return r

    def __delitem__(self, *args, **kwargs):
        r = super().__delitem__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __dir__(self, *args, **kwargs):
    #     r = super().__dir__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __doc__(self, *args, **kwargs):
    #     r = super().__doc__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __eq__(self, *args, **kwargs):
    #     r = super().__eq__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __format__(self, *args, **kwargs):
    #     r = super().__format__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __ge__(self, *args, **kwargs):
    #     r = super().__ge__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __getattribute__(self, *args, **kwargs):
    #     r = super().__getattribute__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __getitem__(self, *args, **kwargs):
    #     r = super().__getitem__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __gt__(self, *args, **kwargs):
    #     r = super().__gt__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __hash__(self, *args, **kwargs):
    #     r = super().__hash__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __init__(self, *args, **kwargs):
    #     r = super().__init__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __init_subclass__(self, *args, **kwargs):
    #     r = super().__init_subclass__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __iter__(self, *args, **kwargs):
    #     r = super().__iter__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __le__(self, *args, **kwargs):
    #     r = super().__le__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __len__(self, *args, **kwargs):
    #     r = super().__len__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __lt__(self, *args, **kwargs):
    #     r = super().__lt__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __ne__(self, *args, **kwargs):
    #     r = super().__ne__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __new__(self, *args, **kwargs):
    #     r = super().__new__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __reduce__(self, *args, **kwargs):
    #     r = super().__reduce__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __reduce_ex__(self, *args, **kwargs):
    #     r = super().__reduce_ex__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __repr__(self, *args, **kwargs):
    #     r = super().__repr__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __reversed__(self, *args, **kwargs):
    #     r = super().__reversed__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __setattr__(self, *args, **kwargs):
    #     r = super().__setattr__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    def __setitem__(self, *args, **kwargs):
        r = super().__setitem__(*args, **kwargs)
        self.checked_serialize()
        return r

    # def __sizeof__(self, *args, **kwargs):
    #     r = super().__sizeof__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __str__(self, *args, **kwargs):
    #     r = super().__str__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def __subclasshook__(self, *args, **kwargs):
    #     r = super().__subclasshook__(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    def clear(self, *args, **kwargs):
        r = super().clear(*args, **kwargs)
        self.checked_serialize()
        return r

    # def copy(self, *args, **kwargs):
    #     r = super().copy(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def fromkeys(self, *args, **kwargs):
    #     r = super().fromkeys(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def get(self, *args, **kwargs):
    #     r = super().get(*args, **kwargs)
    #     self.checked_serialize()
    #     return r

    # def items(self, *args, **kwargs):
    #     r = super().items(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    # def keys(self, *args, **kwargs):
    #     r = super().keys(*args, **kwargs)
    #     self.checked_serialize()
    # return r

    def pop(self, *args, **kwargs):
        r = super().pop(*args, **kwargs)
        self.checked_serialize()
        return r

    def popitem(self, *args, **kwargs):
        r = super().popitem(*args, **kwargs)
        self.checked_serialize()
        return r

    def setdefault(self, *args, **kwargs):
        r = super().setdefault(*args, **kwargs)
        self.checked_serialize()
        return r

    def update(self, *args, **kwargs):
        r = super().update(*args, **kwargs)
        self.checked_serialize()
        return r

    # def values(self, *args, **kwargs):
    #     r = super().values(*args, **kwargs)
    #     self.checked_serialize()
    # return r
