# Private NanoAOD Production for DY Analysis

## Purpose

* For DY MC: save full phase space information for the dressed leptons (remove pt & eta cuts)
* Add branch for the DY-analysis-specific trigger obejcts for a precise matching to the offline muons
* Add `Electron_isOOT` branch to check the effect of electrons made from the out-of-time seed
  * By updating `plugins/EGMSeedGainProducer.cc` and `python/electrons_cff.py`


## Recipe (first setup)

* CMSSW_10_6_X: need to use singularity ([link](https://cms-sw.github.io/singularity.html)) under lxplus >= 8

```shell
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_30

cmssw-el7 # -- under >lxplus7

cd CMSSW_10_6_30/src
cmsenv
# voms-proxy-init --voms cms

git cms-merge-topic KyeongPil-Lee:10_6_30_nAODv9_forDY

scram b -j 10 >&scram.log

#cd PhysicsTools/NanoAOD/test/nanoAOD_DY
# source /cvmfs/cms.cern.ch/common/crab-setup.sh
# python crabcfg_DATA.py # -- submit CRAB jobs for data
# python crabcfg_MC.py # -- submit CRAB jobs for MC

cd PhysicsTools/NanoAOD/test
# -- local test
cmsRun nanoAOD_DY/2018/isOOT/DYNanoAOD_2018_data.py >&DYNanoAOD_2018_data.log& tail -f DYNanoAOD_2018_data.log
```

## Recipe (working space)

```shell
cd /afs/cern.ch/user/k/kplee/work/private/Analysis/nanoAOD_trigObj/CMSSW_10_6_30/src/PhysicsTools/NanoAOD/test/nanoAOD_DY

export SCRAM_ARCH=slc7_amd64_gcc700

cmssw-el7 # -- under >lxplus7

cmsenv
voms-proxy-init --voms cms
```

## NanoAOD production configurations (nanoAOD v9)

* Reference: https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/Instructions/Private-production
* Also check the test commands in McM for nanoAOD samples

### Common

Customizer at the end of the configuration

```python
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')

options.register('isSignal',
                  "false", # default value
                  VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.varType.bool,         # string, int, or float
                  "is signal DY sample? (if so, remove the cuts on the generator level leptons")

options.parseArguments()

print "isSignal = ", options.isSignal

from PhysicsTools.NanoAOD.customizer_nanoAOD_DY import *
process = customizer_nanoAOD_DY(process, options.isSignal)

# -- test miniAOD samples
testFile = ""
process.source.fileNames = cms.untracked.vstring(testFile)
process.maxEvents.input = cms.untracked.int32(1000)
```

### 2016 preAPV

* Data

```shell
cmsDriver.py  \
--python_filename nanoAOD_DY_DATA.py \
--eventcontent NANOAOD \
--customise Configuration/DataProcessing/Utils.addMonitoring \
--datatier NANOAOD \
--fileout file:nanoAOD_DY_DATA.root \
--conditions 106X_dataRun2_v36 \
--step NANO \
--era Run2_2016_HIPM,run2_nanoAOD_106Xv2 \
--no_exec --data -n -1
```

* MC

```shell
cmsDriver.py  \
--python_filename nanoAOD_DY_MC.py \
--eventcontent NANOAODSIM \
--customise Configuration/DataProcessing/Utils.addMonitoring \
--datatier NANOAODSIM \
--fileout file:nanoAOD_DY_MC.root \
--conditions 106X_mcRun2_asymptotic_preVFP_v11 \
--step NANO \
--era Run2_2016_HIPM,run2_nanoAOD_106Xv2 \
--no_exec --mc -n -1
```

### 2018

* Data

```bash
cmsDriver.py NANO \
-s NANO --data \
--conditions 106X_dataRun2_v35 \
--era Run2_2018,run2_nanoAOD_106Xv2 \
--eventcontent NANOAOD \
--datatier NANOAOD \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000" \
-n -1 --no_exec
mv NANO_NANO.py DYNanoAOD_2018_data.py

# -- add customizer
# -- test file: /store/data/Run2018D/SingleMuon/MINIAOD/UL2018_MiniAODv2_GT36-v1/610000/19678FA7-BABE-6145-A2D7-40A3E70406FB.root
cmsRun DYNanoAOD_2018_data.py >&DYNanoAOD_2018_data.log&
tail -f DYNanoAOD_2018_data.log
```

* MC

```bash
cmsDriver.py NANO \
-s NANO --mc \
--conditions 106X_upgrade2018_realistic_v16_L1v1 \
--era Run2_2018,run2_nanoAOD_106Xv2 \
--eventcontent NANOAODSIM \
--datatier NANOAODSIM \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=100" \
-n -1 --no_exec
mv NANO_NANO.py DYNanoAOD_2018_mc.py

# -- add customizer
# -- test file: /store/mc/RunIISummer20UL18MiniAODv2/DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/BE954C4F-7A7A-3B4B-8F92-8F5512A25007.root
cmsRun DYNanoAOD_2018_mc.py isSignal=true >&DYNanoAOD_2018_mc_signal.log&
tail -f DYNanoAOD_2018_mc_signal.log
```

* CRAB status check

```bash
cd /afs/cern.ch/user/k/kplee/work/private/Analysis/nanoAOD_trigObj/CMSSW_10_6_30/src/PhysicsTools/NanoAOD/test/nanoAOD_DY/2018

cmsenv
voms-proxy-init --voms cms

python CRAB_Status.py -d CRABDir_v1 >&CRAB_Status.log&
```



## CRAB configuration

* If you run on CRAB, it is important to add `fakeNameForCrab = cms.untracked.bool(True)` to the configuration of the NanoAODOutputModule in the CMSSW cfg file (and to run a single instance of it - this should normally be the case)
  * Reflected in the customizer





