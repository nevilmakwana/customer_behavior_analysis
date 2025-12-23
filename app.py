import pandas as pd
df =pd.read_csv('customer_shopping_behavior.csv')
print(df.head())

print(df.info())

print(df.describe())

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))

print(df.isnull().sum())

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#create a new column age_group
labels= ['Young Adult','Adult','Middle Age','Senior']
df['age_group'] = pd.qcut(df['age'], q=4 , labels=labels)

print(df[['age','age_group']].head())

#create column purchase_frequency_days 
frequency_mapping = {'Fortnightly':14, 'Monthly':30, 'Quarterly':90, 'Annually':365,'Weekly':7,'Bi-Weekly':14,
             'Every 3 months':90}

df['purchase_frequency_days'] =df['frequency_of_purchases'].map(frequency_mapping)
print(df[['frequency_of_purchases','purchase_frequency_days']].head())

print(df['discount_applied'] == df['promo_code_used'].all())

df.drop(columns=['promo_code_used'], inplace=True)
print(df.columns)

df.to_csv('cleaned_customer_shopping_behavior.csv', index=False)

