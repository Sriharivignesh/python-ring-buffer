#!/bin/bash

pip install -U pip
pip install -r test_requirements.txt
pytest --cache-clear --durations=0 --color=yes --cov=ring_buffer/
