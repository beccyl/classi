import janis_core as j

from janis_core import Array, File
from janis_bioinformatics.data_types import Bam

from ntcard.versions import NtCardLatest
from squeakr.lognumslots.versions import LogNumSlotsLatest
from squeakr.count.versions import SqueakrCountLatest
from gatk4.samtofastq.versions import Gatk4SamToFastqLatest
from classi.filteremptyfiles import FilterEmptyFiles

class BamToSqueakr(j.Workflow):
     def id(self):
         return "bam_to_squeakr"
     def id(self):
         return "bam_to_squeakr"

     def friendly_name(self):
         return "Bam To Squeakr"

     def constructor(self):
         self.input("kmer_size", int)
         self.input("cutoff", int)
         self.input("inp", Bam())
         self.step("samtofastq",
                 Gatk4SamToFastqLatest(
                     inp=self.inp,
                     validation_stringency="LENIENT" ))

         self.step("filterfiles", FilterEmptyFiles(files=self.samtofastq.out))

         self.step("nt_card", NtCardLatest(kmer=self.kmer_size, prefix="./", files=self.filterfiles.outfiles))

         self.step("lognumslots", LogNumSlotsLatest(ntcard_hist=self.nt_card.out))

         self.step("squeakr_count",
             SqueakrCountLatest(
                 kmer_size=self.kmer_size,
                 cutoff=self.cutoff,
                 input_list=self.filterfiles.outfiles,
                 exact=True,
                 no_counts=True,
                 log_slots=self.lognumslots.out.contents().as_int(),
                 num_threads=1,
                 out_file="./output.squeakr"
             ))
         self.output("out", source=self.squeakr_count.out)

     def metadata(self):
         self.metadata.author = "Rebecca Evans"
         self.metadata.version = "v1.0.0"
         self.metadata.documentation = "A tool that converts a bam file to squeakr output"


if __name__ == "__main__":
    BamToSqueakr().translate("cwl")

