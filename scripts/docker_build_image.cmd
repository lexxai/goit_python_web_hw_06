@echo off
PUSHD ..

docker build . -t lexxai/web_hw_06
docker images

POPD