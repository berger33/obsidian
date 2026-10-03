---
id: software.devops.tranche02.000132
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md", "https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Organização dos cinco repositórios do Linkerd e divisão entre Rust, Go e React

## Em uma frase
A seção `Repo layout` do README e a seção correspondente de `BUILD.md` explicam que o ecossistema é dividido em cinco repositórios principais — `linkerd2` (repositório principal da linha 2.x com control plane e CLI), `linkerd2-proxy` (proxy do data plane da linha 2.x), `linkerd2-proxy-api` (bindings da API gRPC/Protobuf do proxy), `linkerd` (linha 1.x legada) e `website` (site `linkerd.io` e código-fonte da documentação) — e que o Linkerd2 é escrito primariamente em **Rust** (data plane de alta performance), **Go** (componentes do control plane e extensões) e **React** (dashboard web).

## Por que importa
Escrever o proxy do plano de dados em Rust evita pausas de coletor de lixo (GC) e vulnerabilidades de memória no caminho crítico dos pacotes, enquanto manter o plano de controle em Go aproveita diretamente as bibliotecas clientes oficiais do Kubernetes.

## Como funciona
Ao investigar código ou abrir issues técnicas, direcione temas do control plane/CLI para `linkerd/linkerd2`, questões do sidecar Rust para `linkerd/linkerd2-proxy` e contratos Protobuf entre ambos para `linkerd/linkerd2-proxy-api`.

## Exemplo
Um engenheiro de performance analisa o consumo de memória do sidecar consultando o repositório `linkerd2-proxy` em Rust, enquanto ajusta um webhook de injeção em Go no repositório `linkerd2`.

## Limites e trade-offs
Não confunda a arquitetura da linha `linkerd` 1.x (baseada na JVM/Finagle) com a linha `linkerd2` (baseada em Rust e Go).

## Como verificar
Conferi a seção Repo layout no README e em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-ultralight-security-first-service-mesh]] — Veja também: Definição do Linkerd como service mesh ultraleve e security-first na CNCF.
- [[linkerd-control-plane-destination-injector-identity]] — Veja também: Componentes nucleares do control plane: destination, proxy-injector e identity.

## Fontes
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
