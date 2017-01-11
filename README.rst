Function to combine p-values with Hartung's method, the Truncated Product Method, or Fisher's method 

QuickStart
==========
::

	combine_pvalues.combine_pvalues(pvalues, method="fisher", tau=0.05)
	pvalues: list of floats
	method: "fisher", "Hartung", or "tpm"
	    "fisher": fisher's method for independent pvalues (Statistical
	            Methods for Research Workers 1932)
	       returns: pvalue
	    "tpm": Truncated Product Method for independent pvalues (Zaykin,
	         Genet Epidemiol. 2002)
	       returns: pvalue
	    "Hartung": Hartung's method for dependent pvalues (Hartung,
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


Usage
-----------------------------------
::

	>>> from combine_pvalues import combine_pvalues
	>>> combine_pvalues([0.01, 0.1, 0.05], method="Hartung")
	{'alternative': 'less',
	'conf_int': (-4.4848693935565098, 0.90608739540426442),
	'estimate': 0.71866297951904023,
	'method': 'modified inverse normal combination',
	'null_value': 'Ht=0',
	'parameter': 3.0,
	'pvalue': 0.028769833077741683,
	'statistic': -1.8991887288117526}
	>>> combine_pvalues([0.01, 0.1, 0.05], method="fisher")
	0.0029971510202077612
	>>> combine_pvalues([0.01, 0.1, 0.05], method="tpm")
	0.005197199025218599


Installation
============

python can be used to install by::

    python setup.py install

If you dont already have numpy and scipy installed, it is best to download
`Anaconda`, a python distribution that has them included.  

    https://continuum.io/downloads

Dependencies can be installed by::

    pip install -r requirements.txt
