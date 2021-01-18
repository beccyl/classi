from base import Gatk4SamToFastqBase
from janis_bioinformatics.tools.gatk4.versions import Gatk_4_1_4_0


class Gatk4SamToFastq_4_1_4(Gatk_4_1_4_0, Gatk4SamToFastqBase):
    pass


Gatk4SamToFastqLatest = Gatk4SamToFastq_4_1_4

if __name__ == "__main__":
    print(Gatk4SamToFastq_4_1_4().help())
