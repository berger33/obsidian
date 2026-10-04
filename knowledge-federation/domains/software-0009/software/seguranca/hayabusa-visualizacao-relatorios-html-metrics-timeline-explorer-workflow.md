---
id: software.seguranca.tranche11.001100
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

# Workflow Completo de DFIR com Hayabusa (Marco **1.100/2.000** do Lote `software-seguranca-2000-0003`): Relatório Executivo HTML (`-H`), Timeline Explorer e `jq`

## Em uma frase
Ao alcançarmos a **Nota 1.100 de 2.000 (55,00%)** do lote `software-seguranca-2000-0003`, consolidamos o workflow operacional completo de **Fast Forensics em Windows Event Logs** com o **Hayabusa**:

## Por que importa
Quando você executa `hayabusa csv-timeline` ou `json-timeline`, adicione sempre a flag **`-H` / `--html-report <caminho.html>`**: além de gerar a timeline detalhada de eventos, o Hayabusa compila um **Relatório Executivo em HTML** autocontido com o resumo geral da investigação, principais alertas por severidade (`critical`, `high`, `medium`, `low`), máquinas com mais detecções e estatísticas de regras!

## Como funciona
Em seguida, abra o `.csv` no **Timeline Explorer** (ou processe o `.jsonl` no terminal Linux com **`jq`** / importe no **Timesketch**) para conduzir a análise cronológica de causa raiz (*Root Cause Analysis — Paciente Zero*) até a erradicação completa!

## Exemplo
```bash
# Workflow completo de Fast Forensics com Hayabusa: gerar simultaneamente a Timeline JSONL e o Relatorio Executivo HTML (-H) e analisar com jq
hayabusa json-timeline \
  --directory /cases/dfir/evtx_collection \
  --JSONL-output \
  --html-report /cases/dfir/resumo_executivo_hayabusa.html \
  --output /cases/dfir/timeline_completa.jsonl

jq -r 'select(.Level == "crit" or .Level == "high") | "\(.Timestamp) [\(.Level)] \(.Computer) - \(.RuleTitle): \(.Details)"' \
  /cases/dfir/timeline_completa.jsonl | head -n 25
```

## Limites e trade-offs
Por que a dupla **SigmaHQ (Padrão Aberto de Regras)** + **Hayabusa (Motor Rust de Timeline e Correlação Sigma v2)** fecha com chave de ouro esta Tranche 11? Porque ela une a inteligência coletiva de mais de 3.000 regras da comunidade mundial com uma execução local ultrarrápida, auditável e independente de SIEM comercial.

## Como verificar
Mantenha um pendrive/pacote de resposta a incidentes atualizado com o binário estático do `hayabusa`, o conjunto `hayabusa-rules` e os bancos `GeoLite2.mmdb` pronto para uso offline em ambientes isolados (*air-gapped*).

## Conexões
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Veja também: Caçando Ataques contra **Active Directory** nos Logs `.evtx` com Hayabusa: **DCSync (`4662`), Kerberoasting (`4769`), AS-REP Roasting (`4768`), Pass-the-Hash e NTLM Relay**.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Referência cruzada direta com hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
