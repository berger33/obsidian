---
id: software.seguranca.tranche12.001105
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

# Forense de Exfiltração de Dados e Consumo de Rede por Processo com **`chainsaw analyse srum`** (**`SRUDB.dat`** + Hive **`SOFTWARE`**)

## Em uma frase
Imagine o seguinte cenário de resposta a incidentes: você sabe que um servidor Windows sofreu exfiltração de 15 GB de dados confidenciais na madrugada de sábado, mas o firewall de borda só registrou tráfego HTTPS criptografado saindo do IP do servidor e você não sabe **qual processo e qual conta de usuário (SID)** transmitiu aqueles 15 GB!

## Por que importa
Desde o Windows 8 e Windows Server 2012, o serviço **System Resource Usage Monitor (SRUM)** mantém um banco de dados Extensible Storage Engine (ESE) em **`C:\Windows\System32\sru\SRUDB.dat`** que registra, a cada hora (por até 30 a 60 dias!), **quantos bytes foram enviados (`BytesSent`) e recebidos (`BytesRecvd`) na rede, tempo de CPU e I/O de disco para cada caminho de executável (`AppId`) e cada usuário (`UserId` / SID)** — mesmo que o executável já tenha sido apagado do disco!

## Como funciona
O subcomando **`chainsaw analyse srum`** utiliza o parser Rust `libesedb` para ler o `SRUDB.dat` e o cruza com o hive de registro **`C:\Windows\System32\config\SOFTWARE`** (que mapeia os SIDs da `ProfileList` para nomes de usuários e interfaces de rede), gerando uma tabela ou JSON detalhado de uso de rede e execução por aplicação!

## Exemplo
```bash
# Analisar o banco SRUDB.dat correlacionando com o hive SOFTWARE para identificar quais binarios e usuarios exfiltraram dados (BytesSent)
chainsaw analyse srum \
  --software ./artefatos_registro/SOFTWARE \
  ./artefatos_sru/SRUDB.dat \
  --json -o ./srum_telemetria_rede_processos.json
```

## Limites e trade-offs
Use a flag **`--stats-only`** (`chainsaw analyse srum -s ./SOFTWARE ./SRUDB.dat`) para inspecionar instantaneamente os metadados das tabelas ESE do SRUM (quais tabelas existem, qual é a retenção temporal configurada e o intervalo de datas coberto pelo `SRUDB.dat`).

## Como verificar
Ao coletar o `SRUDB.dat` de um servidor Windows ligado (*live system*), utilize sempre um coletor que leia via **Volume Shadow Copy (VSS)** ou acesso bruto ao NTFS (como **KAPE** ou **Velociraptor**), pois o arquivo fica bloqueado pelo serviço `DPS` (*Diagnostic Policy Service*).

## Conexões
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Veja também: Reconstrução de Linha do Tempo de Execução com **`chainsaw analyse shimcache`**: Correlação entre **`SYSTEM` (`AppCompatCache`)** e **`Amcache.hve`**.
- [[chainsaw-dump-artefatos-mft-registry-esedb-json-analise-forense]] — Veja também: Extração Bruta e Conversão de Artefatos (**`$MFT`**, Hives de Registro e Bancos ESE) para JSON com **`chainsaw dump`**.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
