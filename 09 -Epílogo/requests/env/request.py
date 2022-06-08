import requests

teste = '04101300'
url = f'https://apigateway.conectagov.estaleiro.serpro.gov.br/api-cpf-light/v2/consulta/cpf'


resposta = requests.get(url)

print(resposta.json())