---
id: software.testes.process-context.000001
tipo: conceito
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
fontes: ["https://astqb.org/1-4-test-activities-testware-and-test-roles/", "https://astqb.org/5-1-test-planning/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Test process in context, Tailoring the test process, Contexto do processo de teste]
lote: software-testes-2000-0001
---

# Adaptar o processo de teste ao contexto

## Em uma frase
Um processo de teste deve ser ajustado ao sistema, SDLC, risco, recursos e objetivos, preservando as atividades necessárias sem impor uma receita única.

## Por que importa
Dois produtos com riscos, ciclos e públicos diferentes precisam de evidências diferentes. Um processo copiado sem ajuste pode gastar recursos em formalidades irrelevantes ou deixar de planejar a cobertura necessária. A adaptação explícita explica por que uma atividade foi incluída, combinada ou não aplicada.

## Como funciona
O CTFL diz que testing é context-dependent e que as atividades, sua implementação e seu momento são definidos pelo planejamento para uma situação específica. Fatores incluem produto, stakeholders, processos e ferramentas, riscos, restrições de prazo/orçamento, habilidades, exigências regulatórias e modelo de desenvolvimento. As atividades podem ser integradas ao fluxo ágil/CI ou estruturadas como ciclos formais; o conteúdo da evidência varia, mas não se deve omitir análise, execução ou comunicação necessárias aos objetivos.

## Exemplo
Um serviço interno com deploy diário pode registrar plano leve em tickets, executar testes automatizados por pull request e revisar risco residual em cada release. Um sistema sob exigência regulatória pode precisar de rastreabilidade mais formal, revisão independente e registros auditáveis. Ambos precisam demonstrar adequação aos seus objetivos e restrições.

## Limites e trade-offs
“Tailoring” não é justificativa para eliminar controles requeridos, nem toda documentação é desperdício. Ao contrário, replicar uma metodologia completa sem relação com risco pode retardar feedback. Mudanças no contexto exigem reavaliar a adaptação.

## Como verificar
Registre quais condições do projeto orientaram a abordagem, quais atividades/artefatos foram adaptados e qual evidência permanece. Compare com políticas, contratos e obrigações aplicáveis; revise após incidentes, alterações de risco ou mudança de cadência.

## Conexões
- [[test-planning-objetivos-escopo-comunicacao]] — registra a abordagem escolhida.
- [[test-objectives-context]] — objetivos dependem do work product e do negócio.
- [[risk-based-testing-priorizacao-risco]] — risco ajuda a escolher rigor e escopo.

## Fontes
- [ASTQB — ISTQB CTFL §1.4: Test Activities, Testware and Test Roles](https://astqb.org/1-4-test-activities-testware-and-test-roles/) — tailoring de atividades ao contexto; acesso em 2026-10-01.
- [ASTQB — ISTQB CTFL §5.1: Test Planning](https://astqb.org/5-1-test-planning/) — planejamento de objetivos e abordagem dentro das restrições; acesso em 2026-10-01.
