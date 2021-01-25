from .base import MantisBuildBase
from ..versions import Mantis_0_1


class MantisBuild_0_1(Mantis_0_1, MantisBuildBase):
    pass


MantisBuildLatest = MantisBuild_0_1

if __name__ == "__main__":
    print(MantisBuild_0_1().help())
