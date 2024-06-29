from scipy.stats import norm

means = [0,1,2,3]
stds = [1,1,2,2]

normal_dists = norm(means,stds)

print(normal_dists.mean)