---
id: software.seguranca.tranche11.001091
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

# **Yamato Security Hayabusa (`Yamato-Security/hayabusa`)**: Arquitetura em **Rust** para Threat Hunting e Geração Ultrarrápida de **Timelines Forenses Windows (`.evtx`)** com **Sigma v2**

## Em uma frase
Criado por Zach Mathis (`@yamatosecurity`) e a equipe da **Yamato Security** no Japão (`Yamato-Security/hayabusa`, licença AGPLv3, escrito em **Rust memory-safe**), o **Hayabusa** (*"Falcão-peregrino"* em japonês) é o gerador de linhas do tempo forenses (**DFIR Timeline**) e motor de **Threat Hunting para Windows Event Logs (`.evtx`)** mais rápido do ecossistema open-source — e a única ferramenta open-source com **suporte completo à especificação Sigma, incluindo Regras de Correlação Sigma v2**!

## Por que importa
Por que o Hayabusa processa gigabytes de arquivos `.evtx` de dezenas ou milhares de máquinas Windows em segundos? Conforme revela o `Cargo.toml` oficial da versão 4.1+, ele combina paralelismo multi-thread (`tokio` + `dashmap` + `mimalloc`), um parser binário `.evtx` otimizado em Rust (`hayabusa-evtx` com `fast-alloc`) e o algoritmo **Aho-Corasick (`aho-corasick`)** + `memchr` para avaliar milhares de regras Sigma e Hayabusa simultaneamente em uma única passagem!

## Como funciona
Ele pode rodar tanto **ao vivo em um endpoint Windows (`--live-analysis`)**, quanto **offline sobre coleções de arquivos `.evtx` (`-d <diretorio>`)** extraídos pelo **Velociraptor** ou KAPE!

## Exemplo
```bash
# Atualizar o repositorio de regras do Hayabusa e gerar uma timeline forense CSV a partir de uma pasta de logs .evtx coletados
hayabusa update-rules
hayabusa csv-timeline \
  --directory /cases/dfir/evtx_collection \
  --output /cases/dfir/hayabusa_timeline.csv
```

## Limites e trade-offs
Na versão 4.x do Hayabusa, você também pode usar o subcomando unificado **`hayabusa dfir-timeline`** (ou `csv-timeline` / `json-timeline`), que consolida eventos de um único host ou de milhares de servidores em uma única timeline pronta para análise no **Eric Zimmerman's Timeline Explorer**, **Timesketch** ou **Elastic Stack**!

## Como verificar
Execute sempre `hayabusa update-rules` antes de iniciar uma nova investigação para sincronizar o conjunto mais recente do repositório `Yamato-Security/hayabusa-rules`.

## Conexões
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Veja também: Geração de Timelines no Hayabusa (`csv-timeline`, `json-timeline`, `dfir-timeline`): **Perfis de Saída (`list-profiles`)** e Integração Direta com **Timesketch & Elastic**.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Referência cruzada direta com hayabusa-comandos-analise-metricas-logon-summary-critical-systems.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.

## Fontes
- [Yamato Security Hayabusa Official GitHub — Windows Event Log Fast Forensics Timeline Generator & Threat Hunting Tool](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/README.md) — repositório oficial do Hayabusa em Rust cobrindo geração de timelines CSV/JSON/JSONL e suporte completo a regras Sigma e correlações v2; consultado em 2026-10-03.
- [Hayabusa Official Documentation — Command Reference (`dfir-timeline`, `logon-summary`, `extract-base64`, `pivot-keywords-list`, `search`)](https://yamato-security.github.io/hayabusa/commands/) — referência oficial de subcomandos de análise, métricas, configuração e geração de timelines do Hayabusa; consultado em 2026-10-03.
- [Hayabusa Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/Yamato-Security/hayabusa/main/Cargo.toml) — especificação técnica dos componentes em Rust do Hayabusa 4.1 (`hayabusa-evtx`, `aho-corasick`, `tokio`, `maxminddb`, `mimalloc`); consultado em 2026-10-03.
