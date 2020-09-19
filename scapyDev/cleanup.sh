#!/bin/bash

set -eou pipefail
readarray -t array <<< $(iw dev | grep -E -o "wl[a-z]+[0-9]mon")
for i in "${array[@]}"
do airmon-ng stop $i
done
