#Visualization with PCA

import    pandas    as    pd
import    numpy    as    np
import    matplotlib.pyplot    as    plt
from    sklearn.preprocessing    import    StandardScaler
data   =   pd.read_csv(
             filepath_or_buffer = 'Vertebral.csv' ,
             header = None ,
             sep = ',' )
data.columns   =   [ 'pelvic_incidence' ,    'pelvic_tilt' ,    'lumbar_lordosis_angle' , 'sacral_slope' ,    'pelvic_radius' ,
                                                 'degree_spondylolisthesis' ,    'class' ] data.dropna( how = "all" ,    inplace = True )
data.tail()
X   =   data.ix[:,    0 : 6 ].  values
y   =   data.ix[:,    6 ].  values


#   Normalization
X_std   =   StandardScaler().fit_transform(X) orig   =   X_std
cov_mat   =   np.cov(X_std.T) print ( 'Covariance   matrix    \n %s'    %   cov_mat)
#   Computing   Eigenvectors   and   Eigenvalues eig_vals,   eig_vecs   =   np.linalg.eig(cov_mat) print ( 'Eigenvectors    \n %s'    %   eig_vecs) print ( ' \n Eigenvalues    \n %s'    %   eig_vals)
#   Make   a   list   of   (eigenvalue,   eigenvector)   tuples
eig_pairs   =   [(np.abs(eig_vals[i]),   eig_vecs[:,   i])    for    i    in range ( len (eig_vals))]
#   Sort   the   (eigenvalue,   eigenvector)   tuples   from   high   to   low eig_pairs.sort()
eig_pairs.reverse()
print ( 'Eigenvalues   in   descending   order:' ) for    i    in    eig_pairs:
             print (i[ 0 ])
Y_sklearn   =   sklearn_pca.fit_transform(X_std)
traces   =   []
for    name    in    ( 'Abnormal' ,    'Normal' ):             trace   =   Scatter(
                     
                       x =Y[y   ==   name,    0 ],                        y =Y[y   ==   name,    1 ],                        mode = 'markers' ,
                       name =name,
                       marker =Marker(
                                   size = 12 ,
                                   line =Line(
                                               color = 'rgba(217,   217,   217,   0.14)' ,                                                width = 0.5 ),
                                   opacity = 0.8 ))           traces.append(trace)

#   Dimension   Reduction   for   k=2
matrix_w   =   np.hstack((eig_pairs[ 0 ][ 1 ].reshape( 6 ,    1 ),
                                                                  eig_pairs[ 1 ][ 1 ].reshape( 6 ,    1 ))) Y   =   X_std.dot(matrix_w)
y1,   y2   =   Y.T
plt.scatter(y1,   y2)
plt.title( "Transformed   Data   in   new   space." ) plt.xlabel( 'PCA   variable   1' ) plt.ylabel( 'PCA   Variable   2' )
plt.show()
#Used   Sklearn   for   Visualization   of   classes
import    plotly.plotly    as    py
from    plotly.graph_objs    import    *
from    sklearn.decomposition    import    PCA    as    sklearnPCA sklearn_pca   =   sklearnPCA( n_components = 2 )
data   =   Data(traces)
layout   =   Layout( showlegend = True ,
                                                 scene =Scene( xaxis =XAxis( title = 'PC1' ),
                                                                                     yaxis =YAxis( title = 'PC2' ),   ))
fig   =   Figure( data =data,    layout =layout) py.iplot(fig)
