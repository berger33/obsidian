---
id: software.seguranca.tranche11.001095
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

# Calibração de Severidade e Regras no Hayabusa: **`level-tuning`**, **`expand-list`**, Perfis de Status (`--status`) e Regras Sigma Customizadas (`--rules`)

## Em uma frase
Em ambientes corporativos onde ferramentas legítimas de administração (como SCCM/MECM, Ansible, Chocolatey ou scripts de logon em PowerShell) geram alertas recorrentes, como o analista de DFIR ajusta os níveis de alerta no Hayabusa sem perder tempo?

## Por que importa
Através dos comandos de configuração de regras do Hayabusa: **(1) `hayabusa level-tuning`** — permite ajustar de forma centralizada o nível de severidade (`level`: `informational`, `low`, `medium`, `high`, `critical`) de regras específicas para adequá-las à realidade do seu ambiente; **(2) `hayabusa expand-list`** — extrai e gerencia os arquivos de placeholders **`|expand` (`%domain_controllers%`, `%admin_users%`, etc.)** da pasta `rules/config/` configurados pelo `config-critical-systems`;

## Como funciona
e **(3) `--rules <diretorio>`** — permite apontar o Hayabusa tanto para a pasta `hayabusa-rules` quanto para o seu próprio repositório privado de regras **Sigma v2**!

## Exemplo
```bash
# Extrair os placeholders de expansao das regras e executar a timeline combinando as regras padrao com regras Sigma customizadas
hayabusa expand-list --rules ./hayabusa-rules
hayabusa csv-timeline \
  --directory /cases/dfir/evtx_collection \
  --rules ./minhas-regras-sigma-corporativas \
  --min-level medium \
  --output /cases/dfir/timeline_custom.csv
```

## Limites e trade-offs
Observe também como o Hayabusa classifica o ruído das regras através de filtros de status e nível: por padrão, regras marcadas como `noisy` (barulhentas) ou `deprecated`/`unsupported` são desativadas para manter a timeline enxuta; se você estiver fazendo um *Threat Hunting* profundo em uma única máquina suspeita e quiser ver absolutamente tudo, adicione **`--enable-all-rules` (`-A`)** e **`--min-level informational`**!

## Como verificar
Execute `hayabusa set-default-profile verbose` se quiser tornar o perfil `verbose` o padrão permanente na sua estação forense.

## Conexões
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Veja também: Caça a Payloads Ocultos nos Logs `.evtx` com Hayabusa: **`extract-base64`**, **`pivot-keywords-list`** e **`search` (Keywords / Regex)**.
- [[hayabusa-coleta-remota-escala-velociraptor-kape-live-analysis]] — Veja também: Caça a Ameaças em Escala Corporativa: Integrando **Hayabusa** com **Rapid7 Velociraptor** e **KAPE** + Execução **`--live-analysis`**.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.
- [[sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo]] — Referência cruzada direta com sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo.
- [[sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork]] — Referência cruzada direta com sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
