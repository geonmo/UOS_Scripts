#!/usr/bin/env python
import os, sys, time,glob,re
from optparse import OptionParser

class submitBatch :
  #input_path = None
  output_path = None
  queue = "batch6"
  input_list = []
  title = None
  pyCfg = None 
  def __init__(self) :
    self.getVariable()
    self.makeDirectory()
 
  def makeDirectory(self) :
    time_dir = time.strftime(self.output_path+"__%d%b%Y_%HH%MM/",time.localtime())
    os.mkdir(time_dir)
    self.output_path = time_dir

  def getVariable( self ) :
    parser = OptionParser()
    parser.add_option("-i","--inpath",action="store",type="string",dest="inputPath")
    parser.add_option("-o","--outpath",action="store",type="string",default="ANA_ROOT",dest="outputPath")
    parser.add_option("-p","--pattern",action="store",type="string",default="*.root",dest="pattern")  
    parser.add_option("-t","--title",action="store",type="string",default="ANA",dest="title")  
    (options,args) = parser.parse_args()
    #self.input_path = options.inputPath
    self.output_path = options.outputPath 
    self.title = options.title
    self.input_list = glob.glob( options.inputPath+'/'+ options.pattern)
    self.pyCfg = args[0]
  def makeCmdFiles(self, idx, input, output ) :
    script_head ="""#PBS -S /bin/bash
#PBS -N %s_%s
#PBS -l nodes=1:ppn=1,walltime=72:00:00
#PBS -o $PBS_JOBID.$PBS_O_HOST.out
#PBS -e $PBS_JOBID.$PBS_O_HOST.err
#PBS -m abe
#PBS -V

#echo $PBS_O_HOST
cat $PBS_NODEFILE
#echo $PBS_TASKNUM

source /pnfs/etc/profile.d/cmsset_default.sh
cd $PBS_O_WORKDIR
eval `scramv1 runtime -sh`
#python %s %s %s
"""%(self.title, self.output_path,self.pyCfg, input, output )
    #print script_head
    return script_head
    

  def Print(self) :
    print self.output_path, self.queue
    print "# of files : %d"%(len(self.input_list))
    print self.pyCfg

  def Ana(self) :
    print "Ana"
    for input in self.input_list :
      idx = re.search(r'\d+',input)
      if ( idx.group() is not None) :
        n_idx = int(idx.group())
      output = self.output_path+"/output_%03d.root"%(int(n_idx))
      config = self.makeCmdFiles(n_idx,input,output )
      tmp_sc = open(self.output_path+"/batch_%d"%n_idx+".cmd","w")
      tmp_sc.write( config )
      tmp_sc.write("python %s %s %s"%(self.pyCfg, input, output))
      tmp_sc.close()
      os.system("qsub -q batch6 "+self.output_path+"/batch_%d"%n_idx+".cmd")
    


if __name__ == "__main__" :
  filename = sys.argv[1]
  sb = submitBatch()
  sb.Ana()
  sb.Print()






