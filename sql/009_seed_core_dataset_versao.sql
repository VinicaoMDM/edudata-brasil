-- EduData Brasil
-- Cadastro da versão 2023 do Censo Escolar da Educação Básica

INSERT INTO core.dataset_versao (
    dataset_id,
    versao,
    periodo_referencia,
    url_download,
    formato,
    data_extracao
)
SELECT
    d.id,
    '2023',
    '2023',
    'https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar',
    'ZIP',
    NULL
FROM core.dataset d
WHERE d.nome = 'Censo Escolar da Educação Básica'
  AND NOT EXISTS (
      SELECT 1
      FROM core.dataset_versao dv
      WHERE dv.dataset_id = d.id
        AND dv.versao = '2023'
  );
