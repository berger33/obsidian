---
id: software.seguranca.tranche07.000668
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

# Fail2ban: Desenvolvimento de **Actions (`action.d/`)** Customizadas, Integração com Webhooks SOC/TheHive e Métricas Prometheus

## Em uma frase
Em `/etc/fail2ban/action.d/`, cada arquivo de ação define os comandos executados no início da jail (`actionstart`), no encerramento (`actionstop`), na verificação de integridade (`actioncheck`), no banimento de um IP (`actionban`) e na remoção do banimento (`actionunban`).

## Por que importa
Uma jail pode executar **múltiplas ações simultaneamente**: por exemplo, bloquear o IP imediatamente no `nftables` local na primeira ação e, na segunda ação, enviar um payload JSON estruturado via webhook para o **SIEM / TheHive** (ou reportar a botnet para o **AbuseIPDB**).

## Como funciona
Ao escrever um comando `actionban` customizado que invoca um script externo passando tags extraídas do log, **jamais interpole tags de texto livre como `<matches>` diretamente em uma linha de shell sem escape**, pois o log contém dados não-confiáveis do atacante; passe apenas **`<ip>`** (que é estritamente validado pelo Fail2ban como IP numérico).

## Exemplo
```ini
# /etc/fail2ban/action.d/soc-webhook-notify.local — Notificar o SOC usando apenas tags estritamente validadas (<ip>, <name>, <failures>)
[Definition]
actionban = curl -sS -m 3 -X POST "https://soar.soc.internal.corp/hooks/fail2ban" \
            -H "Content-Type: application/json" \
            -d '{"jail": "<name>", "banned_ip": "<ip>", "failures": <failures>}' >/dev/null 2>&1 || true
actionunban =
```

## Limites e trade-offs
Sempre adicione um timeout curto (`curl -m 3 ... || true`) em ações de notificação externa para que uma lentidão na rede ou no webhook jamais bloqueie a fila de processamento das ações de firewall do Fail2ban.

## Como verificar
Simule um banimento de teste com `sudo fail2ban-client set sshd banip 198.51.100.250` e verifique o recebimento do evento no receptor do SOC.

## Conexões
- [[fail2ban-agrupamento-sessoes-tags-f-mlfid-f-id-no-failure]] — Veja também: Fail2ban: Correlação Multi-Linha com Tags de Sessão (**`<F-MLFID>`**, **`<F-ID>`**, **`<F-NOFAIL>`**) para Daemons que Logam IP e Falha em Linhas Separadas.
- [[fail2ban-operacao-administrativa-ban-unban-manual-dbpurgeage]] — Veja também: Fail2ban: Operação de Resposta a Incidentes via `fail2ban-client` (`set <jail> banip`, `unbanip`, `unban --all` e Auditoria SQLite).
- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Referência cruzada direta com fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client.
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Referência cruzada direta com fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive.
- [[thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao]] — Referência cruzada direta com thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
