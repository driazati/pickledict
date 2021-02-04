# Read-only methods are commented out

class SerializedDict(dict):
    # def __class__(self, *args, **kwargs):
    #     super().__class__(*args, **kwargs)
    #     self.checked_serialize()

    # def __contains__(self, *args, **kwargs):
    #     super().__contains__(*args, **kwargs)
    #     self.checked_serialize()

    def __delattr__(self, *args, **kwargs):
        super().__delattr__(*args, **kwargs)
        self.checked_serialize()

    def __delitem__(self, *args, **kwargs):
        super().__delitem__(*args, **kwargs)
        self.checked_serialize()

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

    # def __setattr__(self, *args, **kwargs):
    #     super().__setattr__(*args, **kwargs)
    #     self.checked_serialize()

    def __setitem__(self, *args, **kwargs):
        super().__setitem__(*args, **kwargs)
        self.checked_serialize()

    # def __sizeof__(self, *args, **kwargs):
    #     super().__sizeof__(*args, **kwargs)
    #     self.checked_serialize()

    # def __str__(self, *args, **kwargs):
    #     super().__str__(*args, **kwargs)
    #     self.checked_serialize()

    # def __subclasshook__(self, *args, **kwargs):
    #     super().__subclasshook__(*args, **kwargs)
    #     self.checked_serialize()

    def clear(self, *args, **kwargs):
        super().clear(*args, **kwargs)
        self.checked_serialize()

    # def copy(self, *args, **kwargs):
    #     super().copy(*args, **kwargs)
    #     self.checked_serialize()

    # def fromkeys(self, *args, **kwargs):
    #     super().fromkeys(*args, **kwargs)
    #     self.checked_serialize()

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        self.checked_serialize()

    # def items(self, *args, **kwargs):
    #     super().items(*args, **kwargs)
    #     self.checked_serialize()

    # def keys(self, *args, **kwargs):
    #     super().keys(*args, **kwargs)
    #     self.checked_serialize()

    def pop(self, *args, **kwargs):
        super().pop(*args, **kwargs)
        self.checked_serialize()

    def popitem(self, *args, **kwargs):
        super().popitem(*args, **kwargs)
        self.checked_serialize()

    def setdefault(self, *args, **kwargs):
        super().setdefault(*args, **kwargs)
        self.checked_serialize()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.checked_serialize()

    # def values(self, *args, **kwargs):
    #     super().values(*args, **kwargs)
    #     self.checked_serialize()
