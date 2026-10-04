---
id: software.seguranca.tranche14.001368
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/activecm/rita/main/README.md", "https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração de Feeds de **Threat Intelligence (`threat_intel`)** no RITA: Cruzando Conexões Zeek com Listas de IoCs (`online_feeds` e Feeds Customizados)

## Em uma frase
Como fazer com que qualquer conexão no `conn.log`, `ssl.log` ou `dns.log` do Zeek para um IP ou domínio listado em feeds de **Threat Intelligence** (tanto feeds públicos quanto feeds internos do seu **MISP / OpenCTI** servidos via HTTPS ou montados em disco) receba automaticamente severidade máxima (`category: "high"`) no **RITA**?

## Por que importa
No arquivo `/etc/rita/config.hjson`, o RITA possui integração nativa de **Threat Intelligence**: **(1) `threat_intel.online_feeds`** — lista de URLs HTTPS de feeds de indicadores atualizados automaticamente pelo RITA; **(2) Diretório de Feeds Customizados** (arquivos `.txt` com IPs, blocos CIDR ou FQDNs colocados no diretório de feeds montado no RITA); e **(3) `scoring.threat_intel_impact: { category: "high" }`**!

## Como funciona
Sempre que o RITA encontra durante a importação dos logs do Zeek uma comunicação com um destino presente nos feeds de Threat Intel, ele marca o indicador no painel TUI e na exportação CSV e eleva a prioridade daquele par na fila de investigação do caçador!

## Exemplo
```bash
# Exportar uma lista de IPs e dominios maliciosos de alta confianca do seu MISP/CTI para um arquivo de feed consumido pelo RITA
cat << 'EOF' > /etc/rita/threat_intel_custom.txt
198.51.100.220
203.0.113.88
c2-apt-campanha.exemplo.net
EOF
rita validate-config -c /etc/rita/config.hjson
```

## Limites e trade-offs
Sempre execute **`rita validate-config -c /etc/rita/config.hjson`** após editar o arquivo HJSON do RITA: esse subcomando valida toda a estrutura de tipos, limiares de pontuação, sub-redes CIDR e configurações de feeds antes da próxima execução do `rita import`!

## Como verificar
Evite carregar listas de milhões de IPs de baixa fidelidade (como listas genéricas de spam de 5 anos atrás) em `threat_intel`: alimente o RITA apenas com **IoCs de C2, Botnets e Ransomware ativos e de alta confiança (ex.: Abuse.ch Feodo Tracker, URLhaus, ThreatFox e seus próprios IoCs do MISP)**.

## Conexões
- [[rita-filtros-rede-interna-whitelist-safelist-config-hjson-tuning]] — Veja também: Configuração de Sub-redes Internas (**`internal_subnets`**) e Listas de Exclusão (**`never_included_ips` / `never_included_domains`**) no `/etc/rita/config.hjson`.
- [[rita-operacao-continua-rolling-datasets-zeek-cron-automacao-soc]] — Veja também: Operação Contínua no SOC com **Rolling Datasets (`--rolling` vs. `--rebuild`)**, Exportação CSV (`--stdout`) e Integração de Alertas RITA no SIEM.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Referência cruzada direta com rita-modificadores-score-prevalencia-raridade-first-seen-missing-host.
- [[arkime-enriquecimento-wiseservice-threat-intel-regras-yara-tagger]] — Referência cruzada direta com arkime-enriquecimento-wiseservice-threat-intel-regras-yara-tagger.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
