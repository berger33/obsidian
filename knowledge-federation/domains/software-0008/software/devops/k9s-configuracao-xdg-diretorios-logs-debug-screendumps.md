---
id: software.devops.tranche10.000985
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/derailed/k9s/master/README.md", "https://k9scli.io/topics/commands/", "https://github.com/derailed/k9s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K9s: estrutura de diretórios XDG (config.yaml, clusters, screendumps), logs de debug (-l debug) e variável K9S_CONFIG_DIR

## Em uma frase
O K9s segue a especificação **XDG Base Directory** para organizar seus arquivos YAML de configuração, estado e compartilhamento (revelados por `k9s info` ou customizados via `K9S_CONFIG_DIR`), gravando capturas de recursos com `Ctrl-s` (`:screendump`) e logs de diagnóstico com `k9s -l debug`.

## Por que importa
Como o K9s ocupa toda a tela do terminal com a TUI interativa, ele não pode imprimir logs internos de erro no `stdout`/`stderr`; saber onde fica o arquivo `k9s.log` (`k9s info` / `--logFile` / `K9S_LOGS_DIR`) e onde são salvos os manifestos exportados com `Ctrl-s` é indispensável para troubleshooting e customização.

## Como funciona
Conforme detalham as seções `Logs And Debug Logs` e `K9s Configuration` do README oficial: executar **`k9s info`** imprime todos os caminhos ativos no sistema operacional (no Linux em `~/.config/k9s`, `~/.local/state/k9s` e `~/.local/share/k9s`; no macOS em `~/Library/Application Support/k9s` ou `~/.config/k9s`; no Windows em `%LOCALAPPDATA%\k9s`, podendo ser sobrescrito por **`K9S_CONFIG_DIR`**): (1) **`Config`**: `config.yaml` global; (2) **`Logs`**: `k9s.log` (detalhado ao iniciar com **`k9s -l debug`**, customizável com `--logFile /tmp/k9s.log` ou `K9S_LOGS_DIR`); (3) **`Dumps dir`**: pasta `screen-dumps` onde o atalho **`Ctrl-s`** salva em disco o conteúdo da tabela ou manifesto YAML atual (visualizável em `:screendump` ou `:sd`); e (4) arquivos de extensão: `views.yaml`, `plugins.yaml`, `hotkeys.yaml`, `aliases.yaml` e `skins`.

## Exemplo
```bash
# Iniciar o K9s em modo de debug gravando logs em um arquivo específico para diagnosticar falhas de RBAC ou conexão
k9s -l debug --logFile /tmp/k9s-debug.log
```

## Limites e trade-offs
Quando você trabalha conectado a um servidor remoto via SSH ou dentro de um multiplexador de terminal (`tmux`), copiar o nome de um pod (`c`) ou conteúdo de um YAML no K9s pode não chegar à área de transferência da sua máquina local se o clipboard nativo do servidor remoto for usado; para resolver isso, conforme documenta o README oficial, configure a variável de ambiente **`export K9S_CLIPBOARD=osc52`** (ou `auto`) para copiar via sequência de escape ANSI OSC52 pelo túnel SSH.

## Como verificar
Dentro do K9s, selecione qualquer visão ou YAML, pressione `Ctrl-s` para salvar um dump e digite `:sd` (`:screendump`) para visualizar o arquivo salvo no `Dumps dir`.

## Conexões
- [[k9s-visoes-diagnostico-pulses-xray-popeye-usedby]] — Veja também: K9s: visões integradas de diagnóstico de saúde e topologia (:pulses, :xray, :popeye, UsedBy u e Jump to Owner SHIFT-J).
- [[k9s-extensibilidade-plugins-hotkeys-aliases-views-skins]] — Veja também: K9s: extensibilidade com plugins customizados (plugins.yaml), atalhos (hotkeys.yaml), colunas (views.yaml) e temas (skins).
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[k9s-execucao-container-docker-build-multiplataforma-compatibilidade]] — Referência cruzada direta com k9s-execucao-container-docker-build-multiplataforma-compatibilidade.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
