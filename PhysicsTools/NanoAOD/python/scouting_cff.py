import FWCore.ParameterSet.Config as cms

from PhysicsTools.NanoAOD.common_cff import *

# -- calo MET @ HLT
scoutingGlobalVarTable = cms.EDProducer("GlobalVariablesTableProducer",
    variables = cms.PSet(
        SCCaloMET_phi = ExtVar( cms.InputTag("hltScoutingCaloPacker", "caloMetPhi"), "double", doc = "scouting calo MET phi" ),
        SCCaloMET_pt  = ExtVar( cms.InputTag("hltScoutingCaloPacker", "caloMetPt"), "double", doc = "scouting calo MET pt" ),
        SCRho         = ExtVar( cms.InputTag("hltScoutingCaloPacker", "rho"), "double", doc = "scouting rho" ),
    )
)

# -- scouting muons
# -- format: https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/DataFormats/Scouting/interface/ScoutingMuon.h
# -- producer: https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/HLTrigger/Muon/plugins/HLTScoutingMuonProducer.cc
scoutingMuonTable = cms.EDProducer("SimpleScoutingMuonFlatTableProducer",
    src = cms.InputTag("hltScoutingMuonPackerCalo"),
    cut = cms.string(""), # no filter: there should be no cut to have consistent muon index associated with the dimuon vertex
    name = cms.string("SCMuon"),
    doc  = cms.string("Scouting muons"),
    singleton = cms.bool(False), # -- if only one object exists per event (e.g. MET): true. if not (e.g. muon), false.
    extension = cms.bool(False), # -- main table for the scouting muon (not extended version from the other table)
    variables = cms.PSet(
        pt  = Var("pt()", float, doc = "pt of the scouting muon"),
        eta = Var("eta()", float, doc = "eta of the scouting muon"),
        phi = Var("phi()", float, doc = "phi of the scouting muon"),
        charge = Var("charge()", float, doc = "charge of the scouting muon"),
        nPixelHit = Var("nValidPixelHits()", int, doc = "# valid pixel hits"),
        nStripHit = Var("nValidStripHits()", int, doc = "# valid strip hits"),
        nTrackerLayer = Var("nTrackerLayersWithMeasurement()", int, doc = "# tracker layers with the measurements"),
        nMuonHit = Var("nValidMuonHits()", int, doc = "# valid muon hits"),
        nMatchedStation = Var("nMatchedStations()", int, doc = "# matched stations"),
        chi2 = Var("chi2()", float, doc = "chi2-square of the global fit of the track"),
        nDOF = Var("ndof()", int, doc = "degree of freedom of the global fit of the track"),
        dxy  = Var("dxy()", float, doc = "transverse Impact parameter"),
        dz  = Var("dz()", float, doc = "horizontal Impact parameter"),
        trkIso  = Var("trackIso()", float, doc = "tracker isolation"),
    )
)

# -- scouting dimuon vertices
# -- format: https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/DataFormats/Scouting/interface/ScoutingVertex.h
# -- producer: https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/HLTrigger/btau/plugins/HLTDisplacedmumuVtxProducer.cc
scoutingDimuVertexTable = cms.EDProducer("ScoutingDimuonVertexTableProducer",
    SCDimuonVtx = cms.InputTag("hltScoutingMuonPackerCalo", "displacedVtx", "HLT"),
    SCMuon = cms.InputTag("hltScoutingMuonPackerCalo"),
)

# -- scouting pixel vertices
scoutingPixelVertexTable = cms.EDProducer("SimpleScoutingVertexFlatTableProducer",
    src = cms.InputTag("hltScoutingPrimaryVertexPacker", "primaryVtx", "HLT"),
    cut = cms.string(""),
    name = cms.string("SCPixelVtx"),
    doc  = cms.string("Scouting pixel vertices"),
    singleton = cms.bool(False),
    extension = cms.bool(False),
    variables = cms.PSet(
        x = Var("x()", float, doc = "x position"),
        y = Var("y()", float, doc = "y position"),
        z = Var("z()", float, doc = "z position"),
        xErr = Var("xError()", float, doc = "error of x position"),
        yErr = Var("yError()", float, doc = "error of y position"),
        zErr = Var("zError()", float, doc = "error of z position"),
        chi2 = Var("chi2()", float, doc = "chi-square of the vertex fit"),
        nODF = Var("ndof()", int, doc = "degree of freedom of the vertex fit"),
        isValid = Var("isValidVtx()", bool, doc = "is valid vertex?"),
    )
)

# -- scouting pixel vertices near muon
scoutingPixelVertexNearMuTable = cms.EDProducer("SimpleScoutingVertexFlatTableProducer",
    src = cms.InputTag("hltScoutingPrimaryVertexPackerCaloMuon", "primaryVtx", "HLT"),
    cut = cms.string(""),
    name = cms.string("SCPixelVtxNearMu"),
    doc  = cms.string("Scouting pixel vertices near muon"),
    singleton = cms.bool(False),
    extension = cms.bool(False),
    variables = cms.PSet(
        x = Var("x()", float, doc = "x position"),
        y = Var("y()", float, doc = "y position"),
        z = Var("z()", float, doc = "z position"),
        xErr = Var("xError()", float, doc = "error of x position"),
        yErr = Var("yError()", float, doc = "error of y position"),
        zErr = Var("zError()", float, doc = "error of z position"),
        chi2 = Var("chi2()", float, doc = "chi-square of the vertex fit"),
        nODF = Var("ndof()", int, doc = "degree of freedom of the vertex fit"),
        isValid = Var("isValidVtx()", bool, doc = "is valid vertex?"),
    )
)

# -- scouting calo jet table
# -- data format: https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/DataFormats/Scouting/interface/ScoutingCaloJet.h
scoutingCaloJetTable = cms.EDProducer("SimpleScoutingCaloJetFlatTableProducer",
    src = cms.InputTag("hltScoutingCaloPacker"),
    cut = cms.string(""),
    name = cms.string("SCCaloJet"),
    doc  = cms.string("Scouting calo jets"),
    singleton = cms.bool(False), # -- if only one object exists per event (e.g. MET): true. if not (e.g. muon), false.
    extension = cms.bool(False), # -- main table for the scouting muon (not extended version from the other table)
    variables = cms.PSet(
        pt  = Var("pt()", float, doc = "pt of the scouting calo jet"),
        eta = Var("eta()", float, doc = "eta of the scouting calo jet"),
        phi = Var("phi()", float, doc = "phi of the scouting calo jet"),
        m = Var("m()", float, doc = "m of the scouting calo jet"),
        jetArea  = Var("jetArea()", float, doc = "jetArea of the scouting calo jet"),
        maxEInEmTowers  = Var("maxEInEmTowers()", float, doc = "maxEInEmTowers of the scouting calo jet"),
        maxEInHadTowers  = Var("maxEInHadTowers()", float, doc = "maxEInHadTowers of the scouting calo jet"),
        hadEnergyInHB  = Var("hadEnergyInHB()", float, doc = "hadEnergyInHB of the scouting calo jet"),
        hadEnergyInHE  = Var("hadEnergyInHE()", float, doc = "hadEnergyInHE of the scouting calo jet"),
        hadEnergyInHF  = Var("hadEnergyInHF()", float, doc = "hadEnergyInHF of the scouting calo jet"),
        emEnergyInEB  = Var("emEnergyInEB()", float, doc = "emEnergyInEB of the scouting calo jet"),
        emEnergyInEE  = Var("emEnergyInEE()", float, doc = "emEnergyInEE of the scouting calo jet"),
        emEnergyInHF  = Var("emEnergyInHF()", float, doc = "emEnergyInHF of the scouting calo jet"),
        towersArea  = Var("towersArea()", float, doc = "towersArea of the scouting calo jet"),
        mvaDiscriminator  = Var("mvaDiscriminator()", float, doc = "mvaDiscriminator of the scouting calo jet"),
        btagDiscriminator  = Var("btagDiscriminator()", float, doc = "btagDiscriminator of the scouting calo jet"),
    )
)

scoutingTables = cms.Sequence(scoutingGlobalVarTable + scoutingMuonTable + scoutingDimuVertexTable + scoutingPixelVertexTable + scoutingPixelVertexNearMuTable + scoutingCaloJetTable)