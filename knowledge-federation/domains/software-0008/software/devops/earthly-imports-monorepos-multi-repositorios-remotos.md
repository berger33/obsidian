---
id: software.devops.tranche08.000794
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

# Earthly: composição de builds em monorepos e entre múltiplos repositórios Git remotos

## Em uma frase
O Earthly permite referenciar targets, imagens e artefatos de outros diretórios locais (`./subpasta+target`) ou diretamente de repositórios Git remotos (`github.com/org/repo:tag+target`), resolvendo builds complexos de monorepos e polyrepos sem scripts de cola.

## Por que importa
Em arquiteturas de microsserviços (monorepos ou múltiplos repositórios Git), um serviço em Go e um cliente em Python frequentemente precisam importar definições Protobuf ou bibliotecas compartilhadas de outro diretório ou repositório. Conforme destaca a seção `Highlights` do README oficial do Earthly, referenciar targets através de diretórios e repositórios é uma capacidade nativa da sintaxe do Earthfile.

## Como funciona
A referência a um target no Earthly segue o formato `<caminho-ou-repo>+<target>`: (1) **Mesmo Earthfile**: `+build`; (2) **Outro diretório local (Monorepo)**: `./services/auth+docker` ou `../proto+pb-go`; e (3) **Repositório Git remoto (Polyrepo)**: `github.com/org/proto-definitions:v1.2.0+pb-go`. Além disso, a instrução **`IMPORT`** no topo do `Earthfile` permite criar um alias curto (ex.: `IMPORT github.com/earthly/lib/rust:3.0.1 AS rust` ou `IMPORT ./proto`) para invocar targets e funções (`COPY proto+pb-py/pb-py ./pb`) de forma limpa e legível, onde o Earthly clona e cacheia repositórios remotos automaticamente dentro do BuildKit.

## Exemplo
```dockerfile
# Exemplo do README oficial do Earthly importando definições Protobuf compiladas de outro diretório (./proto+pb-py)
VERSION 0.8
FROM python:3.8-alpine3.12
WORKDIR /code
build:
    COPY ./proto+pb-py/pb-py ./pb
    COPY main.py ./
```

## Limites e trade-offs
Ao importar targets de repositórios Git remotos em pipelines de produção (`github.com/org/repo:ref+target`), fixe sempre uma tag imutável ou hash de commit (`:v1.2.0` ou `:a1b2c3d`) em vez de apontar para `:main`, garantindo que mudanças externas no repositório remoto não alterem nem quebrem silenciosamente o seu build.

## Como verificar
Execute `earthly github.com/earthly/hello-world+hello` para verificar como o Earthly resolve, clona no cache isolado e executa um target de um repositório Git remoto sem precisar de `git clone` prévio no host.

## Conexões
- [[earthly-artefatos-save-artifact-as-local-save-image]] — Veja também: Earthly: exportação de artefatos entre targets e para o host (SAVE ARTIFACT ... AS LOCAL) e imagens (SAVE IMAGE).
- [[earthly-reutilizacao-dockerfiles-existentes-from-dockerfile]] — Veja também: Earthly: adoção incremental e reutilização de Dockerfiles existentes com FROM DOCKERFILE.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Referência cruzada direta com earthly-sintaxe-earthfile-targets-dependencias-build.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
