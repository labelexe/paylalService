from app.models import PaymentMethod


class PaymentMethodService:
    def __init__(self):
        self.payment_methods = []

    def get_payment_methods(self, user_id: int = None, status: str = None, type: str = None):
        filtered_payment_methods = self.payment_methods
        if user_id:
            # Filter by user_id
            filtered_payment_methods = [pm for pm in filtered_payment_methods if user_id in pm.users]
        if status:
            # Filter by status
            filtered_payment_methods = [pm for pm in filtered_payment_methods if pm.status == status]
        if type:
            # Filter by type
            filtered_payment_methods = [pm for pm in filtered_payment_methods if pm.type == type]
        return filtered_payment_methods

    def create_payment_method(self, payment_method: PaymentMethod):
        payment_method.id = len(self.payment_methods) + 1
        self.payment_methods.append(payment_method)
        return payment_method

    def update_payment_method(self, payment_method_id: int, updated_payment_method: PaymentMethod):
        for pm in self.payment_methods:
            if pm.id == payment_method_id:
                pm.name = updated_payment_method.name
                pm.logo_url = updated_payment_method.logo_url
                pm.short_name = updated_payment_method.short_name
                pm.description = updated_payment_method.description
                return pm
        return None

    def delete_payment_method(self, payment_method_id: int):
        self.payment_methods = [pm for pm in self.payment_methods if pm.id != payment_method_id]
