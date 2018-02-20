'''
To determine, how   well   the   two   classes   are   separated in Vertebral column dataset
This visualization of data in scatter plot helps us to determine feature-class relations   and   feature-feature   relations
'''

#Task1: Mean, Median and Standard Deviation of two classes : Helps to understand spread of data.
import    pandas
from    prettytable    import    PrettyTable
data   =   pandas.read_csv( 'column_2C_weka.csv' ) attributes   =   data.columns
j   =    0
print ( "Abnormal   Data:" )
t1   =   PrettyTable([ 'Attribute' ,    'Mean' ,    'Standard   Deviation' ,    'Median' ]) while    (j   <    len (attributes)   -    1 ):
            t1.add_row([attributes[j],   data[attributes[j]][data[ 'class' ]   == 'Abnormal' ].mean(),data[attributes[j]][data[ 'class' ]   ==    'Abnormal' ].std(),
                     j       =       j       +        1          data[attributes[j]][data[ 'class' ]   ==    'Abnormal' ].median()])
print (t1)
j   =    0
print ( "Normal   Data:" )
t2   =   PrettyTable([ 'Attribute' ,    'Mean' ,    'Standard   Deviation' ,    'Median' ]) while    (j   <    len (attributes)   -    1 ):
            t2.add_row([attributes[j],   data[attributes[j]][data[ 'class' ]   == 'Normal' ].mean(),data[attributes[j]][data[ 'class' ]   ==    'Normal' ].std(),
                     j       =       j       +        1          data[attributes[j]][data[ 'class' ]   ==    'Normal' ].median()])
print (t2)

#Task2: Generate scatter   plots   for   all   feature   pairs 

import    pandas
import    matplotlib.pyplot    as    plt
import    seaborn    as    sns
csv_data   =   pandas.read_csv( 'column_2C_weka.csv' ) plt.figure()
sns.pairplot(csv_data,    hue = "class" ,    size = 2 ) plt.savefig( "feature_pair_scatter_plot.png" )
