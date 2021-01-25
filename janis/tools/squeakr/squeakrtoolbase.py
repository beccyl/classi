from abc import ABC, abstractmethod
from janis_bioinformatics.tools import BioinformaticsTool

class SqueakrToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "squeakr"

    @classmethod
    @abstractmethod
    def squeakr_command(cls):
        raise Exception(
            "Subclass must implement the squeakr_command method: expects one of: ["
            "   count, query, inner_prod, list, info, help"
            "]"
        )

    @classmethod
    def base_command(cls):
        return ["squeakr", cls.squeakr_command()]

    def inputs(self):
        return []

    def doc(self):
        return """
        Squeakr is a k-mer-counting and multiset-representation system using the recently-introduced
        counting quotient filter (CQF) Pandey et al. (2017), a feature-rich approximate membership
        query (AMQ) data structure.

        Squeakr is memory-efficient, consuming 1.5X–4.3X less memory than the state-of-the-art. It
        offers competitive counting performance, in fact, it is faster for larger k-mers, and
        answers queries about a particular k-mer over an order-of- magnitude faster than other
        systems. The Squeakr representation of the k-mer multiset turns out to be immediately
        useful for downstream processing (e.g., De Bruijn graph traversal) because it supports fast
        queries and dynamic k-mer insertion, deletion, and modification.

        Documentation:  https://github.com/splatlab/squeakr#readme""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the squeakr classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference squeakrbase subclasses, "
            "and the subclass must contain a definition for docker."
        )

    def arguments(self):
        return []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module="squeakr")

