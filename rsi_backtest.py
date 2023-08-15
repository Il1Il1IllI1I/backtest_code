import pandas as pd
import numpy as np
import FinanceDataReader as fdr
import datetime

def rsi_trading_strategy(ticker, period=14):
    """RSI 트레이딩 전략 백테스트 함수"""

    # 데이터 가져오기
    data = fdr.DataReader(ticker, start="2022-06-01")
    
    # RSI 계산
    delta = data['Close'].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    
    avg_gain = pd.Series(gain).rolling(window=period).mean()
    avg_loss = pd.Series(loss).rolling(window=period).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # 매수, 매도 신호 생성
    data['Buy_Signal'] = np.where(data['RSI'] <= 30, 1, 0)
    data['Sell_Signal'] = np.where(data['RSI'] >= 70, -1, 0)
    
    # 매수, 매도 신호 합산
    data['Position'] = data['Buy_Signal'] + data['Sell_Signal']

    # 최근 거래일의 매매 신호 반환 (1: 매수, -1: 매도, 0: 보류)
    return data['Position'].iloc[-1]

# 모든 코스피, 코스닥 종목 정보 가져오기
all_stocks = pd.concat([fdr.StockListing('KOSPI'), fdr.StockListing('KOSDAQ')]).set_index('Code')

# 매수 종목을 저장하기 위한 리스트
buy_tickers = []

# 백테스트 시작 시간 기록
start_time = datetime.datetime.now()

# 각 종목별로 RSI 트레이딩 전략 실행
for ticker in all_stocks.index:
    print(f"{ticker} - {all_stocks.loc[ticker, 'Name']} 테스트 중...")
    signal = rsi_trading_strategy(ticker)
    if signal == 1:
        buy_tickers.append({'Ticker': ticker, 'Name': all_stocks.loc[ticker, 'Name']})

# 백테스트 종료 시간 기록
end_time = datetime.datetime.now()

# 결과 DataFrame 생성
df = pd.DataFrame(buy_tickers)

# 시가총액, 변동률, 시장 정보 추가
df['MarketCap'] = df['Ticker'].apply(lambda x: all_stocks.loc[x, 'Marcap'])
df['ChangesRatio'] = df['Ticker'].apply(lambda x: all_stocks.loc[x, 'ChangesRatio'])
df['Market'] = df['Ticker'].apply(lambda x: all_stocks.loc[x, 'Market'])

# 시가총액으로 내림차순 정렬
df = df.sort_values(by='MarketCap', ascending=False)

# 시가총액 값을 보기 좋게 변경
df['MarketCap'] = (df['MarketCap'] / 10**8).round().astype(int).astype(str) + '억'
df['Market'] = df['Market'].replace({'KOSPI': '코스피', 'KOSDAQ': '코스닥', 'KOSDAQ GLOBAL': '코스닥'})

# 결과 저장
df.to_csv("rsi_buy_tickers.csv", index=False)

# 백테스트에 걸린 시간 출력
print(f"백테스트에 걸린 시간: {end_time - start_time}")
