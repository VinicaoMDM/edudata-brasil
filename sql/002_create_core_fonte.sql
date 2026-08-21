-- EduData Brasil
-- Catálogo de fontes de dados

CREATE TABLE IF NOT EXISTS core.fonte (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sigla VARCHAR(50),
    descricao TEXT,
    url TEXT,
    orgao_responsavel VARCHAR(255),
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
