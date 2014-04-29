UOS_Scripts
===========

Scripts file for Tier3 @ UOS

This directory has files for user to use Tier3@UOS easily.

# create-batch  
This scripts helps user to run batch job with local file.

    
./create-batch  : create pbs jobs
  Mandatory options :
   --jobName  NAME                  Name of job
   --fileList DATA_FILES            File list text file
   --maxFiles N                     Maximum number of files per job
   --cfg      CONFIG_FILE_cfg.py    Configuration file
  Optional :
   -n                               Do not submit jobs to batch
   --scratchDir SCRATCH_DIR         SCRATCH DIRECTORY
   -g                               Grid certificate is required

    
