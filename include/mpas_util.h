/*
 * mpas_util.h
 * Utility and helper functions for generating kd-trees from MPAS 
 * Regional static data.
 */
#pragma once 

#include <vector>
#include "kdtree_node.h"

std::vector<nodeData> merge_lat_lon(std::vector<float> &,
                                    std::vector<float> &);

std::vector<nodeData> merge_lat_lon(std::vector<float> &,
                                    std::vector<float> &, 
                                    std::vector<int> &);

std::vector<nodeData> filter_bdy_mask_cell(std::vector<nodeData> &,
                                           std::vector<int> &,
                                           std::vector<int> &);
