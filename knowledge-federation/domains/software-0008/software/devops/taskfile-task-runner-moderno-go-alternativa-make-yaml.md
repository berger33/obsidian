---
id: software.devops.tranche09.000871
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

# Task (Taskfile.yml): task runner moderno e multiplataforma escrito em Go como alternativa ao Make

## Em uma frase
O **Task** (`go-task/task`, documentado em `taskfile.dev`) é um executor de tarefas e ferramenta de build rápida e multiplataforma escrita em Go, inspirada no GNU Make mas configurada em formato **YAML** (`Taskfile.yml`) com um interpretador shell Go nativo embutido (`mvdan/sh`).

## Por que importa
Embora o `Makefile` clássico seja onipresente em sistemas Unix, sua sintaxe exige indentação obrigatória por caracteres `TAB`, possui regras obscuras de variáveis/escapes e quebra facilmente no Windows onde o `sh`/`bash` não está disponível por padrão. Segundo o README oficial e o guia `Quick Start` (`taskfile.dev/docs/getting-started`), o Task foi projetado para workflows modernos com sintaxe YAML legível e portabilidade real entre Linux, macOS e Windows.

## Como funciona
O usuário inicializa um projeto executando **`task --init`**, que gera um arquivo **`Taskfile.yml`** com `version: '3'`, um mapa `vars:` e um mapa `tasks:`. Para executar uma tarefa, basta invocar `task <nome-da-tarefa>` (ou simplesmente `task` sem argumentos para executar a tarefa especial chamada **`default`**). Crucialmente, o Task utiliza a biblioteca **`mvdan/sh`**, um interpretador POSIX `sh`/bash nativo escrito em Go: isso permite escrever comandos estilo `sh`/`bash` em `cmds:` que rodam de forma idêntica mesmo no Windows sem precisar de Bash/WSL instalado (desde que os executáveis invocados existam como built-ins ou no `$PATH`).

## Exemplo
```yaml
# Taskfile.yml oficial do guia Quick Start definindo a versão 3, variáveis e tarefas default e build
version: '3'

vars:
  GREETING: Hello, World!

tasks:
  default:
    desc: Print a greeting message
    cmds:
      - echo "{{.GREETING}}"
    silent: true

  build:
    desc: Compile the Go binary
    cmds:
      - go build ./cmd/main.go
```

## Limites e trade-offs
Embora o interpretador embutido `mvdan/sh` do Task execute nativamente estruturas de controle de shell (`if`, `for`, pipes `|`, redirecionamentos `>`, variáveis e built-ins básicos como `echo`, `cd`, `pwd`) em qualquer SO, comandos que chamam programas externos específicos do Unix (como `sed`, `awk`, `grep` ou `tar`) ainda exigem que esses executáveis estejam instalados no `$PATH` da máquina Windows ou sejam substituídos por comandos portáveis/Go.

## Como verificar
Execute `task --init` em um diretório de teste, adicione `desc:` às tarefas e rode `task --list` (`task -l`) para listar todas as tarefas documentadas do `Taskfile.yml`.

## Conexões
- [[taskfile-variaveis-argumentos-validacao-segredos-mascarados]] — Veja também: Task: variáveis dinâmicas (sh:), argumentos CLI, validação de entradas (requires) e mascaramento de segredos.
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Referência cruzada direta com taskfile-dependencias-paralelas-sequenciais-loops-matrizes.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
