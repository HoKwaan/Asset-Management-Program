# Asset-Management-Program
# 📊 자산관리 프로그램 (Asset Management Program)

이 프로젝트는 **개인 자산을 체계적으로 관리**하기 위한 파이썬 기반 CLI 프로그램입니다.

* 💰 수입/지출 기록 및 자동 잔액(balance) 관리
* 📈 월별 지출 분석 및 다음 달 지출 예측 (ML 기반)
* 🧠 예측 결과를 활용한 투자 가능 자산 계산
* 🪙 올웨더(All Weather) 포트폴리오 자동 배분
* 📝 투자 완료 여부 관리

---

## 📁 프로젝트 구조

```
project_root/
│
├─ asset_management/
│   ├─ analysis.py              # 월별 지출 집계
│   ├─ expense_model.py         # 지출 예측 모델 + 최신 잔액 조회
│   ├─ transaction_manager.py   # 거래 추가, 잔액 확인
│
├─ asset_saving/
│   ├─ investment.py            # 투자 객체 정의 및 저장
│   ├─ portfolio.py             # 포트폴리오 계산 로직
│
├─ data/
│   ├─ transactions.csv         # 거래 내역 (balance 자동 계산)
│   ├─ investment_status.csv    # 투자 상태 저장
│
└─ main.py                      # 프로그램 실행 진입점
```

---

## 📄 데이터 형식

### transactions.csv

```csv
date,category,amount,type,balance
2024-01-01,Salary,3500000,income,3500000
2024-01-05,Rent,-800000,expense,2700000
```

* `balance`는 **직접 입력하지 않으며**, 항상 이전 거래 기준으로 자동 계산됩니다.
* CSV의 마지막 `balance` 값이 **현재 총 자산의 단일 기준(Source of Truth)** 입니다.

---

## 🧠 주요 기능 설명

### 1️⃣ 계좌 상태 변경

* 수입(income) 또는 지출(expense)을 입력
* 금액만 입력 → 잔액은 자동 누적

### 2️⃣ 자산 상태 확인

* 현재 잔액(balance) 출력
* 최근 거래 내역 확인 가능

### 3️⃣ 지출 분석 및 예측

* 월별 지출 합계 계산
* 최근 패턴을 기반으로 **다음 달 지출 예측**
* 데이터 부족 시 평균값으로 안전 처리

### 4️⃣ 투자 가능 자산 계산

* 예측 지출 + 안전 여유금(buffer)을 제외한 금액 산출

### 5️⃣ 올웨더 포트폴리오 배분

* 투자 가능 자산을 다음 비율로 자동 배분

```python
ALL_WEATHER = {
    "Equity": 0.30,
    "Long_Bond": 0.40,
    "Mid_Bond": 0.15,
    "Gold": 0.075,
    "Commodity": 0.075,
}
```

### 6️⃣ 투자 상태 변경

* 각 자산별로 `y / n` 입력
* 투자 완료 여부를 CSV에 저장

---

## ▶ 실행 방법

```bash
python main.py
```

프로그램 실행 후 메뉴를 통해 기능을 선택합니다.

```
===== 자산관리 프로그램 =====
1. 계좌 상태 변경
2. 투자 상태 변경
3. 자산 분석 및 포트폴리오 실행
4. 자산 상태 확인
0. 종료
```

---

## 🔒 입력 안정성

* 모든 숫자 입력은 예외 처리
* `y / n` 입력은 대소문자 허용, 잘못 입력 시 재요청
* 음수/문자 입력 방어

---

## ✅ 설계 철학

* **관심사 분리 (Separation of Concerns)**
* CSV 기반 상태 관리 (DB 없이도 안정적)
* 확장 가능한 구조 (GUI / 웹으로 확장 가능)

---

## 🚀 향후 확장 아이디어

* 📈 월별 잔액 변화 그래프
* ❌ 거래 수정 / 삭제 기능
* 🧪 예측 정확도 평가
* 🖥 GUI 또는 웹 서비스화

---

## 👤 작성자

* 개인 자산 관리 및 투자 자동화를 목표로 한 학습/실전 프로젝트

---

필요 시 이 README는 GitHub 업로드용으로 바로 사용 가능합니다.
