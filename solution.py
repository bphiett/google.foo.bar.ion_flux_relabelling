import unittest

def heightToSize(height):

        n = (2**height)-1
        return n

def findParent(root, height, node, parent=-1):

    if node != root:
        parent = root
        right_child = root-1
        left_child = root-(2**(height-1))
        height-=1
        
        if node > left_child:
            # node in right subtree
            root = right_child
            parent = findParent(root, height, node, parent)
        else:
            # node in left subtree
            root = left_child
            parent = findParent(root, height, node, parent)
            
    return parent
        
def solution(h, q):
    # for a tree of given height (h), return parent values for values of interest (q)

    n = heightToSize(h)
    p = [findParent(n, h, value) for value in q]
    return p

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(3, [7,3,5,1]), [-1,7,6,3])
        self.assertEqual(solution(5, [19, 14, 28]), [21,15,29])

if __name__ == '__main__':
    unittest.main()
