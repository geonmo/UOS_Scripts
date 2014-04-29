#!/usr/bin/env python
import os,sys
import copy
### Select host

storage_hostname = "uosaf0007.sscc.uos.ac.kr"    # UOS
#storage_hostname = "cluster142.knu.ac.kr"  # KNU
#storage_hostname = "eoscms.cern.ch"             # EOS at CERN



dir_name  = "/store/user/geonmo/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/TTJet_Dilepton_jpsi_20140327_TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/3ab498b34e98168391158211c0d6181f"  # KNU directory
#dir_name  = "/cms/store/user/geonmo/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/TTJet_Dilepton_jpsi_20140327_TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/3ab498b34e98168391158211c0d6181f"  # UOS directory


protocol = "root://"
print sys.argv
cmd = "xrd "+storage_hostname+" ls "+dir_name
lists = os.popen(cmd)
data = []
ss_lists = lists.readlines()
total = len(ss_lists)
for count, line in enumerate( ss_lists ) :
	if ( len(line.split()) == 5 ) :
		#print line.split()
		data_file = (protocol+storage_hostname+"/"+line.split()[4])
		print "Total : "+ total+" / current : "+ (count+1)
		cmd = "xrdcp "+data_file+" ./"
		os.system(cmd)
