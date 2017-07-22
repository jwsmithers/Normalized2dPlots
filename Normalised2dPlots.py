from ROOT import *
import glob


gStyle.SetOptStat(0); 


allMC=["3610XX.VV.p2952.v007.001.root"
,"3641XX.Wenu.p2952.v007.001.root"
,"3641XX.Wmunu.p2952.v007.001.root"
,"3641XX.Wtaunu.p2952.v007.001.root"
,"3641XX.Zee.p2952.v007.001.root"
,"3641XX.Zmumu.p2952.v007.001.root"
,"3641XX.Ztautau.p2952.v007.001.root"
,"364XXX.eegamma.p3152.v007.001.root"
,"364XXX.enugamma.p3152.v007.001.root"
,"364XXX.mumugamma.p3152.v007.001.root"
,"364XXX.munugamma.p3152.v007.001.root"
,"364XXX.taunugamma.p3152.v007.001.root"
,"410082.ttgamma_noallhad.p2952.v007.001.root"
,"4100XX.ST_others.p2952.v007.001.root"
,"4100XX.ST_Wt_inclusive.p2952.v007.001.root"
,"410501.ttbar_nonallhad_P8.p2952.v007.001.root"]
signalMC=["410082.ttgamma_noallhad.p2952.v007.001.root"]

def btagVsELD(typeOfevent,channel):

  if channel=="SL":
    channelLabel="Single lepton"
    toKeep = ["ejets","mujets"]
  if channel=="DL":
    channelLabel="Dilepton"
    toKeep = ["ee","mumu","emu"]


  path = "/eos/atlas/user/j/jwsmith/reprocessedNtuples/v007_flattened/SR1/"
  myttree = TChain("nominal")

  if typeOfevent == "all":
    typeOfevent_label = "Signal+Background"
    for i in allMC:
      for ch in toKeep:
        ntuples = glob.glob(path+ch+"/"+i)
        for n in ntuples:
          myttree.Add(n)

  if typeOfevent == "signal":
    typeOfevent_label = "Signal"
    for i in signalMC:
      for ch in toKeep:
        ntuples = glob.glob(path+ch+"/"+i)
        for n in ntuples:
          myttree.Add(n)

  if typeOfevent == "background":
    typeOfevent_label = "Background"
    for i in list(set(allMC)-set(signalMC)):
      for ch in toKeep:
        ntuples = glob.glob(path+ch+"/"+i)
        for n in ntuples:
          myttree.Add(n)

  c = TCanvas("c")

  cutstring=" event_ngoodphotons == 1 && "
  # eventweight=""
  typeOfPlot="COLZ norm"
  eventweight="weight_mc*weight_pileup*ph_SF_eff[selph_index1]*ph_SF_iso[selph_index1]*weight_leptonSF*weight_jvt*weight_bTagSF_Continuous*event_norm * event_lumi *  "

  # myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram(20,0,1,6,1,5)",  eventweight + cutstring + " event_nbjets77 == 0 " , typeOfPlot)
  myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram1(20,0,1,4,1,5)", eventweight + " (" + cutstring + "  event_nbjets77 == 1) " , typeOfPlot)
  myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram2(20,0,1,4,1,5)", eventweight + " ("  + cutstring + " event_nbjets77 == 2) " , typeOfPlot)
  myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram3(20,0,1,4,1,5)", eventweight + " ("  + cutstring + " event_nbjets77 == 3) " , typeOfPlot)
  myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram4(20,0,1,4,1,5)", eventweight + " ("  + cutstring + " event_nbjets77 >= 4) ",  typeOfPlot)
  #myttree.Draw("event_nbjets77:event_ELD_MVA>> histogram5(20,0,1,5,0.5,5.5)", eventweight + " ("  + cutstring + " event_nbjets77 == 5) ",  typeOfPlot)

  ylabels = ["1","2","3","#ge4"]

  h_sum = TH2D("test","test",20,0,1,4,1,5)
  # h_sum.Add(histogram);
  h_sum.Add(histogram1);
  h_sum.Add(histogram2);
  h_sum.Add(histogram3);
  h_sum.Add(histogram4);
 # h_sum.Add(histogram5);

  h_sum.Draw("COLZ ")
  h_sum.SetTitle("")
  h_sum.SetMinimum(0)
  y1 = h_sum.GetYaxis()
  y1.SetTitle("# of b-tagged jets")
  x1 = h_sum.GetXaxis()
  x1.SetTitle("event level discriminator")

  y1.SetNdivisions(-004)  
  y1.ChangeLabel(-1,-1,-1,-1,-1,-1,"#geq4")
  y1.CenterLabels(True)

  lumi = TLatex();
  lumi.SetNDC();
  lumi.SetTextAlign(12);
  lumi.SetTextFont(63);
  lumi.SetTextSizePixels(15);
  lumifb = 36.1
  lumi.DrawLatex(0.15,0.87, "#it{#scale[1.2]{ATLAS}} #bf{Internal}");
  lumi.DrawLatex(0.15,0.82,"#sqrt{s}=13 TeV, " + str(lumifb) +" fb^{-1}");
  lumi.DrawLatex(0.15,0.77, " #bf{"+typeOfevent_label+"}");
  lumi.DrawLatex(0.15,0.72, " #bf{"+channelLabel+"}");

  c.SaveAs("btagVSEld_"+typeOfevent+"_"+channel+".eps")

# Weird memory leak? I have to do these one at a time...
#btagVsELD("all", "SL")
#btagVsELD("background","SL")
#btagVsELD("signal","SL")
#
#btagVsELD("all", "DL")
#btagVsELD("background","DL")
btagVsELD("signal","DL")

def photonOriginVsPPT():

  path = "/eos/atlas/user/j/jwsmith/reprocessedNtuples/v007_flattened/CR1/*/"
  myttree = TChain("nominal")

  ntuples = glob.glob(path+"*.root")
  for i in ntuples:
    myttree.Add(i)

  c = TCanvas("c")

  cuts="event_ngoodphotons==1 && ph_isoFCT[selph_index1]"
  # eventweight="(weight_mc*weight_pileup*ph_SF_eff[selph_index1]*ph_SF_iso[selph_index1]*weight_leptonSF*weight_jvt*weight_bTagSF_Continuous*event_norm * event_lumi)"

  cutstring=cuts

  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram1(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==1", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram2(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==2", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram3(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==3", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram4(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==4", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram5(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==6", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram6(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==10", "COLZ norm ")
  myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram7(20,0,1,20,0.5,20.5)", cutstring + " && event_photonorigin==20", "COLZ norm")

  h_sum = TH2D("test","test",20,0,1,20,0.5,20.5)
  h_sum.Add(histogram1);
  h_sum.Add(histogram2);
  h_sum.Add(histogram3);
  #h_sum.Add(histogram4);
  h_sum.Add(histogram5);
  h_sum.Add(histogram6);
  h_sum.Add(histogram7);

  h_sum.Draw("COLZ ")
  h_sum.SetTitle("")
  y1 = h_sum.GetYaxis()
  y1.SetTitle("Photon type")
  x1 = h_sum.GetXaxis()
  x1.SetTitle("prompt photon tagger")
  lumi = TLatex();
  lumi.SetNDC();
  lumi.SetTextAlign(12);
  lumi.SetTextFont(63);
  lumi.SetTextSizePixels(15);
  lumifb = 36.1
  lumi.DrawLatex(0.35,0.65, "#it{#scale[1.2]{ATLAS}} #bf{Internal}");
  lumi.DrawLatex(0.35,0.6,"#sqrt{s}=13 TeV, " + str(lumifb) +" fb^{-1}");

  c.SaveAs("photonorigin_HFT_MVA.eps")

# photonOriginVsPPT()

