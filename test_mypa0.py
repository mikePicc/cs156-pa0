import unittest

class TestMyPA(unittest.TestCase):
    def setUp(self) -> None:
        """Create a graph instance and add a few edges.
        """
        pass

    def test_is_in(self):
        """check (1) if true is returned when an element is in a list and (2) if false is returned when an element is not in a list.
        """
        pass

    def test_add_edge_lists(self):
        """add a new edge and check if the edge and end-nodes are correctly added to edge and node lists of the Graph instance.
        """
        pass

    def test_add_edge_multie(self):
        """check if ValueError is raised when a new edge has the endpoints same as an existing edge.
        """
        pass
    
    def test_dirNeighbors(self):
        """check if all the neighbors are correctly included in the neighbor set returned.
        """
        pass
    
    def test_edge_cost(self):
        """check if the edge cost is correctly returned.
        """
        pass

    def test_edge_cost_err(self):
        """check if IndexError is raised if you ask for the cost edge of an edge that does not exist.
        """
        pass


    def test_edge_eq(self):
        """check if two edges are considered as the same object when both edges have the same endpoints.
        """
        pass

if __name__ == '__main__':
    unittest.main()