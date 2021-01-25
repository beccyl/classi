from .base import NtCardToolBase

class NtCard_1_2_2(NtCardToolBase):
    def container(self):
        #return "quay.io/biocontainers/ntcard:1.2.2--he513fc3_0"
        return "beccyl/ntcard:1.2.2"

    def version(self):
        return "1.2.2"


NtCardLatest = NtCard_1_2_2
