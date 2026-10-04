---
id: software.seguranca.tranche12.001110
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

# Playbook Integrado **Chainsaw + Hayabusa** em DFIR: Como Combinar o Melhor dos Dois Motores Rust na Triagem Forense Windows

## Em uma frase
Uma dúvida recorrente em equipes de **DFIR e SOC** é: *"Devemos usar o **Chainsaw** ou o **Hayabusa** nas nossas investigações forenses Windows?"* A resposta dos especialistas é: **ambos são complementares e devem rodar juntos no pipeline automatizado de triagem pós-coleta (KAPE / Velociraptor)**!

## Por que importa
O **Hayabusa** brilha na geração de uma **Super Timeline unificada de `.evtx`** (com mais de 3.900 regras Sigma otimizadas, relatórios `HTML` de métricas, enriquecimento GeoIP MaxMind e correlação de regras `event_count` / `value_count`); já o **Chainsaw** é insubstituível para **analisar os artefatos forenses fora do Event Log (`$MFT`, `SYSTEM` Shimcache, `Amcache.hve`, `SRUDB.dat` SRUM)**, extrair tabelas customizadas de alertas de AV e fazer buscas rápidas com expressões **TAU (`chainsaw search -t`)**!

## Como funciona
Ao integrar ambos em um script de automação de triagem sobre o pacote coletado pelo **KAPE**, o analista recebe em menos de 2 minutos tanto a timeline de eventos `.evtx` do Hayabusa quanto a timeline de execução de binários (`Shimcache + Amcache`) e a matriz de exfiltração de rede por processo (`SRUM`) do Chainsaw!

## Exemplo
```bash
# Pipeline automatizado de triagem DFIR combinando Chainsaw (Shimcache/Amcache + SRUM) e Hayabusa (Timeline EVTX) sobre coleta KAPE
KAPE_OUT="./coleta_kape_host01/C"
mkdir -p ./relatorios_dfir_host01

chainsaw analyse shimcache "${KAPE_OUT}/Windows/System32/config/SYSTEM" \
  --amcache "${KAPE_OUT}/Windows/AppCompat/Programs/Amcache.hve" --tspair \
  -o ./relatorios_dfir_host01/01_shimcache_amcache.csv

chainsaw analyse srum --software "${KAPE_OUT}/Windows/System32/config/SOFTWARE" \
  "${KAPE_OUT}/Windows/System32/sru/SRUDB.dat" --json \
  -o ./relatorios_dfir_host01/02_srum_network_usage.json
```

## Limites e trade-offs
Mantenha binários do **Chainsaw** e do **Hayabusa** pré-compilados nas suas estações forenses Linux/Windows e dentro das imagens Docker de automação de DFIR do seu SOC.

## Como verificar
Ao arquivar o pacote de evidências da investigação, gere e registre o hash `SHA-256` de todos os relatórios CSV/JSON produzidos por ambos os motores.

## Conexões
- [[chainsaw-deteccao-movimentacao-lateral-logins-brute-force-contas]] — Veja também: Investigação de **Movimentação Lateral, Brute-Force e Escalação de Privilégio** (`lateral_movement` e `security`) com o Chainsaw.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Referência cruzada direta com chainsaw-analise-shimcache-amcache-timeline-execucao-binarios.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
