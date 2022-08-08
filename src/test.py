import pickle
import pandas as pd
import numpy as np


country = 'Other'
variety='Other'
aroma=7.42
aftertaste =7.33
acidity =7.42
body=7.25
balance = 7.33
moisture = 0.0

cols=['country','variety', 'aroma','aftertaste','acidity','body','balance','moisture']
data=[country,variety, aroma,aftertaste,acidity,body,balance,moisture]
posted=pd.DataFrame(np.array(data).reshape(1,8),columns=cols)

loaded_model=pickle.load(open('../models/coffee_model.pkl','rb'))
#rb=read binary
result=loaded_model.predict(posted)
text_result=result.tolist()[0]
print(text_result)