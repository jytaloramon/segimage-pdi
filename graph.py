from typing import Any, Dict, List, Tuple


class Node:

    def __init__(self, id: int, area: Tuple[int, int, int]) -> None:

        self._id = id
        self._area = area
        self._neighbors: List[Dict[int, Node]] = [{}, {}, {}, {}]

    def add_neighbor_left(self, node: any) -> None:

        self._neighbors[0][node._id] = node

    def add_neighbor_top(self, node: any,) -> None:

        self._neighbors[1][node._id] = node

    def add_neighbor_right(self, node: any,) -> None:

        self._neighbors[2][node._id] = node

    def add_neighbor_down(self, node: any,) -> None:

        self._neighbors[3][node._id] = node

    def rm_neighbor(self, id) -> Any:

        for side in self._neighbors:
            if side.get(id) is not None:
                side.pop(id)

        return None


class Graph:

    def __init__(self) -> None:

        self._id_auto_increment = 0
        self._nodes: Dict[int, Node] = {}

    def _get_new_id_auto_increment(self) -> int:

        id = self._id_auto_increment
        self._id_auto_increment += 1

        return id

    def create_node(self, area: Tuple[int, int, int]) -> Node:

        id = self._get_new_id_auto_increment()
        node = Node(id, area)
        self._nodes[id] = node

        return node

    def delete_node(self, id: int) -> Node:

        node = self._nodes.get(id)

        for side in node._neighbors:
            for i in side.values():
                i.rm_neighbor(id)

        self._nodes.pop(id)

        return node

    def connect_node(self,
                     node: Node,
                     l: Dict[int, Node],
                     t: Dict[int, Node],
                     r: Dict[int, Node],
                     d: Dict[int, Node]) -> None:

        for i, d in enumerate([l, t, r, d]):
            if d is not None and len(d) > 0:
                node._neighbors[i].update(d)
