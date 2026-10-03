---
id: software.seguranca.tranche07.000669
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

# Fail2ban: Operação de Resposta a Incidentes via `fail2ban-client` (`set <jail> banip`, `unbanip`, `unban --all` e Auditoria SQLite)

## Em uma frase
Durante a operação diária do SOC ou atendimento a chamados de suporte, o **`fail2ban-client`** permite consultar instantaneamente em quais jails um determinado endereço IP está bloqueado, desbloquear um usuário legítimo que errou a senha ou injetar uma lista de IPs de ameaça manualmente.

## Por que importa
Se um administrador legítimo errar a chave SSH repetidas vezes a partir de uma rede externa, o comando **`sudo fail2ban-client unban <IP>`** remove o endereço IP de **todas** as jails onde ele estiver banido simultaneamente, atualizando tanto o conjunto `nftables`/`ipset` no kernel quanto o banco SQLite.

## Como funciona
Para inspeção forense histórica de quais IPs foram banidos nas últimas semanas e quantas vezes reincidiram, o banco `/var/lib/fail2ban/fail2ban.sqlite3` armazena as tabelas `jails`, `logs` e **`bips`** (controlada pelo tempo de retenção `dbpurgeage`).

## Exemplo
```bash
# Listar apenas a lista limpa de IPs banidos na jail sshd, banir um IP manualmente e desbloquear um IP especifico
sudo fail2ban-client get sshd banip
sudo fail2ban-client set sshd banip 203.0.113.88
sudo fail2ban-client set sshd unbanip 203.0.113.88
```

## Limites e trade-offs
Para evitar perder o histórico de reincidentes da jail `recidive` e do `bantime.increment` após um `systemctl restart fail2ban`, ajuste **`dbpurgeage = 30d`** (o padrão original de fábrica em muitas instalações é apenas `1d` / `86400s` em `/etc/fail2ban/fail2ban.local`).

## Como verificar
Consulte `sudo fail2ban-client get dbpurgeage` para confirmar que o tempo de retenção do banco SQLite é superior ao `bantime.maxtime` configurado.

## Conexões
- [[fail2ban-acoes-customizadas-webhooks-thehive-abuseipdb-observabilidade]] — Veja também: Fail2ban: Desenvolvimento de **Actions (`action.d/`)** Customizadas, Integração com Webhooks SOC/TheHive e Métricas Prometheus.
- [[fail2ban-limites-arquiteturais-defesa-em-profundidade-ssh-mfa-wireguard]] — Veja também: Fail2ban: Limites Arquiteturais (*Rate Limiting* vs Autenticação Forte), *IPv6 Subnet Banning* e Defesa em Profundidade.
- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Referência cruzada direta com fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client.
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Referência cruzada direta com fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive.
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Referência cruzada direta com thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
