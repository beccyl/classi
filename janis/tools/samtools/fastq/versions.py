from .base import SamToolsFastqBase
from janis_bioinformatics.tools.samtools.samtools_1_7 import SamTools_1_7
from janis_bioinformatics.tools.samtools.samtools_1_9 import SamTools_1_9


class SamToolsFastq_1_7(SamTools_1_7, SamToolsFastqBase):
    pass


class SamToolsFastq_1_9(SamTools_1_9, SamToolsFastqBase):
    pass


SamToolsFastqLatest = SamToolsFastq_1_9
