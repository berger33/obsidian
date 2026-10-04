---
id: software.devops.tranche08.000796
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/earthly/earthly/main/README.md", "https://docs.earthly.dev/docs/earthfile", "https://github.com/earthly/earthly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Earthly: builds e imagens multiplataforma (linux/amd64 e linux/arm64) em um único comando BUILD --platform

## Em uma frase
O Earthly permite compilar binários e publicar manifest lists de imagens multi-arquitetura (`linux/amd64`, `linux/arm64`, `linux/arm/v7`) sem alterar o target de build, simplesmente invocando `BUILD --platform=linux/amd64 --platform=linux/arm64 +docker`.

## Por que importa
Com a adoção generalizada de processadores ARM64 tanto em estações de trabalho (Apple Silicon M1/M2/M3/M4) quanto em servidores de nuvem (AWS Graviton, Ampere Altra), publicar imagens de container multiplataforma tornou-se obrigatório para equipes de DevOps. A seção `Multi-Platform Builds` do README oficial do Earthly demonstra como fazer isso de forma declarativa.

## Como funciona
Em um `Earthfile`, um target agregador (como `all:`) pode invocar outro target passando múltiplas flags `--platform`: por exemplo, `BUILD --platform=linux/amd64 --platform=linux/arm64 +build`. O Earthly instancia execuções paralelas do target `+build` para cada arquitetura solicitada (utilizando execução nativa ou emulação QEMU transparente configurada no container BuildKit do Earthly, além de expor argumentos embutidos como `TARGETARCH`, `TARGETOS`, `TARGETPLATFORM` e `USERARCH` para cross-compilation rápida em Go/Rust). Se o target invocado contiver `SAVE IMAGE minha-img:latest`, o Earthly combina automaticamente todas as arquiteturas em uma única **manifest list** multi-arch sob a tag `minha-img:latest`.

## Exemplo
```dockerfile
# Exemplo oficial do README construindo imagens multi-arch para linux/amd64 e linux/arm64 em paralelo
VERSION 0.8
FROM golang:1.21-alpine3.18
WORKDIR /go-example

all:
    BUILD --platform=linux/amd64 --platform=linux/arm64 +build

build:
    COPY main.go .
    RUN go build -o build/multiarch-service ./cmd/server
    ENTRYPOINT ["/go-example/build/multiarch-service"]
    SAVE IMAGE --push user/go-example:latest
```

## Limites e trade-offs
Compilar código pesado dentro de emulação QEMU (por exemplo, rodar o compilador `amd64` ou `arm64` emulado via binfmt_misc) é funcionalmente simples mas muito mais lento que compilação nativa; para linguagens que suportam cross-compilation nativa (como Go e Rust), é muito mais rápido fixar o container de compilação na arquitetura nativa do host (`FROM --platform=$USERPLATFORM golang:1.21-alpine`) e passar `GOOS=$TARGETOS GOARCH=$TARGETARCH go build`.

## Como verificar
Execute `earthly +all` (ou inspecione com `docker buildx imagetools inspect` após `--push`) para confirmar que o manifesto publicado contém os descritores tanto para `linux/amd64` quanto para `linux/arm64`.

## Conexões
- [[earthly-reutilizacao-dockerfiles-existentes-from-dockerfile]] — Veja também: Earthly: adoção incremental e reutilização de Dockerfiles existentes com FROM DOCKERFILE.
- [[earthly-gerenciamento-segredos-run-secret-push-seguranca]] — Veja também: Earthly: injeção segura de segredos em tempo de build (RUN --secret) e publicação condicional (RUN --push).
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Referência cruzada direta com earthly-sintaxe-earthfile-targets-dependencias-build.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
