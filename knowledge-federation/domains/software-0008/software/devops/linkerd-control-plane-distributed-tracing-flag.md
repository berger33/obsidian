---
id: software.devops.tranche02.000137
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

# Habilitação de rastreamento distribuído nos componentes do control plane

## Em uma frase
A subseção `Deploying Control Plane components with Tracing` de `BUILD.md` explica que os componentes do plano de controle possuem a flag `trace-collector` para habilitar Distributed Tracing para fins de desenvolvimento e diagnóstico, podendo ser ativada globalmente nos componentes do control plane e em seus proxies durante a instalação com as flags `--set controller.tracing.enable=true` e `--set controller.tracing.collector.endpoint=<endpoint>`.

## Por que importa
Quando se investiga latência ou comportamento interno dos próprios controladores do service mesh, emitir traces dos componentes do control plane para um coletor (como OpenTelemetry Collector ou Jaeger, vistos na Tranche 1) permite visualizar cada chamada interna.

## Como funciona
Em ambientes de desenvolvimento e homologação do mesh, utilize `linkerd install --set controller.tracing.enable=true --set controller.tracing.collector.endpoint=<endpoint> | kubectl apply -f -` apontando para o seu coletor de traces.

## Exemplo
Um desenvolvedor do plano de controle ativa `controller.tracing.enable=true` para inspecionar no Jaeger os spans emitidos pelos controladores do Linkerd.

## Limites e trade-offs
A própria documentação destaca esse recurso como voltado a fins de desenvolvimento; avalie o volume de spans gerado antes de habilitar tracing global do control plane em clusters produtivos de grande porte.

## Como verificar
Conferi a subseção Deploying Control Plane components with Tracing em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-install-crds-check-and-inject-workflow]] — Veja também: Fluxo de instalação em duas etapas (--crds e control plane), linkerd check e linkerd inject.
- [[linkerd-container-registry-and-k3d-dev-workflow]] — Veja também: Registro oficial cr.l5d.io/linkerd e fluxo de build local com k3d e buildx.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
