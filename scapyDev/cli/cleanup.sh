#!/bin/bash

set -eou pipefail
readarray -t array <<< $(iw dev | grep -E -o "wl[0-9A-Za-z]+mon")
for i in "${array[@]}"
do echo "$i" && airmon-ng stop "$i"
done
