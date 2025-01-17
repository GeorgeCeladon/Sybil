# E' necessario aver copiato la cartella sybil nelle cartella delle librerie di python 
from sybil import Serie, Sybil

# Load a trained model, con ensemble sembra non funzionare
model = Sybil("sybil_base")


# Get risk scores
serie = Serie(['D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00002.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00003.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00004.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00005.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00006.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00007.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00008.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00009.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00010.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00011.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00012.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00013.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00014.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00015.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00016.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00017.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00018.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00019.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00020.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00021.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00022.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00023.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00024.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00025.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00026.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00027.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00028.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00029.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00030.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00031.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00032.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00033.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00034.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00035.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00036.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00037.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00038.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00039.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00040.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00041.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00042.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00043.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00044.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00045.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00046.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00047.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00048.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00049.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00050.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00051.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00052.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00053.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00054.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00055.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00056.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00057.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00058.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00059.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00060.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00061.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00062.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00063.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00064.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00065.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00066.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00067.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00068.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00069.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00070.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00071.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00072.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00073.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00074.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00075.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00076.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00077.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00078.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00079.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00080.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00081.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00082.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00083.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00084.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00085.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00086.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00087.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00088.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00089.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00090.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00091.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00092.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00093.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00094.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00095.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00096.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00097.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00098.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00099.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00100.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00101.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00102.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00103.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00104.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00105.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00106.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00107.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00108.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00109.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00110.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00111.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00112.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00113.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00114.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00115.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00116.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00117.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00118.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00119.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00120.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00121.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00122.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00123.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00124.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00125.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00126.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00127.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00128.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00129.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00130.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00131.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00132.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00133.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00134.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00135.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00136.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00137.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00138.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00139.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00140.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00141.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00142.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00143.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00144.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00145.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00146.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00147.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00148.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00149.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00150.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00151.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00152.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00153.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00154.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00155.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00156.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00157.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00158.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00159.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00160.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00161.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00162.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00163.DCM',
'D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.d530.it.orbassano.S1.4263439.1_00164.DCM',
])
scores = model.predict([serie])

# You can also evaluate by providing labels
# serie = Serie(['D:\#Software Repository\Sybil\dicom\LDCT512\A2.orb.66e3.it.orbassano.S1.3968019.1_00001.DCM'], label=1)
# results = model.evaluate([serie])

# crea i dati per fare l'immagine
results = model.predict([serie], return_attentions=True)
attentions = results.attentions

# Stampa in console le previsioni ottenute
print(scores)


# Crea la heatmap
from sybil import visualize_attentions
series_with_attention = visualize_attentions(
    serie,
    attentions = attentions,
    save_directory = "./",
    gain = 3, 
)
