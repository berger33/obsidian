# Reconciliação do lote `software-testes-2000-0001` — tranche 11

- Data: 2026-10-02
- Escopo: notas 450–549; manifesto, relatório factual por IA, fila de revisão, MOC e auditorias.
- Método: conferência dos 100 arquivos e frontmatters, dos registros de revisão e das afirmações centrais por nota contra documentação oficial dos projetos. A auditoria automatizada comprova estrutura, fontes e links; não substitui a verificação factual descrita no relatório da tranche.

## Resultado

- Manifesto: **549 entradas numeradas, únicas e contínuas (1–549)**; todos os destinos existem e pertencem ao lote.
- Tranche 11: **100 notas (450–549)**; cada nota passa pelo gate, tem ao menos duas fontes específicas e revisão factual por IA registrada. Os IDs, slugs, títulos e relatórios foram conferidos sem lacunas ou duplicatas.
- Revisão factual: **100/100 registros** no [relatório da tranche 11](ai-review-software-testes-2000-0001-tranche-11.md). As afirmações centrais foram comparadas às fontes oficiais por tópico, incluindo limites e diferenças de versão pertinentes. Esta revisão é por IA; nenhuma dessas notas recebeu aprovação humana.
- Fontes consultadas por grupo: REST Assured (Usage Wiki e Javadocs); WireMock (stubbing, request matching, cenários, verifying, faults, extensão JUnit e response templating); Robot Framework 7.5 (User Guide, BuiltIn e Collections); Cucumber (Gherkin, Step Definitions, Expressions e API); NUnit (atributos, fontes de casos, execução paralela e TestContext); xUnit.net (Getting Started v3, fixtures, paralelismo, captura de output, assertions e runner config); Locust (locustfile, TaskSet, LoadTestShape, request rate e execução distribuída); Apache JMeter (Test Plan, Component Reference, CLI, Best Practices e Hints and Tips); Gatling (Scenario, Session, Feeders, Checks, Assertions, Injection e Timings); Appium (capabilities, drivers, contextos, quickstart, migrações e requisitos dos drivers Android/Apple).
- Fila: **100 registros novos de IA** nas posições 490–589, ligados um a um às notas 450–549. As **49 aprovações humanas históricas** foram preservadas sem alteração e não foram estendidas à tranche.
- MOC: cada uma das 100 notas novas aparece uma vez; índice de navegação, não validação factual.
- Auditoria de qualidade do lote: **549/549** aprovadas, sendo 9 revisões humanas históricas e 540 revisões por IA; **0** pendências de gate.
- Auditoria global: **689** arquivos Markdown ativos; **589** válidos (49 humanos + 540 IA) e **100** legados pendentes fora da contagem.
- Testes: **11 passaram** em `python3 -m unittest discover -s knowledge-federation/tests -v`.
- O lote continua `in_progress`: **549/2.000** notas válidas; faltam **1.451** notas materiais. Esta tranche não conclui o lote.

## Escopo e ressalvas

O `audit_batch.py` existente lê lotes registrados no SQLite. O lote ativo desta reconciliação é mantido no manifesto Markdown e não possui linha de lote no ledger local; por isso, a auditoria DB-backed não foi apresentada como passe nem foram criadas linhas SQLite para simular sucesso. A contagem usa apenas os arquivos materiais, seus frontmatters e os relatórios registrados.

A revisão por IA não é aprovação humana nem garantia absoluta de ausência de erro. O gate automatizado verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e wikilinks; ele, isoladamente, não certifica a veracidade das afirmações.

## Artefatos de suporte

- [Manifesto ativo](../batches/software-testes-2000-0001.md)
- [Gate do lote e resolução de wikilinks](note-quality-software-testes-2000-0001.md)
- [Auditoria global por arquivos](note-quality-audit.md)
- [Relatório factual por IA da tranche 11](ai-review-software-testes-2000-0001-tranche-11.md)
- [Fila de revisão humana e por IA](human-review-queue.md)
- [MOC de navegação](../../00-home-vault/MOCs/MOC-Testes-Software-0007.md)
