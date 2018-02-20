'''
Generate   100   3-dimensional   vectors   that   come   from   a   normal   distribution   with  
mean vector   as   [1   2   1]t   and   3x3  
covariance   matrix   as   [4   0.8   -0.3;   0.8   2   0.6;   -0.3   0.6   5]
Make   scatter   plots   of   x1   vs   x2,   x1   vs   x3,   and   x2   vs   x3  to explore  relationships'''

import    matplotlib.pyplot    as    plt
from    matplotlib    import    pyplot
from    mpl_toolkits.mplot3d    import    Axes3D import    numpy    as    np
from    scipy.spatial    import    distance
mean   =   ( 1 ,    2 ,    1 )
cov   =   [[ 4 ,    0.8 ,   - 0.3 ],   [ 0.8 ,    2 ,    0.6 ],   [- 0.3 ,    0.6 ,    5 ]]

#   Generating   Data
x   =   np.random.multivariate_normal(mean,   cov,    100 )
print ( "multivariate   Data: \n " ,   x)
print (x.shape) x1,   x2,   x3   =   x.T print ( ' \n x1:' ,   x1)
covariance   =   np.cov(x.T)
inverse   =   np.linalg.inv(covariance)

#   Eucledian   Distance
eucledian_dist   =   distance.euclidean(x[ 0 ],   x[ 1 ])
print ( 'Eucledian   Distance   of   First   pair   of   generated   vectors:   ' , eucledian_dist)

#   mahalanobis   Distance
mahalanobis_dist   =   distance.mahalanobis(x[ 0 ],   x[ 1 ],inverse) 
print ( "Mahalanobis   Distance   of   First   pair   of   generated   vectors:   " , mahalanobis_dist)

plt.scatter(x1,   x2) 
plt.title( "x1   vs   x2" )
plt.grid( True ) 
plt.xlabel( 'x1' ) 
plt.ylabel( 'x2' ) 
plt.show()


plt.scatter(x1,   x3) 
plt.title( "x1   vs   x3" ) 
plt.grid( True ) 
plt.xlabel( 'x1' ) 
plt.ylabel( 'x3' )
plt.show()

plt.scatter(x2,   x3)
plt.title( "x2   vs   x3" ) 
plt.grid( True ) 
plt.xlabel( 'x2' )
plt.ylabel( 'x3' ) 
plt.show()

fig   =   pyplot.figure() 
ax   =   Axes3D(fig) 
ax.scatter(x1,   x2,   x3) 
pyplot.show()
