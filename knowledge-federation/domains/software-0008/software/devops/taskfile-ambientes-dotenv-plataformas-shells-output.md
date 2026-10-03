---
id: software.devops.tranche09.000877
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

# Task: carregamento de arquivos .env (dotenv), filtragem por plataforma (platforms) e modos de saída (output)

## Em uma frase
O Task suporta injeção de variáveis de ambiente (`env:`), carregamento nativo de múltiplos arquivos `.env` (`dotenv:`), restrição de tarefas ou comandos a sistemas operacionais/arquiteturas específicas (`platforms:`) e controle do formato de log de tarefas paralelas (`output: interleaved|group|prefixed`).

## Por que importa
Ao rodar tarefas em paralelo (`deps:`) em CI ou localmente, os logs de múltiplos processos se misturam de forma ilegível se não forem agrupados ou prefixados; além disso, projetos frequentemente precisam carregar `.env.local` + `.env` automaticamente e rodar comandos específicos apenas em `linux` ou `darwin/arm64`. A seção `Environment and output` do guia oficial (`taskfile.dev/docs/guide`) documenta esses recursos.

## Como funciona
(1) **`env:` e `dotenv:`**: a lista `dotenv: ['.env.local', '.env']` (global ou por tarefa) lê arquivos `.env` na ordem declarada sem precisar de ferramentas externas como `direnv` ou `dotenv-cli`; (2) **`platforms:`**: pode ser adicionado a uma tarefa inteira ou a um comando individual dentro de `cmds:` (ex.: `platforms: [linux, darwin]` ou `platforms: [linux/amd64]`), pulando automaticamente o comando quando o SO/arquitetura atual não corresponde; e (3) **`output:`**: controla como os logs de tarefas concorrentes são exibidos — **`interleaved`** (padrão, imprime linha a linha em tempo real), **`group`** (acumula e imprime a saída de cada tarefa em bloco fechado ao terminar, com suporte a grupos retráteis em logs do GitHub Actions/GitLab CI) ou **`prefixed`** (adiciona o prefixo `[nome-da-tarefa]` em cada linha).

## Exemplo
```yaml
# Exemplo de Taskfile.yml carregando .env, prefixando logs paralelos e filtrando comandos por plataforma
version: '3'

output: prefixed
dotenv: ['.env']

tasks:
  setup-os:
    cmds:
      - cmd: sudo apt-get update
        platforms: [linux/amd64, linux/arm64]
      - cmd: brew update
        platforms: [darwin]
```

## Limites e trade-offs
Variáveis que já existem no ambiente do sistema operacional (ou na seção `env:` do `Taskfile.yml`) têm precedência sobre valores lidos dos arquivos listados em `dotenv:`; da mesma forma, na lista `dotenv: ['.env.local', '.env']`, o primeiro arquivo que define uma chave vence, portanto coloque sempre o arquivo mais específico (`.env.local`) **antes** do arquivo genérico (`.env`).

## Como verificar
Execute duas tarefas em paralelo (`deps:`) com `output: prefixed` (ou `output: group`) configurado no topo do `Taskfile.yml` e confirme a separação clara da saída de cada tarefa no terminal.

## Conexões
- [[taskfile-composicao-includes-namespaces-remote-taskfiles]] — Veja também: Task: modularização em monorepos com includes, namespaces e Remote Taskfiles (HTTP/Git com checksums).
- [[taskfile-execucao-diretorios-subpastas-flags-cli-taskfile]] — Veja também: Task: descoberta automática de arquivos Taskfile, execução a partir de subdiretórios (--dir, --taskfile, --global).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-variaveis-argumentos-validacao-segredos-mascarados]] — Referência cruzada direta com taskfile-variaveis-argumentos-validacao-segredos-mascarados.
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Referência cruzada direta com taskfile-dependencias-paralelas-sequenciais-loops-matrizes.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
