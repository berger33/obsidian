---
id: software.seguranca.tranche11.001092
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

# Geração de Timelines no Hayabusa (`csv-timeline`, `json-timeline`, `dfir-timeline`): **Perfis de Saída (`list-profiles`)** e Integração Direta com **Timesketch & Elastic**

## Em uma frase
Durante uma resposta a um incidente de Ransomware ou APT em ambiente Windows Active Directory, diferentes ferramentas de análise exigem formatos e colunas diferentes da timeline de eventos.

## Por que importa
O Hayabusa resolve isso com seus **Perfis de Saída (`hayabusa list-profiles` e `-p` / `--profile`)**: **(1) `standard` (padrão)** — exibe `Timestamp`, `Computer`, `Channel`, `EventID`, `Level`, `RecordID`, `RuleTitle` e um resumo inteligente de **`Details`** (que extrai e formata automaticamente apenas os campos mais relevantes daquele EventID, como `Cmdline`, `User`, `SrcIP`, `LogonType`, `TargetUser`!); **(2) `verbose` / `all-field-info`** — inclui os metadados completos do evento; **(3) `timesketch-minimal` e `timesketch-verbose`** — geram saída JSONL com os campos obrigatórios (`datetime`, `timestamp_desc`, `message`, `tag`) prontos para importação direta no **Google Timesketch**!; e **(4) `super-verbose`**!

## Como funciona
Além disso, você filtra a severidade mínima com **`-m` / `--min-level`** (`informational`, `low`, `medium`, `high`, `critical`) e habilita regras ruidosas/experimentais com `--enable-all-rules`!

## Exemplo
```bash
# Listar os perfis de saida disponiveis e gerar uma timeline JSONL no perfil nativo do Google Timesketch (--profile timesketch-verbose)
hayabusa list-profiles
hayabusa json-timeline \
  --directory /cases/dfir/evtx_collection \
  --profile timesketch-verbose \
  --JSONL-output \
  --min-level low \
  --output /cases/dfir/hayabusa_timesketch.jsonl
```

## Limites e trade-offs
Por que a coluna **`Details`** formatada pelo Hayabusa no perfil `standard` economiza horas de trabalho no **Timeline Explorer**? Porque nos logs `.evtx` brutos do Windows, o nome de usuário pode estar em `SubjectUserName`, `TargetUserName` ou `User` dependendo do EventID, e o comando pode estar enterrado em um XML de 40 linhas — o Hayabusa normaliza tudo em uma linha legível `User: CORP\admin ¦ Cmdline: powershell -enc ...`!

## Como verificar
Use a flag `--ISO-8601` ou `--UTC` para garantir que todos os timestamps da timeline estejam padronizados em UTC antes de cruzar com logs de firewall ou Linux.

## Conexões
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Veja também: **Yamato Security Hayabusa (`Yamato-Security/hayabusa`)**: Arquitetura em **Rust** para Threat Hunting e Geração Ultrarrápida de **Timelines Forenses Windows (`.evtx`)** com **Sigma v2**.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Veja também: Triagem Rápida de Incidentes com Hayabusa: **`logon-summary`**, **`computer-metrics`**, **`eid-metrics`**, **`log-metrics`** e **`config-critical-systems`**.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
