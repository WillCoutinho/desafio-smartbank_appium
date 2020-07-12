from selenium.webdriver.common.by import By


class SeleniumDriver:
    
    def __init__(self, driver):
        self.driver = driver
    
    def pegar_tipo_locator(self, tipo_locator):
        """ Retorna por qual método fará a busca: driver.find_element(By.opcao, 'valor que será buscado')
        - Retorna apenas o tipo, não fazendo a busca
        """
        tipo_locator = tipo_locator.lower()
        
        if tipo_locator == "id":
            return By.ID
        elif tipo_locator == "xpath":
            return By.XPATH
        elif tipo_locator == "name":
            return By.NAME
        elif tipo_locator == "css":
            return By.CSS_SELECTOR
        elif tipo_locator == "class":
            return By.CLASS_NAME
        elif tipo_locator == "link":
            return By.LINK_TEXT
        elif tipo_locator == "tag":
            return By.TAG_NAME
        else:
            print(f"Busca por {tipo_locator} não suportado.")
            return False
    
    def pegar_elemento(self, locator, tipo_locator="id"):
        """ Realiza a busca do elemento com base no Locator e no tipo de busca
        - Retorna o elemento
        - O tipo de busca default é por 'id'
        """
        try:
            tipo_locator = tipo_locator.lower()
            by_type = self.pegar_tipo_locator(tipo_locator)
            elemento = self.driver.find_element(by_type, locator)
            return elemento
        
        except Exception as e:
            print(f"Elemento '{locator}' não encontrado.")
            print(e)
            return False
    
    def clicar_elemento(self, locator="", tipo_locator="id", elemento=None):
        """ Realiza ação de click no elemento (sem retorno)
        - O tipo de busca default é por 'id'
        """
        self.driver.hide_keyboard()
        try:
            if locator != "":
                elemento = self.pegar_elemento(locator, tipo_locator)
            elemento.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {locator}")
            print(e)
    
    def inserir_dados_elemento(self, dados, locator, tipo_locator="id"):
        """ Realiza ações de input nos elementos (sem retorno)
       - Recebe como parâmetro os dados que serão inputados, locator e tipo de busca
       - O tipo de busca default é por 'id'
       """
        try:
            by_type = self.pegar_tipo_locator(tipo_locator)
            elemento = self.pegar_elemento(locator, by_type)
            elemento.click()
            elemento.send_keys(dados)
        
        except Exception as e:
            print(f"Não foi possível inserir dados no campo {locator}")
            print(e)
    
    def status_presenca_elemento(self, locator, tipo_locator='id'):
        """ Checa se o elemento é mostrado na página
        - Caso o elemento seja enviado, o mesmo é utilizado diretamente
        - Retorna um booleano
        """
        elemento = None
        status_elemento = False
        self.driver.hide_keyboard()
        try:
            if locator != '':
                elemento = self.pegar_elemento(locator, tipo_locator)
            if elemento is not None:
                status_elemento = elemento.is_displayed()
            else:
                print(f'Elemento {locator} não encontrado ou nulo')
            return status_elemento
        
        except Exception as e:
            print(e)
            return False
