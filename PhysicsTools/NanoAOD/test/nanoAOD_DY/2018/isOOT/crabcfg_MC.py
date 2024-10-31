from CRABClient.UserUtilities import config
config = config()

def Get_PSetName(era):
    pSetName = "undefined"
    if era == "16pre"    : pSetName = "DYNanoAOD_2016preAPV_mc.py"
    elif era == "16post" : pSetName = "DYNanoAOD_2016postAPV_mc.py"
    elif era == "17"     : pSetName = "DYNanoAOD_2017_mc.py"
    elif era == "18"     : pSetName = "DYNanoAOD_2018_mc.py"

    return pSetName

# -- common setting -- #
config.General.requestName = ''

config.JobType.pluginName = 'Analysis'
config.JobType.numCores = 1
# config.JobType.maxMemoryMB = 2500
# config.JobType.maxJobRuntimeMin = 2000

config.Data.inputDataset = ''

config.Data.inputDBS = 'global'
config.Data.publication = False

# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 3000 # -- ~3000 events per job --> 1000 jobs for ZMuMu_M50to120 (3M events)

config.Site.storageSite = 'T2_BE_IIHE'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'

# config.JobType.allowUndistributedCMSSW = True

# -- DY list: https://github.com/KyeongPil-Lee/GENTool/blob/accCorr_DYFullRun2/EDTool/test/Acceptance/crabcfg_DY.py
dic_sample_DY = {
    "DYMuMu_M10to50"     : '/DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M10to50_ext" : '/DYJetsToMuMu_M-10to50_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/MINIAODSIM',
    "DYMuMu_M50"         : '/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M100to200"   : '/DYJetsToMuMu_M-100to200_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M200to400"   : '/DYJetsToMuMu_M-200to400_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M400to500"   : '/DYJetsToMuMu_M-400to500_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M500to700"   : '/DYJetsToMuMu_M-500to700_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M700to800"   : '/DYJetsToMuMu_M-700to800_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M800to1000"  : '/DYJetsToMuMu_M-800to1000_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M1000to1500" : '/DYJetsToMuMu_M-1000to1500_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M1500to2000" : '/DYJetsToMuMu_M-1500to2000_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
    "DYMuMu_M2000toInf"  : '/DYJetsToMuMu_M-2000toInf_H2ErratumFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
}

dic_sample_bkg = {
    "GGtoLL_M5to50"       : "/GGToLL_M-5To50_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "GGtoLL"              : "/GGToLL_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "ST_sChannel"         : "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
    "ST_tChannel_antitop" : "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
    "ST_tChannel_top"     : "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5CR1_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
    "ST_tW_antitop"       : "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "ST_tW_top"           : "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "TTTo2L2Nu"           : "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
    "DYTauTau_M50"        : "/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "WWTo2L2Nu"           : "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "WZ"                  : "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
    "ZZto4L"              : "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
}

# -- customize for each era -- #
# -- 16pre, 16post, 17, 18
eraTag = "18"

config.JobType.psetName = Get_PSetName(eraTag)
version = 'v4'

config.General.workArea = 'CRABDir_%s' % version
config.Data.outLFNDirBase = '/store/user/kplee/DYNanoAOD_%s' % version

# 'MultiCRAB' part
if __name__ == '__main__':
    
    from multiprocessing import Process
    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        # except HTTPException as hte:
        #     print("Failed submitting task: %s" % (hte.headers))
        except ClientException as cle:
            print("Failed submitting task: %s" % (cle))


    # -- DY sample (signal)
    list_param = ["isSignal=True"]
    for theRequestName in dic_sample_DY.keys():
        theDatasetName = dic_sample_DY[theRequestName]

        config.General.requestName = theRequestName+"_"+eraTag
        config.Data.inputDataset = theDatasetName
        config.JobType.pyCfgParams = list_param

        # print("(%20s, %s)" % (theRequestName, theDatasetName) )

        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

    # -- background sample
    list_param = ["isSignal=False"]
    for theRequestName in dic_sample_bkg.keys():
        theDatasetName = dic_sample_bkg[theRequestName]

        config.General.requestName = theRequestName+"_"+eraTag
        config.Data.inputDataset = theDatasetName
        config.JobType.pyCfgParams = list_param

        print("[%20s, %s]" % (theRequestName, theDatasetName) )

        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

