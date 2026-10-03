---
id: software.devops.tranche09.000879
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

# Task: definição avançada de tarefas (aliases, internal, silent, labels dinâmicas e captura de wildcards *)

## Em uma frase
Na definição de tarefas do `Taskfile.yml`, é possível criar atalhos curtos (`aliases:`), ocultar tarefas auxiliares da listagem/CLI (`internal: true`), suprimir o eco dos comandos (`silent: true`) e capturar parâmetros diretamente no nome da tarefa com wildcards (`start:*` -> `{{index .MATCH 0}}`).

## Por que importa
Em um `Taskfile.yml` grande com 40 tarefas (onde 25 são sub-tarefas internas auxiliares chamadas apenas por outras tarefas), rodar `task --list` sem filtrar tarefas internas polui a ajuda para o usuário; ao mesmo tempo, tarefas frequentes merecem atalhos de 1 ou 2 letras (`task b` para `task build`, `task t` para `task test`) e padrões dinâmicos como `task deploy:staging`. A seção `Defining tasks` e `Command-line arguments` do guia oficial cobre esses recursos.

## Como funciona
Dentro da declaração de uma tarefa em `tasks:`: (1) **`desc:`** e **`summary:`**: definem a descrição curta (exibida em `task --list`) e o texto longo de ajuda (exibido em `task --summary <task>`); (2) **`aliases: [b, compile]`**: permite invocar a tarefa tanto pelo nome completo quanto pelos apelidos curtos; (3) **`internal: true`**: impede que o usuário invoque a tarefa diretamente na linha de comando e a oculta da listagem, restringindo seu uso a chamadas internas via `deps:` ou `task:`; (4) **`silent: true`**: faz o Task imprimir apenas a saída (`stdout`/`stderr`) do programa executado, sem imprimir o comando em si; e (5) **Wildcards (`*`)**: uma tarefa nomeada `run:*:` casa com `task run:api` e expõe o valor capturado no array **`{{index .MATCH 0}}`**.

## Exemplo
```yaml
# Exemplo de Taskfile.yml usando aliases, internal: true, silent: true e captura de wildcard (*) no nome da tarefa
version: '3'

tasks:
  _check-env:
    internal: true
    silent: true
    cmds:
      - test -n "$KUBECONFIG"

  logs:*:
    desc: Exibe os logs de um deployment específico (ex. task logs:api)
    deps: [_check-env]
    cmds:
      - kubectl logs -l app={{index .MATCH 0}} --tail=100
```

## Limites e trade-offs
Por padrão, o comando `task --list` (`task -l`) exibe **apenas** as tarefas que possuem o atributo `desc:` preenchido (tratando tarefas sem `desc:` como não documentadas); se você quiser listar absolutamente todas as tarefas do arquivo mesmo aquelas nas quais esqueceu de colocar `desc:`, deve usar **`task --list-all`** (`task -a`).

## Como verificar
Adicione `aliases: [t]` e `desc: Run unit tests` a uma tarefa `test:` no `Taskfile.yml` e execute `task -l` e `task t` para confirmar o funcionamento do alias e da listagem.

## Conexões
- [[taskfile-execucao-diretorios-subpastas-flags-cli-taskfile]] — Veja também: Task: descoberta automática de arquivos Taskfile, execução a partir de subdiretórios (--dir, --taskfile, --global).
- [[taskfile-templating-sprig-funcoes-instalacao-cicd]] — Veja também: Task: motor de templates Go/slim-sprig embutido (OS, ARCH, joinPath) e instalação em pipelines de CI/CD.
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-variaveis-argumentos-validacao-segredos-mascarados]] — Referência cruzada direta com taskfile-variaveis-argumentos-validacao-segredos-mascarados.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
