# NanoAOD MC with the scouting information

## Quick start
```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_27
cd CMSSW_10_6_27/src
cmsenv

git cms-init
git cms-merge-topic Kyeongpil-Lee:CMSSW_10_6_27_scoutingNAOD_MC

scram b

cd PhysicsTools/NanoAOD/test/addScouting_MC

voms-proxy-init --voms cms

# -- local test
cmsRun nanoAODProducer_addScouting_MC_2018.py >&nanoAODProducer_addScouting_MC_2018.log& tail -f nanoAODProducer_addScouting_MC_2018.log

# -- submit the CRAB jobs
python crabConfig_MC_2018.py

# -- simple script to check the CRAB jobs status
# -- only works when your proxy is valid
python CRAB_Status.py CRABDir
```

## New codes
* `python/scouting_cff.py`
   * Contains all scouting tables: scouting global variables (e.g. calo MET), scouting muon, scouting vertices and scouting calo jets

* `python/custom_scouting_cff.py`
   * Add scouting table in the main nano sequence
   * A line for phothon MVA value map producer to avoid an error when it runs with AOD
   * Modify muon trigger object part to save `DST_DoubleMu3*` path objects

* `plugin/ScoutingDimuonVertexTableProducer.cc`
   * Table producer for the dimuon vertex: save the two muon indices associated to this vertex as well as all basic variables


## Modified codes
* `plugins/SimpleFlatTableProducerPlugins.cc`
   * add `SimpleScoutingMuonFlatTableProducer`, `SimpleScoutingVertexFlatTableProducer`, `SimpleScoutingCaloJetFlatTableProducer`

* `plugins/TriggerOutputBranches.cc`
   * Made it to understand `DST_DoubleMu` paths and save the HLT branch for them
   * `name.compare(0, 3, "HLT") == 0` -> `name.compare(0, 3, "HLT") == 0 || name.compare(0, 12, "DST_DoubleMu") == 0`

* BuildFie.xml
   * add `DataFormats/Scouting`


## How the configuration is made (2018 MC)
1) Get the configuration for the official production
```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_27
cd CMSSW_10_6_27/src
cmsenv

cmsDriver.py NANO \
-s NANO --mc \
--conditions 106X_upgrade2018_realistic_v16_L1v1 \
--era Run2_2018,run2_nanoAOD_106Xv2 \
--eventcontent NANOAODSIM \
--datatier NANOAODSIM \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=100" \
-n -1 --no_exec
```

2) open `NANO_NANO.py` and add a few lines at the end for the scouting information
```
from PhysicsTools.NanoAOD.custom_scouting_cff import customize_add_scouting
process = customize_add_scouting(process)

# -- test AOD/miniAOD samples
process.source.fileNames = cms.untracked.vstring('/store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/5710A7A1-073E-D14D-9BE0-F661A3179580.root')
process.source.secondaryFileNames = cms.untracked.vstring('/store/mc/RunIISummer20UL18RECO/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/280000/85350584-EBC6-D44A-96D6-0A8B9A83D891.root')
process.maxEvents.input = cms.untracked.int32(1000)
```