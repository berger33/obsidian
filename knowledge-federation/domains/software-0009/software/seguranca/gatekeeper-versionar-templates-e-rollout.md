---
id: software.seguranca.tranche19.001880
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

# OPA Gatekeeper: Versionar templates e rollout

## Em uma frase
**OPA Gatekeeper — Versionar templates e rollout:** Mudanças de Template e Constraints devem seguir rollout que permita observar e reverter decisões.

## Por que importa
O recorte de **versionar templates e rollout** ajuda a definir e auditar políticas de admissão com regras como código, parâmetros e escopo de recursos explícitos. A equipe registra risco, evidência e responsável.

## Como funciona
Para **versionar templates e rollout**, ConstraintTemplate instala tipo de Constraint; Constraints instanciadas selecionam recursos e aplicam regras Rego pelo webhook. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Publique versão nova em dryrun, acompanhe audit e altere enforcement após revisão. Teste em staging autorizado.

## Limites e trade-offs
Atualizar controller e policy simultaneamente pode dificultar atribuir regressão. Exceções exigem responsável e prazo.

## Como verificar
Registre hashes, versão do Gatekeeper, contagem de violations e plano de rollback. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[external-secrets-separar-secretstore-e-clustersecretstore]] — Complementa o tópico com external secrets operator: separar secretstore e clustersecretstore.

## Fontes
- [Gatekeeper — How-to guides](https://open-policy-agent.github.io/gatekeeper/website/docs/howto/) — documentação oficial de ConstraintTemplates, Constraints e enforcement; consultado em 2026-10-04.
- [Gatekeeper — Audit](https://open-policy-agent.github.io/gatekeeper/website/docs/audit/) — guia oficial de auditoria de recursos existentes e resultados de violations; consultado em 2026-10-04.
