---
id: software.seguranca.tranche19.001875
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

# OPA Gatekeeper: Auditar recursos já existentes

## Em uma frase
**OPA Gatekeeper — Auditar recursos já existentes:** Audit percorre recursos Kubernetes existentes e registra violações das Constraints configuradas.

## Por que importa
O recorte de **auditar recursos já existentes** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **auditar recursos já existentes**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute auditoria de namespace antes de mudar enforcement de deny em produção. Teste em staging autorizado.

## Limites e trade-offs
Audit é periódico e não equivale a validar cada mudança instantaneamente. Exceções exigem responsável e prazo.

## Como verificar
Compare recursos inventariados com violations e registre hora e versão do controller. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-testar-policies-com-gator]] — Complementa o tópico com opa gatekeeper: testar policies com gator.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
