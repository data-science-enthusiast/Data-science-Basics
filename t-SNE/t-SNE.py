#Visualization   of   t-SNE   in   plots with different perplexity
from    sklearn.manifold    import    TSNE import    pandas    as    pd
from    matplotlib    import    pyplot    as    plt data   =   pd.read_csv(
          filepath_or_buffer = 'data.csv' ,           header = None ,
          sep = ',' )
data.dropna( how = "all" ,    inplace = True ) data.tail()
X   =   data.ix[:,    0 : 5 ].values
from    sklearn.preprocessing    import    StandardScaler X_std   =   StandardScaler().fit_transform(data)


transformed_10   =   TSNE( n_components = 2 ,    perplexity = 10 ,    learning_rate    = 40 , verbose = 1 , n_iter = 200 ).fit_transform(X_std)
plt.figure( figsize    =   ( 15 , 15 ))
plt.title( 'TSNE   Scatter   Plot:   perplexity=10' )
xs_10   =   transformed_10[:, 0 ]
ys_10=   transformed_10[:, 1 ]
plt.scatter(xs_10,   ys_10)
plt.show()
print ( "Transformed   Data   when   perplexity=10:" ,transformed_10)


transformed_50   =   TSNE( n_components = 2 ,    perplexity = 50 , learning_rate    =    40 , verbose = 1 , n_iter = 200 ).fit_transform(X_std)
plt.figure( figsize    =   ( 15 , 15 ))
plt.title( 'TSNE   Scatter   Plot:   perplexity=50' )
xs_50   =   transformed_50[:, 0 ]
ys_50   =   transformed_50[:, 1 ]
plt.scatter(xs_50,   ys_50)
plt.show()
print ( "Transformed   Data   when   perplexity=50:" ,transformed_50)
