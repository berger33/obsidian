---
id: software.seguranca.tranche12.001107
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md", "https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Triagem de Alertas de Antivírus/EDR (**Windows Defender, Sophos, F-Secure e Kaspersky**) e Limpeza de Logs com as Regras Nativas do Chainsaw

## Em uma frase
Em muitos incidentes de ransomware, o atacante passa horas tentando executar diferentes ferramentas de pós-exploração (`Mimikatz`, `Cobalt Strike`, `SharpHound`, `Chisel`) que são inicialmente bloqueadas pelo **Windows Defender** ou pelo antivírus local antes de o invasor conseguir desabilitar a proteção em tempo real (`Tamper Protection` / `DisableRealtimeMonitoring`).

## Por que importa
As regras nativas do Chainsaw (`rules/antivirus/`) extraem e estruturam automaticamente todos os alertas históricos registrados nos canais de Event Log de **Windows Defender (`Microsoft-Windows-Windows Defender/Operational.evtx`, Event IDs `1116`, `1117`, `5001`, `5007`)**, **Sophos**, **F-Secure** e **Kaspersky**, mostrando em uma única tabela exatamente qual malware foi detectado, em qual caminho (`Path`), por qual processo e se a ação de bloqueio falhou!

## Como funciona
Paralelamente, as regras nativas em `rules/event_logs/` identificam imediatamente se o invasor limpou o log de Segurança (`EventID 1102` em `Security.evtx`), limpou qualquer outro canal (`EventID 104` em `System.evtx`) ou parou o serviço de Event Log (`EventID 1100`)!

## Exemplo
```bash
# Executar especificamente as regras nativas do Chainsaw para extrair todos os alertas de Antivirus e tentativas de limpeza de logs
chainsaw hunt ./evtx_triage/ \
  -r ./chainsaw/rules/antivirus/ \
  -r ./chainsaw/rules/event_logs/ \
  --full
```

## Limites e trade-offs
A flag **`--full`** no `chainsaw hunt` impede que valores longos nas colunas da tabela ASCII (como caminhos completos de arquivos em quarentena ou argumentos de linha de comando) sejam truncados na tela.

## Como verificar
Sempre comece sua triagem forense rodando as regras de `antivirus` e `event_logs`: elas revelam em menos de 5 segundos o "paciente zero", a pasta de staging usada pelo atacante e o timestamp exato em que o invasor tentou apagar seus rastros!

## Conexões
- [[chainsaw-dump-artefatos-mft-registry-esedb-json-analise-forense]] — Veja também: Extração Bruta e Conversão de Artefatos (**`$MFT`**, Hives de Registro e Bancos ESE) para JSON com **`chainsaw dump`**.
- [[chainsaw-autoria-regras-customizadas-tau-filter-document-fields]] — Veja também: Autoria de **Regras Nativas do Chainsaw** e Mapeamentos Customizados no Formato **TAU Engine** (`filter`, `group`, `fields`).
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Referência cruzada direta com chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx.
- [[hayabusa-canais-evtx-essenciais-sysmon-powershell-rdp-defender-wmi]] — Referência cruzada direta com hayabusa-canais-evtx-essenciais-sysmon-powershell-rdp-defender-wmi.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
