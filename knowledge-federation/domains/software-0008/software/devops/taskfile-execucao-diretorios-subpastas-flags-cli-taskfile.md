---
id: software.devops.tranche09.000878
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

# Task: descoberta automática de arquivos Taskfile, execução a partir de subdiretórios (--dir, --taskfile, --global)

## Em uma frase
O Task procura automaticamente por `Taskfile.yml` (e variações suportadas como `Taskfile.yaml`, `Taskfile.dist.yml`) e permite executar tarefas de outros diretórios (`--dir`), de arquivos com nomes customizados (`--taskfile`) ou de um Taskfile global do usuário (`--global` em `~/Taskfile.yml`).

## Por que importa
Desenvolvedores frequentemente estão navegando dentro de uma subpasta profunda do projeto (`src/internal/handlers/`) ou querem manter um `Taskfile.local.yml` pessoal sem comitá-lo no Git sobrepondo o `Taskfile.dist.yml` da equipe, além de executar utilitários pessoais globais de qualquer lugar do terminal. O guia oficial `Quick Start` e `Running tasks` documenta essas opções.

## Como funciona
Conforme demonstra o `Quick Start` (`taskfile.dev/docs/getting-started`), `task --init ./subdirectory` ou `task --init Custom.yml` cria o arquivo no destino desejado, e na execução: (1) **`task --dir ./subdirectory <tarefa>`** (`-d`) muda o diretório de trabalho para `./subdirectory` antes de procurar e executar o `Taskfile.yml`; (2) **`task --taskfile Custom.yml <tarefa>`** (`-t`) executa um arquivo com nome customizado; (3) se o comando `task` for rodado dentro de uma subpasta que não tem `Taskfile.yml`, ele sobe a árvore de diretórios pais procurando o `Taskfile.yml` da raiz do repositório; e (4) **`task --global <tarefa>`** (`-g`) executa tarefas definidas no `Taskfile.yml` global da pasta `$HOME` do usuário.

## Exemplo
```bash
# Executar tarefas apontando para outro diretório (--dir), outro nome de arquivo (--taskfile) ou modo dry-run (--dry)
task --dir ./subdirectory build
task --taskfile Custom.yml default
task --dry build
```

## Limites e trade-offs
Quando você mantém tanto um `Taskfile.dist.yml` (versionado no Git para toda a equipe) quanto permite overrides locais via `Taskfile.yml` ignorado no `.gitignore`, se um desenvolvedor criar seu próprio `Taskfile.yml` local sem incluir (`includes:`) o `Taskfile.dist.yml`, o Task carregará apenas o `Taskfile.yml` de maior precedência; por isso, no `Taskfile.yml` local deve-se incluir o `Taskfile.dist.yml` com `flatten: true` e `optional: true`.

## Como verificar
Execute `task --summary <nome-da-tarefa>` para exibir na tela a descrição completa, dependências e lista de comandos que compõem aquela tarefa antes de rodá-la.

## Conexões
- [[taskfile-ambientes-dotenv-plataformas-shells-output]] — Veja também: Task: carregamento de arquivos .env (dotenv), filtragem por plataforma (platforms) e modos de saída (output).
- [[taskfile-aliases-wildcard-tasks-internal-silent-desc]] — Veja também: Task: definição avançada de tarefas (aliases, internal, silent, labels dinâmicas e captura de wildcards *).
- [[taskfile-task-runner-moderno-go-alternativa-make-yaml]] — Referência cruzada direta com taskfile-task-runner-moderno-go-alternativa-make-yaml.
- [[taskfile-composicao-includes-namespaces-remote-taskfiles]] — Referência cruzada direta com taskfile-composicao-includes-namespaces-remote-taskfiles.

## Fontes
- [Task GitHub — README.md & Quick Start Guide (Taskfile.yml v3, task --init, mvdan/sh & Directory Flags)](https://raw.githubusercontent.com/go-task/task/main/README.md) — README e guia Quick Start oficiais do go-task/task documentando sintaxe Taskfile.yml versão 3, interpretador shell nativo Go mvdan/sh e flags --init, --dir e --taskfile; consultado em 2026-10-03.
- [Task Official Guide — Complete Feature Guide (Variables, Requires, Parallel Deps, Loops, Preconditions, Defer, Checksum & Includes)](https://taskfile.dev/docs/getting-started) — Guia completo oficial do Task cobrindo variáveis dinâmicas, validação requires, segredos, deps concorrentes, loops/matrizes, preconditions, prompts, defer, up-to-date checks por checksum, modo watch, dotenv e includes locais/remotos; consultado em 2026-10-03.
- [Task — Official Documentation Portal (taskfile.dev)](https://taskfile.dev/docs/guide) — Portal de documentação oficial do Task; consultado em 2026-10-03.
