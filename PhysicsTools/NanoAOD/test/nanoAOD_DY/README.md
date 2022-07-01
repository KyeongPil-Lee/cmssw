# Private NanoAOD Production for DY Analysis

## Purpose

* Add more trigger object information needed for muon fake rate measurement
  * (Tk)Mu17, 20, 27

## Recipe

```shell
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_30
cd CMSSW_10_6_30/src
cmsenv
# voms-proxy-init --voms cms

git cms-merge-topic KyeongPil-Lee:10_6_30_nAODv9_forDY

scram b -j 10 >&scram.log

cd PhysicsTools/NanoAOD/test/nanoAOD_DY

source /cvmfs/cms.cern.ch/common/crab-setup.sh

python crabcfg_DATA.py # -- submit CRAB jobs for data
python crabcfg_MC.py # -- submit CRAB jobs for MC
```



## Files

### NanoAOD production configuration (nanoAOD v9, 2016 preAPV)

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



* Customizer at the end of the configuration

```python
from PhysicsTools.NanoAOD.customizer_nanoAOD_DY import *
process = customizer_nanoAOD_DY(process)
```

