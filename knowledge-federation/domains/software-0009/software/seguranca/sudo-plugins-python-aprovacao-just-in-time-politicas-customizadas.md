---
id: software.seguranca.tranche07.000678
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

# Sudo 1.9+: Extensão de Políticas e Auditoria com **`sudo_python.so`** (Aprovação *Just-In-Time*, Checagem de Chamados no TheHive/Jira e Contexto)

## Em uma frase
Desde a versão 1.9, o Sudo inclui o plugin oficial **`python_plugin.so`** (`--enable-python`), que permite escrever plugins de Política, Auditoria, I/O e aprovação pré-execução (**Approval Plugins**) diretamente em Python 3.

## Por que importa
Em vez de conceder acesso `sudo` permanente 24x7 em servidores de produção, um **Approval Plugin** em Python é chamado após o `sudoers.so` autorizar a regra: o script Python verifica se há um chamado de mudança ou incidente ativo (`in_progress`) atribuído àquele engenheiro no **TheHive / ServiceNow / PagerDuty** antes de liberar o comando!

## Como funciona
A configuração em `/etc/sudo.conf` adiciona `Plugin python_approval python_plugin.so ModulePath=/usr/local/libexec/sudo/check_ticket.py ClassName=TicketApprovalPlugin`, onde o arquivo `.py` pertence obrigatoriamente a `root:root` com permissão `0600`/`0644` sem escrita por grupo/outros.

## Exemplo
```python
import sudo

class TicketApprovalPlugin(sudo.Plugin):
    def check(self, command_info: tuple, run_argv: tuple, run_env: tuple) -> int:
        # Exemplo: verificar variavel ou servico de plantao antes de aprovar a execucao
        sudo.log_info("Verificando janela de mudanca aprovada no SOC para: " + " ".join(run_argv))
        return sudo.RC.ACCEPT
```

## Limites e trade-offs
O `python_plugin.so` do Sudo recusa-se a carregar qualquer script Python cujo arquivo ou diretório pai possa ser gravado por qualquer usuário diferente de `root` (`world-writable` ou `group-writable`), prevenindo injeção de código no processo privilegiado.

## Como verificar
Verifique o carregamento do plugin com `sudo -V` e teste a aprovação retornando `sudo.RC.REJECT` fora do horário de mudança.

## Conexões
- [[sudo-centralizacao-logs-sudo-logsrvd-tls-mtls-imutabilidade]] — Veja também: Sudo (`sudo_logsrvd`): Transmissão Centralizada em Tempo Real de Logs de Eventos e I/O via TLS Mútuo (**mTLS**) contra Adulteração Local.
- [[sudo-restricoes-chroot-runchroot-runcwd-selinux-role-type-apparmor]] — Veja também: Sudoers: Confinamento de Comandos Delegados com SELinux (`ROLE=` / `TYPE=`), AppArmor (`APPARMOR_PROFILE=`) e `RUNCHROOT=` / `RUNCWD=`.
- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Referência cruzada direta com sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio.

## Fontes
- [Sudo Official Sudoers Manual — sudoers(5) Policy Plugin Reference](https://raw.githubusercontent.com/sudo-project/sudo/main/README.md) — manual oficial sudoers(5) cobrindo plugins sudo.conf, autenticação, Defaults use_pty/env_reset/secure_path, SHA-256 digests, NOEXEC, sudoedit e I/O logging; consultado em 2026-10-03.
- [Sudo Official GitHub — The Sudo Philosophy & Security Architecture](https://www.sudo.ws/docs/man/sudoers.man/) — repositório oficial do projeto Sudo e diretrizes de menor privilégio; consultado em 2026-10-03.
- [Sudo Official Manual — sudo_logsrvd(8) Centralized I/O & Event Log Server](https://www.sudo.ws/docs/man/sudo_logsrvd.man/) — documentação oficial do servidor centralizado de gravação de sessões sudo_logsrvd com TLS mútuo; consultado em 2026-10-03.
