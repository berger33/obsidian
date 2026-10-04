---
id: software.devops.tranche02.000133
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

# Componentes nucleares do control plane: destination, proxy-injector e identity

## Em uma frase
A subseção `Control Plane (Go/React)` de `BUILD.md` detalha os componentes centrais do diretório `controller`: `destination` (aceita requisições das instâncias do `proxy` e serve informações de descoberta de serviços), `proxy-injector` (mutating webhook disparado na criação de pods que injeta o contêiner do proxy como sidecar) e `identity` (fornece uma autoridade certificadora — CA — para distribuir certificados aos proxies a fim de estabelecerem conexões mTLS entre si), além do utilitário de linha de comando `cli` (`linkerd`).

## Por que importa
Compreender o papel específico de cada controlador permite diagnosticar rapidamente se um problema na malha decorre de falha na injeção do pod (`proxy-injector`), na resolução de endpoints (`destination`) ou na emissão de certificados mTLS (`identity`).

## Como funciona
Monitore a saúde e os logs dos deployments de `destination`, `proxy-injector` e `identity` no namespace `linkerd` e verifique a validade da cadeia de certificados usada pelo serviço `identity`.

## Exemplo
Quando um novo pod anotado é criado no cluster, o `proxy-injector` adiciona o contêiner `linkerd-proxy`, que imediatamente solicita seu certificado mTLS ao `identity` e consulta rotas no `destination`.

## Limites e trade-offs
Se os certificados da CA do componente `identity` expirarem sem rotação, a renovação de identidades mTLS entre os proxies falhará; monitore a expiração dos certificados.

## Como verificar
Conferi a subseção Control Plane (Go/React) e o grafo de componentes em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-five-repositories-and-rust-go-react-split]] — Veja também: Organização dos cinco repositórios do Linkerd e divisão entre Rust, Go e React.
- [[linkerd-viz-extension-metrics-tap-and-web]] — Veja também: Extensão viz: metrics-api, tap, tap-injector e dashboard web.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
