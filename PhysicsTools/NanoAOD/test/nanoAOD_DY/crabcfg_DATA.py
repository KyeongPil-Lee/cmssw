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

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'

# config.JobType.allowUndistributedCMSSW = True

config.JobType.psetName = 'nanoAOD_DY_DATA.py' # -- should be filled
version = 'v1'

config.General.workArea = 'CRABDir_%s' % version
config.Data.outLFNDirBase = '/store/user/kplee/nanoAOD_DY_%s' % version


# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # -- SingleMuon
    config.General.requestName = 'SingleMuon_Run2016B_ver1'
    config.Data.inputDataset = '/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'SingleMuon_Run2016B_ver2'
    config.Data.inputDataset = '/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'SingleMuon_Run2016C'
    config.Data.inputDataset = '/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'SingleMuon_Run2016D'
    config.Data.inputDataset = '/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'SingleMuon_Run2016E'
    config.Data.inputDataset = '/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'SingleMuon_Run2016F'
    config.Data.inputDataset = '/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD'
    crabCommand('submit', config = config)


    # -- DoubleMuon
    config.General.requestName = 'DoubleMuon_Run2016B_ver1'
    config.Data.inputDataset = '/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'DoubleMuon_Run2016B_ver2'
    config.Data.inputDataset = '/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'DoubleMuon_Run2016C'
    config.Data.inputDataset = '/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'DoubleMuon_Run2016D'
    config.Data.inputDataset = '/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'DoubleMuon_Run2016E'
    config.Data.inputDataset = '/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'DoubleMuon_Run2016F'
    config.Data.inputDataset = '/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

