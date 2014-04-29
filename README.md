UOS_Scripts
===========

Scripts file for Tier3 @ UOS

This directory has files for user to use Tier3@UOS easily.

# create-batch  
This scripts helps user to run batch job with local file.

<pre><code>
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
</code></pre>

For example,
<pre><code>
./create-batch --jobName JPSI --fileList filelist.txt --maxFiles 100 --cfg pat_cfg.py -g
</code></pre>
This command will make JPSI-<time> directory. 
Then, script will split 100 files per 1 job.
"-g" options must be used for xrootd files.( root://uosaf0007.sscc.uos.ac.kr~~ or /store/ )

    
