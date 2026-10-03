---
id: software.devops.tranche09.000880
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

# Task: motor de templates Go/slim-sprig embutido (OS, ARCH, joinPath) e instalação em pipelines de CI/CD

## Em uma frase
O Task incorpora o motor de templates do Go enriquecido com funções utilitárias (`OS`, `ARCH`, `joinPath`, `fromSlash`, manipulação de strings/listas/JSON) e instala-se em segundos como um binário único em qualquer plataforma ou CI (`go install`, Homebrew, Snap, npm ou script oficial).

## Por que importa
Em scripts multiplataforma, concatenar caminhos de diretórios com `/` fixo ou tentar descobrir no YAML se a máquina atual é `arm64` ou `amd64` geralmente exige chamar subprocessos externos (`uname -m`); o motor de templates do Task resolve tudo isso nativamente em memória durante a avaliação do `Taskfile.yml`.

## Como funciona
Dentro de qualquer expressão `{{ ... }}` no `Taskfile.yml`, o Task disponibiliza constantes e funções nativas de template: (1) **Constantes de sistema**: `{{OS}}` (retorna `linux`, `darwin`, `windows`), `{{ARCH}}` (retorna `amd64`, `arm64`, etc.), `{{.TASKFILE_DIR}}` e `{{.ROOT_DIR}}`; (2) **Funções de caminho e texto**: `{{joinPath .ROOT_DIR "bin" "app"}}`, `{{exeExt}}` (retorna `.exe` no Windows e vazio no Linux/macOS), `upper`, `lower`, `trim`, `split`, `toJson`, `fromJson`; e (3) **Instalação universal**: como é um único binário Go sem dependências de runtime, pode ser instalado via `brew install go-task`, `npm install -g @go-task/cli`, `go install github.com/go-task/task/v3/cmd/task@latest` ou `sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin`.

## Exemplo
```yaml
# Exemplo de Taskfile.yml usando constantes nativas {{OS}}, {{ARCH}} e {{exeExt}} para compilar binários portáveis
version: '3'

tasks:
  build-native:
    desc: Compila o binário nativo para o SO e arquitetura atuais
    cmds:
      - go build -o bin/app-{{OS}}-{{ARCH}}{{exeExt}} ./cmd/app
```

## Limites e trade-offs
Quando um comando dentro de `cmds:` precisa passar uma sintaxe que usa chaves duplas `{{ ... }}` para **outra** ferramenta (como `kubectl get pods -o go-template='{{.items}}'` ou `docker inspect --format '{{.Id}}'`), o motor de templates do Task tentará interpretar `{{.Id}}` como uma variável do Taskfile e falhará; para escapar chaves duplas no `Taskfile.yml`, envolva a string literal como **`{{`{{.Id}}`}}`**.

## Como verificar
Execute `task --version` e teste uma tarefa com `echo "Sistema={{OS}} Arquitetura={{ARCH}}"` para verificar a avaliação nativa das funções de template do Task.

## Conexões
- [[taskfile-aliases-wildcard-tasks-internal-silent-desc]] — Veja também: Task: definição avançada de tarefas (aliases, internal, silent, labels dinâmicas e captura de wildcards *).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-variaveis-argumentos-validacao-segredos-mascarados]] — Referência cruzada direta com taskfile-variaveis-argumentos-validacao-segredos-mascarados.
- [[taskfile-ambientes-dotenv-plataformas-shells-output]] — Referência cruzada direta com taskfile-ambientes-dotenv-plataformas-shells-output.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
