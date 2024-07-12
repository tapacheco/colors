import pandas as pd
from itertools import combinations

class ColorsFactory():
    def __init__(self):
        self.photometry_GCs = {}
        self.colors_GCs = pd.DataFrame()

    def compute_colors(self, photometry):
        self.photometry_GCs = photometry.columns
        data_subtraction = []
        for pair in combinations(self.photometry_GCs, 2):
            subtraction = photometry[pair[0]] - photometry[pair[1]]
            data_subtraction = pd.DataFrame({f'{pair[0]}-{pair[1]}': subtraction})
            data_subtraction.fillna(-99, inplace=True)
            self.colors_GCs = pd.concat([self.colors_GCs, data_subtraction], axis=1)

    def write_output(self, file):
        self.colors_GCs.to_csv(file, sep=' ', index=False)
        

