import FWCore.ParameterSet.Config as cms

def customizer_nanoAOD_DY(process, isSignal=False, saveCT18=False):
    process = customizer_add_more_trigObj(process)

    if isSignal:
        process = customizer_removeCut_dressedLepton(process)

    if saveCT18:
        process = customizer_switch_PDFWeight_CT18(process)

    # -- recommendation for CRAB running
    if hasattr(process, "NANOAODoutput"): # -- data
        process.NANOAODoutput.fakeNameForCrab = cms.untracked.bool(True)

    if hasattr(process, "NANOAODSIMoutput"): # -- MC (SIM)
        process.NANOAODSIMoutput.fakeNameForCrab = cms.untracked.bool(True)

    process = delete_tables(process)

    return process

def customizer_add_more_trigObj(process):
    # -- put in the first place in VPSet: because the trigger object is not saved if it is already found in previous selections
    process.triggerObjectTable.selections.insert(0, 
        cms.PSet(
            name = cms.string("DYMuon"),
            id = cms.int32(113),
            # -- selection should be updated for 2016 - Cascade or TkMu collections
            sel = cms.string("type(83) && pt > 5 && (coll('hltIterL3MuonCandidates') || (pt > 45 && coll('hltHighPtTkMuonCands')) || (pt > 95 && coll('hltOldL3MuonCandidates')))"),
            l1seed = cms.string("type(-81)"), l1deltaR = cms.double(0.5),
            l2seed = cms.string("type(83) && coll('hltL2MuonCandidates')"),  l2deltaR = cms.double(0.3),
            skipObjectsNotPassingQualityBits = cms.bool(True),
            qualityBits = cms.string(
                            "filter('hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07') + " \
                            "2*filter('hltL3fL1DoubleMu155fFiltered17') + " \
                            "4*filter('hltL3fL1DoubleMu155fPreFiltered8') + " \
                            "8*filter('hltDiMuon178Mass3p8Filtered')"),
            qualityBitsDoc = cms.string("1 = IsoMu24, 2 = Mu17 leg, 4 = Mu8 leg, 8 = Mass3p8"),
        )
    )
    return process

        # for sel_mu in process.triggerObjectTable.selections:
        #         if sel_mu.name=='Muon':
        #             qualBits_default = sel_mu.qualityBits
        #             qualBits_update = qualBits_default.value() + \
        #                 "+ \
        #                 4096*max(filter('hltL3fL1sMu10lqL1f0L2f10L3Filtered17'),filter('hltL3fL1sMu15DQlqL1f0L2f10L3Filtered17')) + \
        #                 8192*filter('hltL3fL1sMu18L1f0L2f10QL3Filtered20Q') + \
        #                 16384*filter('hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q') + \
        #                 32768*filter('hltL3fL1sMu10lqTkFiltered17Q') + \
        #                 65536*filter('hltL3fL1sMu18f0TkFiltered20Q') + \
        #                 131072*filter('hltL3fL1sMu22Or25f0TkFiltered27Q')"

        #             sel_mu.qualityBits = cms.string(qualBits_update)
        #             # print sel_mu.qualityBits

        #             doc_default = sel_mu.qualityBitsDoc
        #             doc_update = doc_default.value() + ", 4096 = Mu17, 8192 = Mu20, 16384 = Mu27, 32768 = TkMu17, 65536 = TkMu20, 131072 = TkMu27"
        #             sel_mu.qualityBitsDoc = cms.string(doc_update)
        #             # print sel_mu.qualityBitsDoc

        # return process

# -- should be run only when it is signal "MC" (do not work for data)
def customizer_removeCut_dressedLepton(process):
    process.particleLevel.lepMinPt = cms.double(-1.0)
    process.particleLevel.lepMaxEta = cms.double(9999.0)
    process.rivetLeptonTable.cut = cms.string("")

    return process

def customizer_switch_PDFWeight_CT18(process):
    process.genWeightsTable.preferredPDFs = cms.VPSet( 
        cms.PSet( name = cms.string("CT18NNLO"), lhaid = cms.uint32(14000) )
    )

    process.genWeightsTable.debug = cms.untracked.bool(True)

    for pfPDF in process.genWeightsTable.preferredPDFs:
        print("PDF name = %s, LHAID = %d" % (pfPDF.name, pfPDF.lhaid.value()))
 
    return process

# -- it might be better if relavant calculation modules are removed as well,
# -- but it is hard to track all the depdendencies
# -- (e.g. something produced in a module can be called in the other next module, like MET calculation)
# -- therefore, just drop the table and do not touch the intermediate EDProducer modules
def delete_tables(process):

    process = delete_table(process, "fatJetTable")
    # process = delete_table(process, "saJetTable")
    process = delete_table(process, "tauTable")
    process = delete_table(process, "boostedTauTable")
    # process = delete_table(process, "electronTable")
    # process = delete_table(process, "lowPtElectronTable")
    # process = delete_table(process, "photonTable")
    process = delete_table(process, "simpleCleanerTable") # -- make (obj)_cleanmask branch: not needed for us
    process = delete_table(process, "isoTrackTable")
    process = delete_table(process, "genJetAK8Table")
    process = delete_table(process, "genJetAK8FlavourTable")
    process = delete_table(process, "fatJetMCTable")
    process = delete_table(process, "genSubJetAK8Table")
    process = delete_table(process, "subjetMCTable")
    # process = delete_table(process, "electronMCTable")
    process = delete_table(process, "tauMCTable")
    process = delete_table(process, "lowPtElectronMCTable")
    # process = delete_table(process, "photonMCTable")
    process = delete_table(process, "genVisTauTable")
    process = delete_table(process, "boostedTauMCTable")
    process = delete_table(process, "HTXSCategoryTable")
    process = delete_table(process, "ttbarCategoryTable")

    return process

def delete_table(process, tableName):

    if hasattr(process, tableName):
        delattr(process, tableName)

    return process