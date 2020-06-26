#!/bin/bash
#SBATCH --job-name=naver
#SBATCH --partition=fast
#SBATCH --ntasks=1
#SBATCH --time=22:00:00
#SBATCH --output=output/job-%j.out

source ~/env/bin/activate

echo "Start of Script"


python test.py

echo "End of Script"
