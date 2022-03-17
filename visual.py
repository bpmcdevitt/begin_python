#!/usr/bin/env python3

import numpy as np
from mayavi.mlab import *

# Example from:
# https://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html#mayavi.mlab.volume_slice
def test_volume_slice():
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    scalars = x * x * 0.5 + y * y * 0.5 + z * z * 2.0
    obj = volume_slice(scalars, plane_orientation='x_axes', colormap='plasma')
    return obj

test_volume_slice()
show()