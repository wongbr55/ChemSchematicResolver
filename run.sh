#!/usr/local/bin/bash
conda activate chemschematicresolver
python ./image_extractor/substrate_extraction.py --path $1
conda deactivate
conda activate rde2
python reactiondataextractor/extract.py --path ./reaction.jpeg --output_dir ./
