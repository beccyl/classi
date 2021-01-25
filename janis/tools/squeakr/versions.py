from abc import ABC

class Squeakr_0_7(ABC):
    def container(self):
        return "beccyl/squeakr:0.7"

    def version(self):
        return "0.7"

class Squeakr_master(ABC):
    def container(self):
        return "beccyl/squeakr:master_0d58134"

    def version(self):
        return "master_0d58134"
