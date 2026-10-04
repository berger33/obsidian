---
id: software.seguranca.tranche11.001094
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

# Caça a Payloads Ocultos nos Logs `.evtx` com Hayabusa: **`extract-base64`**, **`pivot-keywords-list`** e **`search` (Keywords / Regex)**

## Em uma frase
Atacantes que operam em ambientes Windows utilizam extensivamente comandos codificados em **Base64** (em argumentos do `powershell.exe -EncodedCommand`, em tarefas agendadas, em consumidores WMI ou em blocos de script do **PowerShell Operational `EventID 4104`**).

## Por que importa
Para acelerar a descoberta de artefatos sem precisar esperar uma timeline completa, o Hayabusa fornece três comandos de caça cirúrgica (`Analysis Commands`): **(1) `hayabusa extract-base64`** — varre todos os arquivos `.evtx`, localiza automaticamente strings codificadas em Base64 (tanto ASCII/UTF-8 quanto UTF-16LE do PowerShell!), **decodifica o conteúdo automaticamente** e exibe a tabela com o timestamp, computador, EventID, string original e o payload decodificado legível!; **(2) `hayabusa pivot-keywords-list`** — extrai das detecções críticas uma lista pronta de **Palavras-Chave Suspeitas (Contas, IPs, Nomes de Processos, Serviços e Tarefas)** para você usar como pivô de investigação!;

## Como funciona
e **(3) `hayabusa search`** — busca ultrarrápida por palavras-chave ou expressões regulares PCRE (`-r` / `--regex`) em todos os campos de todos os `.evtx`!

## Exemplo
```bash
# Extrair e decodificar automaticamente payloads Base64 nos logs .evtx, gerar lista de pivos e buscar por regex em todos os eventos
hayabusa extract-base64 --directory /cases/dfir/evtx_collection
hayabusa pivot-keywords-list \
  --directory /cases/dfir/evtx_collection \
  --output /cases/dfir/pivos_suspeitos.txt
hayabusa search \
  --directory /cases/dfir/evtx_collection \
  --regex "(sekurlsa|lsadump|kerberoast|dcsync|rubeus|chisel)"
```

## Limites e trade-offs
Veja como o fluxo **`pivot-keywords-list` -> `search`** funciona em uma investigação real: primeiro você roda `pivot-keywords-list`, que identifica que o IP interno `10.20.30.55` ou um binário `svc_update.exe` apareceu em um alerta crítico em um servidor; em seguida, você roda `hayabusa search -d /cases/dfir/evtx_collection -k "10.20.30.55"` para encontrar **todos os eventos (inclusive eventos informativos normais sem alerta Sigma!)** em que aquele IP ou arquivo apareceu em todas as máquinas da empresa!

## Como verificar
Isso garante que você reconstrua 100% dos passos do invasor antes e depois do alerta inicial.

## Conexões
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Veja também: Triagem Rápida de Incidentes com Hayabusa: **`logon-summary`**, **`computer-metrics`**, **`eid-metrics`**, **`log-metrics`** e **`config-critical-systems`**.
- [[hayabusa-calibracao-regras-level-tuning-expand-list-custom-rules]] — Veja também: Calibração de Severidade e Regras no Hayabusa: **`level-tuning`**, **`expand-list`**, Perfis de Status (`--status`) e Regras Sigma Customizadas (`--rules`).
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Referência cruzada direta com sigma-logica-detection-modificadores-valores-base64offset-windash-re.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
