# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:20:20 2020

@author: vpe
"""

import numpy as np
import emm_script

from pymoo.algorithms.nsga2 import NSGA2
from pymoo.model.problem import Problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter


class MyProblem(Problem):

    def __init__(self):
        super().__init__(n_var=3,
                         n_obj=3,
                         n_constr=1,
                         xl=np.array([6, 600, 100]),
                         xu=np.array([8.7, 1200, 1800]),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        
        func_res = emm_script.emm_calc (x[1], x[0])
        
        f1 = func_res[0]
        f2 = func_res[1]
        f3 = x[2] / (func_res[2] * 50 * 1000) * 100
        f3 = -f3
        #f1 = x[0] - x[1]
        #f1 = -f1

        
        #f1 = (x[0] + x[1])/x[1]
        #f2 = (x[0] - x[1])/x[1]
        
        #f1 = x[0] ** 2 + x[1] ** 2
        #f2 = (x[0] - 1) ** 2 + x[1] ** 2
        
        g1 = f1 - 2 
        #g1 = 2 * (x[0] - 0.1) * (x[0] - 0.9) / 0.18
        #g2 = - 20 * (x[0] - 0.4) * (x[0] - 0.6) / 4.8

        #out["F"] = [f1, f2]
        out["F"] = [f1, f2, -f3]
        out["G"] = [g1]


problem = MyProblem()

algorithm = NSGA2(pop_size=100)

res = minimize(problem,
               algorithm,
               ("n_gen", 200),
               verbose=True,
               seed=1)
#print(res.F[2])
#res.F[2] = -res.F[2]
plot = Scatter()
plot.add(res.F, color="red")
plot.show()