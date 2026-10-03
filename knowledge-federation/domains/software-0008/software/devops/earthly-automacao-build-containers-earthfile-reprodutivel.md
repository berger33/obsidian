---
id: software.devops.tranche08.000791
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

# Earthly: framework de automação de builds baseado em containers combinando Dockerfile e Makefile

## Em uma frase
O Earthly (`earthly/earthly`, licenciado sob MPL-2.0) é um framework de automação de builds de propósito geral que utiliza containers para executar pipelines (`Earthfile`), combinando a isolamento e cache em camadas do Dockerfile com a sintaxe de alvos e dependências do Makefile.

## Por que importa
Uma das maiores frustrações em DevOps é o ciclo lento de tentar depurar um pipeline de CI/CD (` Jenkinsfile`, `.github/workflows`, `.gitlab-ci.yml`) que só roda na nuvem através de `git commit && git push`, ou ter scripts que funcionam na máquina do desenvolvedor mas falham no servidor de CI por diferenças de ambiente. Segundo o README oficial do Earthly (`Why Earthly`), os builds são autocontidos, reprodutíveis e idênticos na máquina local e em qualquer CI.

## Como funciona
Construído sobre o **BuildKit** (`moby/buildkit`), o Earthly lê um arquivo chamado **`Earthfile`** (que inicia com a declaração `VERSION 0.8` e uma imagem base global ou por alvo, como `FROM golang:1.21-alpine3.18`). Dentro do `Earthfile`, o engenheiro define receitas chamadas **targets** (como `build:`, `test:`, `docker:`) usando comandos familiares de Dockerfile (`FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `ARG`) combinados a referências de alvos estilo Makefile (`+build`, `COPY +deps/node_modules ./`). Ao executar `earthly +docker` ou `earthly +test`, o Earthly monta um grafo acíclico dirigido (DAG) de execução, roda os passos isolados em containers com paralelismo automático e cacheia cada camada inalterada.

## Exemplo
```dockerfile
# Earthfile oficial de exemplo para Go (VERSION 0.8) com targets +build e +docker
VERSION 0.8
FROM golang:1.21-alpine3.18
WORKDIR /go-example

build:
    COPY main.go .
    RUN go build -o build/go-example main.go
    SAVE ARTIFACT build/go-example AS LOCAL build/go-example

docker:
    COPY +build/go-example .
    ENTRYPOINT ["/go-example/go-example"]
    SAVE IMAGE go-example:latest
```

## Limites e trade-offs
Como todo `RUN` dentro de um `Earthfile` executa dentro de um ambiente de container isolado gerenciado pelo BuildKit, o comando não enxerga automaticamente arquivos da máquina host que não tenham sido explicitamente copiados via `COPY` (ou referenciados de outro target); copiar o diretório raiz inteiro (`COPY . .`) logo na primeira linha antes de instalar dependências invalida o cache de dependências a cada edição de código.

## Como verificar
Instale o binário `earthly` (com Docker ou Podman ativo no host) e execute `earthly github.com/earthly/hello-world+hello` para testar um build remoto reprodutível em um único comando.

## Conexões
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Veja também: Earthly: estrutura do Earthfile (VERSION 0.8, base target, indentação e invocação de targets com +).
- [[earthly-artefatos-save-artifact-as-local-save-image]] — Referência cruzada direta com earthly-artefatos-save-artifact-as-local-save-image.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
