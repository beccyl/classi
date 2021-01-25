from .base import SqueakrCountBase
from ..versions import Squeakr_0_7, Squeakr_master


class SqueakrCount_0_7(Squeakr_0_7, SqueakrCountBase):
    pass

class SqueakrCount_master(Squeakr_master, SqueakrCountBase):
    pass

SqueakrCountLatest = SqueakrCount_master

if __name__ == "__main__":
    print(SqueakrCount_master().help())
