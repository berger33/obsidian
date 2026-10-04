---
id: software.devops.tranche02.000134
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
fontes: ["https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md", "https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Extensão viz: metrics-api, tap, tap-injector e dashboard web

## Em uma frase
Ainda na subseção `Control Plane (Go/React)` e no diagrama `Components` de `BUILD.md`, a extensão `viz` (`linkerd-viz`) é composta por quatro módulos: `metrics-api` (aceita requisições da CLI e da web, servindo métricas dos proxies no cluster por meio de consultas ao Prometheus), `tap` (fornece um pipeline ao vivo de requisições direto dos proxies), `tap-injector` (mutating webhook disparado na criação de pods que injeta metadados no contêiner do proxy para habilitar o tap) e `web` (dashboard UI para visualizar e operar o control plane).

## Por que importa
Separar a pilha de visualização e métricas (`viz`) do núcleo do plano de controle mantém a instalação base enxuta e permite que equipes consultem métricas agregadas ou inspecionem fluxos em tempo real apenas quando desejado.

## Como funciona
Instale a extensão com `linkerd viz install | kubectl apply -f -` e, caso queira usar `linkerd viz tap` contra os próprios componentes do control plane, execute `kubectl -n linkerd rollout restart deploy` para que o `tap-injector` injete os metadados de tap nos proxies existentes.

## Exemplo
Um engenheiro executa `linkerd viz stat deployments` e `linkerd viz tap deploy voting` para inspecionar taxas de sucesso, latências e requisições ao vivo de um deployment.

## Limites e trade-offs
O recurso `tap` permite observar metadados de requisições em tempo real; restrinja o acesso à API do `tap` via RBAC do Kubernetes em ambientes produtivos sensíveis.

## Como verificar
Conferi as seções Control Plane (Go/React), Components e Comprehensive em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-control-plane-destination-injector-identity]] — Veja também: Componentes nucleares do control plane: destination, proxy-injector e identity.
- [[linkerd-multicluster-gateway-and-service-mirror]] — Veja também: Extensão multicluster: linkerd-gateway e controlador linkerd-service-mirror.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
