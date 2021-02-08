from .base import LogNumSlotsBase
from ..versions import Squeakr_0_7, Squeakr_master


class LogNumSlots_0_7(Squeakr_0_7, LogNumSlotsBase):
    pass

class LogNumSlots_master(Squeakr_master, LogNumSlotsBase):
    pass

LogNumSlotsLatest = LogNumSlots_master

if __name__ == "__main__":
    print(LogNumSlots_master().help())
