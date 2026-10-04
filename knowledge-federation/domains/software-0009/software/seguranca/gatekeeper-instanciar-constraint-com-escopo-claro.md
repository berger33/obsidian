---
id: software.seguranca.tranche19.001872
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

# OPA Gatekeeper: Instanciar Constraint com escopo claro

## Em uma frase
**OPA Gatekeeper — Instanciar Constraint com escopo claro:** Constraint seleciona kind, namespaces, labels e parâmetros para aplicar template a recursos específicos.

## Por que importa
O recorte de **instanciar constraint com escopo claro** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **instanciar constraint com escopo claro**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique Constraint em namespace piloto antes de expandir para toda organização. Teste em staging autorizado.

## Limites e trade-offs
Match amplo pode bloquear tipos de recursos ou equipes não envolvidos no piloto. Exceções exigem responsável e prazo.

## Como verificar
Liste recursos alcançados pela seleção e teste recurso incluído e recurso excluído. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[gatekeeper-usar-admission-para-prevenir-violacoes]] — Complementa o tópico com opa gatekeeper: usar admission para prevenir violações.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
