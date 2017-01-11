from scipy.stats import chisqprob
import numpy as np

def fisher_combine(pvals):
    '''
    This function applies combined fisher probability with correction.
    
    Arguements:
        pvals: list of pvalues
    
    Returns:
        Value: combined pvalue
    
    Reference:
        Fisher: "Statistical Methods for Research Workers" 1932
    '''
    
    if len(pvals) == 1:
        return pvals[0]
    
    s = -2 * np.sum(np.log(pvals))
    
    return chisqprob(s, 2 * len(pvals))