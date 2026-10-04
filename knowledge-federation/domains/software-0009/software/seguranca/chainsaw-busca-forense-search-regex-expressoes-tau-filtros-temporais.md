---
id: software.seguranca.tranche12.001103
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

# Busca Forense de Alta Precisão com **`chainsaw search`**: Expressões **TAU (`-t`)**, Regex (`-e`), Janelas Temporais e Extração JSON

## Em uma frase
Durante uma investigação de incidente, após encontrar um indicador inicial (um endereço IP de C2, um nome de conta comprometida, um hash de binário ou um `EventID` específico), o analista precisa vasculhar rapidamente todos os artefatos `.evtx`, `.xml` ou `.json` em busca de qualquer ocorrência daquele indicador sem escrever uma regra Sigma completa.

## Por que importa
O subcomando **`chainsaw search`** resolve isso combinando três motores de busca em paralelo (via `rayon` e `aho-corasick`): **(1) Busca literal ou por expressão regular (`-e, --regex <padrao>` e `-i, --ignore-case`)**, **(2) Expressões lógicas do TAU Engine (`-t, --tau <expressao>`)** para filtrar campos exatos da árvore do evento (como `'Event.System.EventID: =4104'` para Script Blocks do PowerShell), e **(3) Recorte temporal (`--from` e `--to`)**!

## Como funciona
Combinando `-t` e `-e` na mesma chamada, você pode, por exemplo, buscar apenas dentro de eventos `4104` (PowerShell) ou `4688` (Process Creation) que correspondam a uma expressão regular específica e exportar os documentos completos em formato JSON (`--json -o saida.json`) para análise com `jq`!

## Exemplo
```bash
# Buscar em todos os arquivos .evtx apenas eventos PowerShell Script Block (EventID 4104) que contenham chamadas de download ou reflexao
chainsaw search \
  -t 'Event.System.EventID: =4104' \
  -e '(Invoke-WebRequest|DownloadString|Reflection\.Assembly)' \
  -i ./evtx_triage/ \
  --json -o ./powershell_suspeito_4104.json
```

## Limites e trade-offs
A flag **`--load-unknown`** permite instruir o `chainsaw search` a tentar carregar e inspecionar arquivos forenses mesmo quando a extensão do arquivo foi renomeada pelo atacante ou pelo coletor forense.

## Como verificar
Sempre combine `-i` (*ignore-case*) ao buscar domínios, caminhos do Windows (`C:\Users\...`), nomes de máquinas (`DC01`) ou comandos PowerShell ofuscados com variação de caixa.

## Conexões
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Veja também: Threat Hunting com **`chainsaw hunt`**: Motor **TAU Engine**, Mapeamentos **`sigma-event-logs-all.yml`** e Regras Nativas do Chainsaw.
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Veja também: Reconstrução de Linha do Tempo de Execução com **`chainsaw analyse shimcache`**: Correlação entre **`SYSTEM` (`AppCompatCache`)** e **`Amcache.hve`**.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Referência cruzada direta com hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
