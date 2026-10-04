---
id: software.seguranca.tranche12.001101
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

# Arquitetura do **Chainsaw (`WithSecureLabs/chainsaw`)**: Triagem Forense Multi-Artefatos Windows (`.evtx`, `$MFT`, Registry Hives, Shimcache e SRUM) em Rust

## Em uma frase
Enquanto o **Hayabusa** é especializado especificamente em logs de eventos `.evtx`, uma investigação completa de **DFIR (*Digital Forensics and Incident Response*)** em Windows exige correlacionar múltiplos artefatos de disco — como a **Master File Table (`$MFT`)**, hives de **Registro (`SYSTEM`, `SOFTWARE`, `NTUSER.DAT`, `Amcache.hve`)**, o cache de compatibilidade de aplicativos (**Shimcache**) e o banco **SRUM (`SRUDB.dat`)**!

## Por que importa
Desenvolvido pelos consultores de resposta a incidentes da **WithSecure Countercept** (James Dorgan e Alex Kornitzer) em **Rust (edição 2024, GPLv3)**, o **Chainsaw** reúne em um único binário estático multiplataforma (Linux, macOS e Windows) parsers de altíssimo desempenho (`evtx`, `mft`, `notatin` para Registry Hives e `libesedb` para bancos ESE do Windows) combinados com o motor de detecção lógica **TAU Engine (`tau-engine`)**!

## Como funciona
A CLI do Chainsaw organiza o fluxo forense em quatro subcomandos principais: **`chainsaw hunt`** (aplicação de regras Sigma e regras nativas Chainsaw com `--mapping`), **`chainsaw search`** (busca por strings, regex `-e` e expressões Tau `-t`), **`chainsaw analyse`** (`shimcache`, `srum`) e **`chainsaw dump`** (extração estruturada de `$MFT`, hives de registro e bancos ESE para JSON/CSV)!

## Exemplo
```bash
# Compilar ou verificar a instalacao do Chainsaw v2+ e listar os subcomandos forenses disponiveis
chainsaw --version
chainsaw --help
chainsaw analyse --help
```

## Limites e trade-offs
O grande diferencial arquitetural do Chainsaw é permitir que o analista de DFIR processe uma imagem forense Windows montada em uma estação Linux de análise (ex.: SIFT Workstation ou Kali) sem precisar de nenhuma máquina Windows ou servidor SIEM: você executa `hunt`, `search`, `analyse shimcache`, `analyse srum` e `dump` diretamente contra os artefatos coletados pelo **KAPE** ou **Velociraptor**!

## Como verificar
Ao compilar o Chainsaw a partir do código-fonte (`cargo build --release`), utilize sempre a flag `--release` para ativar as otimizações de código de máquina do LLVM/Rust.

## Conexões
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Veja também: Threat Hunting com **`chainsaw hunt`**: Motor **TAU Engine**, Mapeamentos **`sigma-event-logs-all.yml`** e Regras Nativas do Chainsaw.
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Referência cruzada direta com chainsaw-analise-shimcache-amcache-timeline-execucao-binarios.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
