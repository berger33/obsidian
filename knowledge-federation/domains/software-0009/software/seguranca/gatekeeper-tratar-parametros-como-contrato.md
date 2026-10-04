---
id: software.seguranca.tranche19.001877
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

# OPA Gatekeeper: Tratar parâmetros como contrato

## Em uma frase
**OPA Gatekeeper — Tratar parâmetros como contrato:** Parâmetros de Constraint precisam seguir schema declarado pelo template e valores devem ser revisáveis.

## Por que importa
O recorte de **tratar parâmetros como contrato** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **tratar parâmetros como contrato**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Versione `parameters` junto do Constraint e teste limite aceito e recusado. Teste em staging autorizado.

## Limites e trade-offs
Parâmetro excessivo ou ausente pode tornar policy permissiva sem alterar Rego. Exceções exigem responsável e prazo.

## Como verificar
Valide schema e examine parâmetros efetivos retornados no recurso instalado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-controlar-match-exclusions-e-namespaces]] — Complementa o tópico com opa gatekeeper: controlar match, exclusions e namespaces.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
