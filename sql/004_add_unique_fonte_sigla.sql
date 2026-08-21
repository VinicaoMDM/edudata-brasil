-- EduData Brasil
-- Garante unicidade da sigla das fontes

ALTER TABLE core.fonte
ADD CONSTRAINT uq_fonte_sigla UNIQUE (sigla);
