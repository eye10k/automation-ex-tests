class PaymentCard:
    def __init__(
        self,
        holder_name: str,
        card_number: str,
        expire_month: str,
        expire_year: str,
        cvc: str
    ):
        self.holder_name = holder_name
        self.card_number = card_number
        self.expire_month = expire_month
        self.expire_year = expire_year
        self.cvc = cvc
