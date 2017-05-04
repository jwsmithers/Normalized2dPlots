from ROOT import *


gStyle.SetOptStat(0); 
#myfile = TFile("/eos/atlas/user/j/jwsmith/reprocessedNtuples/merged_from_julien/v007/ttbar.root","read")
myfile = TFile("/eos/atlas/user/j/jwsmith/reprocessedNtuples/merged_from_julien/v007/ttbar.root","read")
myttree = myfile.Get("nominal")

c = TCanvas("c")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram1(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==1", "COLZ norm ")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram2(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==2", "COLZ norm ")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram3(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==3", "COLZ norm ")
#myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram4(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==4", "COLZ norm ")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram5(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==6", "COLZ norm ")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram6(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==10", "COLZ norm ")
myttree.Draw("event_photonorigin:ph_HFT_MVA[selph_index1]>>histogram7(20,0.000000,1,20,0.5,20.5)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && event_photonorigin==20", "COLZ norm")

h_sum = TH2D("test","test",20,0.000000,1,20,0.5,20.5)
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
y1.SetTitle("Photon Origin")
x1 = h_sum.GetXaxis()
x1.SetTitle("ph_HFT_MVA[selph_index1]")

c.SaveAs("photonorigin_HFT_MVA.png")

# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram1(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] < 0.1", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram2(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.1 && ph_HFT_MVA[selph_index1] < 0.2", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram3(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.2 && ph_HFT_MVA[selph_index1] < 0.3", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram4(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.3 && ph_HFT_MVA[selph_index1] < 0.4", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram5(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.4 && ph_HFT_MVA[selph_index1] < 0.5", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram6(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.5 && ph_HFT_MVA[selph_index1] < 0.6", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram7(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.6 && ph_HFT_MVA[selph_index1] < 0.7", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram8(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.7 && ph_HFT_MVA[selph_index1] < 0.8", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram9(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >= 0.8 && ph_HFT_MVA[selph_index1] < 0.9", "col2z ")
# myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>histogram10(100,0,200,50,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4 && ph_HFT_MVA[selph_index1] >=9", "col2z ")

#myttree.Draw("ph_HFT_MVA[selph_index1]:ph_pt/1e3>>h_sum(50,20,200,40,0,1)","event_ngoodphotons==1 && ph_isTight && ph_pt > 20000 && event_njets >= 4", "col2z norm ")


# h_sum = TH2D("test","test",100,0,200,50,0,1)
# h_sum.Add(histogram1);
# h_sum.Add(histogram2);
# h_sum.Add(histogram3);
# h_sum.Add(histogram4);
# h_sum.Add(histogram5);
# h_sum.Add(histogram6);
# h_sum.Add(histogram7);
# h_sum.Add(histogram8);
# h_sum.Add(histogram9);
# h_sum.Add(histogram10);


#h_sum.Draw("COL2Z norm ")
#h_sum.SetTitle("")
#y1 = h_sum.GetYaxis()
#y1.SetTitle("ph_HFT_MVA[selph_index1]")
#x1 = h_sum.GetXaxis()
#x1.SetTitle("ph_pt")
#c.SaveAs("HFT_MVA_ph_pt.png");

