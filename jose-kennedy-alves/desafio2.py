#Controle de Acesso
U = {'READ', 'EXPORT', 'EDIT', 'DELETE', 'ADMIN'}

# 1- Escrever função can_execute(user_perms,action)
def can_execute(user_perms,action):
    return action in U and action in user_perms

# 2-  Escrever função get)missing(user_perms,req_perms)
def get_missing_perms(user_perms,req_perms):
    return req_perms - user_perms

# 3- Testar se permissões do operador são subconjuntos estrito do admin (operador < admin)
operador = {'READ', 'EXPORT'}
admin = {'READ', 'EXPORT', 'EDIT', 'DELETE', 'ADMIN'}

print('Pode executar READ?', can_execute(operador,'READ'))

print('\nPode executar DELETE?', can_execute(operador,'DELETE'))

print('\nPermissões faltantes:', get_missing_perms(operador,{'READ', 'EXPORT', 'EDIT'}))

print('\nOperador é subconjunto própio do Admin?', operador < admin)