from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''


config.JobType.pluginName = 'Analysis'
config.JobType.numCores = 1
# config.JobType.maxMemoryMB = 2500
# config.JobType.maxJobRuntimeMin = 2000

config.Data.inputDataset = ''

config.Data.inputDBS = 'global'
config.Data.publication = False

config.Data.splitting = 'Automatic'
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 3000 # -- ~3000 events per job --> 1000 jobs for ZMuMu_M50to120 (3M events)

config.Site.storageSite = 'T2_BE_IIHE'

# config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'

# config.JobType.allowUndistributedCMSSW = True

config.JobType.psetName = 'nanoAOD_DY_MC.py' # -- should be filled
version = 'v1'

config.General.workArea = 'CRABDir_%s' % version
config.Data.outLFNDirBase = '/store/user/kplee/nanoAOD_DY_%s' % version


# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # -- DYMuMu -- #
    config.General.requestName = 'QCDMuEnriched_Pt15to20_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt20to30_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt30to50_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt50to80_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt80to120_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt120to170_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt170to300_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt300to470_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt470to600_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt600to800_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt800to1000_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt1000toInf_Pythia8'
    config.Data.inputDataset = '/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)

