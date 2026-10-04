---
id: software.seguranca.tranche14.001369
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

# Operação Contínua no SOC com **Rolling Datasets (`--rolling` vs. `--rebuild`)**, Exportação CSV (`--stdout`) e Integração de Alertas RITA no SIEM

## Em uma frase
Qual é a diferença operacional entre importar logs do Zeek no RITA com a flag **`--rebuild`** versus a flag **`--rolling`**, e como automatizar a caça diária/horária do RITA enviando os resultados de alta severidade para o SIEM (**Wazuh / OpenSearch**) ou **TheHive**?

## Por que importa
A diferença é fundamental para a operação diária: **(1) `--rebuild`** apaga o banco de dados anterior daquele dataset e constrói uma análise limpa do zero apenas com os logs passados no comando (ideal para analisar um pacote de logs forenses ou de um incidente específico, ex.: `--database=caso_incidente_42 --rebuild`); já **(2) `--rolling`** adiciona incrementalmente novos lotes de logs (por exemplo, a última hora de logs rotacionados pelo Zeek!) em uma janela deslizante de 24 horas e **preserva a tabela histórica de `first_seen` de todos os domínios e IPs já vistos na rede ao longo dos meses**!

## Como funciona
Para integrar o RITA ao seu SIEM/SOAR sem precisar abrir a interface TUI interativa, basta usar **`rita view <dataset> --stdout`**: o RITA imprime todas as ameaças pontuadas em formato **CSV padronizado** (`Severity,Source,Destination,Beacon Score,Duration,Subdomains,Threat Intel,...`), pronto para ser filtrado com `awk`/`python` e ingerido no SIEM!

## Exemplo
```bash
# Script de cron/systemd timer para importar incrementalmente (--rolling) os logs da ultima hora do Zeek e extrair ameacas criticas em CSV
rita import --database=producao_rolling --logs=/nsm/zeek/logs/$(date -u +%Y-%m-%d)/ --rolling
rita view producao_rolling --stdout | awk -F',' 'NR==1 || $1 == "high" || $4 > 0.85' > /var/log/rita/high_threats.csv
```

## Limites e trade-offs
Dica operacional importante documentada pela Active Countermeasures ao importar múltiplos diretórios de dias diferentes no modo `--rolling`: **importe sempre os diretórios de logs do Zeek em ordem cronológica (do mais antigo para o mais recente)** para que o cálculo incremental da janela deslizante de 24 horas e os timestamps de `first_seen` reflitam a linha do tempo real!

## Como verificar
Use **`rita list`** para listar todos os datasets existentes no ClickHouse do RITA e **`rita delete --database=<nome>`** para expurgar investigações pontuais antigas.

## Conexões
- [[rita-threat-intel-feeds-customizados-online-ip-fqdn-correlacao]] — Veja também: Integração de Feeds de **Threat Intelligence (`threat_intel`)** no RITA: Cruzando Conexões Zeek com Listas de IoCs (`online_feeds` e Feeds Customizados).
- [[rita-fluxo-investigacao-caca-ameacas-rita-zeek-arkime-wireshark]] — Veja também: Playbook Completo de **Threat Hunting de Rede**: Do Score de Beacon no **RITA** ao Pivotamento no **Zeek (`uid` / `community_id`)** e Captura Bruta no **Arkime**.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Referência cruzada direta com rita-modificadores-score-prevalencia-raridade-first-seen-missing-host.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
