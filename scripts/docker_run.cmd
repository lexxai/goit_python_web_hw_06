@echo off
PUSHD ..\tests

docker run -it --rm  -v web_hw_06_volume:/app/db  --name web_hw_06  lexxai/web_hw_06

rem docker volume ls
                    

POPD