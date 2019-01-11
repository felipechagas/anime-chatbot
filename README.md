#Manual de instalação:
##Instalando o Rasa:
1)Instale o anaconda: https://www.anaconda.com/

2)Crie um ambiente com Python 3.7

3)Abra um terminal dentro deste ambiente

4)Execute pip install -U rasa_core

5)Ao encontrar erros de dependência no final,

pesquise quais são as dependências faltantes e as instale pelo anaconda

6)Repita 4 e 5 até a instalação ser bem sucedida

7)Execute o comando pip install rasa_nlu[tensorflow]

## Fluxo do bot

##Adição de intenções e entidades:
1)https://rasahq.github.io/rasa-nlu-trainer/
2)Fazer upload do arquivo data.json ou data_br.json para adicionar mais coisas
3)Fazer o download do novo arquivo e substitui-lo dentro da pasta data
4) Declarar novos tipos de intenções e entidades dentro do arquivo anime_domain.yml
4)Executar o scrit nlu_model.py para treinar o modelo

##Adição de respostas fixas do bot:
1) Abrir arquivo stories.md dentro da pasta data
2) Adicionar novos stories seguindo o padrão do arquivo
3) A linha que começa com * indica a intenção do usuário
4) A linha que começa com - indica a ação do bot
5) Stories que possuem "Generated Story", são gerados automaticamente durante o treinamento assistido.

##Adição de respostas com chamada de API
1) Abrir arquivo actions.py
2) Criar uma nova classe para a ação
3) Definir os metodos name e run, conforme o padrão
4) O método name define o nome identificador da nossa ação, o run será executado sempre que a ação for utilizado pelo bot.
5) Declarar a nova ação nos arquivos stories.md e anime_domain.yml

##Treinamento das respostas do bot
1) Executar o arquivo train_init.py

##Treinamento assistido com dialogo
1) Em um terminal, executar 'python -m rasa_core_sdk.endpoint --actions actions'
2) Em outro terminal, executar o arquivo train_model.py
3) Iniciar a conversa com o bot e corrigi-lo caso marque uma ação ou entidade errada
4) Ctrl-C para encerrar a conversa e exportar os dados de treino

##Conversação
1)Execute o arquivo dialogue_managemente_model.py

##Criando um bot no Slack
1) Em https://api.slack.com/ crie um novo App
2) Na aba 'Bots' adicione um Bot User
3) Marque a opção para sempre mostrar o Bot Online
4) No canto superior esquero clique em Basic Information
5) Instale o App em seu Workspace
6) Na aba OAuth & Permissions, copie o seu Bot User Auth Token e o insira como parâmetro de SlackInput no arquivo run_slack.py

##Testando no Slack
1) Execute o comando python -m rasa_core_sdk.endpoint --actions actions para rodar as actions do arquivo actions.py em um servidor flask
2) Execute o arquivo run_slack.py para rodar a integração com o slack na porta 5004
3) Instale e execute o ngrok(https://ngrok.com/) para tornar a url localhost pública e visível para a API do Slack
