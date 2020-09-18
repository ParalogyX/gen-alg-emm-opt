# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:16:52 2020

@author: vpe
"""

import numpy as np
from pymoo.model.problem import FunctionalProblem

objs = [
    lambda x: x[0]**2 + x[1]**2,
    lambda x: (x[0]-1)**2 + x[1]**2
]

constr_ieq = [
    lambda x: 2*(x[0]-0.1) * (x[0]-0.9) / 0.18,
    lambda x: - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8
]

functional_problem = FunctionalProblem(2,
                                       objs,
                                       constr_ieq=constr_ieq,
                                       xl=np.array([-2,-2]),
                                       xu=np.array([2,2]))