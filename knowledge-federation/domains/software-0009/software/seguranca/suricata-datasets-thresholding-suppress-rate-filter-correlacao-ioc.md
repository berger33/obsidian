---
id: software.seguranca.tranche02.000200
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://docs.suricata.io/en/latest/what-is-suricata.html", "https://raw.githubusercontent.com/OISF/suricata/main/README.md", "https://github.com/OISF/suricata"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Suricata `Datasets`, `Thresholds`, `Suppress` e `Flowbits`: correlação de estado entre pacotes, listas dinâmicas e controle de ruído

## Em uma frase
O motor de detecção do Suricata inclui quatro recursos de estado para correlação avançada e controle de volume de alertas: **`flowbits`** (marca estado dentro de um fluxo entre múltiplas requisições/respostas), **`datasets` / `datarep`** (conjuntos em memória de milhões de domínios, IPs ou strings atualizáveis a quente via `suricatasc`), **`threshold` / `detection_filter`** (limita alertas repetitivos por IP de origem/destino) e **`suppress`** (em `threshold.config`, silencia um SID para IPs específicos).

## Por que importa
Quando um scanner de vulnerabilidades interno autorizado varre a rede toda noite, ele acionará milhares de alertas no Suricata se o IP do scanner não estiver em uma diretiva `suppress` no `/etc/suricata/threshold.config`.

## Como funciona
Usando `suppress gen_id 1, sig_id <SID>, track by_src, ip <IP_SCANNER>` em `threshold.config`, a assinatura continua ativa para qualquer outro host da rede enquanto ignora apenas o IP autorizado. E com **`datasets`**, você pode alimentar feeds dinâmicos de domínios de phishing/DGA ou criar regras de detecção de * first-seen* (alertar a primeira vez que um User-Agent ou domínio nunca visto antes aparece na rede)!

## Exemplo
```text
# Exemplo no arquivo /etc/suricata/threshold.config:
# 1. Suprime alertas de scan da regra 2001219 originados do scanner interno autorizado (10.20.30.40):
suppress gen_id 1, sig_id 2001219, track by_src, ip 10.20.30.40

# 2. Limita o envio de alertas da regra 2100498 a no máximo 1 alerta a cada 60 segundos por IP de origem:
event_filter gen_id 1, sig_id 2100498, type limit, track by_src, count 1, seconds 60
```

## Limites e trade-offs
Gerencie entradas de `datasets` dinamicamente em tempo de execução sem sequer recarregar as regras usando `suricatasc -c "dataset-add <nome> <tipo> <valor base64>"`.

## Como verificar
Valide seu arquivo `/etc/suricata/threshold.config` executando `suricata -T -c /etc/suricata/suricata.yaml`.

## Conexões
- [[suricata-analise-offline-pcap-replay-regressao-ci-unix-socket]] — Veja também: Suricata Análise Forense de `PCAP` (`-r`) e Automação via Unix Socket (`suricatasc`): processamento em lote de capturas de tráfego.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
