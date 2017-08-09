import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.rcParams['savefig.dpi'] = 144

import numpy as np
import pandas as pd
from binascii import hexlify   # binascii: convert btw binary and ASCII
import math

# bokeh plot
from bokeh.embed import components
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file, show
from bokeh.resources import INLINE

from bokeh.util.string import encode_utf8
from bokeh.models.widgets import CheckboxButtonGroup, RadioButtonGroup
from bokeh.models import CustomJS, Legend, ColumnDataSource, HoverTool, Range1d, LinearColorMapper, LogColorMapper
from bokeh.layouts import gridplot



# plot correlation

sample_data = pd.read_csv('sample_LL.csv')
