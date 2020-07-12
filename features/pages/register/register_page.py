from features.pages.base.selenium_driver import SeleniumDriver


class RegisterPage(SeleniumDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _campo_nome = 'com.example.vamsi.login:id/etRegName'
    _campo_tel = 'com.example.vamsi.login:id/etRegPhone'
    _campo_email = 'com.example.vamsi.login:id/etRegGmail'
    _campo_senha = 'com.example.vamsi.login:id/etRegPassword'
    _botao_register = 'com.example.vamsi.login:id/btnRegLogin'
    _botao_login = 'com.example.vamsi.login:id/btnGotoLogin'
    _logged_message_txt = "//android.widget.TextView[@text='You are now logged in']"
    _register_titulo = "//android.widget.TextView[@text='Registration']"
    
    def _preencher_nome(self, nome):
        self.inserir_dados_elemento(nome, self._campo_nome, tipo_locator="id")
    
    def _preencher_telefone(self, telefone):
        self.inserir_dados_elemento(telefone, self._campo_tel, tipo_locator="id")
    
    def _preencher_email(self, email):
        self.inserir_dados_elemento(email, self._campo_email, tipo_locator="id")
    
    def _preencher_senha(self, senha):
        self.inserir_dados_elemento(senha, self._campo_senha, tipo_locator="id")
    
    def _clicar_botao_login(self):
        self.clicar_elemento(self._botao_login, tipo_locator="id")
    
    def clicar_botao_register(self):
        self.clicar_elemento(self._botao_register, tipo_locator='id')
    
    def preencher_dados_user(self, nome, telefone, email, senha):
        self._preencher_nome(nome)
        self._preencher_telefone(telefone)
        self._preencher_email(email)
        self._preencher_senha(senha)
    
    def tela_registration(self):
        if self.pegar_elemento(self._register_titulo, 'xpath').text == 'Registration':
            return True
        else:
            return False
    
    def dados_preenchidos_tela_register(self, nome='Tester', telefone='00000', email='tester@qa.com', senha='1234'):
        lista_campos = [self._campo_nome, self._campo_tel, self._campo_email, self._campo_senha]
        lista_valores = [nome, telefone, email, senha]
        dados_corretos = False
        for campo in lista_campos:
            for valor in lista_valores:
                if valor in self.pegar_elemento(campo, tipo_locator='id').text:
                    dados_corretos = True
        
        return dados_corretos
    
    def status_elemento_botao_register(self):
        return self.status_presenca_elemento(self._botao_register, tipo_locator='id')
