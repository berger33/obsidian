---
id: software.devops.tranche18.001755
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

# Operator SDK e OLM (*Operator Lifecycle Manager*): instalação, verificação de status e matriz de compatibilidade

## Em uma frase
O Operator SDK integra-se nativamente ao **Operator Lifecycle Manager (OLM)** por meio dos subcomandos `operator-sdk olm install`, `operator-sdk olm uninstall` e `operator-sdk olm status`, trazendo os manifestos das últimas 3 versões minor suportadas do OLM embutidos no próprio binário (`bindata`).

## Por que importa
Testar a instalação de pacotes de operadores, resolução de dependências entre CRDs e atualizações de canais OLM localmente exigiria buscar e aplicar dezenas de manifestos do repositório do OLM se o SDK não embutisse o instalador.

## Como funciona
Conforme documentado na visão geral oficial do Operator SDK, o binário empacota via `bindata` as 3 últimas versões minor do OLM presentes no lançamento (por exemplo `0.26.0`, `0.27.0` e `0.28.0`) para instalação de baixa latência em clusters de desenvolvimento e CI.

## Exemplo
```bash
operator-sdk olm install --version 0.28.0
operator-sdk olm status
```

## Limites e trade-offs
Evite depender da tag móvel `latest` ao instalar o OLM em pipelines automatizados; fixe explicitamente uma das três versões minor oficialmente suportadas e testadas pelo seu release do `operator-sdk`.

## Como verificar
Execute `operator-sdk olm status` contra o cluster para validar a saúde de `catalog-operator`, `olm-operator` e `packageserver`.

## Conexões
- [[operator-sdk-helm-operator-charts-watches-reconciliacao-nativa]] — Veja também: Operator SDK `helm-operator`: conversão de Helm Charts existentes em Operators Kubernetes declarativos.
- [[operator-sdk-generate-bundle-clusterserviceversion-csv-metadata]] — Veja também: Operator SDK Bundles: geração de `ClusterServiceVersion` (CSV) e empacotamento OCI de Bundles para o OLM.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
