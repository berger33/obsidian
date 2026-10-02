# Inventário legado de 1 milhão — registro histórico

Este documento descreve somente o antigo checkpoint/catalogue de 1.000.000 de registros virtuais e os arquivos materializados associados. **Não é a meta editorial ativa.** A meta atual é 1.000 lotes × 2.000 notas substantivas = 2.000.000; acompanhe o [plano contínuo](PLANO-CONTINUO-1M.md) e o [status atual](STATUS-CONSOLIDACAO-1M.md).

## Estado do checkpoint histórico

- Registros virtuais no SQLite: **1.000.000**.
- Registros com marcadores de conteúdo-template: **1.000.000**.
- Caminhos virtuais marcados como materializados: **8.000**.
- Notas físicas do lote inicial: **100**, sem status profundo/revisado no schema legado.
- TAR reconstruído/testado: **1.021.139 entradas**, incluindo arquivos derivados e candidatas históricas. Contagens de entradas/arquivos não são contagens de conhecimento válido.

O TAR reconstruído em 2026-10-01 contém **1.015.608 arquivos de nota representados** (1.000.000 placeholders + 15.600 arquivos dos Study Packs + 8 candidatas presentes na data do empacotamento) e 1.021.139 entradas. Ele antecede as aprovações posteriores e não foi reconstruído. As notas ativas fora do TAR não devem ser atribuídas a esse snapshot.

## Estado editorial atual — fora do snapshot

O cofre contém 79 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 30 revisões factuais por IA registradas separadamente). O lote `software-testes-2000-0001` tem 39/2.000 notas válidas; está em andamento. A auditoria global registra 100 arquivos legados com pendências, ainda excluídos da contagem.

## Artefatos

```text
archives/merge-completo-materializado-1m.tar.xz
archives/study-vault-1m-packs.zip
archives/ledger-v1000000-mat8000.sqlite.xz
```

## Auditoria reproduzível

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

Um passe automatizado não comprova fatos. Para contar uma nota, ela precisa ser substantiva, passar pelo gate e ter revisão factual registrada; revisão humana e revisão por IA ficam separadas nos metadados e relatórios.
