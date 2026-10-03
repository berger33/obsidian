---
id: software.seguranca.tranche11.001098
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md", "https://yamato-security.github.io/hayabusa/commands/", "https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Enriquecimento Automático de **GeoIP (`MaxMind GeoLite2 .mmdb`)** no Hayabusa: Identificando Logons RDP, SMB e Conexões de Rede de Países Incomuns

## Em uma frase
Ao investigar milhares de eventos de autenticação remota (**RDP `EventID 4624/4625/1149`**) ou conexões de saída registradas pelo **Sysmon (`EventID 3`)** e Firewall do Windows (`EventID 5156`), enxergar apenas endereços IPv4/IPv6 numéricos (`185.220.101.45`) dificulta separar acessos legítimos de funcionários no Brasil de acessos originados em VPS estrangeiras ou nós de saída Tor.

## Por que importa
Por isso o Hayabusa traz integrado em Rust o leitor nativo **`maxminddb`** (visível no `Cargo.toml` oficial)!

## Como funciona
Ao passar os bancos gratuitos **MaxMind GeoLite2 (`GeoLite2-City.mmdb`, `GeoLite2-Country.mmdb` e `GeoLite2-ASN.mmdb`)**, o Hayabusa enriquece automaticamente os endereços IP públicos presentes nos eventos `.evtx` com o **País, Cidade e ASN (Provedor de Hospedagem / Telecom)** diretamente na linha da timeline!

## Exemplo
```bash
# Executar o Hayabusa enriquecendo enderecos IP publicos nos eventos .evtx com bancos MaxMind GeoLite2 (.mmdb)
hayabusa csv-timeline \
  --directory /cases/dfir/evtx_collection \
  --geo-ip /opt/maxmind/ \
  --output /cases/dfir/timeline_com_geoip.csv
```

## Limites e trade-offs
Por que o enriquecimento de **ASN (`GeoLite2-ASN.mmdb`)** é ainda mais útil que o país em investigações de DFIR? Porque um atacante sofisticado pode alugar uma VPS em um datacenter localizado em São Paulo (mesmo país da vítima!), mas enquanto os funcionários legítimos conectam a partir de **ASNs de operadoras residenciais/móveis (Claro, Vivo, TIM)**, o atacante conecta a partir de um **ASN de Provedor de Datacenter/Cloud/VPS** — que salta aos olhos imediatamente na coluna de ASN do Hayabusa!

## Como verificar
Como a consulta ao arquivo `.mmdb` ocorre 100% em memória local, nenhum endereço IP do caso confidencial é enviado para APIs externas na internet.

## Conexões
- [[hayabusa-canais-evtx-essenciais-sysmon-powershell-rdp-defender-wmi]] — Veja também: Os **10 Canais de Log Windows (`.evtx`) Mais Valiosos** Analisados pelo Hayabusa: Muito Além de `Security.evtx`, `System.evtx` e `Application.evtx`.
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Veja também: Caçando Ataques contra **Active Directory** nos Logs `.evtx` com Hayabusa: **DCSync (`4662`), Kerberoasting (`4769`), AS-REP Roasting (`4768`), Pass-the-Hash e NTLM Relay**.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Referência cruzada direta com hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Referência cruzada direta com hayabusa-comandos-analise-metricas-logon-summary-critical-systems.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
