#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 2022
@author: Sylvain Brisson sylvain.brisson@ens.fr
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if __name__ == "__main__":
    
    data = np.loadtxt("semucb_model/grid.4", skiprows=1)
    
    print(data[:,0].min(), data[:,0].max())
    print(data[:,1].min(), data[:,1].max())
    
    fig = plt.figure(figsize=(8,8))

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic())

    ax.coastlines()
    ax.add_feature(cfeature.LAND)
    ax.gridlines(linestyle=":", color="k")

    ax.scatter(data[:,0], data[:,1], transform=ccrs.PlateCarree())
    plt.show()