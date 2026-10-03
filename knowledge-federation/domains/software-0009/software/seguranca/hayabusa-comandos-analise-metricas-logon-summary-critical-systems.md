---
id: software.seguranca.tranche11.001093
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

# Triagem Rápida de Incidentes com Hayabusa: **`logon-summary`**, **`computer-metrics`**, **`eid-metrics`**, **`log-metrics`** e **`config-critical-systems`**

## Em uma frase
Quando você recebe um pacote forense com 50 GB de arquivos `.evtx` coletados de 200 máquinas Windows da empresa, por onde começar a investigação antes mesmo de abrir uma timeline de milhões de linhas?

## Por que importa
Conforme listado na documentação oficial de comandos (`yamato-security.github.io/hayabusa/commands/`), o Hayabusa traz cinco subcomandos dedicados de **Triagem Rápida e Métricas Forenses**: **(1) `hayabusa config-critical-systems`** — analisa os logs e identifica automaticamente quais máquinas do conjunto são **Domain Controllers, Servidores de Arquivos ou Sistemas Críticos**!; **(2) `hayabusa logon-summary`** — gera uma tabela consolidada de todos os **Logons Bem-Sucedidos (`EventID 4624`) e Falhos (`EventID 4625`)** separados por usuário, tipo de logon (`3 - Network`, `10 - RemoteInteractive/RDP`, `2 - Interactive`), host de origem e IP!; **(3) `hayabusa eid-metrics`** — mostra a contagem e porcentagem de cada EventID;

## Como funciona
**(4) `hayabusa computer-metrics`**; e **(5) `hayabusa log-metrics`** (mostra o período temporal coberto por cada arquivo `.evtx` para detectar se um log foi apagado ou rotacionado!)!

## Exemplo
```bash
# Identificar automaticamente sistemas criticos (Domain Controllers) na coleta .evtx e gerar o resumo completo de Logons (4624/4625)
hayabusa config-critical-systems --directory /cases/dfir/evtx_collection
hayabusa logon-summary \
  --directory /cases/dfir/evtx_collection \
  --output /cases/dfir/resumo_logons.csv
```

## Limites e trade-offs
Olhe o valor do comando **`hayabusa logon-summary`**: em menos de 10 segundos, ele entrega um mapa completo de **Movimentação Lateral (RDP `LogonType 10` e SMB/WinRM `LogonType 3`)** e tentativas de **Força Bruta (`4625`)** em todo o parque analisado, permitindo identificar imediatamente qual conta comprometida saltou da estação inicial para o Domain Controller!

## Como verificar
E o comando **`hayabusa log-metrics`** revela na hora se o atacante executou `wevtutil cl Security` (`EventID 1102`) ou se o arquivo `Security.evtx` de um servidor tem apenas 2 horas de histórico porque o tamanho máximo do log estava mal configurado.

## Conexões
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Veja também: Geração de Timelines no Hayabusa (`csv-timeline`, `json-timeline`, `dfir-timeline`): **Perfis de Saída (`list-profiles`)** e Integração Direta com **Timesketch & Elastic**.
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Veja também: Caça a Payloads Ocultos nos Logs `.evtx` com Hayabusa: **`extract-base64`**, **`pivot-keywords-list`** e **`search` (Keywords / Regex)**.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo]] — Referência cruzada direta com sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
