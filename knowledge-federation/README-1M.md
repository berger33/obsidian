# Inventário legado de 1 milhão — registro histórico

Este documento descreve somente o antigo checkpoint/catalogue de 1.000.000 de registros virtuais e os arquivos materializados associados. **Não é a meta editorial ativa.** A meta ativa é 500 lotes × 2.000 notas substantivas = 1.000.000; acompanhe o [plano contínuo](PLANO-CONTINUO-1M.md) e o [status atual](STATUS-CONSOLIDACAO-1M.md).

## Estado do checkpoint histórico

- Registros virtuais no SQLite: **1.000.000**.
- Registros com marcadores de conteúdo-template: **1.000.000**.
- Caminhos virtuais marcados como materializados: **8.000**.
- Notas físicas do lote inicial: **100**, sem status profundo/revisado no schema legado.
- TAR reconstruído/testado: **1.021.139 entradas**, incluindo arquivos derivados e candidatas históricas. Contagens de entradas/arquivos não são contagens de conhecimento válido.

O TAR reconstruído em 2026-10-01 contém **1.015.608 arquivos de nota representados** (1.000.000 placeholders + 15.600 arquivos dos Study Packs + 8 candidatas presentes na data do empacotamento) e 1.021.139 entradas. Ele antecede as aprovações posteriores e não foi reconstruído. As notas ativas fora do TAR não devem ser atribuídas a esse snapshot.

## Estado editorial atual — fora do snapshot

Na atualização de 2026-10-02, o repositório tem 989 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 940 revisões factuais por IA registradas separadamente). O diretório ativo tem 1089 arquivos Markdown, incluindo 100 notas legadas com pendências, ainda excluídas da contagem. O lote `software-testes-2000-0001` tem 949/2.000 notas válidas e segue em andamento; as notas 850–949 estão no [relatório factual por IA da tranche 15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md) e na [reconciliação da tranche 15](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-15.md); as notas 750–849 ficam no [relatório da tranche 14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md); as notas 550–649 estão no [relatório factual por IA da tranche 12](exports/reports/ai-review-software-testes-2000-0001-tranche-12.md), as notas 450–549 na [tranche 11](exports/reports/ai-review-software-testes-2000-0001-tranche-11.md), e o [manifesto do lote](exports/batches/software-testes-2000-0001.md) mantém a sequência completa.

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
