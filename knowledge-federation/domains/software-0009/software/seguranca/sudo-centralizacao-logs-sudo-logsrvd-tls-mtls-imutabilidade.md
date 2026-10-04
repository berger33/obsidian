---
id: software.seguranca.tranche07.000677
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

# Sudo (`sudo_logsrvd`): Transmissão Centralizada em Tempo Real de Logs de Eventos e I/O via TLS Mútuo (**mTLS**) contra Adulteração Local

## Em uma frase
Se os arquivos de gravação `/var/log/sudo-io/` ficarem armazenados apenas no disco local do próprio servidor onde o administrador obteve `root`, um administrador malicioso ou invasor pode simplesmente apagar `/var/log/sudo-io/` para destruir seus rastros; o daemon oficial **`sudo_logsrvd`** (introduzido no Sudo 1.9, protocolo `sudo_logsrv.proto`) transmite os fluxos de I/O em tempo real pela rede para um servidor coletor dedicado e isolado!

## Por que importa
No servidor gerenciado, basta configurar **`Defaults log_servers="logsrv.soc.internal.corp:30344(tls)"`** com certificados mTLS (`log_server_cabundle`, `log_server_peer_cert`, `log_server_peer_key`).

## Como funciona
Quando **`Defaults!ALL log_server_keepalive`** e **`!lecture`** são combinados com a política padrão (`log_server_verify`), se o servidor central `sudo_logsrvd` estiver inacessível ou se alguém tentar bloquear a conexão de auditoria no firewall local, **o `sudo` recusa-se a executar o comando privilegiado (*fail-closed*)**!

## Exemplo
```ini
# /etc/sudo_logsrvd.conf no servidor coletor centralizado do SOC (escutando com mTLS na porta 30344)
[server]
listen_address = 0.0.0.0:30344(tls)
tls_cacert = /etc/ssl/sudo/soc-ca.pem
tls_cert = /etc/ssl/sudo/logsrvd-cert.pem
tls_key = /etc/ssl/sudo/logsrvd-key.pem
tls_checkpeer = true

[iolog]
iolog_dir = /var/AuditVault/sudo-io/%{hostname}/%{user}
iolog_file = %{seq}
```

## Limites e trade-offs
Mantenha o comportamento padrão **`Defaults log_server_cabundle=...`** sem adicionar a flag `(optional)` ao `log_servers` em servidores críticos Tier 0: isso garante que nenhum comando privilegiado jamais seja executado sem que cada tecla seja gravada simultaneamente fora da máquina.

## Como verificar
No servidor central de auditoria, execute `sudoreplay -d /var/AuditVault/sudo-io -l` para listar e reproduzir as sessões recebidas de todos os servidores da frota.

## Conexões
- [[sudo-auditoria-io-logging-log-input-log-output-sudoreplay]] — Veja também: Sudo: Gravação Forense Completa de Sessões de Terminal (**I/O Logging** `log_input`, `log_output`, `log_subcmds`) e Reprodução com **`sudoreplay`**.
- [[sudo-plugins-python-aprovacao-just-in-time-politicas-customizadas]] — Veja também: Sudo 1.9+: Extensão de Políticas e Auditoria com **`sudo_python.so`** (Aprovação *Just-In-Time*, Checagem de Chamados no TheHive/Jira e Contexto).
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Referência cruzada direta com sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
