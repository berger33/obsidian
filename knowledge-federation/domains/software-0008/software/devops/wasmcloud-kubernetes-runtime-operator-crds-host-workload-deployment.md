---
id: software.devops.tranche18.001795
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

# wasmCloud Kubernetes `runtime-operator`: reconciliação dos CRDs `Host`, `Workload`, `WorkloadDeployment`, `WorkloadReplicaSet` e `Artifact`

## Em uma frase
O **Runtime Operator** (`runtime-operator/`) do wasmCloud permite operar toda a infraestrutura e as aplicações WebAssembly como recursos nativos do Kubernetes, reconciliando os Custom Resources **`Host`**, **`Workload`**, **`WorkloadDeployment`**, **`WorkloadReplicaSet`** e **`Artifact`** e agendando os componentes nos Pods de host via **NATS**.

## Por que importa
Em vez de gerenciar frotas WebAssembly em um plano de controle paralelo desconectado do GitOps, expor `WorkloadDeployment` e `Host` como CRDs permite que Argo CD, Flux, RBAC do Kubernetes, HPA e Prometheus governem cargas Wasm exatamente como governam containers.

## Como funciona
Instalado via chart OCI (`oci://ghcr.io/wasmcloud/charts/runtime-operator`), o operador observa objetos `WorkloadDeployment` (que gerenciam `WorkloadReplicaSets` e `Workloads` referenciando `Artifacts` OCI) e envia mensagens Protobuf de controle sobre NATS para instruir os Pods `Host` do wasmCloud a instanciar os componentes.

## Exemplo
```bash
helm install wasmcloud oci://ghcr.io/wasmcloud/charts/runtime-operator \
  --namespace wasmcloud --create-namespace \
  -f https://raw.githubusercontent.com/wasmCloud/wasmCloud/refs/heads/main/charts/runtime-operator/values.local.yaml
kubectl get pods -n wasmcloud
```

## Limites e trade-offs
Os esquemas de mensagens trocadas entre o `runtime-operator` e os Pods de host sobre o barramento NATS são formalmente especificados em Protocol Buffers no diretório `proto/` do monorepo.

## Como verificar
Execute `kubectl api-resources | grep wasmcloud` após instalar o chart para verificar os CRDs registrados pelo `runtime-operator`.

## Conexões
- [[wasmcloud-wash-runtime-mecanismos-capacidades-builtin-ingress-plugins]] — Veja também: wasmCloud `wash-runtime`: arquitetura dos 3 mecanismos de capacidades (`wasmtime-wasi`, `Ingress` e `Host Plugins`).
- [[wasmcloud-roteamento-http-endpointslices-kubernetes-services-deprecacao-gateway]] — Veja também: wasmCloud no Kubernetes: roteamento HTTP nativo via `EndpointSlices` em Services padrão e depreciação do `runtime-gateway`.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
