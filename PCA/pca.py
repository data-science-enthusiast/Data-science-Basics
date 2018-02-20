'''
Reducing   the   five-dimensional   records   to   two   dimensions  by   means of   the   principal   component   analysis.
 
 Steps   for   PCA:
1. Standardization   the   data   X.
2. Computing   the   Eigenvectors   and   Eigenvalues   from   the   covariance   matrix.
3. Sorting eigenvalues in descending order and choosing the k eigenvectors that correspond to
the k largest   eigenvalues   where k   will   be   the   number   of   dimensions   of   the   new   feature   space.
4. building   the   projection   matrix W from   the   selected k eigenvectors.
5. Transforming   the   original   dataset X using W to   obtain   a k-dimensional   feature   space. '''

import    pandas    as    pd
import    numpy    as    np
import    matplotlib.pyplot    as    plt
from    sklearn.preprocessing    import    StandardScaler
data   =   pd.read_csv(
             filepath_or_buffer = 'data.csv' ,              header = None ,
             sep = ',' )
data.dropna( how = "all" ,    inplace = True ) data.tail()
X   =   data.ix[:,    0 : 5 ].values
#   Normalization
X_std   =   StandardScaler().fit_transform(X)
cov_mat   =   np.cov(X_std.T) print ( 'Covariance   matrix    \n %s'    %   cov_mat)
#   Computing   Eigenvectors   and   Eigenvalues eig_vals,   eig_vecs   =   np.linalg.eig(cov_mat) print ( 'Eigenvectors    \n %s'    %   eig_vecs) print ( ' \n Eigenvalues    \n %s'    %   eig_vals)
#   Make   a   list   of   (eigenvalue,   eigenvector)   tuples
eig_pairs   =   [(np.abs(eig_vals[i]),   eig_vecs[:,   i])    for    i    in range ( len (eig_vals))]
#   Sort   the   (eigenvalue,   eigenvector)   tuples   from   high   to   low eig_pairs.sort()
eig_pairs.reverse()
print ( 'Eigenvalues   in   descending   order:' ) for    i    in    eig_pairs:
             print (i[ 0 ])
  
#   Visualising   Variation
tot   =    sum (eig_vals)
varince   =   [(j   /   tot)   *    100    for    j    in    sorted (eig_vals,    reverse = True )] with    plt.style.context( 'dark_background' ):
            plt.figure( figsize =( 6 ,    4 ))
            plt.bar( range ( 5 ),   varince,    alpha = 0.5 ,    align = 'center' ,    label = 'individual variance' )
            plt.ylabel( 'variance   ratio' )
            plt.xlabel( 'Principal   components' )
            plt.legend( loc = 'best' )             plt.tight_layout() plt.show()
#   Dimension      Reduction   for   k=2
matrix_w   =   np.hstack((eig_pairs[ 0 ][ 1 ].reshape( 5 ,    1 ),
                                                                  eig_pairs[ 1 ][ 1 ].reshape( 5 ,    1 )))
#   New   Space
Y   =   X_std.dot(matrix_w)
print ( 'New   Representation: \n %s'    %   Y)
y1,   y2   =   Y.T
plt.scatter(y1,   y2)
plt.title( "Data   using   first   two   Eigen   Vectors." ) plt.xlabel( 'PCA   variable   1' )
plt.ylabel( 'PCA   Variable   2' )
plt.show()

