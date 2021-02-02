from .base import MantisQueryBase
from ..versions import Mantis_0_1


class MantisQuery_0_1(Mantis_0_1, MantisQueryBase):
    pass


MantisQueryLatest = MantisQuery_0_1

if __name__ == "__main__":
    print(MantisQuery_0_1().help())
