from rolepermissions.roles import AbstractUserRole


class Client(AbstractUserRole):
    available_permissions = {'buy_products': True}


class Admin(AbstractUserRole):
    available_permissions = {
        'see_products': True, 'create_produts': True, 'update_products': True,
        'delete_products': True
        }
