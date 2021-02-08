import janis_core as j

from janis_core import Array, File
from janis_bioinformatics.data_types import FastqGz

from ntcard.versions import NtCardLatest
from squeakr.lognumslots.versions import LogNumSlotsLatest
from squeakr.count.versions import SqueakrCountLatest

class FastqToSqueakr(j.Workflow):
    def id(self):
        return "fastq_to_squeakr"
    def id(self):
        return "fastq_to_squeakr"

    def friendly_name(self):
        return "Fastq To Squeakr"

    def constructor(self):
        self.input("kmer_size", int)
        self.input("cutoff", int)
        self.input("inp", Array(FastqGz()))

        self.step("nt_card", NtCardLatest(kmer=self.kmer_size, prefix="./", files=self.inp))
        self.step("lognumslots", LogNumSlotsLatest(ntcard_hist=self.nt_card.out))
        self.step("squeakr_count",
            SqueakrCountLatest(
                kmer_size=self.kmer_size,
                cutoff=self.cutoff,
                input_list=self.inp,
                exact=True,
                no_counts=True,
                log_slots=self.lognumslots.out.contents().as_int(),
                num_threads=1,
                #out_file="./generated.squeakr"
            )
        )
        self.output("out", source=self.squeakr_count.out)

if __name__ == "__main__":
    FastqToSqueakr().translate("cwl")
