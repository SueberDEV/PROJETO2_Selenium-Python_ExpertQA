# Bem vindo ao Projeto E-Comerce LambdaTest QA!

<p align="center">
  <img src='https://github.com/SueberDEV/PROJETO2_Selenium-Python_ExpertQA/blob/main/IMG/Your%20Store%20-%20Google%20Chrome.jpg?raw=true' width='350'>
  </p>

Este repositório contém casos de teste automatizados para a aplicação [ecommerce-playground.lambdatest](https://ecommerce-playground.lambdatest.io/) utilizando Selenium e PyTest. Este projeto foi desenvolvido como parte do segundo projeto de conclusão do curso de automação de testes com Python e Selenium, da Academia QA Expert, ministrado pelo Paulo Oliveira.


# Sobre o LambdaTest >>

[LambdaTest](https://https://www.lambdatest.com//) LambdaTest é uma plataforma de teste baseada em nuvem que oferece uma gama completa de serviços de teste de aplicativos web e móveis. A plataforma é amplamente utilizada por desenvolvedores e testadores para garantir a compatibilidade cross-browser, o desempenho e a funcionalidade dos aplicativos em diferentes ambientes e dispositivos. Aqui estão alguns aspectos-chave do LambdaTest:


##  Estrutura do Repositório

**tests/**: Contém todos os arquivos de teste.

-    **test_exceeded_allowed_logins.py**: Teste de Login com Tentativas Excedidas.
-   **test_forgotten_pass.py**: Teste de Recuperação de Senha.
-   **test_register_account.py**: Teste de Registro de Conta.



## Configuração

1 - Crie um ambiente virtual e instale as dependências: 

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

2 - Execute os testes:

    pytest



# Casos de Teste



### Teste de Login com Tentativas Excedidas

Arquivo: `test_exceeded_allowed_logins.py`

Este teste verifica a mensagem de erro exibida quando um usuário excede o número permitido de tentativas de login.


### Teste de Recuperação de Senha

Arquivo: `test_forgotten_pass.py`

Este teste verifica a funcionalidade de recuperação de senha, garantindo que a mensagem de sucesso é exibida após solicitar a recuperação.

### Teste de Registro de Conta

Arquivo: `test_register_account.py`

Este teste verifica a criação de uma nova conta no site, preenchendo todos os campos obrigatórios e aceitando os termos e condições.

## Sobre o Projeto

Este projeto foi desenvolvido como parte do curso de automação de testes com Python e Selenium da Academia QA Expert, ministrado por Paulo Oliveira. Utilizando o site de e-commerce de testes da LambdaTest, o projeto tem como objetivo demonstrar a aplicação de técnicas de automação de testes em um ambiente realista.

O foco principal foi criar e executar casos de teste automatizados para diversas funcionalidades essenciais do site, incluindo:

-   **Verificação de Limite de Tentativas de Login**: Testa a mensagem de erro ao exceder o número permitido de tentativas de login.
-   **Recuperação de Senha**: Testa a funcionalidade de recuperação de senha, garantindo que o usuário receba uma confirmação por e-mail.
-   **Registro de Conta**: Testa a criação de uma nova conta de usuário, preenchendo todos os campos obrigatórios e aceitando os termos e condições.

Este projeto não só reforça a importância dos testes automatizados na garantia de qualidade de software, mas também demonstra habilidades práticas na utilização do Selenium e PyTest para a automação de testes.

## Autor

-   **Suéber F. Passos** - [LinkedIn](https://www.linkedin.com/in/sueberfp) - [GitHub](https://github.com/SueberDEV)
<br>
<br>


<p align="center">
   < Thanks! > <br>
  <img src='https://i.gifer.com/Za3R.gif' width='350'>
  </p>

