import numpy
from z3 import *
from hyperrectangle import Hyperrectangle


class HyperrectangleAbstraction:

    u_hrects = []
    hrects = []

    def __init__(self, side_names, sides, constraint, max_samples=100):
        self.max_samples = max_samples                          # max nb samples per hyperrectangle during abstraction
        self.constraint = constraint
        hr = Hyperrectangle(side_names, sides, constraint, max_samples)
        self.u_hrects.append(hr)                                # list of unprocessed hyperrectangles
        self.volume = hr.volume                                 # abstraction volume
        self.hrects = []

    def compute_abstraction(self, precision=0.5, min_volume = 0.001):
        """
        This procedure computes the abstraction of the constraint as a union of disjoint hyperrectangles

        :param precision: precision percentage in [0,1]
        :return: void
        """

        while self.u_hrects:
            # In every iteration, we process one hyperrectangle from the list of unprocessed
            # hyperrectangles and decide if we (1) throw it away, (2) keep it, or (3) split it

            # We prioritize the order in which we process unprocessed hyperrectangles
            # Here, we process them in the order of rejection rates, from highest to lowest
            # self.u_hrects.sort(key=lambda x: x.rejection_rate, reverse=True)
            hr = self.u_hrects.pop(0)

            # Case 1: hyperrectangle's acceptance rate is higher than the required precision
            # or hyperrectangle is already small enough
            # move it to hrects
            if hr.rejection_rate <= 1 - precision or hr.volume <= min_volume:
                self.hrects.append(hr)
            # Case 2: at least one sample from the hr is accepted by the constraint,
            # but the rejection rate is still high, and hr volume is also still high
            # -> split the hr
            elif hr.rejection_rate < 1:
                left_box, right_box = self.split(hr)
                self.u_hrects.append(left_box)
                self.u_hrects.append(right_box)
            # Case 3: all the samples from the hr are rejected by the constraint
            # -> hr really does not intersect the constraint - remove the hr and update overall volume
            # -> hr does intersect the constraint - split the hr
            else:
                if hr.is_empty():
                    self.volume = self.volume - hr.volume
                else:
                    left_box, right_box = self.split(hr)
                    self.u_hrects.append(left_box)
                    self.u_hrects.append(right_box)

    def split(self, hr):
        """
        Splits the Hyperrectangle hr into 2 hyperrectangles hr1 and hr2, s.t.
        hr1 union hr2 = h2, and
        hr1 intersect hr2 = emptyset
        :param hr: hyperrectangle
        :return: Pair of hyperrectangles (hr1, hr2)
        """

        # Find the dimension d in hr that has the longest side
        i = 0
        size = 0
        side_index = 0
        for side in hr.sides:
            side_size = side[1] - side[0]
            if side_size > size:
                size = side_size
                side_index = i
            i = i + 1

        sides_left = []
        sides_right = []

        # split hyperectangle in the middle of the dimension d
        i = 0
        for side in hr.sides:
            if i == side_index:
                mid = (float(side[1]) - float(side[0]))/2
                sides_left.append([side[0], side[0] + mid])
                sides_right.append([side[0] + mid, side[1]])
            else:
                sides_left.append(side)
                sides_right.append(side)
            i = i + 1

        hr_left = Hyperrectangle(hr.side_names, sides_left, hr.constraint, hr.nb_samples)
        hr_right = Hyperrectangle(hr.side_names, sides_right, hr.constraint, hr.nb_samples)

        return hr_left, hr_right

    def uniform_sample(self):
        '''
        Draws a uniform sample from the abstraction (union of hyperrectangles)
        :return: sample
        '''
        # Compute the cumulative volume of hyperrectangles
        cv = self.cumulative_volume()

        # Assume that we have hyperrectangles [hr1, ..., hrn]
        # and cv = [v1, ..., vn] where
        # v1 = volume(hr1)
        # vi = volume(hr1) + ... + volume(hri)
        # Draw a random number in [0, vn]
        rdm = numpy.random.uniform(0, cv[len(cv)-1])

        # We define a mapping from rdm to an index i
        # which tells us which hyperrectangle i we sample next
        # The mapping is defined as follows
        # if rdm in [0, v1), then idx = 0
        # ...
        # if rdm in [vi, vi+1), then idx = i
        idx = self.binary_search(rdm, cv, 0, len(cv)-1)

        #Draw a uniform sample from hyperrectangle hridx
        hr = self.hrects[idx]
        sample = []
        for side in hr.sides:
            val = numpy.random.uniform(side[0], side[1])
            sample.append(val)

        return sample

    def cumulative_volume(self):
        '''
        For a union of hyperrectangles [h1,...,hn]
        computes a list of volumes [v1,...,vn] s.t.
        v1 = volume(h1)
        vi = volume(h1) + ... + volume(hi)
        Note that vn = volume of the entire abstraction
        :return: list [v1,...,vn] of cumulative volumes
        '''
        out = []
        cumulative_volume = 0
        for box in self.hrects:
            cumulative_volume = cumulative_volume + box.volume
            out.append(cumulative_volume)
        return out

    def binary_search(self, val, val_list, low, high):
        mid = (high + low) // 2

        mid_val = val_list[mid]

        if val >= mid_val:
            if mid == high:
                return mid
            elif val < val_list[mid+1]:
                return mid + 1
            else:
                return self.binary_search(val, val_list, mid+1, high)
        else:
            if mid == low:
                return mid
            elif val >= val_list[mid-1]:
                return mid
            else:
                return self.binary_search(val, val_list, low, mid)



