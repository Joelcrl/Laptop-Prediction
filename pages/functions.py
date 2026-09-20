import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import re

class ResolutionToPixels(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None): return self
    def transform(self, X):
        def to_pixels(val):
            if isinstance(val, str):
                m = re.match(r'(\d+)x(\d+)', val)
                if m: return int(m.group(1)) * int(m.group(2))
            return np.nan
        arr = np.array(X).flatten()
        return np.array([to_pixels(v) for v in arr]).reshape(-1, 1)

class VramEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None): return self
    def transform(self, X):
        def to_num(val):
            if isinstance(val, str):
                if val.lower() == 'shared': return 0
                m = re.match(r'(\d+)gb', val, re.I)
                if m: return int(m.group(1))
            return np.nan
        arr = np.array(X).flatten()
        return np.array([to_num(v) for v in arr]).reshape(-1, 1)

class MultiHotEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        flat = np.array(X).flatten()
        all_vals = set(v for cell in flat for v in (cell if isinstance(cell, list) else []))
        self.categories_ = sorted(all_vals)
        return self
    def transform(self, X):
        flat = np.array(X).flatten()
        return np.array([
            [int(cat in cell) if isinstance(cell, list) else 0 for cat in self.categories_]
            for cell in flat
        ])

def to_str(X):
    return X.astype(str)