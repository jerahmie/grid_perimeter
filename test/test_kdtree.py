"""Unittests for kdtree module"""
import os
import unittest
from grid_perimeter import * 

class TestKDTree2D(unittest.TestCase):
    """Test case for 2D KD Tree"""
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # a non-trivial list of points
        self.p = [(1.1,-2.2), (3.3, 4.4), (-1.1, 2.2), (-6.6, 7.7)]
        # netcdf regional grid file
        this_dir = os.path.abspath(os.path.dirname(__file__))
        self.grid_file = os.path.join(this_dir, 'Manitowoc.static.nc')

    def test_kdtree2d(self):
        """Test create kdtree"""
        p = [(1.1, 2.2), (3.3, 4.4)]
        a = KDTree2D(p)
        self.assertTrue(isinstance(a, KDTree2D))

    def test_sort_points(self):
        """Test ability to sort points over x- or y- points."""
        spx = [(-6.6, 7.7), (-1.1, 2.2), (1.1, -2.2), (3.3, 4.4)]
        spy = [(1.1,-2.2), (-1.1,2.2), (3.3, 4.4), (-6.6, 7.7)]

        # single point should already be sorted
        self.assertEqual([(1.1, 2.2)], sort_points([(1.1, 2.2)], 0))
        self.assertEqual([(1.1, 2.2)], sort_points([(1.1, 2.2)], 1))

        # empty list should return empty list
        self.assertEqual([], sort_points([],0)) 
        # sort multi-point list
        self.assertEqual(spx, sort_points(self.p,0))
        self.assertEqual(spy, sort_points(self.p,1))

        # sorting over wrong index should raise exception
        with self.assertRaises(RuntimeError):
            sort_points(self.p,2)

    def test_median_point_id(self):
        """Test find media point from sorted list."""
        self.assertEqual(((-1.1, 2.2), 1), median_point_id(sort_points(self.p, 0)))
        p5 = self.p
        p5.append((-10.0, -10.0))
        self.assertEqual(((-1.1, 2.2), 2), median_point_id(sort_points(p5, 0)))
        # single point list
        self.assertEqual(((-1.1, 2.2), 0), median_point_id([(-1.1, 2.2)]))
        self.assertEqual(((0, 0), 0), median_point_id([(0, 0)]))

    def test_kdtree2d_node(self):
        """Test the constuction of kdtree node"""
        nroot = Node2D((1.0, 2.0))
        self.assertTrue(isinstance(nroot, Node2D))
        self.assertEqual('((1.0, 2.0))', str(nroot))
        self.assertEqual('(Node2D, \'(1.0, 2.0)\', left=None, right=None)', repr(nroot))

    def test_build_tree(self):
        """Test the construction of a kd tree."""
        pts = [(0.0, 1.1), (1.1, -1.0), (2.2, -1.1), (3.3, 4.4)]
        a = build_tree(pts)
        self.assertEqual("(Node2D, '(1.1, -1.0)', left=((0.0, 1.1)), right=((2.2, -1.1)))", repr(a))

    def test_build_big_tree(self):
        """Test building a meaningful tree from data."""
        mpg = MPASGrid(self.grid_file)
        pts = mpg.cell_points()
        self.assertEqual(len(pts), 441)
        kdtree = build_tree(pts)
        self.assertEqual(repr(kdtree), '(Node2D, \'(0.7498185038566589, 4.627470970153809)\', left=((0.6799139380455017, 4.748469829559326)), right=((0.7500742673873901, 4.756713390350342)))')

    def test_KDTree2D(self):
        """Test the KDTree2D Class and methods"""
        #pts = [(0.0, 1.1), (1.1, -1.0), (2.2, -1.1), (3.3, 4.4)]
        pts1 = [(0.0, 1.1)]
        kd2d1pt = KDTree2D(pts1)
        self.assertTrue(isinstance(kd2d1pt, KDTree2D))
        self.assertEqual(kd2d1pt.max_depth, 1)
        
        pts3 = [(0.0, 1.1), (1.1, -1.0), (2.2, -1.1)]
        kd2d3pt = KDTree2D(pts3)
        self.assertEqual(kd2d3pt.max_depth, 2)

    def test_KDTree2D_medium(self):
        """Test the KDTree2D Class and methods"""
        mpg = MPASGrid(self.grid_file)
        pts = mpg.cell_points()
        kd2 = KDTree2D(pts)
        self.assertEqual(kd2.max_depth, 9)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()

