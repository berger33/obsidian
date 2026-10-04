# Reconciliação do lote `software-testes-2000-0001` — tranche 10

- Data: 2026-10-02
- Escopo: tranche 10 (notas 350–449), manifesto ativo do lote, relatório factual por IA, fila de revisão e MOC.
- Método: reconciliação baseada nos artefatos Markdown e nos frontmatters, além dos relatórios de gate; o resultado não depende de registros virtuais ou IDs sem arquivo.

## Resultado

- Manifesto: **449 entradas numeradas, únicas e contínuas (1–449)**; todas apontam para arquivos Markdown existentes e com ID/frontmatter únicos do lote `software-testes-2000-0001`.
- Tranche 10: **100 notas (350–449)**; cada uma é substantiva, passa no gate, tem ao menos duas fontes específicas, wikilinks resolvidos e revisão factual por IA registrada no relatório correspondente.
- Registro factual: **100/100 linhas** na tranche 10, sem lacunas ou IDs duplicados.
- Fila: **100/100 registros** de IA nas posições 390–489, associados às notas 350–449; nenhuma delas recebeu aprovação humana.
- MOC: as 100 notas da tranche 10 aparecem uma vez cada; o mapa permanece navegação, não validação factual.
- Auditoria de qualidade do lote: **449/449** aprovadas, sendo 9 revisões humanas históricas e 440 revisões por IA; **0** pendências no gate.
- Auditoria global por arquivos: **589** Markdown ativos; **489** válidos (49 humanos + 440 IA) e **100** legados pendentes.
- Lote: permanece `in_progress`, com meta 2.000; **449/2.000** válidas e **1.551** notas substantivas restantes.

## Limite do registro SQLite

O `audit_batch.py` existente lê lotes registrados no SQLite. O lote ativo desta reconciliação é mantido no manifesto Markdown e não possui linha de lote no ledger local; por isso, a auditoria DB-backed não foi apresentada como passe nem foram criadas linhas SQLite para simular sucesso. O gate de arquivos e a reconciliação explícita acima são os registros usados para este escopo.

## Artefatos de suporte

- [Manifesto ativo](../batches/software-testes-2000-0001.md)
- [Gate do lote e resolução de wikilinks](note-quality-software-testes-2000-0001.md)
- [Auditoria global por arquivos](note-quality-audit.md)
- [Revisão factual por IA da tranche 10](ai-review-software-testes-2000-0001-tranche-10.md)
- [Fila de revisão humana e por IA](human-review-queue.md)
- [MOC de navegação](../../00-home-vault/MOCs/MOC-Testes-Software-0007.md)
