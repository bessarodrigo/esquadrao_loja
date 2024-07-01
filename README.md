# Painel de Métricas para o Esporte Clube Bahia

## Descrição
Este projeto foi desenvolvido para criar um painel de visualização no Power BI, permitindo que os gestores da loja do Esporte Clube Bahia mensurem periodicamente as principais métricas de desempenho, como faturamento, quantidade vendida, ticket médio e desempenho da equipe de operadores de caixa e vendedores. Utilizando a metodologia CRISP-DM, o projeto abrange desde o entendimento do problema até a entrega da solução final, utilizando Python para ETL e PostgreSQL para integração dos dados.

## Estrutura do Projeto
1. **Entendimento do Negócio**
   - Identificação das necessidades dos gestores da loja para monitorar as métricas de desempenho.

2. **Entendimento dos Dados**
   - Extração dos dados de relatórios de vendas exportados em Excel.
   - Principais colunas: Data, Valor, Status, Informações Complementares, Operador de Caixa, Vendedor.
   - Outras colunas foram excluídas da análise para manter o foco nas métricas principais.

3. **Preparação dos Dados**
   - Leitura inicial dos dados usando pandas para ler o arquivo Excel.
   - Renomeação das colunas para padronização.
   - Conversão de valores financeiros, adaptando o formato brasileiro (R$).
   - Conversão de datas para o formato adequado.

4. **Modelagem**
   - Criação de um banco de dados PostgreSQL para armazenar os dados transformados.
   - Definição do esquema e das tabelas necessárias.
   - Inserção dos dados no banco de dados utilizando SQLAlchemy.

5. **Avaliação**
   - Validação da integridade e consistência dos dados inseridos no banco.
   - Conferência de amostras de dados para garantir que as transformações foram aplicadas corretamente.

6. **Deploy**
   - Configuração da conexão entre Power BI e o banco de dados PostgreSQL para a criação do painel de visualização.

## Instalação
Instruções para configurar e executar o projeto:

### Pré-requisitos
- Python 3.x
- PostgreSQL
- Power BI

### Configuração
1. Clone o repositório:
    ```bash
    git clone https://github.com/bessarodrigo/esquadrao_loja.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd esquadrao_loja
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados PostgreSQL conforme definido no script `database_setup.sql`.
    ```

    Após isso, faça o push do arquivo `database_setup.sql` para o repositório e adicione instruções para importá-lo:
    ```bash
    psql -U seu_usuario -d seu_banco_de_dados -f database_setup.sql
    ```

5. Execute o script Python para ETL e inserção dos dados:
    ```bash
    python loja_esquadrao.py
    ```

6. Configure a conexão do Power BI com o banco de dados PostgreSQL para visualizar o painel.

Uso
Execute o script ETL para processar e inserir os dados no banco de dados PostgreSQL:

```bash
python loja_esquadrao.py

## Contribuição
Se desejar contribuir com o projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie um branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas alterações (`git commit -m 'Adicionar feature x'`).
4. Push para o branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a [MIT License](link-para-a-licença).

## Contatos
Para mais informações ou dúvidas, entre em contato:

LinkedIn: [Rodrigo Bessa](https://www.linkedin.com/in/rodrigo-bessa/)
