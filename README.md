# Painel de Métricas para o Esporte Clube Bahia

## Descrição
Este projeto foi desenvolvido para criar um painel no Power BI, permitindo que os gestores da loja do Esporte Clube Bahia mensurem periodicamente as principais métricas de desempenho, como faturamento, quantidade vendida, ticket médio e desempenho da equipe de operadores de caixa e vendedores. 

Utilizando a metodologia CRISP-DM, o projeto abrange desde o entendimento do problema até a entrega da solução final, utilizando Python para ETL e PostgreSQL para integração dos dados.

## Artigo no Medium

[Painel de Análise para Gestão de Vendas no Esporte Clube Bahia](https://medium.com/@reisrodri/painel-de-an%C3%A1lise-para-gest%C3%A3o-de-vendas-no-esporte-clube-bahia-d666aa05f2a1)

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
  
4. **Análise Exploratória**

   - Estatísticas Descritivas: Cálculo de métricas como média, mediana e desvio padrão para as colunas principais.
   - Visualizações: Criação de histogramas e boxplots para explorar a distribuição dos valores e identificar anomalias.
   - Desempenho: Gráficos de barras mostraram o desempenho por operador e vendedor, enquanto gráficos de linha analisaram o desempenho mensal.
   - Limpeza dos Dados: Remoção de registros com status 'Cancelada' e 'Inutilizada'.
   - Essas análises ajudaram a obter uma visão clara das vendas e do desempenho da equipe.

4. **Modelagem**
   - Criação de um banco de dados PostgreSQL para armazenar os dados transformados.
   - Definição do esquema e das tabelas necessárias.
   - Inserção dos dados no banco de dados utilizando SQLAlchemy.

5. **Avaliação**
   - Validação da integridade e consistência dos dados inseridos no banco.
   - Conferência de amostras de dados para garantir que as transformações foram aplicadas corretamente.

6. **Deploy**
   - Configuração da conexão entre Power BI e o banco de dados PostgreSQL para a criação do painel de visualização.

### Pré-requisitos
- Python 3.x
- PostgreSQL
- Power BI

## Contatos
Para mais informações ou dúvidas, entre em contato:

LinkedIn: https://www.linkedin.com/in/rodrigo-bessa/
