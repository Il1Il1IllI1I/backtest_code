# 📈 Backtest Code 

🚀 **Project Objective:** Providing code for stock backtesting and strategy evaluation.

## 🔍 Testing Range
- Currently Supported: **KOSPI, KOSDAQ**
- Upcoming: U.S. Stocks (Starting with stocks listed on Toss Securities and expanding thereafter)

## 📊 Strategies
- Currently Supported: **Minervini, Turtle, RSI**
- Ongoing: Continuous updates with diverse investment strategies.

## 🗓 Testing Period
- From **January 1, 2015** to present.

## 📌 Key Indicators (More to come)

### 1. **CAGR (Compound Annual Growth Rate)**
- Represents the geometric progression ratio.
- Indicates the annual growth rate over the investment period.
- Annualizes the total growth rate for the entire investment period.

### 2. **MDD (Maximum Drawdown)**
- The greatest percentage drop in asset price over a specified time period.
- Represents how large of a loss an investment strategy can experience.
- A significant indicator to evaluate the riskiness of an investment.

### 3. **Sharpe Ratio**
- Measures risk-adjusted return.
- Indicates how much return an investment strategy has achieved over the risk-free rate.
- A higher value signifies a better performance relative to the risk taken.

### 4. **Sortino Ratio**
- Similar to the Sharpe Ratio but considers only the downside volatility.
- Useful in assessing how well an investment is protected during market downturns.

### 5. **Calmar Ratio**
- The ratio of CAGR to MDD.
- Typically used based on the data of the most recent three years.
- Represents the return of an investment strategy relative to its risk.

### 6. **Alpha** and **Beta**
- **Alpha**: Represents the excess return of an investment relative to the return of a benchmark.
- **Beta**: Indicates how volatile an investment is compared to its benchmark.

### 7. **Annual Volatility**
- Indicates the annual variability of returns.
- Utilized to assess the riskiness of an investment.

### 8. **Skewness** and **Kurtosis**
- **Skewness**: Represents the asymmetry of returns distribution. Shows the tilt of distribution.
- **Kurtosis**: Indicates the peakedness of the returns distribution. A higher value signifies a heavier-tailed distribution.

### 9. **Maximum Drawdown Duration**
- The duration of the maximum loss.
- Represents the time taken for an investment to recover post MDD.

### 10. **Win Rate**
- The percentage of trades that resulted in a win.

### 11. **Average Win** and **Average Loss**
- Represents the average returns from winning and losing trades, respectively.

### 12. **Profit Factor**
- The ratio of total profit to total loss.
- A value greater than 1 indicates an overall profit.

### 13. **Number of Trades**
- The total number of trades executed during the testing period.

## 🏆 Benchmark (More to come)
- Default Benchmarks: Choice among **KOSPI, KOSDAQ, S&P 500**.

## 🛠 Additional Settings 
- **Slippage**: Default at 0.5% (modifiable).
- **Risk Ratio**: Strategy-specific optimized risk management approach applied.

## 🔗 API Integration and Mock Trading
- In progress. Refer to [quent_py](https://www.youtube.com/watch?v=PIuxm_9Os54) for details. (Link directs to the respective YouTube channel).

💡 **Note:** This code is designed for backtesting purposes. It's crucial to thoroughly review before applying it directly to real investments. For actual investments, consulting with professionals is recommended.




---


# 📈 Backtest Code 

🚀 **프로젝트 목적:** 주식 백테스팅을 위한 코드 제공 및 전략 평가

## 🔍 테스트 범위
- 현재 지원: **KOSPI, KOSDAQ**
- 추가 예정: 미국 주식 (토스증권 상장 종목부터 확장 예정)

## 📊 전략
- 현재 지원: **Minervini, Turtle, RSI**
- 추가 예정: 다양한 투자 전략을 계속해서 업데이트 예정

## 🗓 테스트 기간
- **2015-01-01**부터 현재까지

## 📌 주요 지표 (추가 예정)_

### 1. **CAGR (Compound Annual Growth Rate)**
- 복합 연간 성장률입니다.
- 투자 기간 동안의 연평균 성장률을 나타냅니다.
- 전체 투자 기간 동안의 성장률을 연간화한 값입니다.

### 2. **MDD (Maximum Drawdown)**
- 주어진 기간 동안의 최대 손실률입니다.
- 전략이 얼마나 큰 손실을 경험할 수 있는지를 나타냅니다.
- 투자의 위험성을 평가하는 데 중요한 지표입니다.

### 3. **Sharpe Ratio**
- 초과 수익률 대비 위험을 나타내는 지표입니다.
- 투자 전략의 수익률이 리스크 프리 레이트보다 얼마나 높은지를 나타냅니다.
- 값이 클수록 위험 대비 더 높은 수익률을 얻었다는 것을 의미합니다.

### 4. **Sortino Ratio**
- Sharpe Ratio와 유사하지만 하락 방향의 표준 편차만을 고려합니다.
- 전략이 하락장에서 얼마나 잘 보호되는지 평가하는 데 유용합니다.

### 5. **Calmar Ratio**
- CAGR과 MDD의 비율로 계산됩니다.
- 주로 최근 3년 간의 데이터를 기반으로 사용됩니다.
- 전략의 위험 대비 수익률을 나타냅니다.

### 6. **Alpha**와 **Beta**
- **Alpha**: 전략의 초과 수익률을 나타냅니다. 벤치마크 대비 얼마나 더 좋은 성과를 내었는지를 나타냅니다.
- **Beta**: 전략의 변동성이 벤치마크 대비 얼마나 높은지를 나타냅니다.

### 7. **Annual Volatility**
- 연간 수익률의 변동성을 나타냅니다.
- 투자의 위험성을 평가하는 데 사용됩니다.

### 8. **Skewness**와 **Kurtosis**
- **Skewness**: 수익률 분포의 비대칭도를 나타냅니다. 분포의 기울어진 정도를 나타냅니다.
- **Kurtosis**: 수익률 분포의 뾰족함을 나타냅니다. 높은 값을 가질수록 꼬리가 무거운 분포를 가집니다.

### 9. **Maximum Drawdown Duration**
- 최대 손실 기간을 나타냅니다.
- MDD 발생 후 투자가 복구되기까지 걸린 시간을 나타냅니다.

### 10. **Win Rate**
- 전체 거래 중에서 이긴 거래의 비율입니다.

### 11. **Average Win**와 **Average Loss**
- 평균적으로 이긴 거래와 진 거래에서 발생한 수익률을 나타냅니다.

### 12. **Profit Factor**
- 총 수익의 총 손실로 나눈 값입니다.
- 1보다 큰 값은 전체적으로 수익이 발생했음을 나타냅니다.

### 13. **Number of Trades**
- 테스트 기간 동안 실행된 총 거래 횟수입니다.



## 🏆 벤치마크 (추가 예정)
- 기본 벤치마크: **KOSPI, KOSDAQ, S&P 500** 중 선택 가능

## 🛠 추가 설정 
- **슬리피지(Slippage)**: 기본값 0.5% (변경 가능)
- **리스크 비율(Risk Ratio)**: 전략별 최적화된 리스크 관리 방법 적용

## 🔗 API 연동 및 모의투자
- 진행 예정, [quent_py](https://www.youtube.com/watch?v=PIuxm_9Os54) 참고 (링크는 해당 유튜브 채널로 연결됩니다.)

💡 **주의 사항:** 이 코드는 백테스팅을 위한 것으로 실제 투자에 직접 사용하기 전에 충분한 검토가 필요합니다. 실제 투자 시에는 전문가와 상담하는 것을 추천드립니다.
