## 1. Objetivo do EduData Brasil

Definir o propósito do projeto: integrar e analisar dados públicos da educação brasileira, relacionando indicadores educacionais, investimentos públicos e outros fatores relevantes para identificar padrões, desigualdades e possíveis relações entre recursos aplicados e resultados educacionais.

## 2. Princípios do projeto

Estabelecer as premissas que orientam o desenvolvimento: dados abertos, transparência, rastreabilidade, reprodutibilidade, qualidade dos dados, separação entre ingestão e análise e preferência por evidências em vez de conclusões pré-estabelecidas.

## 3. Arquitetura

Definir o fluxo dos dados dentro do projeto, desde a coleta nas fontes originais até sua transformação em informações prontas para análise, utilizando camadas independentes para preservar os dados originais e permitir novas análises no futuro. A arquitetura deve permitir que novas fontes e novas análises sejam incorporadas sem reconstruir as etapas já consolidadas.

## 4. Raw

Armazenar os dados exatamente como foram obtidos das fontes, preservando arquivos, formatos, estruturas e informações originais. Essa camada funciona como a fonte histórica do projeto e permite reproduzir o processo de tratamento posteriormente.
    
## 5. Staging

Preparar e padronizar os dados brutos para utilização nas etapas seguintes, realizando tarefas como limpeza, conversão de tipos, padronização de nomes, tratamento de valores ausentes e identificação de inconsistências, sem ainda construir os indicadores finais.

## 6. Core

Construir uma camada de dados confiável e integrada, consolidando informações provenientes de diferentes fontes em estruturas padronizadas e relacionadas. É aqui que os dados passam a representar entidades e conceitos comuns ao projeto, como municípios, escolas, redes de ensino, investimentos e indicadores educacionais.

## 7. Analytics

Transformar os dados consolidados em informações analíticas, criando indicadores, agregações, métricas e conjuntos de dados específicos para responder às perguntas de negócio e investigação do projeto. É a camada utilizada para gerar análises, gráficos e estudos.

## 8. Fontes

Documentar a origem de cada informação utilizada, registrando órgão responsável, dataset, endereço da fonte, período de referência, frequência de atualização e outras características relevantes para compreender a procedência dos dados.

## 9. Rastreabilidade

Garantir que cada informação analisada possa ser rastreada até sua origem, permitindo identificar de qual fonte, arquivo, período e transformação um determinado dado ou indicador foi derivado.

## 10. Reprodutibilidade

Permitir que o processo de coleta, transformação e análise seja executado novamente, utilizando código, configurações e documentação versionados para que os resultados possam ser reproduzidos e auditados.

## 11. Estratégia de novas fontes

Estabelecer critérios para incorporar novas bases de dados ao projeto, avaliando relevância, qualidade, periodicidade, cobertura, disponibilidade, compatibilidade e possibilidade de integração com o modelo existente.

## 12. Estratégia de novas análises

Criar uma estrutura que permita desenvolver novas perguntas e análises sem reconstruir todo o pipeline, utilizando os dados consolidados do Core para gerar novos indicadores, cruzamentos e perspectivas analíticas.

## 13. Fluxo de dados

O fluxo do EduData Brasil foi projetado para separar a obtenção,
o tratamento, a integração e a análise dos dados.

```mermaid
flowchart LR
    A[Fontes públicas] --> B[Raw]
    B --> C[Staging]
    C --> D[Core]
    D --> E[Analytics]
    E --> F[Análises e estudos]