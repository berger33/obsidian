---
id: software.seguranca.tranche19.001873
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

# OPA Gatekeeper: Usar admission para prevenir violações

## Em uma frase
**OPA Gatekeeper — Usar admission para prevenir violações:** Webhook de Gatekeeper avalia requests de criação e atualização segundo Constraints ativas.

## Por que importa
O recorte de **usar admission para prevenir violações** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar admission para prevenir violações**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Habilite enforcement em cluster de staging com manifesto deliberadamente não conforme. Teste em staging autorizado.

## Limites e trade-offs
Disponibilidade e failure policy do webhook influenciam se erro bloqueia ou permite admission. Exceções exigem responsável e prazo.

## Como verificar
Teste recusa esperada e comportamento durante webhook indisponível em ambiente controlado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-iniciar-com-enforcementaction-dryrun]] — Complementa o tópico com opa gatekeeper: iniciar com enforcementaction dryrun.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
