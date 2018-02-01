#!/bin/bash
#batch -p short
#SBATCH -o jingsi_midterm%j.out
#SBATCH -N 4
#SBATCH -J jingsi_midterm
#SBATCH -t 00:30:00

module load openmpi/1.8/gcc/4.9.2/cpu
module load python/2.7.6


mpirun -n 4 python mid_2_1.py 
