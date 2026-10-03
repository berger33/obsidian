---
id: software.devops.tranche09.000872
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

# Task: variáveis dinâmicas (sh:), argumentos CLI, validação de entradas (requires) e mascaramento de segredos

## Em uma frase
O Task suporta variáveis estáticas e dinâmicas computadas por comandos shell (`sh:`), passagem de argumentos via `CLI_ARGS`, validação obrigatória de entradas/valores permitidos (`requires`) e variáveis secretas mascaradas nos logs.

## Por que importa
Em automações de DevOps (como scripts de deploy em Kubernetes, publicação de releases ou migrações de banco), executar uma tarefa quando uma variável obrigatória (`ENV` ou `VERSION`) foi esquecida ou tiver um valor inválido (ex.: `ENV=prdo` com erro de digitação) pode causar acidentes graves; além disso, chaves de API nunca devem aparecer em texto claro nos logs do CI. A seção `Variables and arguments` do guia oficial (`taskfile.dev/docs/guide`) cobre esses controles.

## Como funciona
No `Taskfile.yml`, variáveis (globais ou por tarefa) são interpoladas com templates Go `{{.NOME_VAR}}`: (1) **Variáveis dinâmicas**: declarar `GIT_COMMIT: { sh: git rev-parse --short HEAD }` executa o comando e armazena a saída na variável; (2) **Argumentos CLI**: qualquer argumento passado após `--` na linha de comando (`task test -- -v ./pkg/...`) fica disponível na variável especial **`{{.CLI_ARGS}}`**; (3) **Validação (`requires`)**: o bloco `requires: { vars: [ { name: DEPLOY_ENV, enum: [dev, staging, prod] } ] }` aborta imediatamente a tarefa antes de rodar qualquer comando se a variável estiver ausente ou fora da lista permitida; e (4) **Secrets**: permite carregar e mascarar valores sensíveis na saída de log dos comandos do Task.

## Exemplo
```yaml
# Exemplo de Taskfile.yml com variável dinâmica (sh:), validação estrita de enum (requires) e uso de CLI_ARGS
version: '3'

vars:
  GIT_SHA:
    sh: git rev-parse --short HEAD

tasks:
  deploy:
    requires:
      vars:
        - name: DEPLOY_ENV
          enum: [dev, staging, prod]
    cmds:
      - echo "Deploying commit {{.GIT_SHA}} to {{.DEPLOY_ENV}} {{.CLI_ARGS}}"
```

## Limites e trade-offs
Variáveis dinâmicas definidas com `sh:` no nível global (`vars:` no topo do `Taskfile.yml`) podem ser avaliadas na inicialização do arquivo; se um comando `sh:` for lento ou depender de uma ferramenta que só é necessária em uma tarefa específica de release, declare essa variável `sh:` apenas dentro do bloco `vars:` daquela tarefa específica para não atrasar todas as demais tarefas.

## Como verificar
Com o exemplo acima salvo no `Taskfile.yml`, execute `task deploy DEPLOY_ENV=invalido` e confirme que o Task bloqueia a execução imediatamente informando que o valor não pertence ao `enum: [dev, staging, prod]`.

## Conexões
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Veja também: Task (Taskfile.yml): task runner moderno e multiplataforma escrito em Go como alternativa ao Make.
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Veja também: Task: dependências concorrentes (deps), chamadas sequenciais (task:), controle de execução única (run: once) e Loops.
- [[taskfile-execucao-condicional-preconditions-prompts-defer]] — Referência cruzada direta com taskfile-execucao-condicional-preconditions-prompts-defer.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
