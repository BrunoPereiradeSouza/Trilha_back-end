from rolepermissions.roles import AbstractUserRole


class Client(AbstractUserRole):
    available_permissions = {'buy_products': True}
