---
id: software.devops.tranche09.000873
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/go-task/task/main/README.md", "https://taskfile.dev/docs/getting-started", "https://taskfile.dev/docs/guide"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Task: dependências concorrentes (deps), chamadas sequenciais (task:), controle de execução única (run: once) e Loops

## Em uma frase
No Task, dependências declaradas na lista `deps:` de uma tarefa rodam **concorrentemente em paralelo** por padrão, enquanto chamadas `task:` dentro de `cmds:` rodam **em sequência**, contando ainda com deduplicação (`run: once`/`when_changed`) e **Loops** (`for:`) sobre listas, arquivos e matrizes.

## Por que importa
Em um pipeline local de qualidade, tarefas independentes como `lint-go`, `lint-yaml` e `unit-test` devem rodar em paralelo usando todos os cores da CPU para terminar rápido (`deps:`), enquanto `build` -> `docker-build` -> `deploy` precisam rodar estritamente uma após a outra (`cmds:`). A seção `Task execution` do guia oficial (`taskfile.dev/docs/guide`) documenta `deps`, `cmds`, `run` e `for`.

## Como funciona
(1) **Paralelismo (`deps:`)**: todas as tarefas listadas em `deps: [lint, test]` iniciam simultaneamente em goroutines paralelas antes dos comandos de `cmds:` da tarefa pai (podendo limitar o paralelismo global com `--concurrency` / `-C`); (2) **Sequência (`cmds:`)**: invocar `- task: build` seguido de `- task: package` dentro de `cmds:` executa a segunda somente após a primeira terminar com sucesso; (3) **Deduplicação (`run:`)**: configurar `run: once` (ou `run: when_changed` quando chamada com `vars` diferentes) garante que uma tarefa base compartilhada (como `install-deps`) rode apenas uma vez no mesmo fluxo; e (4) **Loops (`for:`)**: permite repetir um comando ou chamada de tarefa iterando sobre um array de valores, sobre as `sources` da tarefa ou sobre uma matriz combinatória (`matrix:`), acessando o item atual via **`{{.ITEM}}`**.

## Exemplo
```yaml
# Exemplo de Taskfile.yml combinando deps em paralelo, run: once e loop em matriz multiplataforma (GOOS/GOARCH)
version: '3'

tasks:
  generate:
    run: once
    cmds:
      - go generate ./...

  build-all:
    deps: [generate]
    cmds:
      - for:
          matrix:
            OS: [linux, darwin]
            ARCH: [amd64, arm64]
        cmd: GOOS={{.ITEM.OS}} GOARCH={{.ITEM.ARCH}} go build -o dist/app-{{.ITEM.OS}}-{{.ITEM.ARCH}} ./cmd/app
```

## Limites e trade-offs
Como todas as tarefas listadas em `deps:` executam em paralelo ao mesmo tempo, nunca coloque em `deps:` duas tarefas que escrevem ou apagam o mesmo diretório temporário simultaneamente (por exemplo, `deps: [clean, build]`, onde `clean` pode apagar arquivos enquanto `build` já começou a compilar!); tarefas com ordem obrigatória devem sempre ser encadeadas em `cmds:` com `- task: clean` seguido de `- task: build`.

## Como verificar
Execute `task build-all --dry` (modo dry-run) para pré-visualizar todas as combinações expandidas pelo loop de matriz sem executar a compilação real.

## Conexões
- [[taskfile-variaveis-argumentos-validacao-segredos-mascarados]] — Veja também: Task: variáveis dinâmicas (sh:), argumentos CLI, validação de entradas (requires) e mascaramento de segredos.
- [[taskfile-execucao-condicional-preconditions-prompts-defer]] — Veja também: Task: execução condicional (if e preconditions), prompts de confirmação (prompt) e limpeza garantida (defer).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-builds-incrementais-sources-generates-watch-mode]] — Referência cruzada direta com taskfile-builds-incrementais-sources-generates-watch-mode.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
