import pandas as pd
result = { 'IND' : '1', 'USA':'66' }
list_l = [ 'code', 'value' ]
ff = pd.DataFrame(result.items(), columns=list_l)
ff.to_csv('./store.csv', sep=',')
