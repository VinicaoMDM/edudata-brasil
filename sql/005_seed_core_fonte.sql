-- EduData Brasil
-- Cadastro inicial de fontes de dados

INSERT INTO core.fonte (
    nome,
    sigla,
    descricao,
    url,
    orgao_responsavel
)
VALUES (
    'Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira',
    'INEP',
    'Autarquia federal responsável por avaliações, exames, pesquisas estatísticas e indicadores educacionais no Brasil.',
    'https://www.gov.br/inep/',
    'Ministério da Educação'
)
ON CONFLICT DO NOTHING;
