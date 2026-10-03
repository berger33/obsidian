---
id: software.seguranca.tranche07.000675
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

# Sudoers: Hardening de `Defaults` — **`env_reset`**, **`secure_path`**, **`use_pty`**, `timestamp_type=tty` e `passwd_tries`

## Em uma frase
As diretivas **`Defaults`** no `/etc/sudoers` controlam como o `sudo` sanitiza variáveis de ambiente, gerencia o terminal (PTY) e armazena o cache temporário de autenticação.

## Por que importa
Se o `sudo` não limpar as variáveis de ambiente do usuário chamador (`PATH`, `LD_PRELOAD`, `LD_LIBRARY_PATH`, `PYTHONPATH`, `PERL5LIB`, `BASH_ENV`, `PS4`), um atacante basta exportar `PYTHONPATH=/tmp/evil` ou alterar o `PATH` para sequestrar a execução do binário privilegiado.

## Como funciona
O conjunto obrigatório de hardening em `/etc/sudoers.d/00-defaults-hardening` inclui: **`Defaults env_reset`** (limpa todas as variáveis exceto o mínimo seguro), **`Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"`** (força um `PATH` imutável e confiável), **`Defaults use_pty`** (executa o comando dentro de um pseudo-terminal dedicado, impedindo que um processo em background sequestre o terminal do administrador via `TIOCSTI`), **`Defaults timestamp_timeout=5`** e **`Defaults timestamp_type=tty`**.

## Exemplo
```sudoers
# /etc/sudoers.d/00-defaults-hardening — Baseline CIS Benchmark para higienizacao de ambiente e isolamento PTY
Defaults env_reset
Defaults mail_badpass
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Defaults use_pty
Defaults logfile="/var/log/sudo.log"
Defaults timestamp_type=tty
Defaults timestamp_timeout=5
Defaults passwd_tries=3
```

## Limites e trade-offs
A diretiva **`Defaults use_pty`** é crítica quando um administrador usa `sudo -u app_user comando` para mudar de `root`/admin para um usuário menos privilegiado: sem `use_pty`, o processo `app_user` herda o descritor de arquivo do terminal do administrador e pode injetar comandos de volta na sessão privilegiada após o término do `sudo`.

## Como verificar
Verifique as configurações `Defaults` ativas executando `sudo sudo -V` (como root, `sudo -V` lista todos os parâmetros `Defaults` compilados e configurados).

## Conexões
- [[sudo-prevencao-gtfobins-noexec-sudoedit-restricao-argumentos-curingas]] — Veja também: Sudoers: Prevenção de Escalação de Privilégio (**GTFOBins**) — Uso da Tag **`NOEXEC:`**, **`sudoedit` (`sudo -e`)** e Perigos do Curinga `*`.
- [[sudo-auditoria-io-logging-log-input-log-output-sudoreplay]] — Veja também: Sudo: Gravação Forense Completa de Sessões de Terminal (**I/O Logging** `log_input`, `log_output`, `log_subcmds`) e Reprodução com **`sudoreplay`**.
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Referência cruzada direta com sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio.
- [[bubblewrap-isolamento-terminal-new-session-tiocsti-die-with-parent]] — Referência cruzada direta com bubblewrap-isolamento-terminal-new-session-tiocsti-die-with-parent.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
