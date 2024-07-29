#!/usr/bin/bash
black $1
flake8 $1
isort $1
pylint $1

