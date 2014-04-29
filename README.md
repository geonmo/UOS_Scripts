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
This command will make JPSI + "time" directory. 
Then, script will split 100 files per 1 job with filelist.txt.
"-g" options must be used for xrootd files.( root://uosaf0007.sscc.uos.ac.kr~~ or /store/ )

fileList must be include path of data files like cmssw input source list.
1. Physics File Name
<pre><code>
file:/pnfs/user/geonmo/a.root
file:/pnfs/user/geonmo/b.root
...
</code></pre>
2. Logical File Name
<pre><code>
/store/user/geonmo/a.root  ## or root://uosaf0007.sscc.uos.ac.kr//cms/store/user/geonmo/a.root
/store/user/geonmo/b.root  ## or root://uosaf0007.sscc.uos.ac.kr//cms/store/user/geonmo/b.root
...
</code></pre>
    
