---
id: software.devops.tranche02.000131
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

# Definição do Linkerd como service mesh ultraleve e security-first na CNCF

## Em uma frase
O README oficial no repositório `linkerd/linkerd2` define o Linkerd como um service mesh ultraleve e security-first para Kubernetes que adiciona recursos críticos de segurança, observabilidade e confiabilidade à pilha Kubernetes sem exigir nenhuma alteração de código nas aplicações (`no code change required`), sendo um projeto da Cloud Native Computing Foundation (CNCF) licenciado sob Apache 2.0.

## Por que importa
Em arquiteturas de microsserviços no Kubernetes, implementar criptografia mTLS, telemetria uniforme por rota e retentativas diretamente no código de cada linguagem é custoso e inconsistente; o Linkerd resolve isso na camada de infraestrutura com baixo consumo de recursos.

## Como funciona
Instale o Linkerd no cluster Kubernetes e injete os proxies nos deployments das aplicações sem modificar o código-fonte dos serviços.

## Exemplo
Uma equipe de plataforma adiciona mTLS automático e métricas de taxa de sucesso entre dezenas de microsserviços heterogêneos apenas injetando os sidecars do Linkerd nos manifestos de deployment.

## Limites e trade-offs
Embora não exija mudança de código na aplicação, a injeção de sidecars adiciona um contêiner proxy por pod, o que deve ser considerado nas cotas de CPU e memória dos namespaces.

## Como verificar
Conferi a abertura e a seção License do README oficial de `linkerd/linkerd2`.

## Conexões
- [[linkerd-five-repositories-and-rust-go-react-split]] — Veja também: Organização dos cinco repositórios do Linkerd e divisão entre Rust, Go e React.

## Fontes
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
