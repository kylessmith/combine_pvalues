import numpy as np
from scipy.stats import norm, chi2


def Hartung(p, L=None, kappa=0.2, alpha=0.10):

    '''
     This function applies the modified inverse normal method for the combination of dependent p-values.

     Arguments:
         p:         vector of p-values.
         lambda:    vector of weights. It must be of the same length of p.
         kappa:     adjustment parameter. It is a positive value (0.2 is the default value),
                    then it is computed as in Hartung, p. 853.
         alpha:     level for the 1-alpha confidence interval for rho (0.10 is the default).
    
    Returns:
         Value: {"statistic": the Ht test statistic
        	     "parameter": the number of combined tests (p-values)
        	     "pvalue": the combined test p-value
        	     "conf_int": the confidence interval for the estimated correlation
        	     "estimate": the estimated correlation
        	     "null_value": the specified hypothesized value under the null
        	     "alternative": string describing the alternative hypothesis
        	     "method": string indicating the type of combination test (only Z-test is implemented)}

     Reference:
     Hartung, J. (1999): "A note on combining dependent tests of significance",
                         Biometrical Journal, 41(7), 849--855.
    '''
    
    if L == None:
        L = np.ones(len(p), dtype=float)

    t = norm.ppf(p)
    n = float(len(p))
    avt = np.sum(t)/n
    q = np.sum((t - avt)**2)/(n-1)                          # Hartung, eqn. (2.2)
    rhohat = 1 - q
    rhostar = max(-1/(n-1), rhohat)                           # Hartung, p. 851
    if kappa=="formula": kappa = (1 + 1/(n-1) - rhostar)/10  # Hartung, p. 853
    if kappa=="formula2": kappa = (1 + 1/(n-1) - rhostar)/5  # Hartung, p. 853

    # Hartung inverse normal corrected. See eqn. (2.4)

    Ht = np.sum(L*t)/np.sqrt(np.sum(L**2)+((np.sum(L))**2-np.sum(L**2))*(rhostar+kappa*np.sqrt(2/(n-1))*(1-rhostar)))
    lower = 1 - (n-1)/chi2.ppf(alpha/2, (n-1)) * q
    upper = 1 - (n-1)/chi2.ppf((1-alpha/2), (n-1)) * q          # Hartung, eqn. (2.3)

    output = dict(statistic=Ht,
                   parameter=n,
                   pvalue=norm.cdf(Ht),
                   conf_int=(lower, upper),
                   estimate=rhohat,
                   null_value="Ht=0",
                   alternative="less",
                   method="modified inverse normal combination")


    return output
