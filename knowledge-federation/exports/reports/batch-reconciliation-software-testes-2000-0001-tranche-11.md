# Reconciliação do lote `software-testes-2000-0001` — tranche 11

- Data: 2026-10-02
- Escopo: notas 450–549; manifesto, relatório factual por IA, fila de revisão, MOC e auditorias.
- Método: inspeção dos 100 arquivos e frontmatters; comparação de cada nota revisada com a versão anterior e com a linha de dados correspondente; conferência das fontes e do registro factual por IA; gate determinístico e verificação de links. A revisão factual por IA não é aprovação humana.

## Resultado

- **Correção editorial concluída:** a versão anterior repetia três parágrafos genéricos por grupo (`why`, `method`, `limits`) em cada uma das dez notas do grupo. Esses prefixos foram removidos das 100 notas e dos dez arquivos de dados; os motivos, procedimentos, exemplos, ressalvas e verificações específicos por nota foram mantidos. O builder agora não injeta contexto de prosa compartilhado e bloqueia frases substantivas idênticas entre notas.
- **Auditoria comparativa: 100/100 notas.** Frontmatter, IDs, títulos, resumo, texto específico, exemplos, verificações, fontes e conexões foram comparados com a versão anterior e com os dados de cada nota. A única diferença no corpo foi a retirada dos três prefixos de grupo; nenhuma afirmação específica nova foi inserida.
- **Substância e gate:** cada uma das 100 notas contém de **171 a 234 palavras**, duas fontes HTTPS específicas, as seções requeridas e wikilinks resolvidos. O relatório de qualidade do subdomínio registra **549/549** candidatas aprovadas, incluindo a tranche 11, sem pendências. Uma varredura do corpo das 100 notas não encontrou sentença substantiva exata repetida entre notas; o builder mantém essa verificação para evitar regressão.
- **Revisão factual:** **100 registros** (IDs 450–549) no [relatório da tranche 11](ai-review-software-testes-2000-0001-tranche-11.md), cada um ligado à fonte principal e a uma decisão factual específica. O texto factual por nota foi preservado e reconferido contra a fonte indicada. São revisões por IA; nenhuma das 100 notas recebeu aprovação humana.
- **Manifesto:** **549 entradas numeradas, únicas e contínuas (1–549)**; todos os destinos existem e pertencem ao lote.
- **Fontes por grupo:** REST Assured (Usage Wiki e Javadocs); WireMock (stubbing, request matching, cenários, verifying, faults, extensão JUnit e response templating); Robot Framework 7.5 (User Guide, BuiltIn e Collections); Cucumber (Gherkin, Step Definitions, Expressions e API); NUnit (atributos, fontes de casos, execução paralela e TestContext); xUnit.net (Getting Started v3, fixtures, paralelismo, captura de output, assertions e runner config); Locust (locustfile, TaskSet, LoadTestShape, request rate e execução distribuída); Apache JMeter (Test Plan, Component Reference, CLI, Best Practices e Hints and Tips); Gatling (Scenario, Session, Feeders, Checks, Assertions, Injection e Timings); Appium (capabilities, drivers, contextos, quickstart, migrações e requisitos dos drivers Android/Apple).
- **Fila de revisão:** 100 registros novos de revisão por IA nas posições 490–589, associados um a um às notas 450–549. As **49 aprovações humanas históricas** foram preservadas sem alteração e não foram estendidas à tranche.
- **MOC:** as 100 notas aparecem uma vez no MOC; o índice é navegação, não validação factual.
- **Auditoria de qualidade do subdomínio:** 549 arquivos; 549 aprovados no gate; 9 com revisão factual humana histórica e 540 com revisão factual por IA identificada; 0 pendências.
- **Auditoria global:** 689 arquivos Markdown ativos; 589 válidos (49 humanos + 540 IA); 100 legados permanecem pendentes fora da contagem. A correção da tranche 11 não alterou as 49 aprovações humanas nem a contagem global válida.
- **Testes:** **12 passaram** em `python3 -m unittest discover -s knowledge-federation/tests -v`.
- **Lote ainda em andamento:** **549/2.000** notas válidas; faltam **1.451** notas materiais. Esta tranche não conclui o lote.

## Escopo e ressalvas

O `audit_batch.py` existente lê lotes registrados no SQLite. O lote ativo desta reconciliação é mantido no manifesto Markdown e não possui linha de lote no ledger local; por isso, a auditoria DB-backed não foi apresentada como passe nem foram criadas linhas SQLite para simular sucesso. A contagem usa somente arquivos materiais, frontmatters e relatórios registrados.

O gate automatizado verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e wikilinks; ele não comprova sozinho a veracidade nem a qualidade editorial. A detecção de repetição do builder cobre sentenças substantivas exatamente iguais, não toda semelhança semântica. A revisão factual por IA permanece separada da revisão humana e não garante ausência absoluta de erros.

## Artefatos de suporte

- [Manifesto ativo](../batches/software-testes-2000-0001.md)
- [Gate do lote e resolução de wikilinks](note-quality-software-testes-2000-0001.md)
- [Auditoria global por arquivos](note-quality-audit.md)
- [Relatório factual por IA da tranche 11](ai-review-software-testes-2000-0001-tranche-11.md)
- [Fila de revisão humana e por IA](human-review-queue.md)
- [MOC de navegação](../../00-home-vault/MOCs/MOC-Testes-Software-0007.md)
