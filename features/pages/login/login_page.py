from features.pages.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _campo_email = 'com.example.vamsi.login:id/etLogGmail'
    _campo_senha = 'com.example.vamsi.login:id/etLoginPassword'
    _botao_login = 'com.example.vamsi.login:id/btnLogin'
    _register_link = 'com.example.vamsi.login:id/tvRegister'
    _logged_message_txt = "//android.widget.TextView[@text='You are now logged in']"
    _login_titulo = "//android.widget.TextView[@text='Login']"
    
    def _preencher_email(self, email):
        self.inserir_dados_elemento(email, self._campo_email, tipo_locator="id")
    
    def _preencher_senha(self, senha):
        self.inserir_dados_elemento(senha, self._campo_senha, tipo_locator="id")
    
    def clicar_botao_login(self):
        self.clicar_elemento(self._botao_login, tipo_locator='id')
    
    def login(self, email, senha):
        self._preencher_email(email)
        self._preencher_senha(senha)
    
    def login_message(self):
        return self.pegar_elemento(self._logged_message_txt, tipo_locator='xpath').text
    
    def tela_login(self):
        if self.pegar_elemento(self._login_titulo, tipo_locator='xpath').text == 'Login':
            return True
        else:
            return False
    
    def tela_novo_usuario(self):
        self.clicar_elemento(self._register_link, tipo_locator='id')
    
    def dados_preenchidos_tela_login(self, email, senha):
        lista_campos = [self._campo_email, self._campo_senha]
        lista_valores = [email, senha]
        dados_corretos = False
        for campo in lista_campos:
            for valor in lista_valores:
                if valor in self.pegar_elemento(campo, tipo_locator='id').text:
                    dados_corretos = True
        
        return dados_corretos
    
    def status_elemento_botao_login(self):
        return self.status_presenca_elemento(self._botao_login, tipo_locator='id')
