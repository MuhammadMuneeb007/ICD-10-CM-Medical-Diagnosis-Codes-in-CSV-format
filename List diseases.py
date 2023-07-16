import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from pybtex.database.input import bibtex
import os
from collections import Counter
import pandas as pd
import numpy as np
import json
from scholarly import scholarly
from tika import parser # pip install tika
from paraphraser import paraphrase
import os
import sys
import scihub
from crossref.restful import Works
works = Works()
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
import pandas as pd
import re
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from wordcloud import WordCloud


data = pd.read_csv("summary_statistics_table_export.tsv",sep="\t")
print(data.columns)
data = data.drop_duplicates(subset=['reportedTrait'])
print(data.head())
data.reportedTrait.to_csv("Alldiseases.csv")


import PyPDF2
count=1
def extract_text_from_pdf(file_path,x,y):
    text = ''
    codes = []
    names = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        print(pdf_reader.pages)
        for loop in range(x,y):
            page = pdf_reader.getPage(loop)
            text = page.extractText()
            print("Processing Page: ",str(loop))
            if count==1:
                for l in text.split("\n")[2:]:
                    uuu = l.strip().split(" ")
                    codes.append(uuu[0].strip())
                    del uuu[0]
                    names.append(" ".join(uuu).strip())
                    
            else:
                for l in text.split("\n"):
                    uuu = l.strip().split(" ")
                    codes.append(uuu[0].strip())
                    del uuu[0]
                    names.append(" ".join(uuu).strip())
                    
            tempdataframe = pd.DataFrame()
            tempdataframe['ICD10_Codes'] = codes
            tempdataframe['Disease_Name'] = names
            #print(tempdataframe)
            tempdataframe.to_csv("ICDCodes"+str(x)+".csv")
            #exit(0)

pdf_file_path = 'icd-10-medical-diagnosis-codes.pdf'
for loop in range(0,3001,50):
    extracted_text = extract_text_from_pdf(pdf_file_path,loop,loop+50)
    print(extracted_text)
    #exit(0)




