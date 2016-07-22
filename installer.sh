#!/usr/bin/env bash

tmp_dir=$HOME/.cwlogs-$RANDOM
## Clone the repo
git clone https://github.com/wusung/cwlogs.git $tmp_dir|| { echo >&2 "Clone failed with $?"; exit 1; }
pushd $tmp_dir
pip install -r $tmp_dir/requirements.txt
popd
