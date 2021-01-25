from abc import ABC, abstractmethod
from janis_bioinformatics.tools import BioinformaticsTool

class MantisToolBase(BioinformaticsTool, ABC):
    def tool_provider(self):
        return "mantis"

    @classmethod
    @abstractmethod
    def mantis_command(cls):
        raise Exception(
            "Subclass must implement the mantis_command method: expects one of: ["
            "   build, mst, validatemst, query, validate, stats, help"
            "]"
        )

    @classmethod
    def base_command(cls):
        return ["mantis", cls.mantis_command()]

    def inputs(self):
        return []

    def doc(self):
        return """
            Mantis is a space-efficient data structure that can be used to index thousands of raw-
            read experiments and facilitate large-scale sequence searches on those experiments.
            Mantis uses counting quotient filters instead of Bloom filters, enabling rapid index
            builds and queries, small indexes, and exact results, i.e., no false positives or
            negatives. Furthermore, Mantis is also a colored de Bruijn graph representation, so
            it supports fast graph traversal and other topological analyses in addition to large-
            scale sequence-level searches.

            Documentation:  https://github.com/splatlab/mantis#overview""".strip()

    @abstractmethod
    def container(self):
        raise Exception(
            "An error likely occurred when resolving the method order for docker for the mantis classes "
            "or you're trying to execute the docker method of the base class (ie, don't do that). "
            "The method order resolution must preference mantisbase subclasses, "
            "and the subclass must contain a definition for docker."
        )

    def arguments(self):
        return []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tool_module="mantis")

