# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 14:47:53 2020

@author: vpe
"""
import math 
def emm_calc(TET, m_air):
    
    ## Macro1 Macro
    ##
    
    ##
            
    #    #Input data
    ##Combustor inlet and outlet
    T3 = 553        #combustor inlet temperature [K]
    #TET = 1060 #Range("C2")  #4.2*Load+833       #combustor outlet temperature [K]
    P3 = 670000     #absolute combustor inlet pressure [Pa]
    #m_air = 5.15 #Range("C3")     #combustor inlet air mass flow rate [kg/s]
    N_comb = 4      #number of combustors
    
    #/Combustor dimensions
    D_casing = 0.212     #Combustor casing diameter [m]
    D_ft_out = 0.162    #Flame tube outlet diameter [m]
    D_PZ = 0.178         #Primizry zone diameter [m]
    L_PZ = 0.256         #Primary zone length [m]
    L_IZ = 0         #Lenght of intermediate and dilution zone [m]
    A_eff_liner = 0.0045       #Flame tube effective area [m2]
    S = 0.15                         #Standard deviation of air-fuel mixture: diffusion burner S=0, pre-mixed burner S={0;0.25}
    
    #Fuel composition (molar fraction)
    CH4 = 0.96
    C2H6 = 0
    C3H8 = 0
    C7H8 = 0
    Diesel = 0
    H2 = 0
    CO = 0
    N2 = 0.04
    CO2 = 0
    H2O = 0
    O2 = 0
    Tfuel = 298
    #LHV_fuel=50
    T_prim = 2479
    
    #Air
    O2_air = 0.209
    N2_air = 0.791
    
    
    #Air distribution over the combustor
    PZ = 0.504  #Primary zone split
    IZ = 0     #Intermediate zone split
    DZ = 1 - PZ - IZ #Dilution zone split
    
    
    ############Calculation of temperature rise over the combustor#############/
    
    #------------NASA polynoms coefficients------------
    #O2 coefficients
    #O2 200 - 1000K
    a111 = 3.78245636
    a112 = -0.00299673415
    a113 = 0.000009847302
    a114 = -9.68129508E-09
    a115 = 3.24372836E-12
    a116 = -1063.94356
    #O2 1000 - 5000K
    a121 = 3.66096083
    a122 = 0.000656365523
    a123 = -0.000000141149485
    a124 = 2.05797658E-11
    a125 = -1.29913248E-15
    a126 = -1215.97725
    
    #N2 coefficients
    #N2 200 - 1000K
    a211 = 3.53100528
    a212 = -0.000123660987
    a213 = -0.000000502999437
    a214 = 2.43530612E-09
    a215 = -1.40881235E-12
    a216 = -1046.97628
    #N2 1000 - 5000K
    a221 = 2.95257626
    a222 = 0.00139690057
    a223 = -0.000000492631691
    a224 = 7.86010367E-11
    a225 = -4.60755321E-15
    a226 = -923.948645
    
    #Ar coefficients
    #Ar 200 - 1000K
    a311 = 2.5
    a312 = 0
    a313 = 0
    a314 = 0
    a315 = 0
    a316 = -745
    #Ar 1000 - 5000K
    a321 = 2.5
    a322 = 0
    a323 = 0
    a324 = 0
    a325 = 0
    a326 = -745
    
    #CO2 coefficients
    #CO2 200 - 1000K
    a411 = 2.35677352
    a412 = 0.00898459677
    a413 = -0.00000712356269
    a414 = 2.45919022E-09
    a415 = -1.43699548E-13
    a416 = -48371.9697
    #CO2 1000 - 5000K
    a421 = 4.63659493
    a422 = 0.00274131991
    a423 = -0.000000995828531
    a424 = 1.60373011E-10
    a425 = -9.16103468E-15
    a426 = -49024.9341
    
    #H2O coefficients
    #H2O 200 - 1000K
    a511 = 4.19864056
    a512 = -0.0020364341
    a513 = 0.00000652040211
    a514 = -5.48797062E-09
    a515 = 1.77197817E-12
    a516 = -30293.7267
    #H2O 1000 - 5000K
    a521 = 2.67703787
    a522 = 0.00297318329
    a523 = -0.00000077376969
    a524 = 9.44336689E-11
    a525 = -4.26900959E-15
    a526 = -29885.8938
    
    #CO coefficients
    #CO 200 - 1000K
    a611 = 3.262452
    a612 = 0.000151
    a613 = -0.00000388
    a614 = 0.00000000558
    a615 = -0.00000000000247
    a616 = -0.00000000000143
    
    #CO 1000 - 5000K
    a621 = 3.025078
    a622 = 0.00144
    a623 = -0.000000563
    a624 = 0.000000000102
    a625 = -6.91E-15
    a626 = -14300
    
    #H2 coefficients
    #H2 200 - 1000K
    a711 = 3.298124
    a712 = 0.000825
    a713 = -0.000000814
    a714 = -0.0000000000948
    a715 = 0.000000000000413
    a716 = -1010
    
    #H2 1000 - 5000K
    a721 = 2.991423
    a722 = 0.0007
    a723 = -0.0000000563
    a724 = -0.00000000000923
    a725 = 1.58E-15
    a726 = -835
    
    #OH coefficients
    #OH 200 - 1000K
    a811 = 3.64
    a812 = 0.000185
    a813 = -0.00000168
    a814 = 0.00000000239
    a815 = -0.000000000000843
    a816 = 3610
    
    #OH 1000 - 5000K
    a821 = 2.88
    a822 = 0.00101
    a823 = -0.000000228
    a824 = 0.0000000000217
    a825 = -5.13E-16
    a826 = 3890
    
    #CH4 coefficients
    #CH4 200 - 1000K
    a1011 = 0.7787415
    a1012 = 0.01747668
    a1013 = -0.00002783409
    a1014 = 0.00000003049708
    a1015 = -1.223931E-11
    a1016 = -9825.229
    
    #CH4 1000 - 6000K
    a1021 = 1.683479
    a1022 = 0.01023724
    a1023 = -0.000003875129
    a1024 = 6.785585E-10
    a1025 = -4.503423E-14
    a1026 = -10080.79
    
    #C2H6 coefficients
    #C2H6 200 - 1000K
    a1111 = 4.29142492
    a1112 = -0.0055015427
    a1113 = 0.0000599438288
    a1114 = -7.08466285E-08
    a1115 = 2.68685771E-11
    a1116 = -11522.2055
    
    #C3H8 coefficients
    #C3H8 200 - 1000K
    a1211 = 4.2110262
    a1212 = 0.00171599803
    a1213 = 0.0000706183472
    a1214 = -9.19594116E-08
    a1215 = 3.64421372E-11
    a1216 = -14381.2106
    
    #Diesel coefficients
    #Diesel 200 - 1000K
    a1311 = 2.0869217
    a1312 = 0.13314965
    a1313 = -0.000081157452
    a1314 = 0.000000029409286
    a1315 = -6.5195213E-12
    a1316 = -35912.814
    
    #C7H8 (Toluene) coefficients
    #C7H8 200 - 1000K
    a1411 = 1.611914
    a1412 = 0.0211188902
    a1413 = 0.0000853221453
    a1414 = -0.000000132566876
    a1415 = 5.59406109E-11
    a1416 = 4096.51976
    
    #formation enthalpies
    Hf_CO2 = -93988 # -94049.46  #[cal/mol]
    Hf_H2O = -57796.766  #[cal/mol]
    Hf_CO = -26416.83  #[cal/mol]
    Hf_H = 52101.94 #[cal/mol]
    Hf_OH = 9404  #[cal/mol]
    #Hf_CH4 = -17908.7  #[cal/mol]
    Hf_O2 = 0
    Hf_N2 = 0
    Hf_H2 = 0
    Hf_CH4 = -17882.4
    Hf_C2H6 = -20040.6
    Hf_C3H8 = -25018.7
    Hf_Diesel = -59683.95
    Hf_C7H8 = 11982.9
    
    #delH0 enthalpies
    delH0_CO2 = -93988 #-94049.46
    delH0_H2O = -57796.766
    delH0_CO = -26416.83
    delH0_H = 52101.94
    delH0_OH = 9404
    #delH0_CH=-17882.4
    delH0_O2 = 0
    delH0_N2 = 0
    delH0_H2 = 0
    delH0_CH4 = -17882.4
    
    L_Diesel = 12845.62 #Diesel - latent heat of evaporation cal/mol
    
    R = 1.98718  #[cal/mol]
    
    #molar mass
    mw_O2 = 32
    mw_N2 = 28.02
    mw_CO2 = 44.01
    mw_H2O = 18.016
    mw_H2 = 2.016
    mw_CO = 28.01
    mw_C = 12.01
    mw_H = 1.008
    
    LHV = -((CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO + 7 * C7H8) * Hf_CO2 + (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) * Hf_H2O - (CH4 * Hf_CH4 + C2H6 * Hf_C2H6 + C3H8 * Hf_C3H8 + Diesel * Hf_Diesel + CO * Hf_CO + C7H8 * Hf_C7H8))
    
    
    mw_air = (O2_air * mw_O2 + N2_air * mw_N2)
    mw_fuel = (CH4 * (mw_C + 4 * mw_H) + C2H6 * (2 * mw_C + 6 * mw_H) + C3H8 * (3 * mw_C + 8 * mw_H) + Diesel * (15 * mw_C + 28 * mw_H) + CO2 * mw_CO2 + H2O * mw_H2O + O2 * mw_O2 + N2 * mw_N2 + CO * mw_CO + H2 * mw_H2 + C7H8 * (7 * mw_C + 8 * mw_H))
    R_air = 8314.472 / mw_air
    R_fuel = 8314.472 / mw_fuel
    #LHV=LHV_fuel*1000*mw_fuel/4.1868-L_Diesel*Diesel
    X_O2 = 1 / O2_air
    X_N2 = N2_air / O2_air
    
    ##############################################
    #air enthalpy at compressor outlet
    delH_T3_O2 = (a111 * T3 + a112 * T3 ** 2 / 2 + a113 * T3 ** 3 / 3 + a114 * T3 ** 4 / 4 + a115 * T3 ** 5 / 5 + a116) * R
    delH_T3_N2 = (a211 * T3 + a212 * T3 ** 2 / 2 + a213 * T3 ** 3 / 3 + a214 * T3 ** 4 / 4 + a215 * T3 ** 5 / 5 + a216) * R
    
    #fuel enthalpy in the inlet except CH
    delH_Tfuel_O2 = (a111 * Tfuel + a112 * Tfuel ** 2 / 2 + a113 * Tfuel ** 3 / 3 + a114 * Tfuel ** 4 / 4 + a115 * Tfuel ** 5 / 5 + a116) * R
    delH_Tfuel_N2 = (a211 * Tfuel + a212 * Tfuel ** 2 / 2 + a213 * Tfuel ** 3 / 3 + a214 * Tfuel ** 4 / 4 + a215 * Tfuel ** 5 / 5 + a216) * R
    delH_Tfuel_CO2 = (a411 * Tfuel + a412 * Tfuel ** 2 / 2 + a413 * Tfuel ** 3 / 3 + a414 * Tfuel ** 4 / 4 + a415 * Tfuel ** 5 / 5 + a416) * R
    delH_Tfuel_H2O = (a511 * Tfuel + a512 * Tfuel ** 2 / 2 + a513 * Tfuel ** 3 / 3 + a514 * Tfuel ** 4 / 4 + a515 * Tfuel ** 5 / 5 + a516) * R
    delH_Tfuel_CO = (a611 * Tfuel + a612 * Tfuel ** 2 / 2 + a613 * Tfuel ** 3 / 3 + a614 * Tfuel ** 4 / 4 + a615 * Tfuel ** 5 / 5 + a616) * R
    delH_Tfuel_H2 = (a711 * Tfuel + a712 * Tfuel ** 2 / 2 + a713 * Tfuel ** 3 / 3 + a714 * Tfuel ** 4 / 4 + a715 * Tfuel ** 5 / 5 + a716) * R
    delH_Tfuel_CH4 = (a1011 * Tfuel + a1012 * Tfuel ** 2 / 2 + a1013 * Tfuel ** 3 / 3 + a1014 * Tfuel ** 4 / 4 + a1015 * Tfuel ** 5 / 5 + a1016) * R
    delH_Tfuel_C2H6 = (a1111 * Tfuel + a1112 * Tfuel ** 2 / 2 + a1113 * Tfuel ** 3 / 3 + a1114 * Tfuel ** 4 / 4 + a1115 * Tfuel ** 5 / 5 + a1116) * R
    delH_Tfuel_C3H8 = (a1211 * Tfuel + a1212 * Tfuel ** 2 / 2 + a1213 * Tfuel ** 3 / 3 + a1214 * Tfuel ** 4 / 4 + a1215 * Tfuel ** 5 / 5 + a1216) * R
    delH_Tfuel_Diesel = (a1311 * Tfuel + a1312 * Tfuel ** 2 / 2 + a1313 * Tfuel ** 3 / 3 + a1314 * Tfuel ** 4 / 4 + a1315 * Tfuel ** 5 / 5 + a1316) * R
    delH_Tfuel_C7H8 = (a1411 * Tfuel + a1412 * Tfuel ** 2 / 2 + a1413 * Tfuel ** 3 / 3 + a1414 * Tfuel ** 4 / 4 + a1415 * Tfuel ** 5 / 5 + a1416) * R
    
    ###############################################
    #########/-----------combustion products enthalpy-----------############/
    ###############################################
    #------TET < 1000 K------
    delH_CO2_1_C = (a411 * TET + a412 * TET ** 2 / 2 + a413 * TET ** 3 / 3 + a414 * TET ** 4 / 4 + a415 * TET ** 5 / 5 + a416) * R
    delH_CO2_1_CO = (a411 * TET + a412 * TET ** 2 / 2 + a413 * TET ** 3 / 3 + a414 * TET ** 4 / 4 + a415 * TET ** 5 / 5 + a416) * R
    
    
    delH_H2O_1_H = (a511 * TET + a512 * TET ** 2 / 2 + a513 * TET ** 3 / 3 + a514 * TET ** 4 / 4 + a515 * TET ** 5 / 5 + a516) * R
    delH_T4_O2_1 = (a111 * TET + a112 * TET ** 2 / 2 + a113 * TET ** 3 / 3 + a114 * TET ** 4 / 4 + a115 * TET ** 5 / 5 + a116) * R
    delH_T4_N2_1 = (a211 * TET + a212 * TET ** 2 / 2 + a213 * TET ** 3 / 3 + a214 * TET ** 4 / 4 + a215 * TET ** 5 / 5 + a216) * R
    delH_T4_CO2_1 = (a411 * TET + a412 * TET ** 2 / 2 + a413 * TET ** 3 / 3 + a414 * TET ** 4 / 4 + a415 * TET ** 5 / 5 + a416) * R
    delH_T4_H2O_1 = (a511 * TET + a512 * TET ** 2 / 2 + a513 * TET ** 3 / 3 + a514 * TET ** 4 / 4 + a515 * TET ** 5 / 5 + a516) * R
    
    delH_O2_1 = delH_T4_O2_1 - delH_T3_O2
    delH_N2_1 = delH_T4_N2_1 - delH_T3_N2
    
    
    delH_O2_fuel_1 = delH_T4_O2_1 - delH_Tfuel_O2
    delH_N2_fuel_1 = delH_T4_N2_1 - delH_Tfuel_N2
    delH_CO2_fuel_1 = delH_T4_CO2_1 - delH_Tfuel_CO2
    delH_H2O_fuel_1 = delH_T4_H2O_1 - delH_Tfuel_H2O
    
    #------TET > 1000 K------
    delH_CO2_2_C = (a421 * TET + a422 * TET ** 2 / 2 + a423 * TET ** 3 / 3 + a424 * TET ** 4 / 4 + a425 * TET ** 5 / 5 + a426) * R
    delH_CO2_2_CO = (a421 * TET + a422 * TET ** 2 / 2 + a423 * TET ** 3 / 3 + a424 * TET ** 4 / 4 + a425 * TET ** 5 / 5 + a426) * R
    delH_H2O_2_H = (a521 * TET + a522 * TET ** 2 / 2 + a523 * TET ** 3 / 3 + a524 * TET ** 4 / 4 + a525 * TET ** 5 / 5 + a526) * R
    delH_T4_O2_2 = (a121 * TET + a122 * TET ** 2 / 2 + a123 * TET ** 3 / 3 + a124 * TET ** 4 / 4 + a125 * TET ** 5 / 5 + a126) * R
    delH_T4_N2_2 = (a221 * TET + a222 * TET ** 2 / 2 + a223 * TET ** 3 / 3 + a224 * TET ** 4 / 4 + a225 * TET ** 5 / 5 + a226) * R
    delH_T4_CO2_2 = (a421 * TET + a422 * TET ** 2 / 2 + a423 * TET ** 3 / 3 + a424 * TET ** 4 / 4 + a425 * TET ** 5 / 5 + a426) * R
    delH_T4_H2O_2 = (a521 * TET + a522 * TET ** 2 / 2 + a523 * TET ** 3 / 3 + a524 * TET ** 4 / 4 + a525 * TET ** 5 / 5 + a526) * R
    
    delH_O2_2 = delH_T4_O2_2 - delH_T3_O2
    delH_N2_2 = delH_T4_N2_2 - delH_T3_N2
    
    delH_O2_fuel_2 = delH_T4_O2_2 - delH_Tfuel_O2
    delH_N2_fuel_2 = delH_T4_N2_2 - delH_Tfuel_N2
    delH_CO2_fuel_2 = delH_T4_CO2_2 - delH_Tfuel_CO2
    delH_H2O_fuel_2 = delH_T4_H2O_2 - delH_Tfuel_H2O
    
    X1 = (LHV - (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + 7 * C7H8 + CO) * (delH_T4_CO2_1 - Hf_CO2) - (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) * (delH_T4_H2O_1 - Hf_H2O) + (2 * CH4 + 3.5 * C2H6 + 5 * C3H8 + 22 * Diesel + H2 / 2 + CO / 2 + 9 * C7H8) * delH_O2_1 - CH4 * (delH_Tfuel_CH4 - Hf_CH4) - C2H6 * (delH_Tfuel_C2H6 - Hf_C2H6) - C3H8 * (delH_Tfuel_C3H8 - Hf_C3H8) - Diesel * (delH_Tfuel_Diesel - Hf_Diesel) - C7H8 * (delH_Tfuel_C7H8 - Hf_C7H8) - CO * (delH_Tfuel_CO - Hf_CO) - H2 * (delH_Tfuel_H2) - CO2 * delH_CO2_fuel_1 - H2O * delH_H2O_fuel_1 - O2 * delH_O2_fuel_1 - N2 * delH_N2_fuel_1) / (delH_O2_1 + X_N2 * delH_N2_1)
    
    X2 = (LHV - (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + 7 * C7H8 + CO) * (delH_T4_CO2_2 - Hf_CO2) - (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) * (delH_T4_H2O_2 - Hf_H2O) + (2 * CH4 + 3.5 * C2H6 + 5 * C3H8 + 22 * Diesel + H2 / 2 + CO / 2 + 9 * C7H8) * delH_O2_2 - CH4 * (delH_Tfuel_CH4 - Hf_CH4) - C2H6 * (delH_Tfuel_C2H6 - Hf_C2H6) - C3H8 * (delH_Tfuel_C3H8 - Hf_C3H8) - Diesel * (delH_Tfuel_Diesel - Hf_Diesel) - C7H8 * (delH_Tfuel_C7H8 - Hf_C7H8) - CO * (delH_Tfuel_CO - Hf_CO) - H2 * (delH_Tfuel_H2) - CO2 * delH_CO2_fuel_2 - H2O * delH_H2O_fuel_2 - O2 * delH_O2_fuel_2 - N2 * delH_N2_fuel_2) / (delH_O2_2 + X_N2 * delH_N2_2)
    
    if (TET < 1000):
        X_OV = X1
    elif (TET >= 1000):
        X_OV = X2
    
    
    AFR = mw_air * X_OV * X_O2 / mw_fuel
    AFR_OV = AFR
    X_S = (2 * CH4 + 3.5 * C2H6 + 5 * C3H8 + 22 * Diesel + H2 / 2 + CO / 2 + 9 * C7H8)
    Phi_OV = X_S / X_OV
    
    #disp("H_O2_1="+string(delH_T4_O2_1), "H_O2_2="+string(delH_T4_O2_2), "H_N2_1="+string(delH_T4_N2_1), "H_N2_2="+string(delH_T4_N2_2), "H_CO2_1="+string(delH_T4_CO2_1), "H_CO2_2="+string(delH_T4_CO2_2), "H_H2O_1="+string(delH_T4_H2O_1), "H_H2O_2="+string(delH_T4_H2O_2))
    
    
    #####################################################################
    #####/Primary zone properties#######/
    ########################/
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    AFR_PZ = AFR_OV * PZ           #Primary zone air-to-fuel ratio
    X_PZ = AFR_PZ * mw_fuel / mw_air / X_O2 #number of mol of air per one mol of fuel
    Phi_PZ = X_S / X_PZ
    
    P_O2_1 = 1
    P_N2_1 = 1
    
    delH_PZ = 0
    T_f1 = TET
    dT = 100
    Q_comb = LHV
    
    while (abs(abs(delH_PZ) - abs(Q_comb)) > 10):
    
        T_f1 = T_f1 + dT
        
        
        Kp1_CO2 = (math.exp((-2.51639E-12 * T_f1 ** 4 + 0.0000000224292 * T_f1 ** 3 - 0.0000778729 * T_f1 ** 2 + 0.131213122 * T_f1 - 96.76853846) * -1))
        Kp1_H2O = (math.exp((-2.6191E-12 * T_f1 ** 4 + 0.0000000232607 * T_f1 ** 3 - 0.0000803923 * T_f1 ** 2 + 0.134909277 * T_f1 - 101.1856037) * -1))
        Kp1_O = 1
        Kp1_N = 1
        ##Stoichiometric coefficients
        CO_PZ = (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO + 7 * C7H8) / (1 + Kp1_CO2 * P_O2_1 ** 0.5)
        H2_PZ = (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) / (1 + Kp1_H2O * P_O2_1 ** 0.5)
        CO2_PZ = (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO + 7 * C7H8) - CO_PZ
        CO2_f = CO2
        H2O_PZ = (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) - H2_PZ
        H2O_f = H2O
        O2_PZ = X_PZ - (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO / 2 - CO_PZ / 2 + 7 * C7H8) - H2O_PZ / 2 + O2
        N2_air = X_N2 * X_PZ
        N2_f = N2
        
        Z_PZ = CO_PZ + H2_PZ + CO2_PZ + CO2_f + H2O_PZ + H2O_f + O2_PZ + N2_air + N2_f
        
        O2_mol_1 = O2_PZ / Z_PZ * 100
        N2_mol_1 = (N2_air + N2_f) / Z_PZ * 100
        CO2_mol_1 = (CO2_PZ + CO2_f) / Z_PZ * 100
        CO_mol_1 = (CO_PZ) / Z_PZ * 100
        H2O_mol_1 = (H2O_PZ + H2O_f) / Z_PZ * 100
        H2_mol_1 = (H2_PZ) / Z_PZ * 100
        
        P_O2_1 = O2_mol_1 * (P3 / 100000) / 100         #oxygen partial pressure
        P_N2_1 = N2_mol_1 * (P3 / 100000) / 100         #nitrogen partial pressure
        P_CO2_1 = CO2_mol_1 * (P3 / 100000) / 100       #carbon dioxide partial pressure
        P_CO_1 = CO_mol_1 * (P3 / 100000) / 100         #carbon monoxide partial pressure
        P_H2O_1 = H2O_mol_1 * (P3 / 100000) / 100       #water partial pressure
        P_H2_1 = H2_mol_1 * (P3 / 100000) / 100         #hydrogen partial pressure
        
        #---PRODUCTS OF REACTIONS---
        delH_CO2_PZ = (a421 * T_f1 + a422 * T_f1 ** 2 / 2 + a423 * T_f1 ** 3 / 3 + a424 * T_f1 ** 4 / 4 + a425 * T_f1 ** 5 / 5 + a426) * R
        delH_CO_PZ = (a621 * T_f1 + a622 * T_f1 ** 2 / 2 + a623 * T_f1 ** 3 / 3 + a624 * T_f1 ** 4 / 4 + a625 * T_f1 ** 5 / 5 + a626) * R
        delH_H2O_PZ = (a521 * T_f1 + a522 * T_f1 ** 2 / 2 + a523 * T_f1 ** 3 / 3 + a524 * T_f1 ** 4 / 4 + a525 * T_f1 ** 5 / 5 + a526) * R
        delH_H2_PZ = (a721 * T_f1 + a722 * T_f1 ** 2 / 2 + a723 * T_f1 ** 3 / 3 + a724 * T_f1 ** 4 / 4 + a725 * T_f1 ** 5 / 5 + a726) * R
        delH_O2_PZ = (a121 * T_f1 + a122 * T_f1 ** 2 / 2 + a123 * T_f1 ** 3 / 3 + a124 * T_f1 ** 4 / 4 + a125 * T_f1 ** 5 / 5 + a126) * R
        delH_N2_PZ = (a221 * T_f1 + a222 * T_f1 ** 2 / 2 + a223 * T_f1 ** 3 / 3 + a224 * T_f1 ** 4 / 4 + a225 * T_f1 ** 5 / 5 + a226) * R
        delH_CH_PZ = (a1021 * T_f1 + a1022 * T_f1 ** 2 / 2 + a1023 * T_f1 ** 3 / 3 + a1024 * T_f1 ** 4 / 4 + a1025 * T_f1 ** 5 / 5 + a1026) * R
        
        delH_O2_PZ_air = delH_O2_PZ - delH_T3_O2
        delH_N2_PZ_air = delH_N2_PZ - delH_T3_N2
        
        delH_O2_PZ_fuel = delH_O2_PZ - delH_Tfuel_O2
        delH_N2_PZ_fuel = delH_N2_PZ - delH_Tfuel_N2
        delH_CO2_PZ_fuel = delH_CO2_PZ - delH_Tfuel_CO2
        delH_H2O_PZ_fuel = delH_H2O_PZ - delH_Tfuel_H2O
        
        Q_comb = H2O_PZ * Hf_H2O + CO2_PZ * Hf_CO2 + CO_PZ * Hf_CO - (CH4 * Hf_CH4 + C2H6 * Hf_C2H6 + C3H8 * Hf_C3H8 + Diesel * (Hf_Diesel - L_Diesel) + CO * Hf_CO + C7H8 * Hf_C7H8)
        
        LHV_theo = (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO + 7 * C7H8) * Hf_CO2 + (2 * CH4 + 3 * C2H6 + 4 * C3H8 + 14 * Diesel + H2 + 4 * C7H8) * Hf_H2O - (CH4 * Hf_CH4 + C2H6 * Hf_C2H6 + C3H8 * Hf_C3H8 + Diesel * Hf_Diesel + CO * Hf_CO + C7H8 * Hf_C7H8)
        
        delH_PZ = (CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + 7 * C7H8) * (delH_CO2_PZ - Hf_CO2) + H2O_PZ * (delH_H2O_PZ - Hf_H2O) + CO_PZ * (delH_CO_PZ - Hf_CO) + H2_PZ * (delH_H2_PZ - Hf_H2) + (O2_PZ - O2) * delH_O2_PZ_air + N2_air * delH_N2_PZ_air + CO2_f * delH_CO2_PZ_fuel + H2O_f * delH_H2O_PZ_fuel + O2 * delH_O2_PZ_fuel + N2_f * delH_N2_PZ_fuel - CH4 * (delH_Tfuel_CH4 - Hf_CH4) + C2H6 * (delH_Tfuel_C2H6 - Hf_C2H6) + C3H8 * (delH_Tfuel_C3H8 - Hf_C3H8) + Diesel * (delH_Tfuel_Diesel - Hf_Diesel) + H2 * (delH_Tfuel_H2) + CO * (delH_Tfuel_CO - Hf_CO) + C7H8 * (delH_Tfuel_C7H8 - Hf_C7H8)
        
        
        if (abs(delH_PZ) - abs(Q_comb) == 0):
            dT = 0
        elif (abs(delH_PZ) - abs(Q_comb) > 0):
            dT = -1
        elif (abs(delH_PZ) - abs(Q_comb) < 0) and (dT == -1):
            dT = 0.001
        
    
    
    comb_eff = Q_comb / LHV_theo
    
    R_comb_out = (R_air * AFR + R_fuel) / (AFR + 1) #gas constant - combustion gas at outlet [J/kg/K]
    R_comb_pz = (R_air * AFR_PZ + R_fuel) / (AFR_PZ + 1) #gas constant - combustion gas at primary zone[J/kg/K]
    ##/Combustor pressure loss and primary zone residence time
    m_comb = m_air / N_comb
    Rho_air = P3 / T3 / R_air
    V_air = m_comb / Rho_air
    A_eff_casing = (D_casing ** 2 - D_ft_out ** 2) * 3.14159265358979 / 4
    v_air_casing = V_air / A_eff_casing
    delP_casing = 0.5 * Rho_air * v_air_casing ** 2
    
    v_air_liner = V_air / A_eff_liner
    delP_liner = 0.5 * Rho_air * v_air_liner ** 2
    
    m_pz = m_comb * (PZ + 1 / AFR)
    Rho_PZ = (P3) / T_f1 / R_comb_out
    PZ_vol_flow = m_pz / Rho_PZ
    PZ_volume = D_PZ ** 2 * 3.14159265358979 / 4 * L_PZ
    t_res_PZ = PZ_volume / PZ_vol_flow
    #disp(+string(Rho_PZ))
    m_comb_out = m_comb * (1 + 1 / AFR)
    Rho_out = (P3 - delP_casing - delP_liner) / TET / R_comb_out
    vol_flow_liner = m_comb_out / Rho_out
    A_out = 3.14159265358979 / 4 * D_ft_out ** 2
    v_out = vol_flow_liner / 3.14159265358979 / 4 * D_ft_out ** 2 #A_out
    delP_outlet = 0.5 * Rho_out * v_out ** 2
    
    T_IZ = T_f1 - (T_f1 - TET) / (1 - PZ) * IZ
    Rho_IZ = (P3 - delP_casing - delP_liner) / T_IZ / R_comb_out
    vol_flow_IZ = m_comb_out / Rho_IZ
    vol_IZ = D_ft_out ** 2 * 3.14159265358979 / 4 * L_IZ
    t_res_IZ = vol_IZ / vol_flow_IZ
    
    delP_tot = delP_casing + delP_liner + delP_outlet
    CPL = delP_tot / P3 * 100
    
    #T_f1=T_prim
    #/++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #############################################################/
    #####-------------------------CARBON MONOXIDE BURN OUT RATE IN PRIMARY ZONE-----------------------##########
    #############################################################/
    CO2_PZ1 = CO2_f
    CO_PZ1 = CH4 + 2 * C2H6 + 3 * C3H8 + 15 * Diesel + CO + 7 * C7H8
    H2O_PZ1 = H2O_PZ + H2O_f
    H2_PZ1 = H2_PZ
    O2_PZ1 = X_PZ - H2O_PZ / 2 - (CH4 / 2 + C2H6 + 1.5 * C3H8 + 7.5 * Diesel + 3.5 * C7H8) + O2 + H2O_f
    N2_PZ1 = X_N2 * X_PZ + N2_f
    
    Z_PZ1 = CO2_PZ1 + CO_PZ1 + H2O_PZ1 + H2_PZ1 + O2_PZ1 + N2_PZ1
    
    CO2_mol_1 = CO2_PZ1 / Z_PZ1
    CO_mol_1 = CO_PZ1 / Z_PZ1
    H2O_mol_1 = H2O_PZ1 / Z_PZ1
    H2_mol_1 = H2_PZ1 / Z_PZ1
    O2_mol_1 = O2_PZ1 / Z_PZ1
    N2_mol_1 = N2_PZ1 / Z_PZ1
    #disp("CO2="+string(CO2_mol_1), "N2="+string(N2_mol_1),"O2="+string(O2_mol_1),"CO="+string(CO_mol_1),"H2O="+string(H2O_mol_1),"H2="+string(H2_mol_1))
    #----------------Reaction rates for defienition of partial equilibrium of O, H and OH radicals---------------------
    k_f1 = 18000000000 * T_f1 * math.exp(-8826 / R / T_f1)       #O+H2<->OH+H
    k_r1 = 8000000000 * T_f1 * math.exp(-6760 / R / T_f1)
    
    k_f2 = 200000000000000 * math.exp(-16800 / R / T_f1)      #H+O2<->OH+O
    k_r2 = 15800000000000 * math.exp(-690 / R / T_f1)
    
    k_f3 = 1170000000 * T_f1 ** 1.3 * math.exp(-3626 / R / T_f1)   #H2+OH<->H2O+H
    k_r3 = 5090000000 * T_f1 ** 1.3 * math.exp(-18588 / R / T_f1)
    
    k_f4 = 4200000000000 * math.exp(-47769 / R / T_f1)        #CO+O2<->CO2+O
    
    k_r4 = 281000000000 * math.exp(-52546 / R / T_f1)
    
    k_f5 = 15100000 * T_f1 ** 1.3 * math.exp(758 / R / T_f1)       #CO+OH<->CO2+H
    k_r5 = 1570000000 * T_f1 ** 1.3 * math.exp(-22337 / R / T_f1)
    
    k_f6 = 180000000 * math.exp(-38370 / T_f1)                        #O+N2<->N+NO
    k_r6 = 38000000 * math.exp(-425 / T_f1)
    
    k_f7 = 18000 * T_f1 * math.exp(-4680 / T_f1)                        #N+O2<->O+NO
    k_r7 = 3800 * T_f1 * math.exp(-20820 / T_f1)
    
    k_f8 = 71000000 * math.exp(-450 / T_f1)                           #N+OH<->H+NO
    k_r8 = 170000000 * math.exp(-24560 / T_f1)
    
    #Molar volume of reactants
    V_CO2 = P3 * (CO2_mol_1) / R / T_f1 * 0.000001
    V_CO = P3 * (CO_mol_1) / R / T_f1 * 0.000001
    V_H2 = P3 * (H2_mol_1) / R / T_f1 * 0.000001
    V_H2O = P3 * (H2O_mol_1) / R / T_f1 * 0.000001
    V_O2 = P3 * (O2_mol_1) / R / T_f1 * 0.000001
    V_N2 = P3 * (N2_mol_1) / R / T_f1 * 0.000001
    V_H = ((k_f1 * k_f2 * k_f3 ** 2 * V_O2 * V_H2 ** 3) / (k_r1 * k_r2 * k_r3 ** 2 * V_H2O ** 2)) ** 0.5
    V_O = (k_f2 * k_f3 * V_O2 * V_H2) / (k_r2 * k_r3 * V_H2O)
    V_OH = ((k_f1 * k_f2) / (k_r1 * k_r2) * V_O2 * V_H2) ** 0.5
    
    t1 = 0
    dt1 = 0.0001
    Sum = Z_PZ1
    
    #Do While t1 < t_res_PZ
    while (t1 < t_res_PZ):
    
        t1 = t1 + dt1
    
        ForwardPZ = V_CO * V_OH * k_f5 + V_CO * V_O2 * k_f4
        ReversePZ = V_CO2 * V_H * k_r5 + V_CO2 * V_O * k_r4
    
        VdelCO2 = (ForwardPZ - ReversePZ) * dt1
    
        delCO2 = VdelCO2 * 1000000 * T_f1 * R / (P3) * Z_PZ1
        CO_1 = V_CO * 1000000 * T_f1 * R / (P3) * Z_PZ1 - delCO2
    
        CO2_1 = V_CO2 * 1000000 * T_f1 * R / (P3) * Z_PZ1 + delCO2
        O2_1 = V_O2 * 1000000 * T_f1 * R / (P3) * Z_PZ1 - delCO2 / 2
        H2O_1 = V_H2O * 1000000 * T_f1 * R / (P3) * Z_PZ1
        N2_1 = V_N2 * 1000000 * T_f1 * R / (P3) * Z_PZ1
    
        Z_PZ1 = CO_1 + CO2_1 + O2_1 + H2O_1 + N2_1
    
        X_CO2 = CO2_1 / Z_PZ1
        X_CO = CO_1 / Z_PZ1
        X_H2O = H2O_1 / Z_PZ1
        X_O2 = O2_1 / Z_PZ1
        X_N2 = N2_1 / Z_PZ1
    
        V_CO2 = P3 * X_CO2 / R / T_f1 * 0.000001
        V_CO = P3 * X_CO / R / T_f1 * 0.000001
        V_H2O = P3 * X_H2O / R / T_f1 * 0.000001
        V_O2 = P3 * X_O2 / R / T_f1 * 0.000001
        V_N2 = P3 * X_N2 / R / T_f1 * 0.000001
        V_H = ((k_f1 * k_f2 * k_f3 ** 2 * V_O2 * V_H2 ** 3) / (k_r1 * k_r2 * k_r3 ** 2 * V_H2O ** 2)) ** 0.5
        V_O = (k_f2 * k_f3 * V_O2 * V_H2) / (k_r2 * k_r3 * V_H2O)
        V_OH = ((k_f1 * k_f2) / (k_r1 * k_r2) * V_O2 * V_H2) ** 0.5
    
    
    CO_emis = V_CO * 1000000 * T_f1 * R / (P3) * 1000000
    
    
    R1 = 8.314
    V_O2_no = P3 * (O2_mol_1) / R1 / T_f1
    V_H2O_no = P3 * (H2O_mol_1) / R1 / T_f1
    V_N2_no = P3 * (N2_mol_1) / R1 / T_f1
    V_O_no = 36.64 * T_f1 ** 0.5 * V_O2_no ** 0.5 * math.exp(-27123 / T_f1)
    V_OH_no = 212.9 * T_f1 ** -0.57 * math.exp(-4595 / T_f1) * V_O_no ** 0.5 * V_H2O_no ** 0.5
    
    V_NO_1 = 0
    t_no = 0
    dt_no = 0.0001
    while (t_no < t_res_PZ):
        
        t_no = t_no + dt_no
        
        delV_NO_1 = 2 * k_f6 * V_O_no * V_N2_no * (1 - (k_r6 * k_r7 * V_NO_1 ** 2) / (k_f6 * V_N2_no * k_f7 * V_O2_no)) / (1 + (k_r6 * V_NO_1) / (k_f7 * V_O2_no + k_f8 * V_OH_no)) * dt_no
        V_NO_1 = V_NO_1 + delV_NO_1
    
    uniformity_factor = 1.244 * math.exp(14.4 * S) - 0.244
    NO_emis1 = V_NO_1 * T_f1 * R1 / (P3) * 1000000 * uniformity_factor
    
    V_NO = ((0.8 / T_f1 ** 0.5) * (76000000000000 * math.exp(-76000 / R / T_f1)) * V_N2 * V_O2 ** 0.5) * math.exp(-62000 / R / T_f1) * t_res_PZ
    
    NO_emis = V_NO * 1000000 * T_f1 * R / (P3) * 1000000
    #############################################################/
    #####---------------CARBON MONOXIDE BURN OUT RATE IN INTERMEDIATE AND DILUSION ZONE---------------##########
    #############################################################/
    #Composition of combution gas in dilution zone
    CO2_dil = PZ * CO2_mol_1
    CO_dil = PZ * V_CO * 1000000 * T_f1 * R / (P3) * Z_PZ1
    H2O_dil = PZ * H2O_mol_1
    H2_dil = PZ * H2_mol_1
    O2_dil = PZ * O2_mol_1 + IZ * O2_air
    N2_dil = PZ * N2_mol_1 + IZ * N2_air
    
    Z_DZ = CO2_dil + CO_dil + H2O_dil + H2_dil + O2_dil + N2_dil
    
    CO2_mol_2 = CO2_dil / Z_DZ
    CO_mol_2 = CO_dil / Z_DZ
    H2O_mol_2 = H2O_dil / Z_DZ
    H2_mol_2 = H2_dil / Z_DZ
    O2_mol_2 = O2_dil / Z_DZ
    N2_mol_2 = N2_dil / Z_DZ
    
    #----------------Reaction rates for defienition of partial equilibrium of O, H and OH radicals---------------------
    k_f1 = 18000000000 * T_IZ * math.exp(-8826 / R / T_IZ)       #O+H2<->OH+H
    k_r1 = 8000000000 * T_IZ * math.exp(-6760 / R / T_IZ)
    
    k_f2 = 200000000000000 * math.exp(-16800 / R / T_IZ)      #H+O2<->OH+O
    k_r2 = 15800000000000 * math.exp(-690 / R / T_IZ)
    
    k_f3 = 1170000000 * T_IZ ** 1.3 * math.exp(-3626 / R / T_IZ)   #H2+OH<->H2O+H
    k_r3 = 5090000000 * T_IZ ** 1.3 * math.exp(-18588 / R / T_IZ)
    
    k_f4 = 4200000000000 * math.exp(-47769 / R / T_IZ)        #CO+O2<->CO2+O
    k_r4 = 281000000000 * math.exp(-52546 / R / T_IZ)
    
    k_f5 = 15100000 * T_IZ ** 1.3 * math.exp(758 / R / T_IZ)       #CO+OH<->CO2+H
    k_r5 = 1570000000 * T_IZ ** 1.3 * math.exp(-22337 / R / T_IZ)
    
    #Molar volume of reactants
    V_CO2 = P3 * (CO2_mol_2) / R / T_IZ * 0.000001
    V_CO = P3 * (CO_mol_2) / R / T_IZ * 0.000001
    V_H2 = P3 * (H2_mol_2) / R / T_IZ * 0.000001
    V_H2O = P3 * (H2O_mol_2) / R / T_IZ * 0.000001
    V_O2 = P3 * (O2_mol_2) / R / T_IZ * 0.000001
    V_N2 = P3 * (N2_mol_2) / R / T_IZ * 0.000001
    V_H = ((k_f1 * k_f2 * k_f3 ** 2 * V_O2 * V_H2 ** 3) / (k_r1 * k_r2 * k_r3 ** 2 * V_H2O ** 2)) ** 0.5
    V_O = (k_f2 * k_f3 * V_O2 * V_H2) / (k_r2 * k_r3 * V_H2O)
    V_OH = ((k_f1 * k_f2) / (k_r1 * k_r2) * V_O2 * V_H2) ** 0.5
    
    t2 = 0
    dt2 = 0.0001
    while (t2 < t_res_IZ):
        t2 = t2 + dt2
    
        Forward = V_CO * V_OH * k_f5 + V_CO * V_O2 * k_f4
        Reverse = V_CO2 * V_H * k_r5 + V_CO2 * V_O * k_r4
    
        VdelCO2 = (Forward - Reverse) * dt2
    
        delCO2 = VdelCO2 * 1000000 * T_IZ * R / (P3) * Z_DZ
        CO_1 = V_CO * 1000000 * T_IZ * R / (P3) * Z_DZ - delCO2
    
        CO2_1 = V_CO2 * 1000000 * T_IZ * R / (P3) * Z_DZ + delCO2
        O2_1 = V_O2 * 1000000 * T_IZ * R / (P3) * Z_DZ - delCO2 / 2
        H2O_1 = V_H2O * 1000000 * T_IZ * R / (P3) * Z_DZ
        N2_1 = V_N2 * 1000000 * T_IZ * R / (P3) * Z_DZ
    
        Z_DZ = CO_1 + CO2_1 + O2_1 + H2O_1 + N2_1
    
        X_CO2 = CO2_1 / Z_DZ
        X_CO = CO_1 / Z_DZ
        X_H2O = H2O_1 / Z_DZ
        X_O2 = O2_1 / Z_DZ
        X_N2 = N2_1 / Z_DZ
    
        V_CO2 = P3 * X_CO2 / R / T_IZ * 0.000001
        V_CO = P3 * X_CO / R / T_IZ * 0.000001
        V_H2O = P3 * X_H2O / R / T_IZ * 0.000001
        V_O2 = P3 * X_O2 / R / T_IZ * 0.000001
        V_N2 = P3 * X_N2 / R / T_IZ * 0.000001
        V_H = ((k_f1 * k_f2 * k_f3 ** 2 * V_O2 * V_H2 ** 3) / (k_r1 * k_r2 * k_r3 ** 2 * V_H2O ** 2)) ** 0.5
        V_O = (k_f2 * k_f3 * V_O2 * V_H2) / (k_r2 * k_r3 * V_H2O)
        V_OH = ((k_f1 * k_f2) / (k_r1 * k_r2) * V_O2 * V_H2) ** 0.5
        
    
    CO_emis1 = V_CO * 1000000 * T_IZ * R / (P3) * 1000000
        
    # Range("F2") = CO_emis1
    # Range("F3") = NO_emis1
    # Range("F4") = m_air / AFR
    result = [CO_emis1, NO_emis1, m_air / AFR]    
    
    return result


#print (emm_calc(1060, 5.144))

