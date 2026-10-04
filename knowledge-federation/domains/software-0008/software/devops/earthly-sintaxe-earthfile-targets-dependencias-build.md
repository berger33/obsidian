---
id: software.devops.tranche08.000792
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

# Earthly: estrutura do Earthfile (VERSION 0.8, base target, indentação e invocação de targets com +)

## Em uma frase
A gramática do `Earthfile` (`docs.earthly.dev/docs/earthfile`) exige iniciar com `VERSION 0.8`, utiliza os comandos antes do primeiro target como **base target** implícito (`base:`) e identifica invocações de targets pelo prefixo `+` (ex.: `BUILD +build`, `COPY +build/artefato`).

## Por que importa
Diferentemente de um `Dockerfile` tradicional (onde mesmo multi-stage builds são pensados primariamente para produzir uma única imagem de container no final), um `Earthfile` modela todo o ciclo de engenharia — geração de código (`+proto`), linting (`+lint`), testes unitários (`+test`), binários locais (`+build`) e imagens (`+docker`) — como funções modulares que se invocam mutuamente. A referência oficial do `Earthfile` documenta suas regras sintáticas.

## Como funciona
Todo `Earthfile` começa obrigatoriamente com `VERSION 0.8`. Os comandos colocados logo após o `VERSION` e antes da declaração do primeiro `<target>:` constituem a receita do target implícito **`base`**: todos os demais targets definidos no arquivo que não começarem com seu próprio `FROM` herdam automaticamente o estado final do target `base` (por exemplo, `FROM golang:1.21-alpine3.18` e `WORKDIR /app`). O corpo de cada target (`meu-target:`) é delimitado por indentação (4 espaços). Para acionar outros targets como dependências no grafo de build (como um target agregador `all:` que roda build e testes em paralelo), utiliza-se o comando **`BUILD +<target>`**.

## Exemplo
```dockerfile
# Earthfile com target agregador 'all:' disparando +lint, +test e +docker em paralelo no grafo BuildKit
VERSION 0.8
FROM node:20-alpine
WORKDIR /app

deps:
    COPY package.json package-lock.json ./
    RUN npm ci

lint:
    FROM +deps
    COPY src ./src
    RUN npm run lint

test:
    FROM +deps
    COPY src ./src
    RUN npm test

all:
    BUILD +lint
    BUILD +test
```

## Limites e trade-offs
Quando um target usa `FROM +deps`, ele herda todo o sistema de arquivos, variáveis de ambiente (`ENV`) e diretório de trabalho (`WORKDIR`) produzidos por `+deps`; já quando um target usa apenas `BUILD +lint`, ele garante que `+lint` seja executado no grafo de build, mas não importa os arquivos de `+lint` para o target atual (para importar apenas um arquivo específico sem herdar a imagem inteira, usa-se `COPY +target/arquivo ./`).

## Como verificar
Execute `earthly +all` no diretório contendo o `Earthfile` e observe nos logs com prefixo de cor por target que `+lint` e `+test` reutilizam o cache de `+deps` e rodam concorrentemente.

## Conexões
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Veja também: Earthly: framework de automação de builds baseado em containers combinando Dockerfile e Makefile.
- [[earthly-artefatos-save-artifact-as-local-save-image]] — Veja também: Earthly: exportação de artefatos entre targets e para o host (SAVE ARTIFACT ... AS LOCAL) e imagens (SAVE IMAGE).
- [[earthly-execucao-paralela-dag-buildkit-cache-camadas]] — Referência cruzada direta com earthly-execucao-paralela-dag-buildkit-cache-camadas.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
