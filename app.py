import pandas as pd


code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]


code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 
code_df = code_df[['회사명', '종목코드']] # 한글로된 컬럼명을 영어로 바꿔준다. 
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

print(len(code_df.index)) #주식 종목 코드수 구하기

stuck_len = len(code_df.index)

for i in range(stuck_len) :
    code = code_df.iloc[i].code
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code) 
    print("요청 URL = {}".format(url)) 
    # code_df.iloc[0].code
    
    df = pd.DataFrame() # 1페이지에서 20페이지의 데이터만 가져오기 
    for page in range(1, 21): 
        pg_url = '{url}&page={page}'.format(url=url, page=page) 
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) # df.dropna()를 이용해 결측값 있는 행 제거 
    df = df.head() # 상위 5개 데이터 확인하기 df.head()
    print(df)
