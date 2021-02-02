from typing import List
from janis_core import File, PythonTool, Array, TOutput

class FilterEmptyFiles(PythonTool):
    @staticmethod
    def code_block(files: List[File]):
        import os
        return {
            "outfiles": [f for f in files if os.stat(f).st_size > 200]  ## not zero but 200, for "empty" gz
        }

    def outputs(self):
        return [TOutput("outfiles", Array(File))]

if __name__ == "__main__":
	FilterEmptyFiles().translate("wdl")
