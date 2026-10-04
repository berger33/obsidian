---
id: software.seguranca.tranche19.001878
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

# OPA Gatekeeper: Controlar match, exclusions e namespaces

## Em uma frase
**OPA Gatekeeper — Controlar match, exclusions e namespaces:** Campos de match determinam grupos, versões, kinds e namespaces alcançados por uma Constraint.

## Por que importa
O recorte de **controlar match, exclusions e namespaces** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **controlar match, exclusions e namespaces**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exclua namespace do sistema apenas após identificar justificativa e revisar exceção. Teste em staging autorizado.

## Limites e trade-offs
Exclusões podem ocultar exatamente os recursos mais privilegiados. Exceções exigem responsável e prazo.

## Como verificar
Audite inclusão e exclusão por namespace e compare com inventário do cluster. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-interpretar-violation-e-source]] — Complementa o tópico com opa gatekeeper: interpretar violation e source.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
