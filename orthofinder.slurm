#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --time=24:00:00
#SBATCH --mem=128G
#SBATCH --job-name=orthofinder
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=gk2319@nyu.edu
#SBATCH --output=slurm_%j.out
#SBATCH --error=slurm_%j.err

module purge
module load orthofinder/2.5.4

DATADIR="/scratch/$USER/orthofinderProject/orthofinderInput"

ls -lh "$DATADIR"/*.fa

python /share/apps/orthofinder/2.5.4/orthofinder.py -f "$DATADIR" -t "$SLURM_CPUS_PER_TASK"