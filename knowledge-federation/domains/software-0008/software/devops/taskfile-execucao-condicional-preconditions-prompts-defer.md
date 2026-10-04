---
id: software.devops.tranche09.000874
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

# Task: execução condicional (if e preconditions), prompts de confirmação (prompt) e limpeza garantida (defer)

## Em uma frase
O Task oferece controle fino do fluxo de execução por meio de `preconditions` (que validam pré-requisitos com mensagens de erro claras), `if` (que pula tarefas opcionais), `prompt` (que exige confirmação humana antes de tarefas perigosas) e `defer` (que garante limpeza mesmo em caso de erro).

## Por que importa
Scripts de automação costumam falhar no meio do caminho porque o usuário esqueceu de ligar o Docker ou criar um arquivo `.env`, deixando containers temporários ou arquivos sujos para trás; além disso, tarefas destrutivas (como `terraform destroy` ou `db-reset`) precisam pedir confirmação explícita antes de rodar. A seção `Conditional execution` e `Errors and cleanup` do guia oficial (`taskfile.dev/docs/guide`) detalha esses quatro mecanismos.

## Como funciona
(1) **`preconditions:`**: lista de comandos (`sh: test -f .env` ou `sh: docker info`) com mensagem customizada `msg: "O arquivo .env não existe!"`; se qualquer pré-condição retornar código diferente de zero, o Task falha imediatamente exibindo `msg`; (2) **`if:`** (ou `status:`): permite pular silenciosamente um passo ou tarefa quando uma condição não se aplica; (3) **`prompt:`**: exibe uma pergunta interativa no terminal (ex.: `prompt: "Tem certeza que deseja aplicar no cluster de PRODUÇÃO?"`) e só prossegue se o operador confirmar (`y`/`yes`, ou se `--yes` for passado em CI); e (4) **`defer:`**: dentro de `cmds:`, declarar `- defer: rm -rf ./tmp-build` ou `- defer: { task: stop-test-db }` agenda o comando para rodar ao final da tarefa **mesmo que um comando anterior falhe** (análogo ao `defer` da linguagem Go ou `trap ... EXIT` no bash).

## Exemplo
```yaml
# Exemplo de Taskfile.yml usando preconditions, prompt de confirmação e defer para limpeza garantida
version: '3'

tasks:
  integration-test:
    preconditions:
      - sh: docker info > /dev/null 2>&1
        msg: "Erro: o daemon Docker precisa estar em execução para rodar os testes de integração."
    cmds:
      - docker run -d --name pg-test-tmp -e POSTGRES_PASSWORD=test postgres:16-alpine
      - defer: docker rm -f pg-test-tmp
      - go test -v ./internal/db/...
```

## Limites e trade-offs
Quando você adiciona `prompt:` a uma tarefa que também será executada em pipelines não-interativos de CI/CD, o job de CI travará ou abortará aguardando entrada de teclado a menos que o comando no servidor de CI passe explicitamente a flag **`--yes`** (`-y`) para auto-confirmar os prompts.

## Como verificar
Pare o serviço Docker (ou teste com um arquivo inexistente em `preconditions`) e execute `task integration-test` para confirmar que a mensagem amigável de `msg:` é exibida antes de qualquer comando de `cmds:` iniciar.

## Conexões
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Veja também: Task: dependências concorrentes (deps), chamadas sequenciais (task:), controle de execução única (run: once) e Loops.
- [[taskfile-builds-incrementais-sources-generates-watch-mode]] — Veja também: Task: checagem de arquivos atualizados (sources, generates, method: checksum/timestamp) e modo Watch (--watch).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
