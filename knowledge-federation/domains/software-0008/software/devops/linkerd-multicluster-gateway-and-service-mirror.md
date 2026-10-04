---
id: software.devops.tranche02.000135
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

# Extensão multicluster: linkerd-gateway e controlador linkerd-service-mirror

## Em uma frase
A subseção `Control Plane (Go/React)` de `BUILD.md` descreve os dois componentes da extensão `multicluster`: `linkerd-gateway` (aceita requisições vindas de outros clusters e as encaminha para o destino apropriado no cluster local) e `linkerd-service-mirror-xxx` (controlador em `multicluster/service-mirror` que observa a rotulagem de serviços exportados no cluster de destino e cria, para cada um deles, um serviço espelhado — mirrored service — no cluster local).

## Por que importa
Diferentemente de abordagens que exigem rede L3 plana entre todos os pods de todos os clusters, o modelo de espelhamento de serviços com gateway permite conectar clusters Kubernetes separados mantendo o isolamento de rede interna de cada cluster.

## Como funciona
Utilize a extensão `multicluster` do Linkerd para exportar seletivamente serviços por meio de labels no cluster de destino e consumi-los no cluster de origem através dos serviços espelhados criados pelo `service-mirror`.

## Exemplo
Um serviço de catálogo rodando em um cluster secundário é rotulado como exportado; o `linkerd-service-mirror` cria o serviço correspondente no cluster principal, roteando o tráfego de forma segura pelo `linkerd-gateway`.

## Limites e trade-offs
Monitore a conectividade e os certificados compartilhados entre os clusters conectados pela extensão `multicluster` para evitar falhas silenciosas de sincronização do `service-mirror`.

## Como verificar
Conferi a subseção Control Plane (Go/React) em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-viz-extension-metrics-tap-and-web]] — Veja também: Extensão viz: metrics-api, tap, tap-injector e dashboard web.
- [[linkerd-install-crds-check-and-inject-workflow]] — Veja também: Fluxo de instalação em duas etapas (--crds e control plane), linkerd check e linkerd inject.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
