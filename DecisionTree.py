import numpy as np

X = np.array([
    [3, 1, 4, 2, 5, 6, 7, 8, 9, 10],  
    [2.5, 1.0, 3.2, 2.8, 4.5, 5.6, 6.1, 7.3, 8.0, 9.1],
    [2.5, 23.0, 17.2, 15.8, 4.9, 2.200, 6.8, 7.3, 19.0, 1.0],  
])

Y = np.array([1, 0, 1, 0, 1, 1, 0, 0, 1, 0])  

class Node:
    """Node structure for Decision Tree."""
    def __init__(self, feature=None, threshold=None, left=None, right=None, gini=None, value=None):
        self.feature = feature  # Feature index for splitting
        self.threshold = threshold  # Threshold value
        self.left = left  # Left subtree
        self.right = right  # Right subtree
        self.gini = gini  # Gini impurity of the node
        self.value = value  # Class label if it's a leaf node

class DecisionTree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def split_tree(self, x, index, threshold):
        """Split the array into two branches based on the threshold."""
        left_indices = x[index] <= threshold
        right_indices = x[index] > threshold
        return left_indices, right_indices

    def _calculate_gini(self, y, left_indices, right_indices):
        total_samples = len(y)
        left_size = np.sum(left_indices)
        right_size = np.sum(right_indices)

        if left_size == 0 or right_size == 0:
            return 1  # Pure node

        left_labels = y[left_indices]
        right_labels = y[right_indices]

        left_gini = 1 - np.sum((np.bincount(left_labels, minlength=2) / left_size) ** 2)
        right_gini = 1 - np.sum((np.bincount(right_labels, minlength=2) / right_size) ** 2)

        weighted_gini = (left_size / total_samples) * left_gini + (right_size / total_samples) * right_gini
        return weighted_gini

    def find_best_split(self, x, y):
        """Finds the best feature and threshold to split the dataset."""
        best_gini = float("inf")
        best_feature = None
        best_threshold = None
        best_left_indices = None
        best_right_indices = None

        for feature in range(x.shape[0]):
            unique_values = np.unique(x[feature])
            for threshold in unique_values:
                left_indices, right_indices = self.split_tree(x, feature, threshold)
                gini = self._calculate_gini(y, left_indices, right_indices)

                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold
                    best_left_indices = left_indices
                    best_right_indices = right_indices

        return best_feature, best_threshold, best_gini, best_left_indices, best_right_indices

    def grow_tree(self, x, y):
        """Recursively grows the decision tree."""
        # Base Case: If all labels are the same, return a leaf node
        if np.all(y == y[0]):
            return Node(value=y[0])

        # Find the best split
        feature, threshold, gini, left_indices, right_indices = self.find_best_split(x, y)

        if feature is None:
            return Node(value=np.bincount(y).argmax())  # Majority class as leaf

        # Recursively create left and right subtrees
        left_subtree = self.grow_tree(x[:, left_indices], y[left_indices])
        right_subtree = self.grow_tree(x[:, right_indices], y[right_indices])

        return Node(feature=feature, threshold=threshold, left=left_subtree, right=right_subtree, gini=gini)

    def fit(self):
        """Builds the tree using recursive growth."""
        self.root = self.grow_tree(self.x, self.y)

    def print_tree(self, node=None, depth=0):
        """Helper function to print the decision tree structure."""
        if node is None:
            node = self.root

        if node.value is not None:
            print(" " * depth * 4, f"Leaf: Class {node.value}")
            return

        print(" " * depth * 4, f"Feature {node.feature} <= {node.threshold} (Gini: {node.gini:.4f})")
        self.print_tree(node.left, depth + 1)
        self.print_tree(node.right, depth + 1)

# Creating object
obj = DecisionTree(X, Y)
obj.fit()
obj.print_tree()