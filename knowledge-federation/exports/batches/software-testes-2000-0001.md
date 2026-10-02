# Lote de escala software-testes-2000-0001

- Data de início: 2026-10-01
- Escopo: engenharia de software — testes e qualidade
- Tamanho-alvo solicitado: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **99 / 2.000 (4,95%)**
- Gate automatizado: **99/99 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks)
- Revisão factual humana: **9/99**
- Revisão factual por IA: **90/99**
- Contabilizadas como válidas: **99/99**
- Revisor das nove notas aprovadas humanamente: `usuario-da-sessao` (confirmação explícita; nome nominal não informado)
- Revisor das 90 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranche 1 (9 notas) preserva aprovação humana; tranches 2–6 (90 notas) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado
- Auditoria reproduzível da tranche: [`note-quality-software-testes-2000-0001.md`](../reports/note-quality-software-testes-2000-0001.md)
- Relatórios factuais por IA: [`tranches 2–3`](../reports/ai-review-software-testes-2000-0001.md), [`tranche 4`](../reports/ai-review-software-testes-2000-0001-tranche-04.md), [`tranche 5`](../reports/ai-review-software-testes-2000-0001-tranche-05.md) e [`tranche 6`](../reports/ai-review-software-testes-2000-0001-tranche-06.md)
- Navegação: [`MOC-Testes-Software-0007.md`](../../00-home-vault/MOCs/MOC-Testes-Software-0007.md)

> **Contagem literal:** 2.000 é a meta deste lote, não a quantidade já criada. Existem 99 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.901 restantes. A contagem válida só avança com conteúdo substantivo, fontes específicas, gate aprovado e revisão factual humana ou por IA registrada separadamente.

## Tranche 1 — fundamentos e técnicas (9 notas; aprovada pelo usuário)

1. [Test doubles: dummies, fakes, stubs, spies e mocks](../../domains/software-0007/software/testes/test-doubles-fakes-stubs-spies-mocks.md)
2. [Testes herméticos e dependências declaradas](../../domains/software-0007/software/testes/testes-hermeticos-dependencias.md)
3. [Testes flaky e determinismo](../../domains/software-0007/software/testes/testes-flaky-determinismo.md)
4. [Fixtures do pytest: ciclo de vida e escopos](../../domains/software-0007/software/testes/fixtures-pytest-ciclo-vida-escopos.md)
5. [Testes baseados em propriedades com Hypothesis](../../domains/software-0007/software/testes/property-based-testing-hypothesis.md)
6. [Shrinking de contraexemplos em testes gerativos](../../domains/software-0007/software/testes/shrinking-contraexemplos-hypothesis.md)
7. [Testes stateful com modelos e Hypothesis](../../domains/software-0007/software/testes/testes-stateful-model-based-hypothesis.md)
8. [Fuzzing guiado por cobertura com libFuzzer](../../domains/software-0007/software/testes/fuzzing-coverage-guided-libfuzzer.md)
9. [Mutation testing para avaliar a eficácia dos testes](../../domains/software-0007/software/testes/mutation-testing-eficacia-testes.md)

## Tranche 2 — seleção de casos, cobertura e estratégia (10 notas; revisão factual por IA registrada)

10. [Particionamento de equivalência e valores de fronteira](../../domains/software-0007/software/testes/particionamento-equivalencia-valores-fronteira.md)
11. [Decision table testing para regras condicionais](../../domains/software-0007/software/testes/decision-table-testing-regras-condicionais.md)
12. [Teste de transição de estados e critérios de cobertura](../../domains/software-0007/software/testes/state-transition-testing-coverage.md)
13. [Combinatorial testing: pairwise e cobertura t-way](../../domains/software-0007/software/testes/combinatorial-testing-pairwise-t-way.md)
14. [Metamorphic testing e relações entre execuções](../../domains/software-0007/software/testes/metamorphic-testing-oracle-relations.md)
15. [Differential testing: comparar implementações equivalentes](../../domains/software-0007/software/testes/differential-testing-comparacao-implementacoes.md)
16. [Cobertura de statements e branches: o que medem](../../domains/software-0007/software/testes/cobertura-branches-statement-interpretacao.md)
17. [MC/DC: efeito independente de cada condição](../../domains/software-0007/software/testes/mcdc-coverage-condicoes-independentes.md)
18. [Pirâmide de testes como estratégia contextual](../../domains/software-0007/software/testes/piramide-testes-estrategia-contexto.md)
19. [Snapshot testing com Jest e revisão dos resultados](../../domains/software-0007/software/testes/snapshot-testing-jest-revisao.md)

## Tranche 3 — risco, exploração, confiabilidade e contratos (10 notas; revisão factual por IA registrada)

20. [Risk-based testing para priorizar o esforço](../../domains/software-0007/software/testes/risk-based-testing-priorizacao-risco.md)
21. [Exploratory testing: aprender enquanto se testa](../../domains/software-0007/software/testes/exploratory-testing-aprendizado-design-execucao.md)
22. [Session-based testing com charters e debriefs](../../domains/software-0007/software/testes/session-based-testing-charters-debriefs.md)
23. [Test oracle e problema do resultado esperado](../../domains/software-0007/software/testes/test-oracles-resultados-esperados.md)
24. [Priorização de testes de regressão por risco e impacto](../../domains/software-0007/software/testes/regression-test-prioritization-risco-impacto.md)
25. [Teste de acessibilidade: automação e avaliação humana](../../domains/software-0007/software/testes/teste-acessibilidade-automatizada-revisao-humana.md)
26. [Performance testing com modelagem de carga](../../domains/software-0007/software/testes/performance-testing-modelagem-carga.md)
27. [Chaos experiments com steady state e blast radius](../../domains/software-0007/software/testes/chaos-experiments-steady-state-blast-radius.md)
28. [Teste de API baseado em schema com OpenAPI](../../domains/software-0007/software/testes/schema-based-api-testing-schemathesis-openapi.md)
29. [Dados de teste sintéticos e proteção de privacidade](../../domains/software-0007/software/testes/test-data-privacidade-sinteticos.md)

## Tranche 4 — gestão, planejamento e feedback (10 notas; revisão factual por IA registrada)

30. [Plano de testes: objetivos, escopo e comunicação](../../domains/software-0007/software/testes/test-planning-objetivos-escopo-comunicacao.md)
31. [Critérios de entrada e saída em atividades de teste](../../domains/software-0007/software/testes/test-entry-exit-criteria.md)
32. [Estimativa de esforço de teste: métodos e incerteza](../../domains/software-0007/software/testes/test-effort-estimation-techniques.md)
33. [Priorização e ordenação de casos de teste](../../domains/software-0007/software/testes/test-case-prioritization-dependencies.md)
34. [Monitoramento de testes e relatórios de progresso/conclusão](../../domains/software-0007/software/testes/test-progress-metrics-relatorios-conclusao.md)
35. [Gerenciamento de configuração para testware e ambientes](../../domains/software-0007/software/testes/test-environment-configuration-management.md)
36. [Rastreabilidade entre requisitos, testes e resultados](../../domains/software-0007/software/testes/requirements-test-traceability.md)
37. [Relatório de defeito: reprodução, evidência e triagem](../../domains/software-0007/software/testes/defect-report-reproducibility-severity-priority.md)
38. [Investimento, manutenção e riscos da automação de testes](../../domains/software-0007/software/testes/test-automation-investment-maintenance-risks.md)
39. [Testes em CI: feedback rápido e regressão selecionada](../../domains/software-0007/software/testes/ci-feedback-testes-regressao.md)


## Tranche 5 — fundamentos, revisões e níveis de teste (20 notas; revisão factual por IA registrada)

40. [Objetivos de teste dependem do contexto](../../domains/software-0007/software/testes/test-objectives-context.md)
41. [Teste e debugging são atividades distintas](../../domains/software-0007/software/testes/testing-vs-debugging.md)
42. [Erro, defeito, falha e causa raiz](../../domains/software-0007/software/testes/error-defect-failure-root-cause.md)
43. [Princípios de teste como orientação, não receita](../../domains/software-0007/software/testes/testing-principles-contextual.md)
44. [Atividades do processo de teste](../../domains/software-0007/software/testes/fundamental-test-activities.md)
45. [Adaptar o processo de teste ao contexto](../../domains/software-0007/software/testes/test-process-context-tailoring.md)
46. [Testware: artefatos produzidos para testar](../../domains/software-0007/software/testes/testware-artifacts.md)
47. [Papéis de gestão e execução técnica de testes](../../domains/software-0007/software/testes/testing-roles-management-and-testing.md)
48. [Teste estático e work products inspecionáveis](../../domains/software-0007/software/testes/static-testing-work-products.md)
49. [Teste estático e dinâmico são complementares](../../domains/software-0007/software/testes/static-vs-dynamic-testing.md)
50. [Feedback frequente de stakeholders durante o SDLC](../../domains/software-0007/software/testes/early-frequent-stakeholder-feedback.md)
51. [Atividades de um processo de revisão](../../domains/software-0007/software/testes/review-process-activities.md)
52. [Tipos de revisão e níveis de formalidade](../../domains/software-0007/software/testes/review-types-formality-purpose.md)
53. [Fatores para revisões de software eficazes](../../domains/software-0007/software/testes/review-success-factors.md)
54. [Níveis de teste e seus diferentes objetivos](../../domains/software-0007/software/testes/test-levels-overview.md)
55. [Teste de componente em isolamento](../../domains/software-0007/software/testes/component-testing-isolation.md)
56. [Integração de componentes e contratos entre módulos](../../domains/software-0007/software/testes/component-integration-testing-interfaces.md)
57. [Teste de sistema contra requisitos do produto integrado](../../domains/software-0007/software/testes/system-testing-requirements.md)
58. [Integração do sistema com serviços externos](../../domains/software-0007/software/testes/system-integration-testing-external-systems.md)
59. [Acceptance testing valida necessidades e readiness](../../domains/software-0007/software/testes/acceptance-testing-validation.md)


## Tranche 6 — SDLC, técnicas, colaboração e suporte (40 notas; revisão factual por IA registrada)

60. [Como o SDLC muda o escopo e o momento dos testes](../../domains/software-0007/software/testes/sdlc-impact-on-testing.md)
61. [Testes em ciclos sequenciais, iterativos e incrementais](../../domains/software-0007/software/testes/testing-sequential-and-iterative-sdlc.md)
62. [Práticas de teste úteis em diferentes SDLCs](../../domains/software-0007/software/testes/good-testing-practices-across-sdlc.md)
63. [Abordagens test-first: TDD, ATDD e BDD](../../domains/software-0007/software/testes/test-first-approaches-tdd-atdd-bdd.md)
64. [TDD dirige a implementação por testes](../../domains/software-0007/software/testes/test-driven-development.md)
65. [ATDD deriva testes de critérios de aceitação](../../domains/software-0007/software/testes/acceptance-test-driven-development.md)
66. [BDD descreve comportamento em exemplos compartilhados](../../domains/software-0007/software/testes/behavior-driven-development.md)
67. [DevOps integra teste, desenvolvimento e operação](../../domains/software-0007/software/testes/devops-testing-continuous-feedback.md)
68. [Shift left antecipa testes sem eliminar verificações tardias](../../domains/software-0007/software/testes/shift-left-testing.md)
69. [Retrospectivas transformam experiência de teste em melhoria](../../domains/software-0007/software/testes/testing-retrospectives-process-improvement.md)
70. [Manutenção de software: dimensionar o teste pela mudança](../../domains/software-0007/software/testes/maintenance-testing-change-scope.md)
71. [Gatilhos para teste de manutenção](../../domains/software-0007/software/testes/maintenance-testing-triggers.md)
72. [Testes em migrações e upgrades de plataforma](../../domains/software-0007/software/testes/testing-migrations-and-platform-upgrades.md)
73. [Testes na aposentadoria e arquivamento de dados](../../domains/software-0007/software/testes/retirement-testing-data-archival.md)
74. [Níveis de independência em teste](../../domains/software-0007/software/testes/independence-of-testing-levels.md)
75. [Abordagem whole-team compartilha responsabilidade por qualidade](../../domains/software-0007/software/testes/whole-team-approach-quality.md)
76. [Habilidades que apoiam o trabalho de teste](../../domains/software-0007/software/testes/essential-skills-for-testers.md)
77. [Teste funcional verifica o que o sistema deve fazer](../../domains/software-0007/software/testes/functional-testing-quality-characteristics.md)
78. [Teste não funcional avalia como o sistema se comporta](../../domains/software-0007/software/testes/nonfunctional-testing-quality-attributes.md)
79. [Teste de confirmação verifica se uma correção resolveu o defeito](../../domains/software-0007/software/testes/confirmation-testing-after-fix.md)
80. [Teste de regressão detecta efeitos adversos de mudanças](../../domains/software-0007/software/testes/regression-testing-change-effects.md)
81. [Teste black-box deriva casos do comportamento especificado](../../domains/software-0007/software/testes/black-box-testing-specification-based.md)
82. [Teste white-box usa estrutura interna como base de teste](../../domains/software-0007/software/testes/white-box-testing-structure-and-limits.md)
83. [Técnicas baseadas em experiência complementam especificações](../../domains/software-0007/software/testes/experience-based-testing-techniques.md)
84. [Error guessing transforma experiência em hipóteses de teste](../../domains/software-0007/software/testes/error-guessing-experience.md)
85. [Checklist-based testing usa condições focadas e revisáveis](../../domains/software-0007/software/testes/checklist-based-testing.md)
86. [Abordagens colaborativas buscam evitar defeitos antes de codificar](../../domains/software-0007/software/testes/collaboration-based-test-approach.md)
87. [Os 3 Cs organizam conversa sobre histórias de usuário](../../domains/software-0007/software/testes/user-story-three-cs.md)
88. [Critérios de aceitação podem ser tratados como condições de teste](../../domains/software-0007/software/testes/acceptance-criteria-as-test-conditions.md)
89. [Papéis de revisão distribuem decisão, facilitação e identificação de anomalias](../../domains/software-0007/software/testes/review-roles-responsibilities.md)
90. [Moderador facilita uma revisão segura e produtiva](../../domains/software-0007/software/testes/review-moderator-facilitator.md)
91. [Scribe registra anomalias, decisões e informações da revisão](../../domains/software-0007/software/testes/review-scribe-recorder.md)
92. [Reviewer avalia o work product e descreve anomalias](../../domains/software-0007/software/testes/review-reviewer-role.md)
93. [Author cria e corrige o work product em revisão](../../domains/software-0007/software/testes/review-author-feedback-correction.md)
94. [Review leader responde pela organização geral da revisão](../../domains/software-0007/software/testes/review-leader-responsibility.md)
95. [Manager decide o que revisar e viabiliza recursos](../../domains/software-0007/software/testes/review-manager-resources.md)
96. [Alocação de papéis de revisão depende do tipo e do risco](../../domains/software-0007/software/testes/review-role-allocation-context.md)
97. [Categorias de ferramentas apoiam diferentes atividades de teste](../../domains/software-0007/software/testes/test-tool-categories.md)
98. [Ferramentas podem apoiar teste sem executar casos automaticamente](../../domains/software-0007/software/testes/test-tools-beyond-automation.md)
99. [Adoção de ferramenta exige implantação, treinamento e análise de riscos](../../domains/software-0007/software/testes/test-tool-introduction-and-risk.md)

## Critérios e próximo passo

Cada tranche é auditada antes de ser adicionada ao lote de escala. A aprovação automática verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e links; não certifica a verdade das afirmações. O protocolo atualizado aceita revisão factual humana ou por IA, registradas separadamente. As nove notas da tranche 1 preservam aprovação humana; as 90 das tranches 2–6 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 99/2.000 notas válidas, restando 1.901 notas materiais. Continuar em tranches de conteúdo real, sem contar placeholders, IDs ou progresso parcial como conclusão; cada nota deve ter fontes conferidas e relatório de revisão factual.
