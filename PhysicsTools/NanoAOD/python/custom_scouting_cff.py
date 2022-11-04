# -- customizer to add the scouting information (Run-2) in nanoAOD production
import FWCore.ParameterSet.Config as cms

def customize_add_scouting(process):
    # -- remove error when it runs with AOD
    # -- it will automatically look for the corresponding object in miniAOD
    process.photonMVAValueMapProducer.src = cms.InputTag("")

    # -- add trigger objects of the scouting path
    process = customize_triggerObj_add_scouting(process)

    # -- add scouting tables
    process.load("PhysicsTools.NanoAOD.scouting_cff")
    # process.nanoSequenceCommon.insert(process.nanoSequenceCommon.index(process.isoTrackTables)+1, process.scoutingTables) # -- it does not make branches
    process.nanoAOD_step.insert(process.nanoSequenceCommon.index(process.isoTrackTables)+1, process.scoutingTables)

    # -- remove unncessary tables for DY analysis    
    process = delete_tables(process)

    # -- just for monitoring: should be turned off for the production
    # process = add_monitoring_timing_memory(process)

    # print process.nanoSequenceCommon
    # print process.nanoAOD_step

    return process

# -- reference: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDMTimingAndMemory
def add_monitoring_timing_memory(process):

    process.Timing = cms.Service("Timing",
      summaryOnly = cms.untracked.bool(False),
      useJobReport = cms.untracked.bool(True)
    )

    process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
        ignoreTotal = cms.untracked.int32(1)
    )

    return process

# -- it might be better if relavant calculation modules are removed as well,
# -- but it is hard to track all the depdendencies
# -- (e.g. something produced in a module can be called in the other next module, like MET calculation)
# -- therefore, just drop the table and do not touch the intermediate EDProducer modules
def delete_tables(process):

    process = delete_table(process, "fatJetTable")
    process = delete_table(process, "saJetTable")
    process = delete_table(process, "tauTable")
    process = delete_table(process, "boostedTauTable")
    process = delete_table(process, "electronTable")
    process = delete_table(process, "lowPtElectronTable")
    process = delete_table(process, "photonTable")
    process = delete_table(process, "simpleCleanerTable") # -- make (obj)_cleanmask branch: not needed for us
    process = delete_table(process, "isoTrackTable")
    process = delete_table(process, "genJetAK8Table")
    process = delete_table(process, "genJetAK8FlavourTable")
    process = delete_table(process, "fatJetMCTable")
    process = delete_table(process, "genSubJetAK8Table")
    process = delete_table(process, "subjetMCTable")
    process = delete_table(process, "electronMCTable")
    process = delete_table(process, "tauMCTable")
    process = delete_table(process, "lowPtElectronMCTable")
    process = delete_table(process, "photonMCTable")
    process = delete_table(process, "genVisTauTable")
    process = delete_table(process, "boostedTauMCTable")
    process = delete_table(process, "HTXSCategoryTable")
    process = delete_table(process, "ttbarCategoryTable")

    return process

def delete_table(process, tableName):

    if hasattr(process, tableName):
        delattr(process, tableName)

    return process

def customize_triggerObj_add_scouting(process):
    if hasattr(process, "triggerObjectTable"):
        selectionSets = process.triggerObjectTable.selections.value()
        for index in range(0, len(selectionSets)):
            if selectionSets[index].id == 13: # -- muon trigger object:
                sel_old = selectionSets[index].sel.value()
                l2seed_old = selectionSets[index].l2seed.value()
                qualityBits_old = selectionSets[index].qualityBits.value()
                qualityBitsDoc_old = selectionSets[index].qualityBitsDoc.value()

                sel_new = sel_old
                sel_new = sel_new.replace("pt > 5", "pt > 0") # -- lower pT
                sel_new = sel_new.replace("coll('hltIterL3MuonCandidates')", "coll('hltIterL3MuonCandidates') || coll('hltIterL3MuonCandidatesNoVtx')")

                l2seed_new = l2seed_old
                l2seed_new = l2seed_new.replace("coll('hltL2MuonCandidates')", "(coll('hltL2MuonCandidates') || coll('hltL2MuonCandidatesNoVtx'))")

                qualityBits_new = qualityBits_old + " + 4096*filter('hltDoubleMu3L3FilteredNoVtx')" # -- hltDoubleMu3L3FilteredNoVtx* = hltDoubleMu3L3FilteredNoVtx or hltDoubleMu3L3FilteredNoVtxMass10. No *
                qualityBitsDoc_new = qualityBitsDoc_old + ", 4096 = 2mu (DoubleMu3)"

                selectionSets[index].sel = cms.string(sel_new)
                selectionSets[index].l2seed = cms.string(l2seed_new)
                selectionSets[index].qualityBits = cms.string(qualityBits_new)
                selectionSets[index].qualityBitsDoc = cms.string(qualityBitsDoc_new)

                # print sel_new
                # print l2seed_new
                # print qualityBits_new
                # print qualityBitsDoc_new

    return process
