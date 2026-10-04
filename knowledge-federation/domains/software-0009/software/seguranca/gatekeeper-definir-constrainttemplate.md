---
id: software.seguranca.tranche19.001871
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://open-policy-agent.github.io/gatekeeper/website/docs/howto/", "https://open-policy-agent.github.io/gatekeeper/website/docs/audit/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OPA Gatekeeper: Definir ConstraintTemplate

## Em uma frase
**OPA Gatekeeper — Definir ConstraintTemplate:** ConstraintTemplate declara schema de parâmetros e lógica Rego que Gatekeeper usa para criar tipo de Constraint.

## Por que importa
O recorte de **definir constrainttemplate** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **definir constrainttemplate**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie template de laboratório que exige label de owner em workload e defina schema do parâmetro. Teste em staging autorizado.

## Limites e trade-offs
Template publicado sem testes pode afetar recursos novos quando Constraints forem criadas. Exceções exigem responsável e prazo.

## Como verificar
Valide schema e Rego com recursos que devem e não devem violar a regra. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-instanciar-constraint-com-escopo-claro]] — Complementa o tópico com opa gatekeeper: instanciar constraint com escopo claro.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
