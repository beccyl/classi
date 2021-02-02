from .base import MantisMstBase
from ..versions import Mantis_0_1


class MantisMst_0_1(Mantis_0_1, MantisMstBase):
    pass


MantisMstLatest = MantisMst_0_1

if __name__ == "__main__":
    print(MantisMst_0_1().help())
