---
id: software.seguranca.tranche11.001099
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

# Caçando Ataques contra **Active Directory** nos Logs `.evtx` com Hayabusa: **DCSync (`4662`), Kerberoasting (`4769`), AS-REP Roasting (`4768`), Pass-the-Hash e NTLM Relay**

## Em uma frase
Lembra das ferramentas ofensivas de Active Directory que estudamos na Tranche 6 (**Responder**, **Fortra Impacket** e **NetExec**) e no **BloodHound CE** na Tranche 5?

## Por que importa
Como o **Hayabusa** detecta cada um desses ataques nos arquivos `.evtx` dos **Domain Controllers** e servidores Windows?

## Como funciona
Veja o mapeamento exato de detecção que o Hayabusa executa automaticamente: **(1) DCSync (`secretsdump.py` do Impacket)**: detectado no **`EventID 4662`** do Domain Controller quando uma conta que não é um DC solicita as propriedades de replicação `Replicating Directory Changes All` (`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2`); **(2) Kerberoasting (`GetUserSPNs.py`)**: detectado no **`EventID 4769`** (solicitação de Service Ticket TGS Kerberos) quando o tipo de criptografia solicitado sofre downgrade para **RC4 (`TicketEncryptionType: 0x17`)** em contas de serviço!; **(3) AS-REP Roasting (`GetNPUsers.py`)**: detectado no **`EventID 4768`** com `PreAuthType: 0` e `0x17`; e **(4) Pass-the-Hash / Overpass-the-Hash**: detectado no **`EventID 4624`** com `LogonType: 9` (`NewCredentials` / `seclogon`) ou `LogonType: 3` com `AuthenticationPackageName: NTLM`!

## Exemplo
```bash
# Gerar a timeline forense dos logs .evtx de um Domain Controller filtrando alertas de alta/critica severidade e sumario de logons
hayabusa csv-timeline \
  --directory /cases/dfir/dc01_evtx \
  --min-level high \
  --output /cases/dfir/dc01_high_alerts.csv
```

## Limites e trade-offs
Quando o Hayabusa processa os `.evtx` de múltiplos Domain Controllers com regras de **Correlação Sigma v2 (`event_count` / `value_count`)**, ele identifica não apenas uma solicitação isolada `4769` com RC4 (`0x17`), mas também o disparo em rajada de dezenas de solicitações `4769` para SPNs diferentes em poucos segundos pelo mesmo usuário — assinatura inequívoca de automação com Impacket/Rubeus/NetExec!

## Como verificar
Cruze os usuários e computadores sinalizados pelo Hayabusa no Domain Controller com o grafo do **BloodHound CE** para visualizar quais caminhos de privilégio o atacante percorreu.

## Conexões
- [[hayabusa-enriquecimento-geoip-maxmind-mmdb-conexoes-externas-rdp]] — Veja também: Enriquecimento Automático de **GeoIP (`MaxMind GeoLite2 .mmdb`)** no Hayabusa: Identificando Logons RDP, SMB e Conexões de Rede de Países Incomuns.
- [[hayabusa-visualizacao-relatorios-html-metrics-timeline-explorer-workflow]] — Veja também: Workflow Completo de DFIR com Hayabusa (Marco **1.100/2.000** do Lote `software-seguranca-2000-0003`): Relatório Executivo HTML (`-H`), Timeline Explorer e `jq`.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
