from behave import given, then, when

_nome = 'Tester'
_telefone = '00000'
_email = 'tester@qatest.com'
_senha = '1234'


@given(u'que estou na tela de login')
def tela_login(context):
    assert context.app.login_page.tela_login(), "Tela de Login inválida."


@given(u'clico no link "New User? Register"')
def clicar_link_novo_user(context):
    context.app.login_page.tela_novo_usuario()
    assert context.app.register_page.tela_registration(), "Link 'New User? Register' não encontrado."


@when(u'preencho todos os campos em branco')
def preencher_campos_register(context):
    context.app.register_page.preencher_dados_user(_nome, _telefone, _email, _senha)
    assert context.app.register_page.dados_preenchidos_tela_register(_nome, _telefone, _email, _senha), "Dados preenchidos não batem com dados enviados."


@when(u'clico no botão "Register"')
def clicar_register(context):
    assert context.app.register_page.status_elemento_botao_register(), "Botão 'Register' não encontrado."
    context.app.register_page.clicar_botao_register()


@then(u'o usuário é criado e permanecemos na tela de cadastro')
def mensagem_sucesso_register(context):
    assert context.app.register_page.tela_registration(), "Tela de cadastro inválida. "


@given(u'preencho os campos com dados já cadastrados')
def login_valido(context):
    context.app.login_page.login(_email, _senha)
    assert context.app.login_page.dados_preenchidos_tela_login(_email, _senha), "Dados preenchidos não batem com dados enviados."


@when(u'clico no botão "Login"')
def clicar_login(context):
    assert context.app.login_page.status_elemento_botao_login(), "Botão 'Login' não encontrado."
    context.app.login_page.clicar_botao_login()


@then(u'a mensagem "You are now logged in" é exibida na tela')
def mensagem_sucesso_login(context):
    assert context.app.login_page.login_message() == "You are now logged in", "Mensagem 'You are now logged in' não encontrada."


@given(u'preencho os campos com dados não cadastrados')
def login_invalido(context):
    context.app.login_page.login(email='teste', senha='01020304')
    assert context.app.login_page.dados_preenchidos_tela_login(email='teste', senha='01020304'), "Dados preenchidos não batem com dados enviados."


@then(u'o login não é realizado e permanecemos na tela de login')
def erro_login(context):
    assert context.app.login_page.tela_login(), "Tela de Login inválida."
