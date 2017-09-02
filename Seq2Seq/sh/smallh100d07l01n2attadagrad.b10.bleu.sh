
#!/bin/bash
#PBS -q isi
#PBS -l walltime=1:00:00
#PBS -l nodes=1:ppn=8

ROOT_DIR=../
PY=$ROOT_DIR/py/run.py
BLEU=$ROOT_DIR/py/util/multi-bleu.perl
MODEL_DIR=$ROOT_DIR/model/smallh100d07l01n2attadagrad
DATA_DIR=$ROOT_DIR/data/small/
TRAIN_PATH_FROM=$DATA_DIR/train.src
TRAIN_PATH_TO=$DATA_DIR/train.tgt
DEV_PATH_FROM=$DATA_DIR/valid.src
DEV_PATH_TO=$DATA_DIR/valid.tgt
TEST_PATH_FROM=$DATA_DIR/test.src
TEST_PATH_TO=$DATA_DIR/test.tgt
DECODE_OUTPUT=$MODEL_DIR/decode_output/b10.output
BLEU_OUTPUT=$MODEL_DIR/decode_output/b10.bleu

source /home/nlg-05/xingshi/sh/init_tensorflow.sh

perl $BLEU -lc $TEST_PATH_TO < $DECODE_OUTPUT > $BLEU_OUTPUT
cat $BLEU_OUTPUT
