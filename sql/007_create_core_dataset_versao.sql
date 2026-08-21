-- EduData Brasil
-- Controle de versões dos datasets

CREATE TABLE IF NOT EXISTS core.dataset_versao (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    dataset_id BIGINT NOT NULL,

    versao VARCHAR(100) NOT NULL,

    periodo_referencia VARCHAR(50),

    url_download TEXT,

    formato VARCHAR(50),

    data_extracao TIMESTAMPTZ,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_dataset_versao_dataset
        FOREIGN KEY (dataset_id)
        REFERENCES core.dataset(id),

    CONSTRAINT uq_dataset_versao
        UNIQUE (dataset_id, versao)
);
