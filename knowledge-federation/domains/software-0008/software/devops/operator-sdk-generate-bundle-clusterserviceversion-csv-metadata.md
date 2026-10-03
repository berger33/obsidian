---
id: software.devops.tranche18.001756
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://sdk.operatorframework.io/docs/overview/", "https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md", "https://github.com/operator-framework/operator-sdk"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operator SDK Bundles: geração de `ClusterServiceVersion` (CSV) e empacotamento OCI de Bundles para o OLM

## Em uma frase
Para distribuir um operador através do Operator Lifecycle Manager (OLM) ou do OperatorHub.io, o Operator SDK fornece o fluxo `make bundle` (`operator-sdk generate kustomize manifests` + `operator-sdk generate bundle`), que gera o diretório `bundle/` contendo os CRDs, o **`ClusterServiceVersion` (CSV)** e os metadados de anotações (`bundle/metadata/annotations.yaml`), além de `bundle.Dockerfile`.

## Por que importa
Um operador não é apenas uma imagem de container: o cluster precisa saber quais CRDs o operador fornece (`owned`), quais CRDs de terceiros ele requer (`required`), quais permissões RBAC e webhooks ele exige e qual versão substitui qual (`replaces`/`skipRange`).

## Como funciona
O arquivo `ClusterServiceVersion` (`operators.coreos.com/v1alpha1`) consolida os metadados de exibição, especificação do Deployment do `manager`, regras RBAC e definições de CRDs. Em seguida, `make bundle-build bundle-push` constrói e publica a imagem OCI imutável do bundle e `operator-sdk bundle validate ./bundle` valida sua conformidade.

## Exemplo
```bash
make bundle VERSION=1.0.0 IMG=ghcr.io/org/webapp-operator:v1.0.0
operator-sdk bundle validate ./bundle --select-optional suite=operatorframework
```

## Limites e trade-offs
Execute sempre `operator-sdk bundle validate ./bundle` no pipeline de CI antes de publicar a imagem do bundle para detectar erros de schema no CSV ou falta de descrições obrigatórias para o OperatorHub.

## Como verificar
Inspecione os arquivos gerados em `bundle/manifests/` e `bundle/metadata/annotations.yaml` após rodar `make bundle`.

## Conexões
- [[operator-sdk-olm-integration-operator-sdk-olm-install-status]] — Veja também: Operator SDK e OLM (*Operator Lifecycle Manager*): instalação, verificação de status e matriz de compatibilidade.
- [[operator-sdk-run-bundle-run-bundle-upgrade-testes-ciclo-vida-olm]] — Veja também: Operator SDK `run bundle` e `run bundle-upgrade`: validação ponta a ponta de instalação e upgrade no OLM.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
