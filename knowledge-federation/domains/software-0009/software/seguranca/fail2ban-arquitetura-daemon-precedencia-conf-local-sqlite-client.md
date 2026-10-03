---
id: software.seguranca.tranche07.000661
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
fontes: ["https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md", "https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5", "https://github.com/fail2ban/fail2ban/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fail2ban: Arquitetura do Daemon, Ordem Estrita de Precedência (`*.conf` vs `*.local`) e Operação via **`fail2ban-client`**

## Em uma frase
**Fail2ban** (`fail2ban/fail2ban`, GPLv2+, Python 3) é o daemon de prevenção de intrusão em nível de host que monitora arquivos de log (`/var/log/auth.log`, Nginx, Postfix, OpenVPN) ou o `systemd-journal` em tempo real e atualiza dinamicamente o firewall do sistema (`nftables`, `iptables`/`ipset`, `ufw`, `firewalld`) para bloquear endereços IPv4 e IPv6 que realizam força bruta ou varreduras.

## Por que importa
Reduz drasticamente o ruído de ataques automatizados de força bruta contra serviços expostos (SSH, gateways de e-mail, portais de autenticação e APIs) e persiste os banimentos no banco SQLite **`/var/lib/fail2ban/fail2ban.sqlite3`** para restaurá-los automaticamente após reinicializações.

## Como funciona
Conforme documentado na manpage oficial `jail.conf(5)`, a configuração é carregada na ordem estrita: **`jail.conf` -> `jail.d/*.conf` -> `jail.local` -> `jail.d/*.local`**. O administrador **jamais deve editar os arquivos `.conf` originais** (que são sobrescritos em atualizações de pacotes da distribuição), devendo colocar todas as customizações exclusivamente em arquivos **`.local`** (`jail.local` ou `jail.d/99-hardening.local`).

## Exemplo
```bash
# Verificar a versao do daemon, status de todas as jails ativas e recarregar configuracoes sem derrubar o servico
sudo fail2ban-client version
sudo fail2ban-client status
sudo fail2ban-client reload
```

## Limites e trade-offs
Conforme alerta o `README.md` oficial do Fail2ban, sempre interaja com o daemon através do **`fail2ban-client`** (que se comunica pelo socket `/var/run/fail2ban/fail2ban.sock`) e nunca invoque `fail2ban-server` diretamente na mão.

## Como verificar
Execute `sudo fail2ban-client -d` para imprimir toda a configuração final mesclada (`conf` + `local`) e validar as diretivas efetivas.

## Conexões
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Veja também: Fail2ban: Anatomia de uma **Jail** (`findtime`, `maxretry`, `bantime`, `ignoreip`, `ignoreself` e `backend = systemd`).
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Referência cruzada direta com fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos.
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Referência cruzada direta com fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
