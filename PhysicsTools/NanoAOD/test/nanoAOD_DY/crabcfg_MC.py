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
    config.General.requestName = 'DYJetsToMuMu_M50_PowhegMiNNLO'
    config.Data.inputDataset = '/DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- single top, s-channel -- #
    config.General.requestName = 'ST_sChannel_aMCNLO'
    config.Data.inputDataset = '/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- single top, t-channel -- #
    config.General.requestName = 'ST_tChannel_top_aMCNLO'
    config.Data.inputDataset = '/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'ST_tChannel_antitop_aMCNLO'
    config.Data.inputDataset = '/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- single top, tW -- #
    config.General.requestName = 'ST_tW_top_Powheg'
    config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'ST_tW_antitop_Powheg'
    config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- ttbar, leptonic decay
    config.General.requestName = 'TTTo2L2Nu_Powheg'
    config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- DYTauTau, at least one tau -> e or mu decay
    config.General.requestName = 'DYJestToTauTau_M50_AtLeastOneEorMuDecay_PowhegMiNNLO'
    config.Data.inputDataset = '/DYJetsToTauTau_M-50_AtLeastOneEorMuDecay_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- W+jets
    config.General.requestName = 'WJetsToLNu_aMCNLO'
    config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
    crabCommand('submit', config = config)


    # -- WW
    config.General.requestName = 'WW_Pythia8'
    config.Data.inputDataset = '/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'WWTo2L2Nu_Powheg'
    config.Data.inputDataset = '/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM'
    crabCommand('submit', config = config)


    # -- WZ
    config.General.requestName = 'WZ_Pythia8'
    config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- ZZ
    config.General.requestName = 'ZZ_Pythia8'
    config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM'
    crabCommand('submit', config = config)

