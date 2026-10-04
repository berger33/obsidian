---
id: software.seguranca.tranche07.000676
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/sudo-project/sudo/main/README.md", "https://www.sudo.ws/docs/man/sudoers.man/", "https://www.sudo.ws/docs/man/sudo_logsrvd.man/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sudo: Gravação Forense Completa de Sessões de Terminal (**I/O Logging** `log_input`, `log_output`, `log_subcmds`) e Reprodução com **`sudoreplay`**

## Em uma frase
Quando um administrador precisa inevitavelmente de um shell interativo ou executa uma ferramenta complexa via `sudo`, o log padrão do `syslog` mostra apenas `COMMAND=/bin/bash`, deixando o SOC cego quanto ao que foi digitado dentro do shell; o subsistema de **I/O Logging** do `sudo` (`log_input`, `log_output` e `log_subcmds`) resolve esse gap gravando toda a sessão como um filme reproduzível via **`sudoreplay`**!

## Por que importa
Ativar **`Defaults log_output`** e **`Defaults log_input`** faz o plugin `sudoers_io` gravar em `/var/log/sudo-io/` (comprimido em gzip) cada tecla digitada (`stdin`), tudo o que apareceu na tela (`stdout`/`stderr`), redimensionamentos de janela e os intervalos exatos de tempo.

## Como funciona
Mais ainda, no Sudo 1.9+, ativar **`Defaults log_subcmds`** (que utiliza `sudo_intercept.so` ou `ptrace` para interceptar chamadas `execve`/`execveat`) registra no log de auditoria **todos os subcomandos executados a partir de dentro de um shell ou editor aberto via `sudo`**!

## Exemplo
```sudoers
# /etc/sudoers.d/10-io-session-recording — Gravar I/O completo do terminal e interceptar todos os subcomandos filhos
Defaults iolog_dir="/var/log/sudo-io/%{user}"
Defaults log_input, log_output
Defaults log_subcmds
Defaults log_stdin, log_stdout, log_stderr
```

## Limites e trade-offs
Para evitar capturar senhas digitadas em prompts dentro da sessão gravada, o `sudoers` habilita por padrão `Defaults passprompt_regex`, que pausa temporariamente a gravação de `log_input` quando o eco do terminal (`ECHO` termios) está desligado.

## Como verificar
Liste todas as sessões gravadas com **`sudo sudoreplay -l`** (ou filtre por usuário/comando `sudoreplay -l user alice command bash`) e reproduza a sessão exata em tempo real com **`sudo sudoreplay <TSID>`**.

## Conexões
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Veja também: Sudoers: Hardening de `Defaults` — **`env_reset`**, **`secure_path`**, **`use_pty`**, `timestamp_type=tty` e `passwd_tries`.
- [[sudo-centralizacao-logs-sudo-logsrvd-tls-mtls-imutabilidade]] — Veja também: Sudo (`sudo_logsrvd`): Transmissão Centralizada em Tempo Real de Logs de Eventos e I/O via TLS Mútuo (**mTLS**) contra Adulteração Local.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
