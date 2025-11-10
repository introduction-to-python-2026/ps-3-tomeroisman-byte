def app_pi(n_terms):
  pi_est = 0
  for n in range(n_terms):
    term = (-1) ** n / (2 * n +1 )
    pi_est = pi_est + term  
  pi_est = pi_est * 4
  return app_pi
