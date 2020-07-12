# – FILE: features/login.feature # language: pt

Funcionalidade: Efetuar login no app
Como usuário
Quero realizar login
Assim posso me autenticar e acessar o app

  Cenário: Criar cadastro de usuário
    Dado que estou na tela de login
     E clico no link "New User? Register"
     Quando preencho todos os campos em branco
     E clico no botão "Register"
     Então o usuário é criado e permanecemos na tela de cadastro

  Cenário: Login válido
    Dado que estou na tela de login
     E preencho os campos com dados já cadastrados
     Quando clico no botão "Login"
     Então a mensagem "You are now logged in" é exibida na tela

  Cenário: Login inválido
    Dado que estou na tela de login
     E preencho os campos com dados não cadastrados
     Quando clico no botão "Login"
     Então o login não é realizado e permanecemos na tela de login

