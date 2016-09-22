from .models import DeviceData

import numpy as np
import pandas as pd
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot


df = pd.DataFrame(list(DeviceData.objects.all().values()))
print(df)
