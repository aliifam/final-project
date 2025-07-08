#!/bin/bash

msg="revisi skripsi $(date '+%Y-%m-%d %H:%M:%S')"
if [ $# -eq 1 ]; then
    msg="$1"
fi

git add .
git commit -m "$msg"
git push