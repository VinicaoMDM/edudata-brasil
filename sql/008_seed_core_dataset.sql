-- EduData Brasil
-- Cadastro do dataset Censo Escolar da Educação Básica

INSERT INTO core.dataset (
    fonte_id,
    nome,
    descricao,
    url,
    periodicidade,
    formato
)
SELECT
    f.id,
    'Censo Escolar da Educação Básica',
    'Principal pesquisa estatística da educação básica brasileira, realizada anualmente pelo INEP, reunindo informações sobre escolas, gestores, turmas, alunos, profissionais da educação, matrículas e infraestrutura escolar.',
    'https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar',
    'Anual',
    'CSV/XLSX/ZIP'
FROM core.fonte f
WHERE f.sigla = 'INEP'
  AND NOT EXISTS (
      SELECT 1
      FROM core.dataset d
      WHERE d.fonte_id = f.id
        AND d.nome = 'Censo Escolar da Educação Básica'
  );
