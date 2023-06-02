#ifndef _KDTREE_NODE_H_
#define _KDTREE_NODE_H_

//#include <iostream>

struct nodeData {
  double lat;
  double lon;
  int cell_index;
  friend std::ostream& operator<<(std::ostream& os, const nodeData& nd);
};

class KDTreeNode2D {
  private:
    KDTreeNode2D* left;
    KDTreeNode2D* right;
    nodeData node_data;
  public:
    KDTreeNode2D(KDTreeNode2D*, KDTreeNode2D*,nodeData);
    KDTreeNode2D* getLeft(void);
    KDTreeNode2D* getRight(void);
    nodeData getData(void);
    friend std::ostream& operator<<(std::ostream& os, const KDTreeNode2D& kd2);

    //~KDTreeNode2D();
};

#endif /* _KDTREE_NODE_H_ */