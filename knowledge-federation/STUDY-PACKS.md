# Study packs materializados do ledger de 1M

Data: 2026-10-01

Este diretório contém recortes materializados do checkpoint de 1 milhão de notas lógicas. Cada study pack é pequeno o suficiente para abrir/copiar no Obsidian sem precisar restaurar ou abrir o ledger completo.

## Checkpoint-fonte

```text
knowledge-federation/archives/ledger-v1000000-mat8000.zip
```

## Study packs criados

| Tema | Notas | Zip |
|---|---:|---|
| IA — agentes | 100 | `archives/study-pack-ia-agentes-from-1m.zip` |
| IA — RAG | 200 | `archives/study-pack-ia-rag.zip` |
| Software — backend | 200 | `archives/study-pack-software-backend.zip` |
| Vibe coding — orquestração | 200 | `archives/study-pack-vibe-coding-orquestracao.zip` |
| Jogos — MMO | 200 | `archives/study-pack-jogos-mmo.zip` |
| Cannabis medicinal — documentação do paciente | 200 | `archives/study-pack-cannabis-documentacao-paciente.zip` |
| Micologia — riscos e redução de danos | 200 | `archives/study-pack-micologia-riscos-reducao-danos.zip` |

Total materializado em pastas ativas nesta rodada: 1.300 notas.

## Pastas materializadas ativas

As pastas intermediárias em `knowledge-federation/checkpoint-materialized/` foram removidas após a geração do vault consolidado para manter o workspace abaixo do limite de arquivos ativos. Os recortes continuam preservados em:

```text
knowledge-federation/archives/study-pack-*.zip
knowledge-federation/study-vault-1m-packs/
knowledge-federation/archives/study-vault-1m-packs.zip
```

## Como criar outro pack

Exemplo:

```bash
python knowledge-federation/scripts/materialize_from_checkpoint.py \
  --domain software \
  --subdomain arquitetura \
  --limit 500 \
  --out checkpoint-materialized/software-arquitetura \
  --zip archives/study-pack-software-arquitetura.zip \
  --clean
```

Consulta antes de materializar:

```bash
python knowledge-federation/scripts/query_checkpoint.py "arquitetura" --domain software --limit 20
```

## Segurança

Os packs de `cannabis-medicinal` e `micologia` são educacionais e não operacionais. Eles foram gerados com `conteudo_operacional: false` e devem ser usados para estudo, documentação, rastreabilidade, leitura crítica e perguntas a profissionais habilitados.
