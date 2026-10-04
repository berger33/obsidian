---
id: software.devops.tranche03.000231
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
fontes: ["https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md", "https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Diferenças arquiteturais do Gatekeeper em relação ao OPA clássico com sidecar kube-mgmt

## Em uma frase
O README oficial no repositório open-policy-agent/gatekeeper explica como o Gatekeeper difere do uso tradicional do Open Policy Agent (OPA) com seu sidecar kube-mgmt (conhecido historicamente como Gatekeeper v1.0), introduzindo seis capacidades nativas: uma biblioteca de políticas parametrizada e extensível, CRDs nativas do Kubernetes para instanciar políticas (constraints), CRDs nativas para estender a biblioteca (constraint templates), CRDs nativas para suporte a mutação (mutation), funcionalidade de auditoria (audit) e suporte a dados externos (external data).

## Por que importa
Na abordagem antiga com kube-mgmt, políticas eram carregadas via ConfigMaps sem validação de esquema pela API do Kubernetes nem auditoria estruturada em CRDs; o Gatekeeper transforma templates e restrições em recursos declarativos de primeira classe do Kubernetes.

## Como funciona
Implante o Gatekeeper no cluster Kubernetes (`open-policy-agent.github.io/gatekeeper/website/docs/install`) para governar admissão, mutação e auditoria por meio de Custom Resources nativos em vez de gerenciar sidecars kube-mgmt manuais.

## Exemplo
Uma organização migra políticas Rego antigas baseadas em ConfigMaps do kube-mgmt para `ConstraintTemplates` e `Constraints` gerenciados declarativamente via GitOps.

## Limites e trade-offs
Ao escolher entre OPA Gatekeeper (baseado em Rego e Constraint Framework) e Kyverno (baseado em YAML nativo), evite rodar ambos aplicando regras conflitantes de mutação sobre os mesmos recursos.

## Como verificar
Conferi a seção How is Gatekeeper different from OPA? no README oficial de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-opa-constraint-framework-and-targets]] — Veja também: Uso do OPA Constraint Framework para validação na admissão, auditoria e mutação.

## Fontes
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
