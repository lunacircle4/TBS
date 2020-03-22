#!/bin/sh

# volume 초기화
#rm -rf db/volume

# development image build
echo "1. development image build"
docker-compose -f dev.yml build

# migrate
echo "2. db migrate"
docker-compose -f dev.yml up -d db
docker-compose -f dev.yml run --entrypoint="sh ./init.sh" api

# finish
docker-compose -f dev.yml down
echo "development environment finished!"
