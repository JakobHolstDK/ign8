#!/usr/bin/env bash

git pull
git checkout staging
pip install .

ign8 service


