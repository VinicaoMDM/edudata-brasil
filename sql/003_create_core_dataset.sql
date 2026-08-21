-- EduData Brasil
-- Catálogo de datasets

CREATE TABLE IF NOT EXISTS core.dataset (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    fonte_id BIGINT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    url TEXT,
    periodicidade VARCHAR(100),
    formato VARCHAR(50),
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_dataset_fonte
        FOREIGN KEY (fonte_id)
        REFERENCES core.fonte(id)
);
