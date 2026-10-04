---
id: software.devops.tranche03.000232
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md", "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Uso do OPA Constraint Framework para validação na admissão, auditoria e mutação

## Em uma frase
A abertura do guia oficial `website/docs/howto.md` explica que o Gatekeeper utiliza o **OPA Constraint Framework** (`open-policy-agent/frameworks/tree/master/constraint`) para descrever e impor políticas: a validação usa recursos `ConstraintTemplate` e `Constraint` para avaliar objetos do Kubernetes — podendo negar (`deny`), emitir aviso (`warn`) ou simular (`dry-run`) requisições durante a admissão e avaliar recursos existentes reportando violações no modo de auditoria (`audit mode`) —, enquanto políticas de mutação modificam recursos durante a admissão.

## Por que importa
Separar o momento de admissão (que protege o cluster contra novas mudanças inválidas) do modo de auditoria periódica (que detecta recursos antigos já existentes no cluster que violam uma nova política) permite adotar governança em clusters legados sem derrubar serviços em execução.

## Como funciona
Utilize o par `ConstraintTemplate` + `Constraint` com target `admission.k8s.gatekeeper.sh` para políticas de validação e consulte a documentação específica de mutação (`mutation.md`) quando precisar modificar campos na entrada.

## Exemplo
Antes de bloquear deploys sem labels obrigatórios, a equipe implanta a Constraint e analisa os resultados do ciclo de auditoria sobre os namespaces já existentes.

## Limites e trade-offs
Políticas de validação nunca alteram o objeto avaliado; se o objetivo for injetar um valor padrão, utilize as CRDs específicas de mutação do Gatekeeper.

## Como verificar
Conferi a abertura e a seção Constraint Templates em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-evolution-beyond-opa-kube-mgmt-sidecar]] — Veja também: Diferenças arquiteturais do Gatekeeper em relação ao OPA clássico com sidecar kube-mgmt.
- [[gatekeeper-constrainttemplate-openapi-schema-and-rego]] — Veja também: Estrutura do ConstraintTemplate (`templates.gatekeeper.sh/v1`): esquema openAPIV3Schema e código Rego.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
