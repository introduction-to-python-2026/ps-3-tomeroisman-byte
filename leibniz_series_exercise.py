def app_pi(n_term):
  sigma = []
  for n in range(n_terms):
    sigma.append(((-1) ** n)/( 2* n + 1))
  pi = 4* sum(sigma)
  return pi
