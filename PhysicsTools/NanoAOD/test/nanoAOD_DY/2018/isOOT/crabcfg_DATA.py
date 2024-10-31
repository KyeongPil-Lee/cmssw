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

# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 3000 # -- ~3000 events per job --> 1000 jobs for ZMuMu_M50to120 (3M events)

config.Site.storageSite = 'T2_BE_IIHE'

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'

# config.JobType.allowUndistributedCMSSW = True

config.JobType.psetName = 'DYNanoAOD_2018_data.py' # -- should be filled

version = 'v4'
config.General.workArea = 'CRABDir_%s' % version
config.Data.outLFNDirBase = '/store/user/kplee/DYNanoAOD_%s' % version

# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    config.General.requestName = 'EGamma_Run2018A'
    config.Data.inputDataset = '/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'EGamma_Run2018B'
    config.Data.inputDataset = '/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)

    config.General.requestName = 'EGamma_Run2018C'
    config.Data.inputDataset = '/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD'
    crabCommand('submit', config = config)


    # config.General.requestName = 'EGamma_Run2018D'
    # config.Data.inputDataset = '/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD'
    # crabCommand('submit', config = config)