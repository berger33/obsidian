---
id: software.seguranca.tranche11.001097
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

# Os **10 Canais de Log Windows (`.evtx`) Mais Valiosos** Analisados pelo Hayabusa: Muito Além de `Security.evtx`, `System.evtx` e `Application.evtx`

## Em uma frase
Um erro clássico de administradores que configuram coletores de log no Windows é coletar apenas os 3 arquivos tradicionais (`Security.evtx`, `System.evtx` e `Application.evtx`) e ignorar as dezenas de **Canais de Logs de Aplicativos e Serviços (`Applications and Services Logs/Microsoft/Windows/...`)** que ficam em `C:\Windows\System32\winevt\Logs\`!

## Por que importa
As regras Sigma do Hayabusa tiram proveito máximo desses canais especializados do Windows para detectar técnicas que **não deixam rastro no `Security.evtx`**:

## Como funciona
Veja os 7 canais adicionais indispensáveis que o Hayabusa analisa automaticamente: **(1) `Microsoft-Windows-Sysmon%4Operational.evtx`** (criação de processo com hashes, rede, DNS, injeção em LSASS EventID 10); **(2) `Microsoft-Windows-PowerShell%4Operational.evtx`** (`EventID 4104` *Script Block Logging* — grava o código desofuscado de scripts PowerShell em memória!); **(3) `Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx` & `RemoteConnectionManager`** (sessões RDP, reconexões e IPs de origem); **(4) `Microsoft-Windows-TaskScheduler%4Operational.evtx`** (persistência via Tarefas Agendadas); **(5) `Microsoft-Windows-WMI-Activity%4Operational.evtx`** (persistência e execução remota WMI EventID 5861); **(6) `Microsoft-Windows-Windows Defender%4Operational.evtx`** (histórico de detecções de malware e exclusões adicionadas pelo atacante!); e **(7) `Microsoft-Windows-Bits-Client%4Operational.evtx`** (downloads furtivos via `bitsadmin`)!

## Exemplo
```bash
# Filtrar a analise do Hayabusa por um intervalo de tempo especifico do incidente (--timeline-start e --timeline-end)
hayabusa csv-timeline \
  --directory /cases/dfir/evtx_collection \
  --timeline-start "2026-10-01 00:00:00 +00:00" \
  --timeline-end "2026-10-03 23:59:59 +00:00" \
  --output /cases/dfir/timeline_janela_incidente.csv
```

## Limites e trade-offs
Dica de **Hardening de Logging Windows (Pré-Incidente)** para garantir que o Hayabusa encontre evidências ricas: habilite por GPO em todas as estações e servidores o **PowerShell Script Block Logging (`EventID 4104`)**, a **Auditoria de Linha de Comando no `EventID 4688` (`Include command line in process creation events`)**, o canal **`TaskScheduler/Operational`** e aumente o tamanho máximo do `Security.evtx` para pelo menos **512 MB a 1 GB**!

## Como verificar
Use `--timeline-start` e `--timeline-end` no Hayabusa quando quiser focar a timeline exatamente na janela temporal suspeita.

## Conexões
- [[hayabusa-coleta-remota-escala-velociraptor-kape-live-analysis]] — Veja também: Caça a Ameaças em Escala Corporativa: Integrando **Hayabusa** com **Rapid7 Velociraptor** e **KAPE** + Execução **`--live-analysis`**.
- [[hayabusa-enriquecimento-geoip-maxmind-mmdb-conexoes-externas-rdp]] — Veja também: Enriquecimento Automático de **GeoIP (`MaxMind GeoLite2 .mmdb`)** no Hayabusa: Identificando Logons RDP, SMB e Conexões de Rede de Países Incomuns.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Referência cruzada direta com hayabusa-comandos-analise-metricas-logon-summary-critical-systems.
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Referência cruzada direta com sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
