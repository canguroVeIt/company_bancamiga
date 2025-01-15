{
    'name': 'Configuracion de Bancamiga',
    'version': '1.0',
    'author': 'Manuel',
    'website': 'https://komerzio.net',
    'category': 'Custom',
    'summary': 'Gestión de autorizacion bancarios para diferentes sedes.',
    'description': '''Este módulo permite registrar, administrar y consultar los tokens
    bancarios de cada una de las sedes de la empresa, garantizando
    una gestión centralizada y segura de esta información.''',
    'depends': ['base'],  # Agrega otros módulos si tu módulo depende de ellos.
    'data': [
        'views/bank_token.xml',
    ],
    'installable': True,
    'application': True,
}
