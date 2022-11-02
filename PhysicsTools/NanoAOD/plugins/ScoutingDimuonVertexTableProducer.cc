// -- Author: Kyeongpil Lee (kplee@cern.ch)

// -- Produce a flat table to save scouting dimuon vertex information
// -- It will save the associated scouting muon index for each vertex
// -- -> no need to save vector<int> vtx_Indx of scouting muon (which is not easy to save in nanoAOD flat format)
// -- written based on VertexTableProducer.cc


// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

// -- scouting
#include "DataFormats/Scouting/interface/ScoutingVertex.h"
#include "DataFormats/Scouting/interface/ScoutingMuon.h"

#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

#include "DataFormats/NanoAOD/interface/FlatTable.h"



//
// class declaration
//

class ScoutingDimuonVertexTableProducer : public edm::stream::EDProducer<> {
public:
  explicit ScoutingDimuonVertexTableProducer(const edm::ParameterSet&);
  ~ScoutingDimuonVertexTableProducer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginStream(edm::StreamID) override;
  void produce(edm::Event&, const edm::EventSetup&) override;
  void endStream() override;

  void GetMuonIndex_AssociatedToVertex(edm::Event& iEvent, const ScoutingVertex& vtx, int theVtxIndex, int& index1_mu, int& index2_mu);

  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  // ----------member data ---------------------------

  const edm::EDGetTokenT< std::vector<ScoutingVertex> > t_SCDimuonVtx_;
  const edm::EDGetTokenT< std::vector<ScoutingMuon> >   t_SCMuon_;

};

//
// constructors and destructor
//
ScoutingDimuonVertexTableProducer::ScoutingDimuonVertexTableProducer(const edm::ParameterSet& iConfig):
t_SCDimuonVtx_( consumes< std::vector<ScoutingVertex> >(iConfig.getParameter<edm::InputTag>("SCDimuonVtx")) ),
t_SCMuon_(       consumes< std::vector<ScoutingMuon>   >(iConfig.getParameter<edm::InputTag>("SCMuon")) ) {

  produces<nanoaod::FlatTable>("SCDimuonVtx");

}

ScoutingDimuonVertexTableProducer::~ScoutingDimuonVertexTableProducer() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
}

void ScoutingDimuonVertexTableProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  using namespace edm;
  
  // -- save information
  std::vector<float> vtx_x, vtx_y, vtx_z, vtx_xErr, vtx_yErr, vtx_zErr, vtx_chi2;
  std::vector<int> vtx_trackSize, vtx_nDOF, vtx_muonIndex1, vtx_muonIndex2;
  std::vector<bool> vtx_isValid;

  edm::Handle< std::vector<ScoutingVertex> > h_SCDimuonVtx;
  iEvent.getByToken( t_SCDimuonVtx_, h_SCDimuonVtx );

  unsigned int nVtx = 0;
  // -- fill the vector
  if( h_SCDimuonVtx.isValid() ) { // -- if dimuon vertex is available in the event:
    for(unsigned int i_vtx=0; i_vtx<h_SCDimuonVtx->size(); ++i_vtx) {
      // std::cout << "dimuon vertex: available" << std::endl;

      nVtx = h_SCDimuonVtx->size();

      const ScoutingVertex &vtx = (*h_SCDimuonVtx)[i_vtx];

      vtx_x.push_back( vtx.x() );
      vtx_y.push_back( vtx.y() );
      vtx_z.push_back( vtx.z() );
      vtx_xErr.push_back( vtx.xError() );
      vtx_yErr.push_back( vtx.yError() );
      vtx_zErr.push_back( vtx.zError() );
      vtx_chi2.push_back( vtx.chi2() );

      vtx_trackSize.push_back( vtx.tracksSize() );
      vtx_nDOF.push_back( vtx.ndof() );

      int index1_mu, index2_mu;
      GetMuonIndex_AssociatedToVertex(iEvent, vtx, i_vtx, index1_mu, index2_mu);
      vtx_muonIndex1.push_back( index1_mu );
      vtx_muonIndex2.push_back( index2_mu );

      vtx_isValid.push_back( vtx.isValidVtx() );
    }
  }
  else { // -- if not: fill empty values
    // std::cout << "dimuon vertex: NOT available" << std::endl;

    nVtx = 0;

    vtx_x.clear();
    vtx_y.clear();
    vtx_z.clear();
    vtx_xErr.clear();
    vtx_yErr.clear();
    vtx_zErr.clear();
    vtx_chi2.clear();

    vtx_trackSize.clear();
    vtx_nDOF.clear();

    vtx_muonIndex1.clear();
    vtx_muonIndex2.clear();

    vtx_isValid.clear();
  }


  // -- fill the table
  auto table = std::make_unique<nanoaod::FlatTable>(nVtx, "SCDimuonVtx", false);
  table->addColumn<float>("x", vtx_x, "x position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("y", vtx_y, "y position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("z", vtx_z, "z position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("xErr", vtx_xErr, "error of x position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("yErr", vtx_yErr, "error of y position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("zErr", vtx_zErr, "error of z position", nanoaod::FlatTable::FloatColumn);
  table->addColumn<float>("chi2", vtx_chi2, "vertex chi-square", nanoaod::FlatTable::FloatColumn);

  table->addColumn<int>("trackSize",  vtx_trackSize,  "track size", nanoaod::FlatTable::IntColumn);
  table->addColumn<int>("nDOF",       vtx_nDOF,       "degree of freedom of the vertex fit", nanoaod::FlatTable::IntColumn);
  table->addColumn<int>("muonIndex1", vtx_muonIndex1, "index of the 1st scouting muon associated with the vertex", nanoaod::FlatTable::IntColumn);
  table->addColumn<int>("muonIndex2", vtx_muonIndex2, "index of the 2nd scouting muon associated with the vertex", nanoaod::FlatTable::IntColumn);

  // -- not addColumn<bool>: it will give "unsupported type" error
  // -- according to https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_27/DataFormats/NanoAOD/interface/FlatTable.h#L156-L168
  table->addColumn<uint8_t>("isValid", vtx_isValid, "is valid vertex?", nanoaod::FlatTable::BoolColumn); 

  iEvent.put(std::move(table), "SCDimuonVtx");
}

void ScoutingDimuonVertexTableProducer::GetMuonIndex_AssociatedToVertex(edm::Event& iEvent, const ScoutingVertex& vtx, int theVtxIndex, int& index1_mu, int& index2_mu) {
  index1_mu = -1;
  index2_mu = -1;

  edm::Handle< std::vector<ScoutingMuon> > h_SCMuon;
  iEvent.getByToken( t_SCMuon_, h_SCMuon );

  for(unsigned int i_mu=0; i_mu<h_SCMuon->size(); ++i_mu) {
    const auto& mu = (*h_SCMuon)[i_mu];

    std::vector<int> vec_vtxIndex = mu.vtxIndx();

    for(int i_vtx : vec_vtxIndex) {
      if( theVtxIndex == i_vtx ) {
        if( index1_mu == -1 )      index1_mu = i_mu;
        else if( index2_mu == -1 ) index2_mu = i_mu;
        else
          std::cout << "(Index1_mu, index2_mu) = (" << index1_mu << ", " << index2_mu << "): already filled --> the " << i_mu << "th muon will be ignored" << std::endl;

        if( index1_mu != -1 && index2_mu != -1 ) break; // -- to speed up
      }
    } // -- iteration over vertex index associated with the given muon
  } // -- iteration over muons  
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void ScoutingDimuonVertexTableProducer::beginStream(edm::StreamID) {}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void ScoutingDimuonVertexTableProducer::endStream() {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void ScoutingDimuonVertexTableProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ScoutingDimuonVertexTableProducer);

