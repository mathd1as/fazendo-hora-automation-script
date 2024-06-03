# fazendo-hora-automation-script
Script desenvolvido em python que automatiza o registro de pontos no site Fazendo Hora (utilizado em várias empresas). 

## Informações e motivação do desenvolvimento do script
Este script foi desenvolvido com o intuito de estudar segurança da informação em aplicações web. A vulnerabilidade explorada é considerada grave e existem diversas tratativas para a mesma. A vulnerabilidade em questão já foi reportada e está sendo corrigida pela empresa.


### Como rodar

Adicionar os headers 'cookie' e 'x-csrf-token' na request realizada no script. Verificar a request create_ponto do sistema.

executar o script `python3 schedule.py`
