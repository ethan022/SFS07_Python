# ============================================================
# 💳 추상 클래스와 추상 메서드 학습 예제
# ============================================================

# abc 모듈: 추상 클래스 및 추상 메서드를 정의할 때 사용
from abc import ABC, abstractmethod


# ==============================
# 1. PaymentSystem (추상 클래스)
# ==============================
class PaymentSystem(ABC):
    """
    결제 시스템의 공통 기능을 정의한 추상 클래스
    - 직접 객체 생성 불가
    - 자식 클래스가 반드시 구현해야 하는 메서드를 정의
    """

    @abstractmethod
    def authenticate(self):
        """사용자 인증 메서드 (반드시 구현 필요)"""
        pass

    @abstractmethod
    def process_payment(self, amount):
        """결제 처리 메서드 (반드시 구현 필요)"""
        pass

    def payment_summary(self, amount):
        """
        일반 메서드
        - 자식 클래스에서 구현하지 않아도 상속됨
        """
        print(f"{amount} 원 결제가 완료되었습니다.")


# ========================================
# 2. CreditCard 클래스 (추상 클래스 구현)
# ========================================
class CreditCard(PaymentSystem):
    """
    신용카드 결제 시스템 클래스
    - 추상 클래스인 PaymentSystem을 상속받아 구현
    """

    def authenticate(self):
        """신용카드 인증 로직"""
        print("신용카드 인증 완료")

    def process_payment(self, amount):
        """신용카드 결제 처리 로직"""
        print(f"신용카드로 {amount} 원 결제합니다.")


# ============================================================
# ✅ 사용 예제
# ============================================================
print("========== abstractmethod ===========")

# 추상 클래스를 직접 사용할 수는 없음 → 반드시 구현된 클래스로 생성
credit_card = CreditCard()  # CreditCard는 추상 메서드를 모두 구현했기 때문에 인스턴스 생성 가능

credit_card.authenticate()          # 인증 메서드 호출
credit_card.process_payment(3000)   # 결제 처리
credit_card.payment_summary(5000)   # 일반 메서드도 상속되어 사용 가능
