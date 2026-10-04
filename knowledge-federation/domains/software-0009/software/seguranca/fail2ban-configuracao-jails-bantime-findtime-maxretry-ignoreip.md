---
id: software.seguranca.tranche07.000662
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

# Fail2ban: Anatomia de uma **Jail** (`findtime`, `maxretry`, `bantime`, `ignoreip`, `ignoreself` e `backend = systemd`)

## Em uma frase
Cada **Jail** em `/etc/fail2ban/jail.d/*.local` conecta um **Filter** (`filter.d/<nome>.conf`, que define *o que* procurar no log) a uma ou mais **Actions** (`action.d/<nome>.conf`, que definem *como* bloquear o IP) dentro de uma janela deslizante de tempo.

## Por que importa
Três parâmetros governam a máquina de estados de detecção de uma jail: se um mesmo endereço IPv4/IPv6 (não listado em `ignoreip`) acumular **`maxretry`** falhas dentro da janela temporal **`findtime`** (ex.: `5` falhas em `10m`), a jail dispara a ação `actionban` bloqueando o IP por **`bantime`** (ex.: `1h` ou `-1` para banimento permanente).

## Como funciona
Em distribuições Linux modernas baseadas em `systemd` (Debian 12+, Ubuntu 24.04+, RHEL 9+, Fedora), onde muitos serviços gravam apenas no `journald` binário sem criar arquivos em `/var/log/`, definir **`backend = systemd`** (com `journalmatch = _SYSTEMD_UNIT=sshd.service`) lê os eventos diretamente da API C do `systemd-journal` com zero latência de polling em disco.

## Exemplo
```ini
# /etc/fail2ban/jail.d/10-sshd-hardened.local
[DEFAULT]
ignoreself = true
ignoreip = 127.0.0.1/8 ::1 10.99.0.0/24
bantime = 1h
findtime = 10m
maxretry = 5
banaction = nftables-multiport
banaction_allports = nftables-allports

[sshd]
enabled = true
port = ssh
backend = systemd
mode = aggressive
```

## Limites e trade-offs
Sempre inclua a sub-rede de gerência/bastion do SOC em **`ignoreip`** e mantenha `ignoreself = true` para impedir que um atacante com capacidade de falsificar pacotes UDP ou injetar strings em logs de aplicação provoque um auto-bloqueio (*Self-DoS*) contra os próprios servidores internos.

## Como verificar
Verifique o estado detalhado da jail com `sudo fail2ban-client status sshd` confirmando `Currently failed` e `Currently banned`.

## Conexões
- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Veja também: Fail2ban: Arquitetura do Daemon, Ordem Estrita de Precedência (`*.conf` vs `*.local`) e Operação via **`fail2ban-client`**.
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Veja também: Fail2ban: Escrita Segura de Filtros (`failregex`, `ignoreregex`, `<HOST>` vs `<ADDR>`) e Prevenção de **ReDoS** e *Log Injection*.
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Referência cruzada direta com fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
