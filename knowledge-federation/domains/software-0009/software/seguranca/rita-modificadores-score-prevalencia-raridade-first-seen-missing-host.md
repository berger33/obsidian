---
id: software.seguranca.tranche14.001366
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

# Modificadores Inteligentes de Score (**`modifiers`**) no RITA: **Prevalência na Rede (`prevalence`)**, **`first_seen`** e **`missing_host_count` (Conexões Diretas a IP Sem DNS)**

## Em uma frase
Como o **RITA v5+** diferencia um serviço legítimo de telemetria corporativa (como o agente do antivírus ou do Windows Update instalado em todas as 500 máquinas da empresa, que faz *check-in* periódico a cada 10 minutos) de um **implante de C2 real** que infectou apenas 1 ou 2 máquinas da rede?

## Por que importa
Através do motor de **Modificadores Contextuais de Score (`scoring.modifiers`)** no `/etc/rita/config.hjson`!

## Como funciona
Veja os 4 modificadores inteligentes que ajustam a nota final de risco no RITA: **(1) `prevalence` (Prevalência / Raridade na Rede Interna)** — se **menos de `2%`** dos hosts internos se comunicam com aquele destino externo (`prevalence_score_increase.threshold: 0.02`), o RITA **soma `+15` pontos de risco** (pois C2s reais são raros na rede!); já se **mais de `50%`** das máquinas da empresa falam com aquele destino (`prevalence_score_decrease.threshold: 0.50`), o RITA **desconta `-25` pontos** (pois provavelmente é infraestrutura padrão da empresa!)!; **(2) `first_seen`** — destinos recém-vistos pela primeira vez nos últimos 7 dias ganham **`+15` pontos**!; **(3) `missing_host_count`** — conexões HTTP/HTTPS que conectam direto a um endereço IP sem cabeçalho `Host` / sem resolução DNS prévia ganham **`+10` pontos**!; e **(4) `rare_signature`** (User-Agent ou assinatura TLS rara para aquele host)!

## Exemplo
```hjson
// Modificadores contextuais de pontuacao de risco no /etc/rita/config.hjson do RITA (Prevalencia, First Seen e Conexao Direta a IP)
scoring: {
  modifiers: {
    prevalence_score_increase: {
      score: 15
      threshold: 0.02
    }
    prevalence_score_decrease: {
      score: -25
      threshold: 0.50
    }
    first_seen_score_increase: {
      score: 15
      threshold: 7
    }
    missing_host_count_score_increase: {
      score: 10
      threshold: 1
    }
  }
}
```

## Limites e trade-offs
Por que o modificador **`missing_host_count_score_increase`** é tão valioso na caça a ameaças? Porque usuários humanos usando navegadores sempre digitam nomes de domínio (que geram uma consulta DNS e preenchem o SNI / Host Header), enquanto shells reversos, *stagers* de malware e *scanners* frequentemente conectam diretamente a um **endereço IP hardcoded (`https://198.51.100.44:443`) sem enviar SNI nem fazer consulta DNS**!

## Como verificar
Para que o modificador **`first_seen`** funcione ao longo das semanas, importe seus logs do Zeek diariamente usando a flag **`--rolling`** (`rita import --database=empresa --logs=... --rolling`), que mantém o histórico contínuo de primeira aparição de cada domínio e IP externo!

## Conexões
- [[rita-deteccao-dns-tunneling-subdominios-unicos-iodine-dnscat2]] — Veja também: Detecção de **C2 e Exfiltração por DNS Tunneling (`iodine`, `dnscat2`, `sliver dns`, `cobalt strike dns`)** no RITA.
- [[rita-filtros-rede-interna-whitelist-safelist-config-hjson-tuning]] — Veja também: Configuração de Sub-redes Internas (**`internal_subnets`**) e Listas de Exclusão (**`never_included_ips` / `never_included_domains`**) no `/etc/rita/config.hjson`.
- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Referência cruzada direta com rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling.
- [[rita-matematica-deteccao-beacons-intervalos-jitter-tamanho-score]] — Referência cruzada direta com rita-matematica-deteccao-beacons-intervalos-jitter-tamanho-score.
- [[rita-operacao-continua-rolling-datasets-zeek-cron-automacao-soc]] — Referência cruzada direta com rita-operacao-continua-rolling-datasets-zeek-cron-automacao-soc.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
