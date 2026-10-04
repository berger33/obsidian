---
id: software.devops.tranche08.000799
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

# Earthly: paralelismo automático por DAG no BuildKit, mounts de cache (--mount type=cache) e funções reutilizáveis (FUNCTION)

## Em uma frase
Apoiado no motor BuildKit da próxima geração, o Earthly executa passos independentes em paralelo automaticamente sem o usuário gerenciar locks, suporta diretórios de cache persistentes (`CACHE` / `RUN --mount=type=cache`) e permite abstrair receitas repetitivas com `FUNCTION` e `DO`.

## Por que importa
Em pipelines tradicionais ou Makefiles manuais, paralelizar tarefas sem causar condições de corrida em diretórios compartilhados é difícil, e repetir a mesma sequência de instalação/configuração em 10 targets diferentes gera duplicação de código. O README oficial e a referência do `Earthfile` detalham o paralelismo BuildKit, caches e funções.

## Como funciona
(1) **Paralelismo automático por DAG**: sempre que dois targets ou duas ramificações (`COPY +a/...` e `COPY +b/...`, ou múltiplos `BUILD +...`) não dependem sequencialmente um do outro, o BuildKit agenda e executa suas camadas concorrentemente com isolamento de filesystem; (2) **Cache Mounts (`CACHE /caminho` ou `RUN --mount=type=cache,target=/root/.cache/go-build`)**: preserva diretórios de cache de compiladores e gerenciadores de pacotes entre execuções sucessivas mesmo quando uma camada anterior foi invalidada por mudança de código; e (3) **Funções (`FUNCTION` / `COMMAND` e `DO`)**: permite definir um bloco parametrizado reutilizável (`MINHA_FUNCAO: FUNCTION ...`) e invocá-lo em qualquer target (local ou importado via `IMPORT`) usando `DO +MINHA_FUNCAO --ARG1=valor`.

## Exemplo
```dockerfile
# Exemplo de uso de FUNCTION parametrizada invocada com DO e mount de cache de compilação no Earthfile
VERSION 0.8

GO_BUILD:
    FUNCTION
    ARG --required pkg
    ARG output
    RUN --mount=type=cache,target=/root/.cache/go-build go build -o ${output} ${pkg}

build-api:
    FROM golang:1.21-alpine3.18
    WORKDIR /app
    COPY . .
    DO +GO_BUILD --pkg=./cmd/api --output=bin/api
    SAVE ARTIFACT bin/api
```

## Limites e trade-offs
Diretórios montados via `RUN --mount=type=cache,target=...` (ou instrução `CACHE`) persistem no volume de cache do daemon BuildKit durante os passos `RUN`, mas **não** são incluídos na imagem final exportada por `SAVE IMAGE` (exceto se configurado o modo específico da instrução `CACHE`); portanto, nunca grave o binário final da aplicação dentro do diretório montado como `type=cache`, copiando-o sempre para o `WORKDIR` normal antes de `SAVE ARTIFACT`.

## Como verificar
Altere uma linha em `main.go` e reexecute `earthly +build-api` para verificar que o cache de compilação em `/root/.cache/go-build` acelera a recompilação incremental.

## Conexões
- [[earthly-integracao-docker-in-docker-with-docker-testes]] — Veja também: Earthly: testes de integração com containers e Docker Compose dentro do build usando WITH DOCKER.
- [[earthly-integracao-qualquer-ci-github-actions-gitlab-jenkins]] — Veja também: Earthly: camada agnóstica sobre qualquer CI (GitHub Actions, GitLab CI, CircleCI, Jenkins, Tekton) e modo interativo de debug (-i).
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.
- [[earthly-sintaxe-earthfile-targets-dependencias-build]] — Referência cruzada direta com earthly-sintaxe-earthfile-targets-dependencias-build.

## Fontes
- [Earthly GitHub — README.md (Containerized Build Framework, Earthfile Examples, Cross-Directory Imports, Multi-Platform & Secrets)](https://raw.githubusercontent.com/earthly/earthly/main/README.md) — README oficial do Earthly (MPL-2.0) demonstrando sintaxe Earthfile VERSION 0.8, SAVE ARTIFACT AS LOCAL, SAVE IMAGE, FROM DOCKERFILE, imports entre diretórios/repositórios, builds multiplataforma e RUN --push --secret; consultado em 2026-10-03.
- [Earthly Official Documentation — Earthfile Reference](https://docs.earthly.dev/docs/earthfile) — Referência técnica oficial da gramática do Earthfile, base target, invocação de targets (+), WITH DOCKER, CACHE e FUNCTION; consultado em 2026-10-03.
- [Earthly — Official GitHub Repository](https://github.com/earthly/earthly) — Repositório oficial MPL-2.0 do Earthly; consultado em 2026-10-03.
