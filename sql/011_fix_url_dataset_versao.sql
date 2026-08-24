-- EduData Brasil
-- Corrige a URL de download dos microdados do Censo Escolar 2023

UPDATE core.dataset_versao
SET url_download = 'https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2023.zip'
WHERE dataset_id = 1
  AND versao = '2023';
