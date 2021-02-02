from .base import SqueakrQueryBase
from ..versions import Squeakr_0_7, Squeakr_master


class SqueakrQuery_0_7(Squeakr_0_7, SqueakrQueryBase):
    pass

class SqueakrQuery_master(Squeakr_master, SqueakrQueryBase):
    pass

SqueakrQueryLatest = SqueakrQuery_master

if __name__ == "__main__":
    print(SqueakrQuery_master().help())
