---
id: software.devops.tranche04.000360
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

# Construção de imagens multi-plataforma e rastreamento distribuído com OpenTelemetry no BuildKit

## Em uma frase
O README oficial do BuildKit destaca suporte nativo à **construção de imagens multi-plataforma** (`docs/multi-platform.md`, gerando manifest lists / OCI image indexes para arquiteturas como `linux/amd64` e `linux/arm64` via cross-compilation no grafo LLB, QEMU ou workers distribuídos) e suporte integrado a **OpenTelemetry** para exportar traces e métricas detalhadas de cada etapa do build.

## Por que importa
Equipes de plataforma precisam produzir imagens multi-arquitetura (`amd64` + `arm64`) em um único build e, ao mesmo tempo, medir onde estão os gargalos de tempo (download de imagem base, compilação, compressão de camadas ou push para o registro) através de traces OpenTelemetry.

## Como funciona
Utilize estágios com `$BUILDPLATFORM` e `$TARGETPLATFORM` para cross-compilation nativa rápida no BuildKit e configure o exportador OpenTelemetry do `buildctl`/`buildkitd` para enviar spans de build ao coletor de observabilidade da engenharia de plataforma.

## Exemplo
Ao instrumentar os runners de CI com OpenTelemetry no BuildKit, a equipe visualiza no Jaeger/Tempo que 60% do tempo de um build multi-plataforma estava concentrado em uma etapa emulada via QEMU e refatora o Dockerfile para usar cross-compilation nativa com `--platform=$BUILDPLATFORM`.

## Limites e trade-offs
Prefira cross-compilation nativa (`FROM --platform=$BUILDPLATFORM`) em linguagens como Go e Rust em vez de emular toda a compilação pesada via QEMU para `arm64`, o que reduz drasticamente o tempo de CPU do build.

## Como verificar
Verifique o manifesto multi-arquitetura publicado no registro OCI confirmando as entradas para todas as plataformas-alvo e inspecione os spans gerados no coletor OpenTelemetry.

## Conexões
- [[buildkit-rootless-execution-and-containerized-kubernetes-deployments]] — Veja também: Execução rootless do BuildKit sem privilégios de root e implantação em Kubernetes.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.
