import numpy
from z3 import *

class Hyperrectangle:
    def __init__(self, side_names: object, sides: object, constraint: object, nb_samples: object = 100) -> object:
        self.sides = sides                                      # list of sides, each side is an interval [begin, end]
        self.side_names = side_names                            # list of names for each dimension
        self.dimensions = len(self.sides)                       # number of dimensions
        self.nb_samples = nb_samples                            # number of samples (100 default)
        self.constraint = constraint                            # constraint
        self.volume = self.compute_volume()                     # volume of the hyperrectangle
        self.rejection_rate = self.compute_rejection_rate()     # rejection rate of the node in [0,1]
        self.side_name_idx_dict = dict()                        # maps side names to index

    def compute_volume(self):
        volume = 1;
        for side in self.sides:
            begin = side[0]
            end = side[1]
            volume = volume * abs(end - begin)
        return volume

    def compute_rejection_rate(self):
        """
        Computes the rate of samples drawn from the Hyperrectangle that are
        rejected by the constraint
        :return: float in [0,1] (0 - all samples accepted, 1 - all samples rejected)
        """
        samples_accepted = 0
        samples_rejected = 0

        for i in range(self.nb_samples):
            sample = []
            for side in self.sides:
                val = numpy.random.uniform(side[0], side[1])
                sample.append(val)
            accepted = self.constraint.evaluate(sample)
            if accepted:
                samples_accepted = samples_accepted + 1
            else:
                samples_rejected = samples_rejected + 1
        rate = float(samples_rejected)/float(samples_rejected + samples_accepted)
        return rate

    def is_empty(self):
        # take the original constraint
        s = self.constraint.solver

        # We will now add the Hyperrectangle constraint to the original one
        # We push the context so that we can later pop them once we are
        # done with the sat check
        s.push()
        i = 0

        # for each dimension x bounded by [b, e]
        # we add constraint x >= b and x <= e
        for side in self.sides:
            begin = side[0]
            end = side[1]
            name = self.side_names[i]
            var = Real(name)
            c1 = var >= begin
            c2 = var <= end
            s.add(c1)
            s.add(c2)
            i += 1

        # satisfiability check
        out = False
        if s.check() == unsat:
            out = True
        s.pop()
        return out

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def rejection_rate(self):
        return self.__rejection_rate

    @rejection_rate.setter
    def rejection_rate(self, rejection_rate):
        self.__rejection_rate = rejection_rate

    @property
    def nb_samples(self):
        return self.__nb_samples

    @nb_samples.setter
    def nb_samples(self, nb_samples):
        self.__nb_samples = nb_samples

    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint):
        self.__constraint = constraint



