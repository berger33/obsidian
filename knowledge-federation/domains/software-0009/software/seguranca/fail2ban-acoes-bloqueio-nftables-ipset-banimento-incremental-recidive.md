---
id: software.seguranca.tranche07.000665
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

# Fail2ban: Escalabilidade de Firewall com Sets **`nftables` / `ipset`**, *Exponential Backoff* (`bantime.increment`) e Jail **`recidive`**

## Em uma frase
Em servidores sob ataque distribuído que bloqueiam dezenas de milhares de IPs maliciosos, usar a ação antiga que insere uma regra linear `iptables -I f2b-sshd 1 -s <IP> -j REJECT` por IP degrada a performance de rede do kernel Linux (`O(N)` por pacote); a solução moderna é usar conjuntos hash **`nftables` (`nftables-multiport` / `nftables-allports`)** ou **`iptables-ipset`** (`O(1)` constante).

## Por que importa
Além disso, atacantes sofisticados configuram botnets em *low-and-slow* que pausam os ataques por 1 hora após o primeiro banimento e voltam imediatamente após o `unban`: para derrotá-los, o Fail2ban (>= 0.11) oferece **Banimento Incremental Exponencial (`bantime.increment = true`)** e a jail especial **`[recidive]`**.

## Como funciona
Com `bantime.increment = true`, o Fail2ban consulta o histórico do IP no banco SQLite (`dbpurgeage` estendido para ex.: `7d` ou `30d`) e multiplica automaticamente o tempo de banimento a cada reincidência (`10m -> 20m -> 40m -> 80m -> ...` ou `bantime.multipliers = 1 5 30 60 300 720 1440 2880`), enquanto a jail **`recidive`** monitora o próprio `/var/log/fail2ban.log` e bloqueia em **todas as portas (`banaction_allports`)** por 1 semana qualquer IP que seja banido repetidas vezes em jails diferentes.

## Exemplo
```ini
# /etc/fail2ban/jail.d/20-exponential-backoff-and-recidive.local
[DEFAULT]
bantime.increment = true
bantime.rndtime = 8m
bantime.factor = 2
bantime.maxtime = 5w

[recidive]
enabled = true
logpath = /var/log/fail2ban.log
banaction = %(banaction_allports)s
bantime = 1w
findtime = 1d
maxretry = 4
```

## Limites e trade-offs
A diretiva **`bantime.rndtime = 8m`** adiciona um jitter aleatório ao tempo de desbloqueio de cada IP, impedindo que botnets sincronizadas descubram o segundo exato em que o banimento expira.

## Como verificar
Inspecione o conjunto hash criado no kernel com `sudo nft list set inet f2b-table addr-set-sshd` para verificar os elementos e seus timeouts de expiração.

## Conexões
- [[fail2ban-testes-performance-fail2ban-regex-benchmark-logs]] — Veja também: Fail2ban: Validação e Benchmark de Expressões Regulares com **`fail2ban-regex`** antes do Deploy em Produção.
- [[fail2ban-protecao-proxies-reversos-nginx-http-auth-limit-req-xff]] — Veja também: Fail2ban: Proteção de Proxies Reversos **Nginx / Envoy** (`nginx-http-auth`, `nginx-limit-req`, `nginx-botsearch`) e Cuidados com `X-Forwarded-For`.
- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Referência cruzada direta com fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client.
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Referência cruzada direta com fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip.
- [[fail2ban-operacao-administrativa-ban-unban-manual-dbpurgeage]] — Referência cruzada direta com fail2ban-operacao-administrativa-ban-unban-manual-dbpurgeage.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
