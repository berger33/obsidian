---
id: software.seguranca.tranche12.001102
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

# Threat Hunting com **`chainsaw hunt`**: Motor **TAU Engine**, Mapeamentos **`sigma-event-logs-all.yml`** e Regras Nativas do Chainsaw

## Em uma frase
Como o Chainsaw consegue avaliar simultaneamente milhares de regras **Sigma** (originalmente agnósticas de SIEM) e regras nativas do próprio Chainsaw contra dezenas de gigabytes de arquivos `.evtx`, XML ou JSON em segundos?

## Por que importa
No subcomando **`chainsaw hunt`**, você fornece o diretório de regras Sigma (`-s sigma/`), o arquivo de mapeamento YAML (**`-m mappings/sigma-event-logs-all.yml`**) e opcionalmente o diretório de regras nativas do Chainsaw (**`-r rules/`**); o arquivo de mapeamento instrui o **TAU Engine (`WithSecureLabs/tau-engine`)** sobre como traduzir cada `logsource` e nome de campo abstrato do Sigma para o caminho exato no documento JSON/XML do Event Log (ex.: `Event.EventData.CommandLine` ou `Event.System.EventID`)!

## Como funciona
Além das regras Sigma, o diretório `rules/` nativo do Chainsaw traz detectores prontos para **alertas de antivírus (Windows Defender, Sophos, F-Secure, Kaspersky)**, **limpeza de logs (`1102` / `104`)**, **criação de contas ou adição a grupos sensíveis**, **logins remotos (RDP/SMB/Service)** e **força bruta de contas locais**!

## Exemplo
```bash
# Executar hunting combinado com regras Sigma e regras nativas do Chainsaw filtrando por janela temporal e exportando CSV
chainsaw hunt ./evtx_triage/ \
  -s ./sigma/rules/windows/ \
  --mapping ./chainsaw/mappings/sigma-event-logs-all.yml \
  -r ./chainsaw/rules/ \
  --from "2026-10-01T00:00:00" \
  --to "2026-10-03T23:59:59" \
  --csv --output ./resultados_chainsaw_csv/
```

## Limites e trade-offs
Você pode refinar as regras carregadas no `chainsaw hunt` usando as flags **`--level <critical|high|medium|low|informational>`**, **`--status <stable|test|experimental>`** e **`--kind <chainsaw|sigma>`**, além de usar `--skip-errors` para continuar o processamento caso um arquivo `.evtx` de um disco corrompido esteja truncado.

## Como verificar
Use `--timezone America/Sao_Paulo` ou `--local` quando precisar alinhar os timestamps das detecções ao fuso horário local do incidente.

## Conexões
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Veja também: Arquitetura do **Chainsaw (`WithSecureLabs/chainsaw`)**: Triagem Forense Multi-Artefatos Windows (`.evtx`, `$MFT`, Registry Hives, Shimcache e SRUM) em Rust.
- [[chainsaw-busca-forense-search-regex-expressoes-tau-filtros-temporais]] — Veja também: Busca Forense de Alta Precisão com **`chainsaw search`**: Expressões **TAU (`-t`)**, Regex (`-e`), Janelas Temporais e Extração JSON.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
