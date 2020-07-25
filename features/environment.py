from appium import webdriver
from app.aplicacao import Aplicacao


def before_scenario(context, cenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities={'platformName': 'Android',
                                                            "deviceName": "emulator-5554",
                                                            "appPackage": "com.example.vamsi.login",
                                                            "appActivity": "com.example.vamsi.login.MainActivity",
                                                            "app": "/home/coutinho/Desktop/DEV/desafio-smartbank_appium/app/app-debug.apk",
                                                            "noReset": "true"
                                                            })
    
    context.driver.implicitly_wait(5)
    context.app = Aplicacao(context.driver)
