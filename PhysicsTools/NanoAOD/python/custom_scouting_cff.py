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
    
    # print process.nanoSequenceCommon
    # print process.nanoAOD_step

    # -- skip events without a product
    # -- due to scouting dimuon vertex: it sometimes doesn't exist in some events
    # process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
    # print "[customize_add_scouting:Warning] SkipEvent = cms.untracked.vstring('ProductNotFound') is turned on"

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
                # qualityBits_new = qualityBits_old + " + 4096*filter('hltL3crIso*Filtered0p07')"
                qualityBitsDoc_new = qualityBitsDoc_old + ", 4096 = 2mu (DoubleMu3)"

                selectionSets[index].sel = cms.string(sel_new)
                selectionSets[index].l2seed = cms.string(l2seed_new)
                selectionSets[index].qualityBits = cms.string(qualityBits_new)
                selectionSets[index].qualityBitsDoc = cms.string(qualityBitsDoc_new)

                print sel_new
                # print l2seed_new
                # print qualityBits_new
                # print qualityBitsDoc_new

    return process
