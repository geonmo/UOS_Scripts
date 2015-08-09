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
  pattern = "*.root" 
  def __init__(self) :
    self.getVariable()
    self.makeDirectory()
  def getInputListFromInputPath( self, inputPath ) :
    list =[]
    if ( inputPath.find("/store") != -1) :
      print "LFN dir : inputPath"
      dir = inputPath.split("/store")[1]
      cmd = "xrdls /store%s"%(dir)
      print cmd
      output = os.popen(cmd)
      list = output.readlines()
    else :
      list = glob.glob( inputPath+'/'+ self.pattern)
    return list
  def getInputListFromFileList( self, fileList ) :
    list =[]
    file = open(fileList)
    for x in file.readlines() :
      if ( x.find( "/store") != -1 ) :
        label = "root://uosaf0007.sscc.uos.ac.kr//cms/store/%s"%(x.split("/store")[1])
        list.append(label)
      else :
        list.append(x)
    return list
         
 
  def makeDirectory(self) :
    time_dir = time.strftime(self.output_path+"__%d%b%Y_%HH%MM/",time.localtime())
    os.mkdir(time_dir)
    self.output_path = time_dir

  def getVariable( self ) :
    usage = """%prog [options] pyROOT_Script.py\negs)submitTorqueBatch.py -d /pnfs/user/cat_data/JpsiFilteredCattuple/ -p \"catTuple*.root\" calAngle.py\n
or\n
%prog [options] pyROOT_Script.py\negs)submitTorqueBatch.py -i filelist.txt -p \"catTuple*.root\" calAngle.py\n
"""
    parser = OptionParser(usage)
    parser.add_option("-i","--listfile",action="store",type="string",dest="listFile",help="input file list.")
    parser.add_option("-d","--inpath",action="store",type="string",dest="inputPath",help="input files(.ROOT)'s directory path.")
    parser.add_option("-o","--outpath",action="store",type="string",default="ANA_ROOT",dest="outputPath",help="output file path.(Default : ANA_ROOT)")
    parser.add_option("-p","--pattern",action="store",type="string",default="*.root",dest="pattern",help="Input file's name pattern.(Default : \"*.root\")")  
    parser.add_option("-t","--title",action="store",type="string",default="ANA",dest="title",help="Job's Title.(Default : ANA) ")  
    parser.add_option("-q","--queue",action="store",type="string",default="batch6",dest="queue",help="torque queue name.(Default : batch6)" )  
    (options,args) = parser.parse_args()
    ###self.input_path = options.inputPath
    self.output_path = options.outputPath 
    self.title = options.title
    self.pattern = options.pattern
    if ( options.listFile is not None ) :
      self.input_list = self.getInputListFromFileList( options.listFile )
    elif ( options.inputPath is not None ) :
      self.input_list = self.getInputListFromInputPath( options.inputPath )
    else :
      print "Input file is required."
      
      sys.exit(-1)
 
    self.pyCfg = args[0]
    self.queue = options.queue
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
cp ./x509up_u`id -u` /tmp
eval `scramv1 runtime -sh`
"""%(self.title, self.output_path)
    #print script_head
    return script_head

  def CheckCertificate(self) :
    print "@@ Checking grid certificate to access files..."
    if os.system("voms-proxy-info -exists --hours 8") != 0:
      os.system("voms-proxy-init -voms cms --valid 144:00")    
    os.system("cp /tmp/x509up_u`id -u` ./")

  def Print(self) :
    print self.output_path, self.queue
    print "# of files : %d"%(len(self.input_list))
    print self.pyCfg

  def Ana(self) :
    print "Ana"
    self.CheckCertificate()
    self.input_list.sort()
    print "list : "
    for idx, input in enumerate(self.input_list) :
      input_idx = input.split("/")[-1]
      output = self.output_path+"/"+self.title+"_%03d.root"%(idx)
      config = self.makeCmdFiles(idx,input,output )
      tmp_sc = open(self.output_path+"/batch_%d"%idx+".cmd","w")
      tmp_sc.write( config )
      tmp_sc.write("python %s %s %s"%(self.pyCfg, input.strip(), output))
      tmp_sc.close()
      command = "qsub -q %s %s/batch_%d.cmd"%(self.queue,self.output_path,idx)
      os.system(command)


if __name__ == "__main__" :
  sb = submitBatch()
  sb.Ana()
  sb.Print()

