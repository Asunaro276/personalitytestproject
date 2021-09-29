from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns

from personality import make_result, normalize


n_factors = 2
data = pd.read_csv('HBDS-data/data.csv', sep='\t')
data = data[[f'Q{i+1}' for i in range(20)]]
data = data.drop(['Q7', 'Q13'], axis=1)
questions = [f'Q{i+1}' for i in range(18)]
fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax')
fa.fit(data)
with open('./factor_analyzer', 'wb') as fa_file:
    pickle.dump(fa, fa_file)

fl = pd.DataFrame(fa.loadings_, columns=[f'factor{i+1}' for i in range(n_factors)], index=questions)
from PIL import Image
res = pd.DataFrame(fa.transform(data[92:93]), columns=[f'factor{i+1}' for i in range(n_factors)])
res = np.squeeze(res)
res['factor1'] /= 3.11708
res['factor2'] /= 2.47097
res['factor1'] = 1280 * (res['factor1'] + 1) / 2
res['factor2'] = 720 * (res['factor2'] + 1) / 2

img_back = Image.open('../static/images/plt_axis.png')
img_back = img_back.convert('RGB')
img_back = np.array(img_back)
img_back = np.flipud(img_back)
plt.figure(figsize=(5, 3))
plt.imshow(img_back)
plt.scatter(res['factor1'], res['factor2'], s=50)
plt.xlim(-20, 1300)
plt.ylim(-20, 740)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.tick_params(labelbottom=False,
                labelleft=False,
                labelright=False,
                labeltop=False)
plt.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)

plt.show()
