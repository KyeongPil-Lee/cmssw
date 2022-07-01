import FWCore.ParameterSet.Config as cms

def customizer_nanoAOD_DY(process, isSignal = False):
    process = customizer_add_more_trigObj(process)

    if isSignal:
        process = customizer_removeCut_dressedLepton(process)

    return process

def customizer_nanoAOD_DY(process):
        for sel_mu in process.triggerObjectTable.selections:
                if sel_mu.name=='Muon':
                    qualBits_default = sel_mu.qualityBits
                    qualBits_update = qualBits_default.value() + \
                        "+ \
                        4096*max(filter('hltL3fL1sMu10lqL1f0L2f10L3Filtered17'),filter('hltL3fL1sMu15DQlqL1f0L2f10L3Filtered17')) + \
                        8192*filter('hltL3fL1sMu18L1f0L2f10QL3Filtered20Q') + \
                        16384*filter('hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q') + \
                        32768*filter('hltL3fL1sMu10lqTkFiltered17Q') + \
                        65536*filter('hltL3fL1sMu18f0TkFiltered20Q') + \
                        131072*filter('hltL3fL1sMu22Or25f0TkFiltered27Q')"

                    sel_mu.qualityBits = cms.string(qualBits_update)
                    print sel_mu.qualityBits

                    doc_default = sel_mu.qualityBitsDoc
                    doc_update = doc_default.value() + ", 4096 = Mu17, 8192 = Mu20, 16384 = Mu27, 32768 = TkMu17, 65536 = TkMu20, 131072 = TkMu27"
                    sel_mu.qualityBitsDoc = cms.string(doc_update)
                    print sel_mu.qualityBitsDoc

        return process

def customizer_removeCut_dressedLepton(process):
    process.particleLevel.lepMinPt = cms.double(-1.0)
    process.particleLevel.lepMaxEta = cms.double(9999.0)

    return process


def customizer_output_DY(process):
    
    return process