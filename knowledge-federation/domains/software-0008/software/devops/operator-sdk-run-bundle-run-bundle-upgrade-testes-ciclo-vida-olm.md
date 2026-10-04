---
id: software.devops.tranche18.001757
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

# Operator SDK `run bundle` e `run bundle-upgrade`: validação ponta a ponta de instalação e upgrade no OLM

## Em uma frase
Os comandos `operator-sdk run bundle <bundle-image>` e `operator-sdk run bundle-upgrade <new-bundle-image>` permitem implantar e atualizar uma imagem de Bundle OCI diretamente em um cluster com OLM habilitado usando um único comando CLI.

## Por que importa
Configurar manualmente um `CatalogSource` gRPC, um `OperatorGroup`, uma `Subscription` e aprovar `InstallPlans` apenas para testar se o bundle `v1.0.1` atualiza corretamente a partir do bundle `v1.0.0` em um ambiente de teste é lento e repetitivo.

## Como funciona
Quando você executa `operator-sdk run bundle ghcr.io/org/webapp-operator-bundle:v1.0.0`, o SDK cria automaticamente um pod de índice efêmero (`CatalogSource`), o `OperatorGroup` (se necessário) e a `Subscription`, aguardando até que o `ClusterServiceVersion` atinja a fase `Succeeded`. Em seguida, `operator-sdk run bundle-upgrade ghcr.io/org/webapp-operator-bundle:v1.0.1` testa a transição de versão in-place, e `operator-sdk cleanup <package>` remove tudo ao final.

## Exemplo
```bash
operator-sdk run bundle ghcr.io/org/webapp-operator-bundle:v1.0.0 --namespace operators
kubectl get csv -n operators
operator-sdk cleanup webapp-operator --namespace operators
```

## Limites e trade-offs
A imagem `ghcr.io/org/webapp-operator-bundle:v1.0.0` precisa estar acessível para pull pelos nós do cluster Kubernetes onde o comando `operator-sdk run bundle` está sendo executado.

## Como verificar
Execute `operator-sdk run bundle` seguido de `kubectl get csv,installplan,sub -n operators` para confirmar a instalação completa via OLM.

## Conexões
- [[operator-sdk-generate-bundle-clusterserviceversion-csv-metadata]] — Veja também: Operator SDK Bundles: geração de `ClusterServiceVersion` (CSV) e empacotamento OCI de Bundles para o OLM.
- [[operator-sdk-scorecard-test-kuttl-validacao-boas-praticas-bundles]] — Veja também: Operator SDK `scorecard`: validação automatizada de bundles com suítes básicas, OLM e testes declarativos KUTTL.

## Fontes
- [Operator SDK GitHub — README.md (Operator Framework Toolkit, Controller-Runtime Integration & Metrics Authn/Authz Notice)](https://sdk.operatorframework.io/docs/overview/) — README oficial do operator-framework/operator-sdk detalhando a arquitetura do SDK e a substituição do kube-rbac-proxy por WithAuthenticationAndAuthorization; consultado em 2026-10-03.
- [Operator SDK Official Documentation — Overview (Go/Ansible/Helm Workflows, 5 Capability Levels, Kubernetes/client-go & OLM Compatibility)](https://raw.githubusercontent.com/operator-framework/operator-sdk/master/README.md) — Documentação oficial Overview do Operator SDK cobrindo fluxos Go/Ansible/Helm, 5 níveis de maturidade, versões embutidas do OLM e suporte multi-arquitetura; consultado em 2026-10-03.
- [Operator SDK — Official GitHub Repository](https://github.com/operator-framework/operator-sdk) — Repositório oficial Apache-2.0 do Operator SDK na CNCF; consultado em 2026-10-03.
