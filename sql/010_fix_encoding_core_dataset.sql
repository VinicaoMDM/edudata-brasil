-- EduData Brasil
-- Correção de dados inseridos com encoding incorreto

UPDATE core.fonte
SET
    nome = 'Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira',
    descricao = 'Autarquia federal responsável por avaliações, exames, pesquisas estatísticas e indicadores educacionais no Brasil.',
    orgao_responsavel = 'Ministério da Educação'
WHERE sigla = 'INEP';

UPDATE core.dataset
SET
    nome = 'Censo Escolar da Educação Básica',
    descricao = 'Principal pesquisa estatística da educação básica brasileira, realizada anualmente pelo INEP, reunindo informações sobre escolas, gestores, turmas, alunos, profissionais da educação, matrículas e infraestrutura escolar.'
WHERE id = 1;
