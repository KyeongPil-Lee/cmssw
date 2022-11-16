from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''
config.General.workArea = 'CRABDir'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nanoAODProducer_addScouting_MC_2018.py'

config.Data.inputDataset = ''

config.Data.inputDBS = 'global'
# config.Data.splitting = 'Automatic'
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 5 # -- too many failed due to memory problem
# config.Data.unitsPerJob = 1 # -- event per miniAOD file: ~100k -> # jobs for 1M sample: ~10

config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 50000; # -- 50k
config.JobType.maxMemoryMB = 3000 # -- several modules in nanoAOD production consumes large memory more than 2000 MB

config.Data.publication = False

config.Data.useParent = True # -- scouting: in AOD

config.Site.storageSite = 'T2_BE_IIHE'

version = 'v01_2nd'
config.Data.outLFNDirBase = '/store/user/kplee/NanoAOD_SC_MC_2018_%s' % version

config.JobType.allowUndistributedCMSSW = True

# 'MultiCRAB' part
if __name__ == '__main__':
    
    from CRABAPI.RawCommand import crabCommand

    # -- DY, M10-50 (Madgraph)
    config.General.requestName = 'DYJetsToLL_M10to50_Madgraph'
    config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- DY, M50 (aMCNLO)
    config.General.requestName = 'DYJetsToLL_M50toInf_aMCNLO'
    config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- DY, M50 (MiNNLO)
    config.General.requestName = 'DYJetsToLL_M50toInf_MiNNLO'
    config.Data.inputDataset = '/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- J/Psi (for tag and probe test)
    config.General.requestName = 'JPsiToMuMu_JPsiPt8_Pythia8'
    config.Data.inputDataset = '/JpsiToMuMu_JpsiPt8_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- QCD, inclusive
    config.General.requestName = 'QCDMuEnriched_Pt20toInf'
    config.Data.inputDataset = '/QCD_Pt-20_MuEnrichedPt15_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- QCD, pT-binned
    config.General.requestName = 'QCDMuEnriched_Pt15to20'
    config.Data.inputDataset = '/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt20to30'
    config.Data.inputDataset = '/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt30to50'
    config.Data.inputDataset = '/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt50to80'
    config.Data.inputDataset = '/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt80to120'
    config.Data.inputDataset = '/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt120to170'
    config.Data.inputDataset = '/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt170to300'
    config.Data.inputDataset = '/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt300to470'
    config.Data.inputDataset = '/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt470to600'
    config.Data.inputDataset = '/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt600to800'
    config.Data.inputDataset = '/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt800to1000'
    config.Data.inputDataset = '/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    config.General.requestName = 'QCDMuEnriched_Pt1000toInf'
    config.Data.inputDataset = '/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- ttbar
    config.General.requestName = 'TTTo2L2Nu_Powheg'
    config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM'
    crabCommand('submit', config = config)

    # -- already submitted for a test 
    # # -- W+jets (Madgraph)
    # config.General.requestName = 'WJetsToLNu_aMCNLO'
    # config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
    # crabCommand('submit', config = config)
