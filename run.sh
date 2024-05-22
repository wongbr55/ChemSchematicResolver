#!/usr/local/bin/bash
conda activate chemschematicresolver
python substrate_extraction.py --path $1
conda deactivate
conda activate rde2
python reactiondataextractor/extract.py --path $1 --output_dir ./
