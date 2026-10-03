---
id: software.devops.tranche03.000234
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

# Instanciação declarativa de Constraints (`constraints.gatekeeper.sh/v1beta1`) e inspeção com kubectl get constraints

## Em uma frase
As seções `Constraints` e `Listing constraints` de `website/docs/howto.md` demonstram que, uma vez registrado o `ConstraintTemplate`, o administrador aplica um recurso do tipo gerado sob `apiVersion: constraints.gatekeeper.sh/v1beta1` (por exemplo, `kind: K8sRequiredLabels`, `name: ns-must-have-gk`) combinando os blocos `spec.match` e `spec.parameters`, podendo listar todas as restrições ativas no cluster com o comando `kubectl get constraints`.

## Por que importa
Como um mesmo `ConstraintTemplate` pode ser instanciado dezenas de vezes com diferentes seletores `match` e diferentes `parameters`, a equipe reutiliza uma única regra Rego auditada para impor exigências distintas em produção, homologação e desenvolvimento.

## Como funciona
Instancie objetos `Constraint` em `constraints.gatekeeper.sh/v1beta1` passando os parâmetros desejados para cada escopo do cluster e utilize `kubectl get constraints` para inspecionar o status e a contagem de violações.

## Exemplo
A constraint `ns-must-have-gk` usa o template `K8sRequiredLabels` sobre recursos `Kind: Namespace` (`apiGroups: [""]`) exigindo a presença do label `gatekeeper`.

## Limites e trade-offs
Se você tentar remover um `ConstraintTemplate` enquanto ainda existirem `Constraints` dependentes ou precisar auditar o inventário global de regras, execute `kubectl get constraints` para localizar todas as instâncias ativas.

## Como verificar
Conferi as seções Constraints e Listing constraints em `website/docs/howto.md` de open-policy-agent/gatekeeper.

## Conexões
- [[gatekeeper-constrainttemplate-openapi-schema-and-rego]] — Veja também: Estrutura do ConstraintTemplate (`templates.gatekeeper.sh/v1`): esquema openAPIV3Schema e código Rego.
- [[gatekeeper-match-field-selectors-and-glob-support]] — Veja também: Os sete seletores do campo match e suporte a globs baseados em prefixo.

## Fontes
- [OPA Gatekeeper Documentation — How to use Gatekeeper (howto.md)](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/website/docs/howto.md) — Guia oficial do Gatekeeper detalhando OPA Constraint Framework, ConstraintTemplate (openAPIV3Schema e Rego), Constraint, os 7 seletores de match, escopo Cluster vs Namespaced e enforcementAction (deny, dryrun, warn).; consultado em 2026-10-03.
- [OPA Gatekeeper — GitHub README](https://raw.githubusercontent.com/open-policy-agent/gatekeeper/master/README.md) — Visão geral do Gatekeeper em comparação ao OPA com sidecar kube-mgmt (Gatekeeper v1.0), CRDs de constraints/templates/mutação, auditoria, external data e biblioteca de políticas.; consultado em 2026-10-03.
