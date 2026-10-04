---
id: software.testes.acceptance-testing.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/2-2-test-levels-and-test-types/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Acceptance testing, UAT, Teste de aceitação]
lote: software-testes-2000-0001
---

# Acceptance testing valida necessidades e readiness

## Em uma frase
Acceptance testing avalia se o sistema satisfaz necessidades e critérios de aceitação e pode fornecer evidência sobre sua prontidão para uso ou implantação.

## Por que importa
Um produto tecnicamente conforme ainda pode ser difícil de usar, inadequado ao fluxo de negócio ou indisponível para operação. Envolver pessoas que representam uso e negócio ajuda a validar se a solução serve ao propósito, não apenas se implementa uma especificação.

## Como funciona
O CTFL caracteriza acceptance testing como nível focado em validação e demonstração de readiness para deployment. Idealmente participam os intended users, mas contratos, regulação, operação ou representantes autorizados também podem definir critérios. Formas incluem UAT, operational acceptance, contractual/regulatory acceptance, alpha e beta testing. Critérios e responsáveis variam pelo produto e acordo.

## Exemplo
Para um sistema de folha, representantes autorizados podem validar os cenários de fechamento, reconciliação e tratamento de exceções com dados aprovados. Uma verificação técnica automatizada pode apoiar a atividade, mas não substitui a decisão de stakeholders sobre critérios de negócio ou aceitação formal.

## Limites e trade-offs
Acceptance testing não é garantia de ausência de defeitos nem sempre ocorre apenas no fim do ciclo. Se critérios são vagos, diferentes stakeholders podem julgar o mesmo resultado de maneira incompatível. A decisão de release pode considerar riscos residuais além do resultado de testes.

## Como verificar
Converta necessidades em critérios claros antes de executar, envolva representantes adequados, registre evidência e divergências e documente quem aceita riscos ou rejeita o produto. Distinga aceite do cliente, prontidão operacional e conformidade contratual quando forem objetivos diferentes.

## Conexões
- [[test-entry-exit-criteria]] — critérios de aceitação podem integrar definição de pronto/concluído.
- [[test-objectives-context]] — orienta validação contra necessidades de stakeholders.
- [[test-oracles-resultados-esperados]] — critérios sustentam avaliação de resultados.

## Fontes
- [ASTQB — ISTQB CTFL §2.2: Test Levels and Test Types](https://astqb.org/2-2-test-levels-and-test-types/) — aceitação como nível de teste e distinção de tipo; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 2.2.1, validação, readiness e formas de acceptance testing; acesso em 2026-10-01.
