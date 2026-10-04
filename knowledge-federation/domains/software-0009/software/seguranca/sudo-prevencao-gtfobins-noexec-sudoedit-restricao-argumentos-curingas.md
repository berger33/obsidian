---
id: software.seguranca.tranche07.000674
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

# Sudoers: Prevenção de Escalação de Privilégio (**GTFOBins**) — Uso da Tag **`NOEXEC:`**, **`sudoedit` (`sudo -e`)** e Perigos do Curinga `*`

## Em uma frase
Centenas de utilitários Unix legítimos (documentados no catálogo **GTFOBins**: `vim`, `less`, `more`, `man`, `journalctl`, `systemctl`, `find`, `awk`, `tar`, `zip`, `gdb`, `git`) permitem escapar para um shell interativo (ex.: digitando `!/bin/sh` dentro do `less` ou `vim`, ou `--checkpoint-action=exec=/bin/sh` no `tar`): se executados via `sudo`, o shell filho herda `UID 0 (root)`.

## Por que importa
Três controles nativos do `sudoers` neutralizam essa classe inteira de escalação de privilégio: **(1) Tag `NOEXEC:`** (injeta a biblioteca `sudo_noexec.so` ou filtro seccomp que faz todas as chamadas `execve()`/`system()`/`popen()` dentro do programa autorizado falharem com `EACCES`, impedindo `less` ou `vim` de abrir um shell!), **(2) `sudoedit` (`sudo -e`)** para edição de arquivos de configuração e **(3) Proibição do curinga `*` aberto** em argumentos.

## Como funciona
Com **`sudoedit /etc/nginx/nginx.conf`**, o editor de texto (`vim`/`nano`) roda **como o próprio usuário comum sem privilégios** sobre uma cópia temporária segura; assim, se o usuário digitar `:!/bin/sh` no `vim`, ele abrirá um shell apenas dele mesmo, nunca de `root`!

## Exemplo
```sudoers
# /etc/sudoers.d/40-safe-viewer-and-editor — Usar sudoedit para edicao e NOEXEC + SYSTEMD_PAGER="" para leitura
%webops ALL = (root) sudoedit /etc/nginx/conf.d/app.conf
Defaults!/usr/bin/systemctl env_keep -= "SYSTEMD_PAGER PAGER"
%webops ALL = (root) NOEXEC: /usr/bin/systemctl status nginx.service
```

## Limites e trade-offs
Cuidado extremo com o curinga **`*`** em argumentos do `sudoers`: na regra `/bin/chmod 0644 /var/www/html/*`, o `*` casa inclusive com `../../etc/shadow` (*path traversal*) e com flags adicionais `--reference=...`! Prefira comandos exatos sem curingas ou expressões regulares POSIX ancordas do Sudo 1.9.10+ (`^/var/www/html/[a-zA-Z0-9._-]+$`).

## Como verificar
Teste executar `sudo systemctl status nginx.service` com a regra `NOEXEC:` acima e confirme que tentar invocar `!/bin/sh` dentro do paginador é bloqueado.

## Conexões
- [[sudo-integridade-binarios-sha256-digest-pinning-scripts-administrativos]] — Veja também: Sudoers: Pinagem Criptográfica de Binários e Scripts com **SHA-224 / SHA-256 / SHA-384 / SHA-512 Digest** no `/etc/sudoers`.
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Veja também: Sudoers: Hardening de `Defaults` — **`env_reset`**, **`secure_path`**, **`use_pty`**, `timestamp_type=tty` e `passwd_tries`.
- [[sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra]] — Referência cruzada direta com sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
