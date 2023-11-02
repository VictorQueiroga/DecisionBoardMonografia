# DecisionBoard

Uma ferramenta para auxiliar os gestores das empresas públicas do estado de Pernambuco a tomar melhores decisões com base nos dados de reclamações coletados da plataforma Reclame AQUI

## Requisitos para execução

Para executar a aplicação é necessário: 
  1. Ter instalado o Python na versão 3.9.12
  2. Usar no terminal o comando "pip install -r requirements.txt" para instalar as depedências
  3. Ir na pasta do projeto pelo terminal e digitar o comando "streamlit run main.py"

## Como utilizar

No menu a esquerda da aplicação será possivel escolher por exemplo a página "board" onde o usuário poderá selecionar a empresa, o local e palavras chave para pesquisar nas reclamações, exibindo as seguintes informações:
  1. Quantidade de reclamações por ano
     ![QtdAno](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/qtd-ano.png)
  2. Quantidade de reclamações por mês
     ![QtdMes](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/qtd-mes.png)
  3. Quantidade de reclamações por status
     ![QtdStatus](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/qtd-status.png)
  4. As 5 palavras mais frequentes nas reclamações
     ![Palavras](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/palavras.png)

Na página "historico" é possível consultar o histórico das decisões tomadas:
     ![Historico](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/historico.png).

Na página "registrar" é possível escrever uma nova decisão a ser tomada e ao clicar no botão "Registrar" essa decisão será salva no histórico:
     ![Registrar](https://github.com/VictorQueiroga/DecisionBoard/blob/main/assets/registrar.png).
     
## Autor

Victor Queiroga

