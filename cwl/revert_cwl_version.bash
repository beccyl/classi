#!/usr/bin/env bash
unameOut="$(uname -s)"
extraOps=()
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac
        extraOps=('')
        ;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac
#echo ${machine}

find . -name \*.cwl -exec sed -i "${extraOps[@]}" 's/v1\.2/v1\.0/' '{}' \;
