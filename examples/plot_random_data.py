#!/usr/bin/env python3
"""
Generate random points 
"""
import os
import sys
from typing import List, Tuple
from random import uniform
#import grid_perimeter as gp
from grid_perimeter import KDTree2D, Node2D, MPASGrid

def gen_random_plots(kd2d: KDTree2D, pts: List[Tuple[float, float]], n: int)->None:
    for i in range(n):
        test_pt = (uniform(0.6, 0.9), uniform(4.6, 4.9))
        nearest_cell_id = kd2d.nearest_cell(test_pt)
        print(i, test_pt, nearest_cell_id, pts[nearest_cell_id] )

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="MPAS regional grid data NetCDF file.")
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        ERR_TXT = "Could not find NetCDF file: {filename}"
        sys.exit(ERR_TXT.format(filename=args.filename))
    
    mpg = MPASGrid(args.filename)
    # cell grid points (lat, lon)
    pts = mpg.cell_points()
    # cell grid points with index (lat, lon, i)
    ptsi = [(pts[i][0], pts[i][1], i) for i in range(len(pts))]
    kd2d = KDTree2D(ptsi)
    gen_random_plots(kd2d, pts, 100)