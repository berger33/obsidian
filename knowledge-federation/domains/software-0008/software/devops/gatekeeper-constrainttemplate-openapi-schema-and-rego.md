---
id: software.devops.tranche03.000233
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

# Estrutura do ConstraintTemplate (`templates.gatekeeper.sh/v1`): esquema openAPIV3Schema e código Rego

## Em uma frase
A seção `Constraint Templates` de `website/docs/howto.md` mostra que, antes de definir uma restrição, o administrador deve criar um `ConstraintTemplate` (`apiVersion: templates.gatekeeper.sh/v1`), que descreve duas partes fundamentais: (1) em `spec.crd.spec`, o nome do Kind gerado (como `K8sRequiredLabels`) e o esquema `openAPIV3Schema` dos parâmetros aceitos; e (2) em `spec.targets`, a regra escrita na linguagem **Rego** (como `violation[{"msg": msg, "details": ...}]`) que avalia `input.review` e `input.parameters`.

## Por que importa
Separar a lógica Rego e a assinatura de tipos (`ConstraintTemplate`, escrita uma única vez pela equipe de plataforma ou importada da biblioteca oficial) da instanciação com valores concretos (`Constraint`) funciona exatamente como declarar uma função tipada e depois invocá-la com argumentos diferentes.

## Como funciona
Defina em `spec.crd.spec.validation.openAPIV3Schema` a tipagem estrita de todos os parâmetros esperados pela regra Rego antes de aplicar o `ConstraintTemplate` no cluster.

## Exemplo
O template `k8srequiredlabels` define que o parâmetro `labels` é um array de strings em `openAPIV3Schema` e calcula em Rego `missing := required - provided` sobre `input.review.object.metadata.labels`.

## Limites e trade-offs
Ao instalar um novo `ConstraintTemplate`, aguarde alguns segundos até que o controlador do Gatekeeper registre a CRD correspondente (como `K8sRequiredLabels`) no API Server antes de aplicar a `Constraint` que a instancia.

## Como verificar
Conferi a seção Constraint Templates e o exemplo YAML `k8srequiredlabels` em `website/docs/howto.md`.

## Conexões
- [[gatekeeper-opa-constraint-framework-and-targets]] — Veja também: Uso do OPA Constraint Framework para validação na admissão, auditoria e mutação.
- [[gatekeeper-constraint-instantiation-and-listing]] — Veja também: Instanciação declarativa de Constraints (`constraints.gatekeeper.sh/v1beta1`) e inspeção com kubectl get constraints.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
