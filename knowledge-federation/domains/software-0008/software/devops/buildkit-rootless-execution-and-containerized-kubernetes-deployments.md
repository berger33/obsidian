---
id: software.devops.tranche04.000359
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/moby/buildkit/master/README.md", "https://pkg.go.dev/github.com/moby/buildkit/client/llb", "https://github.com/moby/buildkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução rootless do BuildKit sem privilégios de root e implantação em Kubernetes

## Em uma frase
O BuildKit foi projetado desde a origem para permitir **execução sem privilégios de root** (`docs/rootless.md`, usando `rootlesskit` e user namespaces) e containerização nativa em **Podman, Nerdctl, Kubernetes** (`examples/kubernetes`) e modo **daemonless** (onde um único comando inicia o `buildkitd` efêmero e executa o `buildctl`).

## Por que importa
Executar builds de contêineres com privilégios de `root` no host ou montando `/var/run/docker.sock` em runners compartilhados de CI equivale a conceder acesso root irrestrito no nó hospedeiro a qualquer repositório que execute um pipeline.

## Como funciona
Em clusters Kubernetes de CI/CD (como Tekton Pipelines, GitHub Actions Runner Controller ou GitLab Kubernetes Executor), utilize a imagem rootless oficial do BuildKit (`moby/buildkit:rootless`) e siga os manifestos de `examples/kubernetes` sem conceder root no nó.

## Exemplo
Uma plataforma multi-tenant de CI migra seus jobs de build de Docker-in-Docker privilegiado para pods baseados em `moby/buildkit:rootless`, permitindo que equipes construam imagens OCI com segurança em um cluster compartilhado.

## Limites e trade-offs
Verifique que o kernel dos nós Kubernetes suporta user namespaces desprivilegiados e ajuste os perfis AppArmor/Seccomp conforme documentado em `docs/rootless.md` e `examples/kubernetes`.

## Como verificar
Inspecione o contexto de segurança do pod/processo `buildkitd` rootless e confirme a execução sob UID não-root capaz de construir e enviar uma imagem para o registro.

## Conexões
- [[buildkit-automatic-garbage-collection-and-storage-management]] — Veja também: Coleta de lixo automática (automatic garbage collection) do cache interno no BuildKit.
- [[buildkit-multi-platform-builds-and-opentelemetry-tracing]] — Veja também: Construção de imagens multi-plataforma e rastreamento distribuído com OpenTelemetry no BuildKit.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.
