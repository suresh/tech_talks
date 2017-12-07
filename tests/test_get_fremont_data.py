from unittest import TestCase

import numpy as np
import pandas as pd

from jupyterworkflow.data import get_fremont_data


class TestGet_fremont_data(TestCase):

    def test_get_fremont_data(self):
        data = get_fremont_data()
        assert all(data.columns == ['West', 'East', 'Total'])
        assert isinstance(data.index, pd.DatetimeIndex)
        assert len(np.unique(data.index.time) == 24)
