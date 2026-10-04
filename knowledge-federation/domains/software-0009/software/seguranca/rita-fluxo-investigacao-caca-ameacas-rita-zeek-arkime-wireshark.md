---
id: software.seguranca.tranche14.001370
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

# Playbook Completo de **Threat Hunting de Rede**: Do Score de Beacon no **RITA** ao Pivotamento no **Zeek (`uid` / `community_id`)** e Captura Bruta no **Arkime**

## Em uma frase
Quando o analista de Threat Hunting abre o **`rita view`** pela manhã e vê no topo da tela um alerta **`Severity: high (Beacon Score: 96%)`** entre a estação interna `10.20.4.55` e o domínio externo `cdn-metrics-edge.net` (com `Prevalence: 1 host` e `First Seen: ontem`), qual é o **Playbook Técnico de 4 Etapas** para confirmar ou descartar o comprometimento em menos de 10 minutos?

## Por que importa
Veja como **RITA + Zeek + Arkime + EDR/Osquery** trabalham em sinfonia perfeita: **(Etapa 1 — Detecção Comportamental no RITA)**: Anote o IP interno (`10.20.4.55`), o destino (`cdn-metrics-edge.net` / IPs resolvidos), a contagem de conexões e o tamanho típico dos pacotes;

## Como funciona
Na camada complementar de operação e execução técnica: **(Etapa 2 — Pivotamento nos Logs de Transação do Zeek)**: Filtre `conn.log`, `dns.log`, `ssl.log` e `http.log` do Zeek para `10.20.4.55` e extraia o `uid`, o `community_id`, o certificado X.509 (`issuer` / `subject`), o fingerprint `JA3`/`JA4` e o `user_agent`!; **(Etapa 3 — Inspeção Forense de Pacotes no Arkime)**: Busque o `communityId` no **Arkime** para inspecionar os headers e o timing exato do handshake no `.pcap`!; e **(Etapa 4 — Correlação no Endpoint via Osquery/Sysmon/Wazuh)**: Consulte no endpoint `10.20.4.55` qual processo (`pid`, `path`, `sha256`, `cmdline`) abriu socket para aquele IP/porta!

## Exemplo
```bash
# Etapa 2 do Playbook: Pivotar do alerta do RITA para os logs do Zeek extraindo os UIDs, portas, bytes, SNI e JA3 das conexoes suspeitas
zeek-cut ts uid id.orig_h id.resp_h id.resp_p proto duration orig_bytes resp_bytes < /nsm/zeek/logs/current/conn.log \
  | awk '$3 == "10.20.4.55"' | head -n 20
```

## Limites e trade-offs
Por que esse fluxo em funil (**RITA -> Zeek -> Arkime -> Endpoint**) é a arquitetura de referência de **Network Threat Hunting** ensinada nos treinamentos de elite de defesa cibernética? Porque você não tenta procurar uma agulha manualmente em 10 Terabytes de arquivos `.pcap` brutos: o **RITA** destila 24 horas de rede nos **5 fluxos matematicamente mais anômalos**, o **Zeek** fornece o contexto de protocolo daqueles 5 fluxos e o **Arkime** entrega a prova forense irrefutável do pacote!

## Como verificar
Documente todo falso positivo legítimo validado na Etapa 4 (ex.: um software específico de engenharia usado apenas por 1 máquina) antes de decidir se deve incluí-lo na safelist do RITA.

## Conexões
- [[rita-operacao-continua-rolling-datasets-zeek-cron-automacao-soc]] — Veja também: Operação Contínua no SOC com **Rolling Datasets (`--rolling` vs. `--rebuild`)**, Exportação CSV (`--stdout`) e Integração de Alertas RITA no SIEM.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[arkime-integracao-zeek-suricata-snort-malcolm-correlacao-community-id]] — Referência cruzada direta com arkime-integracao-zeek-suricata-snort-malcolm-correlacao-community-id.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
