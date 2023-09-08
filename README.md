#grid_perimeter

Python module to extract the perimeter cells of a MPAS regional grid.

Exterior Point | Interior Point
:---------:|:-----------:
![](doc/pt_exterior1.png) | ![](doc/pt_interior2.png)

# Required Python modules
- numpy
- matplotlib
- cartopy
- cartopy.util
- geocat
- geocat-comp
- geocat-viz
- geometric_features

# Build and Test
```$ cmake -B buildtree && cmake --build buildtree```

```$ cd buildtree```

```$ ctest```

# Example

An example of using the grid_perimeter module to generate the above plots:


```$ python3 examples/plot_random_nearest.py test/python_tests/Manitowoc.static.nc```

LAM Domain Filter an observation file against a MPAS regional domain.

```$ filter_obs <static_file> <obs_file lam_mask_file> <output_file>```

Example:

```$ filter_obs conus_15km.static.nc satwind_obs_2019050100.h5 lam_domain.h5```

Plot Filtered Observations:

```$ examples/plot_obs.py satwind_obs_2019050100.h5 --mask-file lam_domain.h5 --output lam_domain.png```

No Filter |  Filter
:---------:|:-----------:
![](doc/plot_obs_nomask.png) | ![](doc/plot_obs_masked.png)
