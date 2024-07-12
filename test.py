import pandas as pd
from astropy.table import Table
from itertools import combinations
import src.tap_colors.photometry as ptm

data = Table.read('/home/thayse/Documents/analysis_M81/data/m81_photometry.fits')
photometry_GCs =  pd.DataFrame({'uJAVA': data['umag'],
                                'J0378': data['J378'],
                                'J0395': data['J395'],
                                'J0410': data['J410'],
                                'J0430': data['J430'],
                                'gSDSS': data['gmag'],
                                'J0515': data['J515'],
                                'rSDSS': data['rmag'],
                                'J0660': data['J660'],
                                'iSDSS': data['imag'],
                                'J0861': data['J861'],
                                'zSDSS': data['zmag']})

for key in photometry_GCs:
    if photometry_GCs[key].dtype.byteorder == '>':
        photometry_GCs[key] = photometry_GCs[key].values.byteswap().newbyteorder()

colFact = ptm.ColorsFactory()
colFact.compute_colors(photometry_GCs)
colFact.write_output('/home/thayse/Documents/syntheticMagnitudes/colors_JPAS_m81data.csv')
print(colFact.colors_GCs)