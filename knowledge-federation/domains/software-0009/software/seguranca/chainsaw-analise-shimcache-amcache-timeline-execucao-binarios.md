---
id: software.seguranca.tranche12.001104
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

# Reconstrução de Linha do Tempo de Execução com **`chainsaw analyse shimcache`**: Correlação entre **`SYSTEM` (`AppCompatCache`)** e **`Amcache.hve`**

## Em uma frase
Quando um atacante executa um binário malicioso (`mimikatz.exe`, `rclone.exe`, `psexec.exe`), apaga o arquivo do disco e limpa todos os logs `.evtx` (`wevtutil cl`), como o perito forense comprova que aquele binário existiu e foi executado na máquina?

## Por que importa
O Windows mantém dois artefatos de compatibilidade de aplicativos no Registro que sobrevivem à exclusão do executável e à limpeza dos Event Logs: o **Shimcache (`AppCompatCache`)**, armazenado no hive **`C:\Windows\System32\config\SYSTEM`** (sob `ControlSet001\Control\Session Manager\AppCompatCache`), e o **`Amcache.hve`**, localizado em **`C:\Windows\AppCompat\Programs\Amcache.hve`** (que registra inclusive o **hash SHA-1** do binário, tamanho, timestamp de compilação PE e caminho completo)!

## Como funciona
O subcomando **`chainsaw analyse shimcache`** analisa o hive `SYSTEM` (usando a biblioteca Rust `notatin`), extrai as entradas do Shimcache em ordem cronológica e, quando recebe **`--amcache Amcache.hve`** e **`--regexfile`** (ou `-r` para detectar padrões suspeitos), enriquece automaticamente a timeline com os metadados e hashes SHA-1 do Amcache!

## Exemplo
```bash
# Gerar uma timeline enriquecida de Shimcache + Amcache a partir dos hives coletados (SYSTEM e Amcache.hve)
chainsaw analyse shimcache \
  ./artefatos_registro/SYSTEM \
  --amcache ./artefatos_registro/Amcache.hve \
  --tspair \
  --output ./shimcache_amcache_timeline.csv
```

## Limites e trade-offs
A flag **`--tspair`** (*timestamp pair matching*) correlaciona os pares de timestamps próximos entre entradas do Shimcache e entradas do `Amcache.hve` para identificar com alta precisão o momento exato de modificação/execução e o hash SHA-1 de cada binário!

## Como verificar
Lembre-se de que o Windows grava as alterações do Shimcache (`AppCompatCache`) no hive `SYSTEM` em memória e faz o flush no desligamento/reinicialização (ou em checkpoints periódicos do registro); já o `Amcache.hve` é atualizado de forma muito mais imediata.

## Conexões
- [[chainsaw-busca-forense-search-regex-expressoes-tau-filtros-temporais]] — Veja também: Busca Forense de Alta Precisão com **`chainsaw search`**: Expressões **TAU (`-t`)**, Regex (`-e`), Janelas Temporais e Extração JSON.
- [[chainsaw-analise-srum-srudb-dat-telemetria-rede-processos-exfiltracao]] — Veja também: Forense de Exfiltração de Dados e Consumo de Rede por Processo com **`chainsaw analyse srum`** (**`SRUDB.dat`** + Hive **`SOFTWARE`**).
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-dump-artefatos-mft-registry-esedb-json-analise-forense]] — Referência cruzada direta com chainsaw-dump-artefatos-mft-registry-esedb-json-analise-forense.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
