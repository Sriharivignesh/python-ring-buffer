#!/bin/bash

pip install -U pip
pip install -r test_requirements.txt

rm -rf ring_buffer/*.pyc ring_buffer/__pycache__ test/*.pyc test/__pycache__
pytest --cache-clear --durations=0 --color=yes --cov=ring_buffer/
rm -rf ring_buffer/*.pyc ring_buffer/__pycache__ test/*.pyc test/__pycache__

