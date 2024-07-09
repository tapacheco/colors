import pandas as pd
from itertools import combinations

def photometry_to_colors(photometry_GCs):
    colors_GCs = []
    columns = photometry_GCs.columns
    for pair in combinations(columns, 2):
        subtraction = photometry_GCs[pair[0]] - photometry_GCs[pair[1]]
        data_subtraction = pd.DataFrame({f'{pair[0]}-{pair[1]}': subtraction})
        data_subtraction.fillna(-99, inplace=True)
        colors_GCs.append(data_subtraction)
    colors_output = pd.concat(colors_GCs, axis=1)
    return colors_output
