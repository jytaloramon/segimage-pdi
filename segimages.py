import queue
from typing import Any, List, Tuple

import numpy as np


class SegImageGrowing:

    def __init__(self, image: List[List[int]]) -> None:

        self._image = np.array(image, np.float32)
        self._shape = self._image.shape
        self._image_avg_global = np.average(image)

    def run_segmentation(self, seed_start_posi: Tuple[int, int], seed_color: int, target: int) -> Any:

        img_out = np.zeros(self._shape, dtype=np.float32)

        queue: List[Tuple[int, int, int, int]] = [
            (seed_start_posi[0], seed_start_posi[1], seed_color, self._image[1][1])]

        neighborhood: List[Tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (1, -1),
                                               (1, 0), (1, 1), (0, -1), (0, 1)]

        img_out[1][1] = 1
        while len(queue) > 0:
            l, c, i, b = queue.pop(0)

            for l_add, c_add in neighborhood:
                next_l, next_c = l + l_add, c + c_add

                if self._is_valid_pixel(next_l, next_c) and img_out[next_l][next_c] == 0:
                    if abs(b - self._image[next_l][next_c]) <= target:
                        img_out[next_l][next_c] = i
                        queue.append((next_l, next_c, i, b))
                    else:
                        new_i = 255 if i == 1 else 1
                        img_out[next_l][next_c] = new_i
                        queue.append(
                            (next_l, next_c, new_i, self._image[next_l][next_c]))

        return img_out

    def _is_valid_pixel(self, l: int, c: int) -> bool:

        return not(l < 0 or c < 0 or l >= self._shape[0] or c >= self._shape[1])
