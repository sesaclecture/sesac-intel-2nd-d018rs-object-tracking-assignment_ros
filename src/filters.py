import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        # TODO: Implement internal variables

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        pass

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        pass

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        pass

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        pass
