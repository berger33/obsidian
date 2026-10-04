---
id: software.devops.tranche18.001796
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
fontes: ["https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md", "https://wasmcloud.com/docs/concepts/components/", "https://github.com/wasmCloud/wasmCloud"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# wasmCloud no Kubernetes: roteamento HTTP nativo via `EndpointSlices` em Services padrão e depreciação do `runtime-gateway`

## Em uma frase
A partir do wasmCloud 2.0.3+, o componente dedicado **`runtime-gateway`** foi depreciado e o roteamento de tráfego HTTP para cargas WebAssembly no Kubernetes passou a ser realizado diretamente pelo `runtime-operator` gerenciando **`EndpointSlices`** em `Services` Kubernetes padrão.

## Por que importa
Manter um proxy reverso intermediário proprietário (`runtime-gateway`) entre o Ingress/Service do Kubernetes e os Pods de host do wasmCloud adicionava um salto extra de rede e ponto de falha desnecessário.

## Como funciona
Com o roteamento nativo (ativado aplicando `values.local.yaml` ou definindo `gateway.enabled: false` no Helm chart `runtime-operator`), o operador popula automaticamente `EndpointSlices` apontando exatamente para os Pods de host wasmCloud onde cada `WorkloadDeployment` está ativo, permitindo expor qualquer componente Wasm via `Service`, `Ingress` ou `Gateway API` padrão.

## Exemplo
```bash
helm upgrade --install wasmcloud oci://ghcr.io/wasmcloud/charts/runtime-operator \
  --namespace wasmcloud --create-namespace \
  --set gateway.enabled=false
kubectl get svc,endpointslices -n wasmcloud
```

## Limites e trade-offs
Por compatibilidade retroativa, o chart `runtime-operator` ainda habilita o `runtime-gateway` se instalado sem overrides; em novas implantações, passe `-f values.local.yaml` ou `--set gateway.enabled=false`.

## Como verificar
Verifique os objetos `EndpointSlice` criados pelo `runtime-operator` ao implantar um `WorkloadDeployment` HTTP no cluster.

## Conexões
- [[wasmcloud-kubernetes-runtime-operator-crds-host-workload-deployment]] — Veja também: wasmCloud Kubernetes `runtime-operator`: reconciliação dos CRDs `Host`, `Workload`, `WorkloadDeployment`, `WorkloadReplicaSet` e `Artifact`.
- [[wasmcloud-nats-control-plane-messaging-kv-blobstore-plugins]] — Veja também: wasmCloud e NATS: barramento de controle Protobuf e backend para `wasi:keyvalue`, `wasi:blobstore` e `wasmcloud:messaging`.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
