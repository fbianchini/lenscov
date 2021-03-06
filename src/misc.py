# Copyright (C) 2016 Peloton
import numpy as np
import os

def get_exp_configuration(exp='_test_'):
	'''
	Quick access to pre-configured experimental configurations.
	Input:
		* exp: string, name of the experiment to simulated
	Output:
		* noise_uK_arcmin: float, level of noise in uK.arcmin
		* fwhm_arcmin: float, beam size (FWHM) in arcmin
		* lmin: int, minimum multipole for the reconstruction
		* lmax: int, maximum multipole for the reconstruction
		* folder_cache: string, where the data will be saved
	'''
	do_cori = False
	do_edison = False
	if os.getenv('NERSC_HOST')=='cori':
		do_cori = True
		folder_cache = os.path.join(os.getenv('SCRATCH'),'cache')
	elif os.getenv('NERSC_HOST')=='edison':
		do_edison = True
		folder_cache = os.path.join(os.getenv('SCRATCH'),'cache')
	else:
		folder_cache = 'cache'

	if exp == '_test_':
		lmin = 2
		lmax = 250
		noise_uK_arcmin = 1.0
		fwhm_arcmin = 1.0
		TTcorr = False
	elif exp == 'Planck':
		'''
		From Schmittfull et al 13
		'''
		lmin = 2
		lmax = 2500
		noise_uK_arcmin = 27.0
		fwhm_arcmin = 7.0
		TTcorr = False
	elif exp == 'Core++':
		'''
		From Jojo article (1509.06770) @ 150 GHz
		'''
		lmin = 2
		lmax = 4000
		noise_uK_arcmin = 5.0
		fwhm_arcmin = 6.0
		TTcorr = False
	elif exp == 'CMB-S4':
		'''
		From Jojo article (1509.06770) @ 150 GHz
		Comment: I find the lmax a bit low, however if
		we take into account that the main contribution at high ell is
		the point source contribution, foregrounds etc. it sounds somehow ok.
		'''
		lmin = 20
		lmax = 3000
		noise_uK_arcmin = 1.5
		fwhm_arcmin = 3.0
		TTcorr = False
	elif exp == 'CMB-S4_noisecorr':
		'''
		Same as above, but with a correlated noise component for the noise.
		'''
		lmin = 20
		lmax = 3000
		noise_uK_arcmin = 1.5
		fwhm_arcmin = 3.0
		TTcorr = 1000

	return noise_uK_arcmin, fwhm_arcmin, lmin, lmax, TTcorr, folder_cache

def add_text_imshow(ax,text,array):
	lmin=0
	lmax=len(array[0])
	ax.text(lmin,lmax,text,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round',alpha=0.9,ec='none'),weight='bold')
