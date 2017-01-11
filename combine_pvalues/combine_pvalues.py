'''
Implementation of 3 methods to combine pvalues
    fisher's method: (Statistical Methods for Research Workers 1932)
    Hartung's modified inverse normal method: (Hartung, Biometrical
                                               Journal 1999)
    Truncated Product Method: (Zaykin, Genet Epidemiol. 2002)
'''

from tpm import tpm
from Hartung import Hartung
from fishers import fisher_combine
import numpy as np
import time

def combine_pvalues(pvalues, method="fisher", tau=0.05, seed=time.time(),
                    nperms=1000, weights=None, kappa=0.2, alpha=0.10):
    '''
    combine_pvalues.combine_pvalues(pvalues, method="fisher", tau=0.05)
        pvalues: list of floats
        method: fisher, Hartung, or tpm
            fisher: fisher's method for independent pvalues (Statistical
                    Methods for Research Workers 1932)
               returns: pvalue
            tpm: Truncated Product Method for independent pvalues (Zaykin,
                 Genet Epidemiol. 2002)
               returns: pvalue
            Hartung: Hartung's method for dependent pvalues (Hartung,
                     Biometrical Journal 1999)
               returns: {"alternative": string describing the alternative
                                        hypothesis
                         "conf_int": the confidence interval for the
                                     estimated correlation
                         "estimate": the estimated correlation
                         "method": string indicating the type of combination
                                   test (only Z-test is implemented)
                         "null_value": the specified hypothesized value under
                                       the null
                         "parameter": the number of combined tests (p-values)
                         "pvalue": the combined test p-value
                         "statistic": the Ht test statistic}
        tau: (used for tpm) between 0 and 1
        seed: (used for tpm) random number generator seed
        nperms: (used for tpm) number of permutations to do
        weights: (used in Hartung) list of weights. It must be of the same
                 length of p.
        kappa: (used in Hartung) adjustment parameter. It is a positive 
               value (0.2 is the default value), then it is computed as
               in Hartung, p. 853.
        alpha: (used in Hartung) level for the 1-alpha confidence interval
               for rho (0.10 is the default).
    '''
    
    #check if all values are NA
    if all(p == "NA" for p in pvalues):
        print "all values are NA"
        return np.nan
    #remove NAs from list
    pvalues = [p for p in pvalues if p != "NA"]
    
    if method == "Hartung":
        combined_pval = Hartung(pvalues, weights, kappa, alpha)
    elif method == "tpm":
        combined_pval = tpm(tau, nperms, seed, pvalues)
    elif method == "fisher":
        combined_pval = fisher_combine(pvalues)
    else:
        print "method = fisher, Hartung, or tpm!"
        return np.nan
        
    return combined_pval