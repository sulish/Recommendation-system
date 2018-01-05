#inisialisasi awal

import numpy as np
import random
from scipy.optimize import differential_evolution
indv=[]

#contoh cost function, yang digunakan untuk optimization

def func1(x):
	#shere function, dengan boundary, f(0,...,0)=0
	return sum([x[i]**2 for i in range(len(x))])

def func2(x):
	#Beale's function dengan boundary =[(-4.5,4.5),(-4.5,4.5)], f(3,0.5)=0
	term1 = (1.500-x[0]+x[0]*x[1])**2
	term2 = (2.250-x[0]+x[0]*x[1]**2)**2
	term3 = (2.625-x[0]+x[0]*x[1]**3)**2
	return term1 +term2 + term3

def func3(x):
	#ackley function, dengan boundary = [(-5,5),(5,5)]
	term1 = -0.2 * np.sqrt(0.5*(x[0] ** 2 + x[1] ** 2))
	term2 = 0.5 * (np.cos(2. * np.pi * x[0]) +np.cos(2. * np.pi * x[1]))
	return -20. * np.exp(term1) - np.exp(term2) + 20. + np.e

def ensure_bounds(vec,bounds):
	vec_new=[1]
	for i in range(len(vec)):
		if vec[i] < bounds [i][0]:
			vec_new.append(bounds[i][0])
		if vec[i] > bounds [i][0]:
			vec_new.append(bounds[i][1])
		if bounds[i][0] <= vec[i] <= bounds[i][1]:
			vec_new.append(vec[i])
	return vec_new

def main(cost_func, bounds, popsize, mutate, recombination, maxier,indv):
	population=[]
	for i in range(len(bounds)):
		indv.append(random.uniform(bounds[i][0],bounds[i][1]))
	population.append(indv)

	for i in range(1,maxiter+1):
		print 'GENERATION:',i

		gen_scores=[]

	for j in range(0,popsize):
		canidates = range(0, popsize)
		canidates.remove(j)
		random_index = random.sample(canidates,3)

		x_1 = population[random_index[0]]
		x_2 = population[random_index[1]]
		x_3 = population[random_index[2]]
		x_t = population[j]

		x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
		v_donor = [x_1_i + mutate * x_diff_i for x_1, x_diff_i in zip(x_1, x_diff)]

		v_donor = ensure_bounds(v_donor, bounds)


		v_trial =[]
		for k in range(len(x_t)):
			crossover = random.random()
			if crossover==recombination:
				v_trial.append(v_donor[k])

			else:
				v_trial.append(x_t[k])

		score_trial = cost_func(v_trial)
		score_target = cost_func(x_t)

		if score_trial < score_target:
			population[j] = v_trial
			gen_scores.append(score_trial)
			print '    >', score_trial, v_trial

		else:
			print '    >', score_target, x_t
			gen_scores.append(score_target)


	gen_avg = sum(gen_scores) / popsize
	gen_best = min(gen_scores)
	gen_sol = population[gen_scores.index(min(gen_scores))]
	print '		> GENERATION AVERAGE: ',gen_avg
	print '		> GENERATION BEST: ', gen_best
	print '		> BEST SOLUTION: ', gen_sol, '\n'

	return gen_sol


cost_func = func3 						#cost function pilih salah satu
bounds = [(-5,5),(5,5)] 				#boundary [(x1_min,x1_max),(x2_min,x2_max),....]
popsize = 10
mutate = 0.5
recombination = 0.7
maxiter = 20

main (cost_func, bounds, popsize, mutate, recombination, maxiter, indv)



