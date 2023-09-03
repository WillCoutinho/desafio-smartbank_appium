## Desafio 2 - Appium
Passo a passo para instalar, configurar e rodar os testes do Appium.\
Cenários feitos para o apk disponível em: https://bit.ly/2YTkkIV

##
### Pré Requisitos para Windows 10

Instale a versão 3.8.3 (executable) do [**Python**](https://www.python.org/downloads/release/python-383/)
>**_Nota_**: Antes de instalar, selecione a opção 'Add Python 3.8 to PATH'

Instale o [**GIT**](https://git-scm.com/download/win) para clonar o repositório

Instale o [**Appium Server - Desktop**](http://appium.io/downloads.html)

Baixe o framework de report [**Allure (2.13.5)**](https://github.com/allure-framework/allure2/releases) e descompacte na pasta que desejar.

- Abra o terminal _Powershell_: ``Menu Iniciar > digite _'Powershell'``
- Configure o ``PATH`` do _Allure Framework_ com o comando: 
````bash
$env:PATH += ';\Caminho_Pasta_Allure\allure-2.13.5\bin'
````

Instale o [**Java JDK**](https://www.java.com/pt_BR/download/) e abra as opções: ``Menu Iniciar > Digite 'Ambiente' > 'Editar Variáveis de Ambiente' > Variáveis de Ambiente``

- Crie uma nova variável de usuário ``JAVA_HOME`` e como valor o caminho onde o Java foi instalado
- Crie uma nova variável de sistema em ``Path``, adicionando o valor ``%JAVA_HOME%\bin``


Instale o [**Android Studio**](https://developer.android.com/studio?hl=pt-br) e abra as opções: ``Menu Iniciar > Digite 'Ambiente' > 'Editar Variáveis de Ambiente' > Variáveis de Ambiente`` 

- Crie uma nova variável de usuário ``ANDROID_HOME`` e como valor o caminho onde o Android Studio-SDK foi instalado (ex.``C:\Users\UserName\AppData\Local\Android\Sdk``)
- Crie uma nova variável de sistema em ``Path``, adicionando os valores ``%ANDROID_HOME%\tools``, ``%ANDROID_HOME%\build-tools`` e ``%ANDROID_HOME%\platform-tools``
> _**Nota**_: Em caso de dúvidas utilize o [guia de instalação](https://developer.android.com/studio/install?hl=pt-br#windows)\
> E para variáveis de ambiente o [guia de usuário](https://developer.android.com/studio/command-line/variables)

Após a instalação do _Android Studio_, crie um emulador e configure-o no ``AVD Manager``.
Vamos utilizar o flavor _Pie (API 28 - Google Play)_. 
> _**Nota**_: Verifique a arquitetura do seu processador (x64 ou x86) e instale de acordo com o mesmo.\
> Em caso de dúvidas utilize o [guia do Android Studio](https://developer.android.com/studio/run/managing-avds?hl=pt-br)

*Reinicie a máquina para que as alterações nas variáveis de ambiente sejam realizadas.*

##
### Pré Requisitos para Linux (Ubuntu)
Instale a versão 3.8.3 do **Python**: ``sudo apt-get install python3.8``

Instale o **Python pip**: ``sudo apt install python3-pip``

Instale o **GIT**: ``sudo apt install git``

Baixe o [**Appium Server - Desktop**](http://appium.io/downloads.html) extensão _AppImage_ e dê as permissões necessárias:
````bash
sudo chmod u+x Appium.AppImage
````

Baixe o framework de report [**Allure (2.13.5)**](https://github.com/allure-framework/allure2/releases) e descompacte na pasta que desejar.\
Abra o terminal e insira o caminho da pasta ``bin`` do _Allure Framework_ no ``PATH`` environment: 
````bash 
sudo nano /etc/environment
>> PATH="[...]:/Allure_Path/bin"
>> CTRL+X > Yes > Enter 
source /etc/environment
````

Instale o [**Java JDK Oracle**](https://www.java.com/pt_BR/download/) e crie as variáveis de ambiente ``JAVA_HOME`` e como valor o caminho onde Java está instalado.\
Insira também a pasta ``\bin`` no Path environment.
> _**Nota**_: Em caso de dúvidas para instalar o Java da Oracle utilize o [guia da Oracle](https://www.java.com/pt_BR/download/help/path.xml)  
>
>> Podemos utilizar também o **OpenJDK** e **OpenJRE** que é mais simples de instalar, e que supre o Java da Oracle:
>>````bash
>>- sudo apt install default-jre
>>- sudo apt install default-jdk
>>````
>> Feito isso, basta incluir nas variáveis de ambiente a pasta ``\bin`` no ``PATH`` e a variável ``JAVA_HOME``
>>````bash 
>> sudo nano /etc/environment
>> >> PATH="[...]:$JAVA_HOME/bin"
>> >> JAVA_HOME="/JDK_Path/"
>> >> CTRL+X > Yes > Enter 
>> source /etc/environment
>> ````

Deste ponto já será possível checar a versão do _Allure_ (``allure --version``) ou Java (``java --version``) para confirmar se o ``PATH`` foi configurado corretamente.

Instale o [**Android Studio**](https://developer.android.com/studio?hl=pt-br) ou use o _Snap_ para instalá-lo: ``sudo snap install android-studio`` 
Instale também as libs para arquitetura 32 bits: ``sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386`` \
E configure a variável de ambiente ``ANDROID_HOME`` e suas pastas internas como ``build-tools``, ``emulator``, ``platforms``, ``platform-tools`` e ``tools``.
````bash
sudo nano /etc/environment
>> PATH="[...]:$ANDROID_HOME/build-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/platforms:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools"
>> ANDROID_HOME="/Android_Sdk_path/"
>> CTRL+X > Yes > Enter 
source /etc/environment
````
> _**Nota**_: Em caso de dúvidas utilize o [guia de instalação](https://developer.android.com/studio/install?hl=pt-br#linux)

Após a instalação do _Android Studio_, crie um emulador e configure-o no ``AVD Manager``.
Vamos utilizar o flavor _Pie (API 28 - Google Play)_. 
> _**Nota**_: Verifique a arquitetura do seu processador (x64 ou x86) e instale de acordo com o mesmo.\
> Utilize o [guia no site do Android Studio](https://developer.android.com/studio/run/managing-avds?hl=pt-br) em caso de dúvidas


##
### Git Clone, Instalação das Libs e Execução dos testes

Crie uma pasta com o nome e no diretório que quiser (para clonar o repositório).\
Clone o repositório do [Desafio 2 - Appium](https://github.com/WillCoutinho/desafio-smartbank_appium.git) e entre na pasta clonada.

Instale o ``pipenv`` com o comando: ``sudo pip3 install pipenv``\
Instale as dependências pelo ``Pipfile`` (que está no diretório raiz) com o comando: ``sudo pipenv install``\
Aguarde as dependências serem instaladas. Após o processo use o comando: ``sudo pipenv shell`` para rodar uma _VirtualEnv_.

Baixe o arquivo _apk_ ([aqui](https://bit.ly/2YTkkIV)) que vamos utilizar nos testes e salve dentro do diretório ``app`` da pasta clonada anteriormente.\
Agora vamos iniciar o emulador. Vá em ``Android Studio > AVD Manager`` e inicie o emulador criado nos passos anteriores.\
Após o mesmo ser lançado, abra um terminal (Powershell p/ Windows || bash p/ Linux) e insira o comando ``adb devices``\
Se o emulador estiver rodando e configurado corretamente, então este comando deve retornar o _número do device_ disponível (ex. ``emulator-0123``). 

Com essas informações, vamos atualizar o arquivo ``environment.py`` para que os testes possam rodar corretamente.\
Acesse na pasta clonada ``features > environment.py`` e em ``desired_capabilities`` altere os respectivos campos abaixo com os seus dados:
````json
{
	 "deviceName": "número_emulador_adb_services",
	 "app": "absolute_path_onde_apk_está_salvo" 
} 
````

Com o **emulador rodando** e o arquivo ``environment.py`` configurado, já podemos rodar os testes.\
Abra o _Appium Server - Desktop_ e inicie o servidor com os dados de ``host`` e ``port`` padrão.
 
Para rodar os testes vamos usar o comando abaixo. 
Os parâmetros deste comando são:\
``--lang=pt``: língua utilizada nos arquivos ``.feature``\
``-f allure_behave.formatter:AllureFormatter``: formato que vamos utilizar na saída (_Allure Framework_)\
``-o allure_result_folder``: pasta onde será salvo a saída do teste\
``./features``: features que serão executadas
       
````bash
behave --lang=pt -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
````
 
Após os testes rodarem, usamos o comando abaixo para gerar o relatório.
O comando criará um servidor local que vai ler os arquivos em ``allure_result_folder`` e lançará os resultados no browser:
````bash
allure serve allure_result_folder
````

Pronto, relatório dos testes mobile disponíveis no browser.

##
#### Repositório

GitHub: [Desafio 2 - Appium (Smartbank)](https://github.com/WillCoutinho/desafio-smartbank_appium) 

##
#### Libs utilizadas

* [Behave](https://pypi.org/project/behave/#description) - BDD com suporte ao Python
* [Allure-Behave](https://pypi.org/project/allure-behave/#description) - Framework para gerar reports
* [Pipenv](https://pypi.org/project/pipenv/#description) - Package/VirtualEnv manager 
* [Selenium](https://pypi.org/project/selenium/#description) - API WebDriver
* [Appium Python Client](https://pypi.org/project/Appium-Python-Client/#description) - Extensão para teste mobile

