#import_pandas
import pandas as pd
####Read_my_csv_file#######
df= pd.read_csv("/Users/emam22/Desktop/example.csv", sep=',')
df=pd.DataFrame(df)
dff=pd.DataFrame(df)
####df=my_data_withoutSampleID_into_Dataframeformat_dff=all_data_in_dataframe#####
df=df.loc[:, df.columns != 'SampleID']
#Here_write_the_hedear_name_of_sample_column_name
column_count=len(df.columns)
column_length=len(pd.DataFrame(df[[df.columns[1]]]))
########extract_value_column#########
value_column=pd.concat([df, df.T.stack().reset_index(name='value')['value']], axis=1)
value_column=value_column[['value']]
value_column=pd.DataFrame(value_column)
value_column_length=len(value_column[['value']])
########extract_view_and_group_column#########
loop_value=0
view_column=[]
group_column=[]
while loop_value < value_column_length:
    view_column.append("view0")
    #here_you_can_insert_your_view_name
    group_column.append("group0")
    #here_you_can_insert_your_group_name
    loop_value=loop_value+1
view_column=pd.DataFrame(view_column, columns=["view"])
group_column=pd.DataFrame(group_column, columns=["group"])
########extract_sample_column#########
sample_column=[]
for i in range(column_count):
    sample_column.append(dff.loc[: ,'SampleID'])
sample=pd.DataFrame(sample_column).T
sample=pd.concat([sample, sample.T.stack().reset_index(name='sample')['sample']], axis=1)
sample=sample[['sample']]
sample_column=pd.DataFrame(sample)
########extract_feature_column#########
feature_column=[]
columns_name=df.columns
for i in range(column_count):
    for _ in range(column_length):
        feature_column.append(columns_name[i+0])        
feature_column=pd.DataFrame(feature_column, columns=["feaure"])
########concatonate_and_exporting_data#########
concat=pd.concat([sample_column, group_column, feature_column, view_column, value_column],axis=1, sort=False)
concat.to_csv("/Users/emam22/Desktop/emam.csv",index=False)  
########concatonate_multiview_files_and_exporting_data#########
#concat2=df1.append(df2, ignore_index = True)
#concat2.to_csv("/Users/emam22/Desktop/emmam.csv",index=False)
