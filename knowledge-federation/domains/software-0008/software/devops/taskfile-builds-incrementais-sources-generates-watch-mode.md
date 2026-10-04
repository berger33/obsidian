---
id: software.devops.tranche09.000875
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

# Task: checagem de arquivos atualizados (sources, generates, method: checksum/timestamp) e modo Watch (--watch)

## Em uma frase
O Task evita recompilações desnecessárias (`up-to-date checks`) monitorando padrões glob em `sources:` e `generates:` por hash de conteúdo (`method: checksum`, o padrão) ou data de modificação (`method: timestamp`), além de reexecutar tarefas automaticamente ao salvar arquivos com `task --watch`.

## Por que importa
A principal razão histórica pela qual desenvolvedores usavam o `make` era evitar recompilar alvos cujos arquivos de origem não mudaram; contudo, o `make` baseia-se apenas em timestamps (`mtime`), que falham quando se troca de branch no Git ou em clones de CI. A seção `Up-to-date checks` e `Watch mode` do guia oficial do Task resolve isso usando checksums por padrão.

## Como funciona
Quando uma tarefa declara a lista de globs de entrada em **`sources:`** (ex.: `["**/*.go", "go.mod"]`) e a lista de artefatos de saída em **`generates:`** (ex.: `["./bin/app"]`), o Task verifica antes de rodar se a tarefa já está atualizada: (1) com **`method: checksum`** (o padrão), o Task calcula um hash rápido do conteúdo de todos os arquivos em `sources` (gravado em `.task/checksum/`) e verifica se os arquivos em `generates` existem; se nada mudou, imprime `task: Task "build" is up to date` e pula a compilação; (2) com **`method: timestamp`**, compara as datas de modificação de `sources` contra `generates`; e (3) com **`task --watch build`** (`-w`), o Task permanece rodando em modo watch e reexecuta a tarefa instantaneamente toda vez que qualquer arquivo listado em `sources:` é salvo.

## Exemplo
```yaml
# Exemplo de Taskfile.yml com build incremental baseado em checksum de sources e verificação de generates
version: '3'

tasks:
  build:
    desc: Compila o binário apenas se os arquivos .go mudaram ou se bin/app não existir
    sources:
      - cmd/**/*.go
      - internal/**/*.go
      - go.mod
      - go.sum
    generates:
      - ./bin/app
    cmds:
      - go build -o ./bin/app ./cmd/app
```

## Limites e trade-offs
Como o modo padrão `method: checksum` grava os hashes calculados das últimas execuções no diretório oculto **`.task/`** na raiz do projeto, lembre-se sempre de adicionar **`.task/`** ao arquivo `.gitignore` do repositório para não comitar arquivos temporários de cache local do Task no controle de versão.

## Como verificar
Execute `task build` duas vezes seguidas sem alterar nenhum arquivo `.go` e confirme que a segunda execução retorna instantaneamente com a mensagem `Task "build" is up to date` (ou force a reexecução com `task build --force`).

## Conexões
- [[taskfile-execucao-condicional-preconditions-prompts-defer]] — Veja também: Task: execução condicional (if e preconditions), prompts de confirmação (prompt) e limpeza garantida (defer).
- [[taskfile-composicao-includes-namespaces-remote-taskfiles]] — Veja também: Task: modularização em monorepos com includes, namespaces e Remote Taskfiles (HTTP/Git com checksums).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Referência cruzada direta com taskfile-dependencias-paralelas-sequenciais-loops-matrizes.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
