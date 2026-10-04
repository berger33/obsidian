---
id: software.seguranca.tranche07.000679
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

# Sudoers: Confinamento de Comandos Delegados com SELinux (`ROLE=` / `TYPE=`), AppArmor (`APPARMOR_PROFILE=`) e `RUNCHROOT=` / `RUNCWD=`

## Em uma frase
Mesmo quando uma regra no `sudoers` delega a execução de um binário como `root`, você não precisa permitir que esse binário rode no domínio SELinux ou perfil AppArmor irrestrito do administrador: o `sudoers` permite forçar a transição para um contexto **SELinux (`ROLE=`, `TYPE=`)**, um perfil **AppArmor (`APPARMOR_PROFILE=`)** ou um diretório **`RUNCHROOT=`** específico por regra!

## Por que importa
Isso une o controle de acesso discricionário (`sudo`) com o controle de acesso obrigatório (**MAC — SELinux / AppArmor**): se o binário delegado sofrer uma vulnerabilidade ou tiver uma função de escape não prevista, o kernel Linux (LSM) bloqueia qualquer acesso fora dos caminhos e sockets permitidos pelo perfil MAC.

## Como funciona
Na linha da regra do `sudoers`, esses modificadores são declarados diretamente antes do comando (ex.: `APPARMOR_PROFILE=nginx_reload_profile /usr/sbin/nginx -s reload`).

## Exemplo
```sudoers
# /etc/sudoers.d/50-mac-confined-sudo — Forcar transicao de perfil AppArmor ou tipo SELinux ao delegar comando via sudo
%sec_auditor ALL = (root) APPARMOR_PROFILE=usr.sbin.tcpdump_restricted /usr/bin/tcpdump -i eth0 -c 100 -w /cases/pcaps/capture.pcap
```

## Limites e trade-offs
No Sudo 1.9.3+, `RUNCWD=/var/www/app` força o diretório de trabalho inicial do comando, impedindo ataques contra ferramentas que carregam arquivos de configuração ou bibliotecas do diretório atual (`.` do usuário chamador).

## Como verificar
Execute o comando delegado via `sudo` e verifique em outro terminal com `ps -efZ` (SELinux) ou `aa-status` (AppArmor) que o processo filho entrou exatamente no perfil MAC especificado.

## Conexões
- [[sudo-plugins-python-aprovacao-just-in-time-politicas-customizadas]] — Veja também: Sudo 1.9+: Extensão de Políticas e Auditoria com **`sudo_python.so`** (Aprovação *Just-In-Time*, Checagem de Chamados no TheHive/Jira e Contexto).
- [[sudo-auditoria-superficie-ataque-cve-2021-3156-cve-2023-22809-alternativas]] — Veja também: Auditoria da Superfície de Ataque do Sudo (Lições de `CVE-2021-3156` *Baron Samedit* e `CVE-2023-22809`), `nosuid` e Alternativas Mínimas.
- [[sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra]] — Referência cruzada direta com sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
