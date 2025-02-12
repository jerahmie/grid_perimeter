/*
 * file - lam_domain_filter.h
 *
 * KDTree filter observation points.
 */
#pragma once

#include <vector>
#include "kdtree.h"

#define BDYCELL 7  /* External boundary cell type */

std::vector<int> lam_domain_filter_omp(KDTree &,
                                   std::vector<point2D>::iterator,
                                   std::vector<point2D>::iterator); 

std::vector<int> lam_domain_filter(KDTree &,
                                   std::vector<point2D>::iterator,
                                   std::vector<point2D>::iterator);

