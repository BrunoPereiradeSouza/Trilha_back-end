from rolepermissions.roles import AbstractUserRole


# Cria grupos de Usuários. Isso permite controlar os níveis de acesso na aplicação.
class Client(AbstractUserRole):
    available_permissions = {'buy_products': True}  # Permissões do grupo


class Admin(AbstractUserRole):
    available_permissions = {       # Permissões do grupo
        'see_products': True,
        'create_produts': True, 
        'update_products': True,
        'delete_products': True
        }
