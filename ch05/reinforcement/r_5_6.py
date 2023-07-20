"""
Our implementation of insert for the DynamicArray class, as given in
Code Fragment 5.5, has the following inefficiency. In the case when a
resize occurs, the resize operation takes time to copy all the elements
from an old array to a new array, and then the subsequent loop in the
body of insert shifts many of those elements.

Give an improved implementation of the insert method, so that, in the
case of a resize, the elements are shifted into their final position
during that operation, thereby avoiding the subsequent shifting.
"""
from ch05.dynamic_array import DynamicArray


class EfficientInsertDynamicArray(DynamicArray):
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values right."""
        if self._n == self._capacity:
            # Create a bigger array and copy over existing items.
            new_capacity = 2 * self._capacity
            B = self._make_array(new_capacity)

            for i in range(self._n):
                if k <= i:
                    # Shift items after k rightward.
                    B[i + 1] = self._A[i]
                else:
                    B[i] = self._A[i]
            self._A = B
            self._capacity = new_capacity
        else:
            for i in range(self._n - 1, -1, -1):  # Iterate backwards.
                current_value = self._A[i]
                if k <= i:
                    # Shift items after k rightward.
                    self._A[i + 1] = current_value

        self._A[k] = value
        self._n += 1
