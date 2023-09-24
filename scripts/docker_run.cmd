@echo off
PUSHD ..\tests

docker run -it -d --rm  -v web_hw_06_volume:/app/db  --name web_hw_06  lexxai/web_hw_06

docker volume ls
                    

POPD