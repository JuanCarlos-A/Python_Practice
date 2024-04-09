"""
Ejemplo 1 : (https://sergio1998.medium.com/qu%C3%A9-son-los-mixin-en-python-y-como-deber%C3%ADa-usarlos-8b6e3a4a5755)

Supongamos que tenemos una jerarquía de clases de cuentas bancarias, en donde se tiene el requerimiento de 
que solo algunas de ellas tienen que tener el comportamiento de enviar reportes mediante email.

El requerimiento es que tanto CorporativeBankAccount y SharedBankAccount implementen la lógica de enviar 
reportes mediante email.

"""

class SendEmailReportMixin:

    def send_email_report(self, transactions):
        pass

class BankAccount:
    pass

class CorporativeBankAccount(BankAccount, SendEmailReportMixin):
    pass

class PersonBankAccount(BankAccount):
    pass

class SharedBankAccount(BankAccount, SendEmailReportMixin):
    pass

