from typing import Any

def is_in(element: Any, list: list) -> bool:
    """judges if a given element is in a given list
    returns True if contained; otherwise, False.

    Args:
        element (Any): an element
        list (list): a list

    Returns:
        bool: true if the element is in the list; otherwise, false
    """
    pass

class Edge:
    """Edge object
    """
    def __init__(self, n1: int, n2: int, edge_cost: float=0.0):
        """initializes an edge object with a given n1-n2 pair and its cost
        
        Args:
            n1 (int): node 1
            n2 (int): node 2
            edge_cost (float, optional): edge cost. Defaults to 0.0.
        """
        self.n1 = n1
        self.n2 = n2
        self.edge_cost = edge_cost
    
    def __eq__(self, edge) -> bool:
        """returns True if a given edge has the same endpoints (n1 and n2) 
        Note: Do not allow multiple edges between the same endpoints

        Args:
            edge (Edge): another edge

        Returns:
            bool: if n1 and n2 match, True. 
        """
        pass
    
    def __repr__(self) -> str:
        """specifies representation of an edge

        Returns:
            str: show n1, n2 and the cost (you can decide a format)
        """
        pass

class Graph:
    """Graph object that maintains node and edge lists
    """
    def __init__(self):
        """prepares empty node/link lists
        """
        self.nodes = list()
        self.edges = list()

    def add_edge(self, n1: int, n2: int, edge_cost: float=0.0):
        """adds an edge object consisting of given n1, n2, and edge_cost.
        The nodes n1 and n2 should be added to the node list if they are still not in the list.
        The edge object should be added to the edge list if it is still not in the list. If there is an edge from n1 to n2 already, raise a ValueError.

        Args:
            n1 (int): node 1
            n2 (int): node 2
            edge_cost (float, optional): edge cost. Defaults to 0.0.

        Raises:
            ValueError: If an edge added to the nodes that are already connected by another edge, raise this error and do not add the new edge.
        """
        pass

    def dirNeighbors(self, node: int) -> list[int]:
        """returns neighbors considering the direction of edges. 
        e.g. b is a neighbor of b if a -> b, but a is NOT a neighbor of b.

        Args:
            node (int): a node 

        Returns:
            list[int]: a list of neighbor nodes
        """
        pass
    
    def neighbors(self, node: int) -> list[int]:
        """returns neighbors in undirected graphs  
        e.g. if there is an edge (a, b), a is a neighbor of b and b is a neighbor of a.

        Args:
            node (int): a node 

        Returns:
            list[int]: a list of neighbor nodes
        """
        pass
    
    def edge_cost(self, n1: int, n2: int) -> float:
        """returns the edge cost of a given pair of nodes

        Args:
            n1 (int): node 1
            n2 (int): node 2

        Raises:
            IndexError: If an edge between n1 and n2 does not exist in the graph edge list, raise an error.

        Returns:
            float: the edge cost
        """
        pass