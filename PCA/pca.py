#Suppose we   are   interested   in   reducing   the   five-dimensional   records   to   two   dimensions  
#by   means of   the   principal   component   analysis.
 
 Steps   for   PCA:
#1. Standardization   the   data   X.
#2. Computing   the   Eigenvectors   and   Eigenvalues   from   the   covariance   matrix.
#3. Sorting eigenvalues in descending order and choosing the k eigenvectors that correspond to
#the k largest   eigenvalues   where k   will   be   the   number   of   dimensions   of   the   new   feature   space.
#4. building   the   projection   matrix W from   the   selected k eigenvectors.
#5. Transforming   the   original   dataset X using W to   obtain   a k-dimensional   feature   space. 
