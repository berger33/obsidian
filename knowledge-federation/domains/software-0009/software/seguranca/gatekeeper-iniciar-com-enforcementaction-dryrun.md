---
id: software.seguranca.tranche19.001874
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

# OPA Gatekeeper: Iniciar com enforcementAction dryrun

## Em uma frase
**OPA Gatekeeper — Iniciar com enforcementAction dryrun:** Ação dryrun reporta violações sem bloquear objetos, permitindo observar impacto antes de enforcement.

## Por que importa
O recorte de **iniciar com enforcementaction dryrun** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **iniciar com enforcementaction dryrun**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique Constraint em dryrun e revise violações antes de promovê-la a deny. Teste em staging autorizado.

## Limites e trade-offs
Dryrun não impede configuração insegura de chegar ao cluster. Exceções exigem responsável e prazo.

## Como verificar
Confirme que violações aparecem e que objeto de teste continua admitido nessa fase. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-auditar-recursos-ja-existentes]] — Complementa o tópico com opa gatekeeper: auditar recursos já existentes.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
