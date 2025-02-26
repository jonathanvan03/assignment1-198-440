class Cell:

    def __init__(self, x, y, g, h, larger_g = True, parent=None):
        """
        Initialize a cell.
        :param x: x-coordinate of the cell
        :param y: y-coordinate of the cell
        :param g: cost from the start to this cell
        :param h: heuristic value (estimated cost to the goal)
        :param parent: parent cell in the path
        """
        self.x = x
        self.y = y
        self.g = g  # Cost from start to this cell
        self.h = h  # Heuristic (Manhattan distance to goal)
        self.f = h  # Total cost (f = g + h)
        self.parent = parent  # Pointer to the parent cell
        self.larger_g = larger_g
        self.search = 0

    def __lt__(self, other):
        """
        Defines how cells are compared in the priority queue.
        :param other: another cell to compare with
        :return: True if this cell has higher priority, False otherwise
        """
        if self.f == other.f:
            # Tie-breaking: prefer larger g-values if larger_g is True, else prefer smaller g-values
            return self.g > other.g if self.larger_g else self.g < other.g
        # Default: prefer smaller f-values
        return self.f < other.f

    def __eq__(self, other):
        """
        Defines equality between two cells based on their coordinates.
        :param other: another cell to compare with
        :return: True if the cells have the same coordinates, False otherwise
        """
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        """
        Defines the hash value of a cell based on its coordinates.
        :return: hash value of the cell
        """
        return hash((self.x, self.y))

    def update(self, new_g, new_parent = None):
        """
        Update the cell's g-value, f-value, and parent.
        :param new_g: new g-value (cost from start to this cell)
        :param new_parent: new parent cell in the path
        """

        self.g = new_g
        self.f = self.g + self.h  # Update f-value
        if new_parent is not None:
            self.parent = new_parent  # Update parent