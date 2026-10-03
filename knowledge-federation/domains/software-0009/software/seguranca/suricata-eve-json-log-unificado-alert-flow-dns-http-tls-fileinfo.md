---
id: software.seguranca.tranche02.000192
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

# Suricata `EVE JSON` (`eve.json`): telemetria unificada de alertas, fluxos (`flow`), `dns`, `http`, `tls`, `ssh`, `smb` e `fileinfo`

## Em uma frase
O formato de saída padrão e mais poderoso do Suricata é o **`EVE JSON` (*Extensible Event Format*, gravado em `/var/log/suricata/eve.json`)**, que emite em um único stream JSON Lines correlacionado por **`flow_id`** e **`community_id`** tanto os alertas de assinaturas (`"event_type": "alert"`) quanto os logs completos de protocolo NSM (`"dns"`, `"http"`, `"tls"`, `"quic"`, `"ssh"`, `"smb"`, `"krb5"`, `"rdp"`, `"fileinfo"`, `"anomaly"`, `"flow"`, `"netflow"`, `"stats"`).

## Por que importa
Receber apenas um alerta isolado dizendo "Possível Trojan na porta 443" sem saber qual domínio DNS foi consultado milissegundos antes, qual era o SNI/certificado TLS e quantos bytes foram transferidos naquela conexão atrasa drasticamente a investigação do SOC.

## Como funciona
No `eve.json` do Suricata, todos os eventos gerados pela mesma conexão TCP/UDP compartilham o mesmo número **`flow_id`** (e opcionalmente o hash padrão **`community_id` v1** compatível com Zeek/Corelight/Elastic): basta filtrar no SIEM/jq por `flow_id` para reconstruir toda a sessão de rede!

## Exemplo
```bash
# Filtrando em tempo real no eve.json os alertas e os metadados TLS/DNS associados usando jq:
tail -f /var/log/suricata/eve.json | jq 'select(.event_type=="alert" or .event_type=="tls") | {timestamp, event_type, flow_id, src_ip, dest_ip, alert: .alert.signature, sni: .tls.sni}'
```

## Limites e trade-offs
Habilite `community-id: true` na seção `eve-log` do `suricata.yaml` para gerar o hash de 5-tupla compatível entre Suricata, Zeek e coletores Elastic/OpenSearch/Splunk.

## Como verificar
Inspecione os tipos de eventos ativos no seu `eve.json` com `jq -r .event_type /var/log/suricata/eve.json | sort | uniq -c`.

## Conexões
- [[suricata-arquitetura-oisf-network-ids-ips-nsm-multithreaded]] — Veja também: OISF Suricata: arquitetura multi-thread de alta performance para `IDS`, `IPS` e `Network Security Monitoring (NSM)`.
- [[suricata-gerenciamento-regras-suricata-update-et-open-fontes]] — Veja também: Suricata Gerenciamento de Regras (`suricata-update`): atualização automatizada do *Emerging Threats Open (ET Open)* e tuning via `enable.conf`/`disable.conf`/`modify.conf`.

## Fontes
- [OISF Suricata Official Documentation — What is Suricata (Multi-Threaded IDS/IPS/NSM Engine, EVE JSON Telemetry, Protocol Parsers & File Extraction)](https://docs.suricata.io/en/latest/what-is-suricata.html) — Documentação oficial da OISF explicando a arquitetura multi-thread do Suricata como IDS, IPS e NSM, logs estruturados EVE JSON, inspeção TLS e extração de arquivos; consultado em 2026-10-03.
- [OISF Suricata GitHub — README.md (High-Performance Network Threat Detection Engine, Rust Parsers, AF_PACKET/eBPF IPS & PCAP Processing)](https://raw.githubusercontent.com/OISF/suricata/main/README.md) — README oficial do OISF/suricata detalhando recursos de captura de pacotes em alta velocidade, segurança de memória com Rust, testes de regressão e operação via Unix Socket; consultado em 2026-10-03.
- [OISF Suricata — Official GitHub Repository](https://github.com/OISF/suricata) — Repositório oficial GPL-2.0 do OISF Suricata; consultado em 2026-10-03.
