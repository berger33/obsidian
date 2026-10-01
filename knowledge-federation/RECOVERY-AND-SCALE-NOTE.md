# Nota de recuperação e escala

Data: 2026-10-01

## O que aconteceu

Durante a tentativa de continuar a geração para centenas de milhares de notas, ficou claro que o workspace atual não preservou os artefatos massivos das rodadas anteriores. A política prática do ambiente limita snapshots grandes e árvores com muitos arquivos. Como consequência, a continuação real deve abandonar a estratégia de manter centenas de milhares de arquivos Markdown ativos no repositório.

Estado observado no workspace após a última retomada:

- `knowledge-federation/` ativo: aproximadamente 1.2 MB.
- Registry atual: contém apenas o lote inicial de teste, com 100 notas.
- Scripts avançados criados nas rodadas anteriores não estavam mais presentes.
- Archives grandes anteriores também não estavam presentes no workspace ativo.

## Decisão técnica

A partir daqui, o caminho correto para atingir 1 milhão de notas é usar arquitetura **ledger-first**:

1. Registrar milhões de notas no SQLite/Parquet/JSONL compactado, não como milhões de arquivos soltos.
2. Materializar para Markdown apenas subconjuntos estudáveis, por exemplo:
   - 500 notas por lote;
   - 5.000 notas por sub-vault;
   - MOCs e trilhas prioritárias;
   - resultados de busca ou estudo.
3. Manter `domains/` como cache descartável, não como fonte de verdade.
4. Manter archives compactados fora da árvore ativa sempre que possível.
5. Nunca ultrapassar milhares de arquivos ativos se o objetivo é persistência confiável neste ambiente.

## Nova estratégia

```text
knowledge-federation/
  registry/
    knowledge.sqlite          # fonte de verdade
    virtual_notes.jsonl.xz    # opcional: export de notas virtuais
  materialized/
    software-0001/            # apenas recortes materializados
    ia-0001/
  exports/
    reports/
  scripts/
    generate_virtual_notes.py
    materialize_batch.py
    global_audit_fast.py
```

## Regras novas

- Gerar volume como registros virtuais.
- Materializar somente o que for usado no Obsidian agora.
- Criar checkpoints compactados antes de qualquer limpeza.
- Evitar gerar dezenas de milhares de `.md` ativos no workspace.

## Próximo passo recomendado

Implementar a versão `virtual-note` do pipeline:

```bash
python knowledge-federation/scripts/generate_virtual_notes.py --count 100000 --prefix vscale1
python knowledge-federation/scripts/materialize_batch.py --domain software --limit 1000
python knowledge-federation/scripts/global_audit_fast.py
```

Isso permite crescer rumo a 1 milhão sem depender de 1 milhão de arquivos no repositório.
