# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:52:43 2022

@author: braya
"""

infos = {
 'WW': {'DSID'    : 105985,
        'events'  : 2499890,
        'red_eff' : 0.388,
        'sumw'    : 2489550.66,
        'xsec'    : 20.90286},

 'ZZ': {'DSID'    : 105986,
        'events'  : 245000,
        'red_eff' : 0.95088,
        'sumw'    : 243674.74,
        'xsec'    : 1.5376},

 'WZ': {'DSID'    : 105987,
        'events'  : 999998,
        'red_eff' : 0.96668,
        'sumw'    : 996210.5,
        'xsec'    : 6.9673},

 'stop_tchan_top': {'DSID'    : 110090,
                    'events'  : 4994481,
                    'red_eff' : 0.08947185,
                    'sumw'    : 0.087147591,
                    'xsec'    : 18.39495},

 'stop_tchan_antitop': {'DSID': 110091,
                        'events': 4944880,
                        'red_eff': 0.058425933,
                        'sumw': 0.046283642,
                        'xsec': 9.95976},

 'stop_schan': {'DSID'    : 110119,
                'events'  : 5999781,
                'red_eff' : 0.051100576,
                'sumw'    : 5972600.588,
                'xsec'    : 1.817694},



 'stop_wtchan': {'DSID'    : 110140,
                 'events'  : 999692,
                 'red_eff' : 0.636162836,
                 'sumw'    : 996333.734,
                 'xsec'    : 22.3014},

 'ZPrime400': {'DSID'    : 110899,
               'events'  : 100000,
               'red_eff' : 1,
               'sumw'    : 99711.94,
               'xsec'    : 4.2589},
               
 'ZPrime500': {'DSID'    : 110901,
               'events'  : 100000,
               'red_eff' : 1,
               'sumw'    : 99492.841,
               'xsec'    : 3.925},

 'ZPrime750': {'DSID'    : 110902,
               'events'  : 100000,
               'red_eff' : 1,
               'sumw'    : 99473.46,
               'xsec'    : 1.243},

 'ZPrime1000': {'DSID'    : 110903,
                'events'  : 99999,
                'red_eff' : 1,
                'sumw'    : 99854.551,
                'xsec'    : 0.3937},

 'ZPrime1250': {'DSID'    : 110904,
                'events'  : 100000,
                'red_eff' : 1,
                'sumw'    : 99847.67,
                'xsec'    : 0.1387},

 'ZPrime1500': {'DSID'    : 110905,
                'events'  : 99999,
                'red_eff' : 1,
                'sumw'    : 99613.589,
                'xsec'    : 0.0524},

 'ZPrime1750': {'DSID'    : 110906,
                'events'  : 99997,
                'red_eff' : 1,
                'sumw'    : 99471.892,
                'xsec'    : 0.0211},

 'ZPrime2000': {'DSID'    : 110907,
                'events'  : 99900,
                'red_eff' : 1,
                'sumw'    : 99693.276,
                'xsec'    : 0.00894},

 'ZPrime2250': {'DSID'    : 110908,
                'events'  : 100000,
                'red_eff' : 1,
                'sumw'    : 99618.188,
                'xsec'    : 0.00394},

 'ZPrime2500': {'DSID'    : 110909,
                'events'  : 100000,
                'red_eff' : 1,
                'sumw'    : 99661.651,
                'xsec'    : 0.0018},

 'ZPrime3000': {'DSID'    : 110910,
                'events'  : 99499,
                'red_eff' : 1,
                'sumw'    : 99104.295,
                'xsec'    : 0.000434},

 'ttbar_had': {'DSID'    : 117049,
               'events'  : 9822240,
               'red_eff' : 1,
               'sumw'    : 9753687.763,
               'xsec'    : 115.518854},

 'ttbar_lep': {'DSID'    : 117050,
               'events'  : 49973332,
               'red_eff' : 0.072212854,
               'sumw'    : 49761200.21,
               'xsec'    : 137.29749},

 'Zee': {'DSID'    : 147770,
         'events'  : 50182160,
         'red_eff' : 0.151816307,
         'sumw'    : 203795455568148.0,
         'xsec'    : 1241.2072},

 'Zmumu': {'DSID'    : 147771,
           'events'  : 96086594,
           'red_eff' : 0.124706551,
           'sumw'    : 225316022111048.0,
           'xsec'    : 1241.2072},

 'Ztautau': {'DSID'    : 147772,
             'events'  : 14968269,
             'red_eff' : 0.921502294,
             'sumw'    : 31508540303680.9,
             'xsec'    : 1240.8988},

 'WenuWithB': {'DSID'    : 167740,
               'events'  : 14717449,
               'red_eff' : 0.129496439,
               'sumw'    : 4260058.061,
               'xsec'    : 154.374},

 'WenuJetsBVeto': {'DSID'    : 167741,
                   'events'  : 5659977,
                   'red_eff' : 0.981554126,
                   'sumw'    : 1719244.25,
                   'xsec'    : 591.624},

 'WenuNoJetsBVeto': {'DSID'   : 167742,
                     'events' : 23588938,
                     'red_eff': 0.946929361,
                     'sumw'   : 13179098.28,
                     'xsec'   : 11324.5},

 'WmunuWithB': {'DSID'    : 167743,
                'events'  : 13850964,
                'red_eff' : 0.133223309,
                'sumw'    : 4010756.4,
                'xsec'    : 154.429},


 'WmunuJetsBVeto': {'DSID'    : 167744,
                    'events'  : 5999888,
                    'red_eff' : 0.905793003,
                    'sumw'    : 1726755.472,
                    'xsec'    : 513.117},
                    
 'WmunuNoJetsBVeto': {'DSID'    : 167745,
                      'events'  : 20782761,
                      'red_eff' : 0.943743915,
                      'sumw'    : 11600960.24,
                      'xsec'    : 11404.8},

 'WtaunuWithB': {'DSID'    : 167746,
                 'events'  : 14999453,
                 'red_eff' : 0.188978183,
                 'sumw'    : 4343529.568,
                 'xsec'    : 154.374},

 'WtaunuJetsBVeto': {'DSID'    : 167747,
                     'events'  : 5999680,
                     'red_eff' : 0.913648001,
                     'sumw'    : 1776192.932,
                     'xsec'    : 557.095},
                     
 'WtaunuNoJetsBVeto': {'DSID'    : 167748,
                       'events'  : 23844450,
                       'red_eff' : 0.926932574,
                       'sumw'    : 13316520.62,
                       'xsec'    : 11359.7},
    
 'DYeeM08to15': {'DSID'    : 173041,
                 'events'  : 4999994,
                 'red_eff' : 0.893071694,
                 'sumw'    : 4772549.624,
                 'xsec'    : 92.15},

 'DYeeM15to40': {'DSID'    : 173042,
                 'events'  : 13980986,
                 'red_eff' : 0.945799529,
                 'sumw'    : 13895470.42,
                 'xsec'    : 279.19},

 'DYmumuM08to15': {'DSID'    : 173043,
                   'events'  : 4996000,
                   'red_eff' : 0.960298189,
                   'sumw'    : 4977032.008,
                   'xsec'    : 92.08},

 'DYmumuM15to40': {'DSID'    : 173044,
                   'events'  : 14960488,
                   'red_eff' : 0.999654588,
                   'sumw'    : 11510844.32,
                   'xsec'    : 279.2},

 'DYtautauM08to15': {'DSID'    : 173045,
                     'events'  : 2499696,
                     'red_eff' : 1,
                     'sumw'    : 2489620.309,
                     'xsec'    : 92.12},

 'DYtautauM15to40': {'DSID'    : 173046,
                     'events'  : 13828870,
                     'red_eff' : 1,
                     'sumw'    : 13704752.81,
                     'xsec'    : 279.11},

 'ggH125_ZZ4lep': {'DSID': 160155,
                   'events': 200000,
                   'red_eff': 0.854398386,
                   'sumw': 198997.386,
                   'xsec': 0.00538752},

 'VBFH125_ZZ4lep': {'DSID': 160205,
                    'events': 199999,
                    'red_eff': 0.767804987,
                    'sumw': 199291.076,
                    'xsec': 0.000435528},

 'ggH125_WW2lep': {'DSID': 161005,
                   'events': 500000,
                   'red_eff': 0.357042356,
                   'sumw': 497986.026,
                   'xsec': 0.21288},

 'VBFH125_WW2lep': {'DSID': 161055,
                    'events': 300000,
                    'red_eff': 0.544650854,
                    'sumw': 298858.242,
                    'xsec': 0.0181},


 'Zprime_ee': {'DSID': 158020,
               'events': 20000,
               'red_eff': 1,
               'sumw': 20000,
               'xsec': 0.1515},
 'Zprime_mm': {'DSID': 158026,
               'events': 20000,
               'red_eff': 1,
               'sumw': 20000,
               'xsec': 0.15323},
}