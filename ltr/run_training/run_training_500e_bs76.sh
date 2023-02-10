
#!/usr/bin/env bash

set -x

TRAIN_MOUDLE='transt'
TRAIN_NAME='transt_light_500e_bs76'

# PYTHONPATH="$(dirname $0)/../..":$PYTHONPATH \

python -u ltr/run_training.py --train_module ${TRAIN_MOUDLE} --train_name=${TRAIN_NAME}
