"""
Ejemplo 1 : 

Supongamos que tenemos una jerarquía de clases de cuentas bancarias, en donde se tiene el 
requerimiento de que solo algunas de ellas tienen que tener el comportamiento de enviar reportes 
mediante email.

El requerimiento es que tanto CorporativeBankAccount y SharedBankAccount implementen la lógica 
de enviar reportes mediante email.

"""


class SendEmailReportMixin:
    """Clase Mixin que implementa el comportamiento de enviar reportes mediante email."""

    def send_email_report(self, transactions):
        """ Método que envía un reporte de transacciones mediante email."""
        pass


class BankAccount:
    """Clase base para las cuentas bancarias."""
    pass


class CorporativeBankAccount(BankAccount, SendEmailReportMixin):
    """Clase que representa una cuenta corporativa. Haciendo mixin con SendEmailReportMixin."""
    pass


class PersonBankAccount(BankAccount):
    """Clase que representa una cuenta personal."""
    pass


class SharedBankAccount(BankAccount, SendEmailReportMixin):
    """Clase que representa una cuenta compartida. Haciendo mixin con SendEmailReportMixin."""
    pass
