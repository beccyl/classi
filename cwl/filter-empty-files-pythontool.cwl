#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
label: FilterEmptyFiles
doc: ''

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: FilterEmptyFiles-script.py
    entry: |2

      import argparse, json, sys
      from typing import Optional, List, Dict, Any
      cli = argparse.ArgumentParser("Argument parser for Janis PythonTool")
      cli.add_argument("--files", nargs='+', default=[], type=str)

      Array = List
      String = str
      Filename = str
      Int = int
      Float = float
      Double = float
      Boolean = str
      File = str
      Directory = str
      Stdout = str
      Stderr = str
      class PythonTool:
          File = str
          Directory = str



      def code_block(files: List[File]):
          import os
          return {
              "outfiles": [f for f in files if os.stat(f).st_size > 200]
          }


      try:
          args = cli.parse_args()
          result = code_block(files=args.files)

          from os import getcwd, path
          cwd = getcwd()
          def prepare_file_or_directory_type(file_or_directory, value):
              if value is None:
                  return None
              if isinstance(value, list):
                  return [prepare_file_or_directory_type(file_or_directory, v) for v in value]
              return {
                  "class": file_or_directory,
                  "path": path.join(cwd, value)
              }
          result["outfiles"] = prepare_file_or_directory_type("File", result["outfiles"])
          print(json.dumps(result))
      except Exception as e:
          print(str(e), file=sys.stderr)
          raise
- class: InlineJavascriptRequirement
- class: DockerRequirement
  dockerPull: python:3.8.1

inputs:
- id: files
  label: files
  type:
    type: array
    items: File
  inputBinding:
    prefix: --files

outputs:
- id: outfiles
  label: outfiles
  type:
    type: array
    items: File
stdout: cwl.output.json
stderr: python-capture.stderr

baseCommand:
- python
- FilterEmptyFiles-script.py
id: FilterEmptyFiles
