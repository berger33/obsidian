---
id: software.seguranca.tranche14.001361
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

# Arquitetura do **RITA (`activecm/rita` — *Real Intelligence Threat Analytics*)**: Caça a Ameaças (**Threat Hunting**) em Logs **Zeek** para Detecção de **C2 Beaconing**

## Em uma frase
Quando um implante moderno de Comando e Controle (**Cobalt Strike, Sliver, Havoc, Brute Ratel, Mythic**) infecta uma estação corporativa, ele raramente mantém uma conexão TCP aberta o tempo todo (que seria fácil de ver no `netstat`) e quase sempre usa **HTTPS (TLS 1.3)** para um domínio legítimo em CDN (*Domain Fronting* / *Redirectors*). Se o payload é 100% criptografado com TLS 1.3 e o certificado é válido, **como detectar o canal de Comando e Controle na rede sem precisar quebrar o TLS**?

## Por que importa
Analisando matematicamente o **Comportamento Temporal e Volumétrico das Conexões (`C2 Beaconing`)** com o **RITA (*Real Intelligence Threat Analytics*)**, mantido pela **Active Countermeasures**!

## Como funciona
Escrito em **Go** (e utilizando **ClickHouse** nas versões modernas v5+ como banco analítico colunar de altíssima velocidade!), o **RITA** ingere os logs gerados pelo **Zeek (`conn.log`, `dns.log`, `http.log`, `ssl.log`)** em formato TSV ou JSON e aplica algoritmos estatísticos sobre janelas de 24 horas para identificar: **(1) `C2 Beaconing` (IP, SNI/FQDN e Strobe)**, **(2) `Long Connections`**, **(3) `DNS Tunneling` (`exploded dns` / muitos subdomínios únicos)** e **(4) `Threat Intel` / `Prevalence` (*Outliers* raros na rede)**!

## Exemplo
```bash
# Importar 24 horas de logs do Zeek em um dataset do RITA (--rebuild) e visualizar os resultados no terminal TUI ou em CSV (--stdout)
rita import --database=rede_corporativa --logs=/nsm/zeek/logs/2026-10-03/ --rebuild
rita view rede_corporativa
rita view rede_corporativa --stdout > ./relatorio_caca_rita.csv
```

## Limites e trade-offs
Por que o modelo do RITA (que analisa **24 horas completas de logs `Zeek`** de uma vez ou em modo contínuo `--rolling`) encontra implantes furtivos que passam invisíveis por NIDS de assinatura (Snort/Suricata) e por regras de correlação de 5 minutos do SIEM? Porque um implante configurado com *Sleep = 15 minutos e Jitter = 20%* só faz 96 conexões ao longo de um dia inteiro — invisível em uma janela curta de 5 minutos, mas **estatisticamente óbvio quando o RITA analisa o histograma de intervalos de 24 horas**!

## Como verificar
Você pode gerar logs do Zeek a partir de qualquer arquivo `.pcap` (`zeek -r captura.pcap local`) e importá-los imediatamente no RITA para investigar incidentes forenses!

## Conexões
- [[rita-matematica-deteccao-beacons-intervalos-jitter-tamanho-score]] — Veja também: A Matemática da Detecção de **Beaconing C2 (Com e Sem *Jitter*)** no RITA: Desvio de Intervalos (`Delta Times`), Simetria de Bytes, dispersão MADM e Score.
- [[rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting]] — Referência cruzada direta com rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting.

## Fontes
- [RITA (`activecm/rita`) Official GitHub — Real Intelligence Threat Analytics](https://raw.githubusercontent.com/activecm/rita/main/README.md) — repositório oficial do framework RITA cobrindo ingestão de logs Zeek (`import --rolling` / `--rebuild`), detecção de C2 Beaconing, Long Connections, DNS Tunneling e exportação `--stdout`; consultado em 2026-10-03.
- [RITA Official Configuration Reference (`docs/Configuration.md` — `config.hjson`)](https://raw.githubusercontent.com/activecm/rita/main/docs/Configuration.md) — documentação oficial do `/etc/rita/config.hjson` detalhando `scoring.beacon`, `long_connection`, `c2` (DNS subdomínios), `strobe_impact`, `threat_intel_impact`, `modifiers` (`prevalence`, `first_seen`, `missing_host_count`) e `filter.internal_subnets`; consultado em 2026-10-03.
