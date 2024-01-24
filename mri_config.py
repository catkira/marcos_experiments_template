data_path = "~/" 

lo_freq = 17.302 # MHz

# Shim
shim_x = 0.01
shim_y = -0.02
shim_z = -0.02
shim_z2 = 0.0
shim = (shim_x, shim_y, shim_z, shim_z2)

gamma = 42570000 # Hz/T    
max_grad_current = 8 # amps
if True:
    grad_max_Hz_per_m = 19E6 # experimental value
    grad_max_x_Hz_per_m = 19E6
    grad_max_y_Hz_per_m = 21E6
    grad_max_z_Hz_per_m = 19E6
    grad_max_z2_Hz_per_m = 19E6
else:
    # value for tabletopMRI  gradient coil
    grad_B_per_m_per_current = 0.02 # [T/m/A], approximate value for tabletop gradient coil

    # values for gpa fhdo
    gpa_current_per_volt = 2.5 # gpa fhdo 6A configuration
    max_dac_voltage = 2.5
    grad_max_Hz_per_m = max_dac_voltage * gpa_current_per_volt * grad_B_per_m_per_current * gamma	


if True:
    hf_max_Hz_per_m = 19000 # experimental value
else:    
    # values of tabletop coil
    R_coil = 2
    hf_B_per_m_current = 2.483E-4 # [T/A] theoretical value

    # values for red pitaya 
    hf_max_dac_voltage = 1 # +-

    # HF-PA
    hf_PA_gain = 20 # dB
    
    hf_max_Hz_per_m = np.sqrt(1/50 * 10**(hf_PA_gain/10) / R_coil) * hf_B_per_m_current * gamma    

