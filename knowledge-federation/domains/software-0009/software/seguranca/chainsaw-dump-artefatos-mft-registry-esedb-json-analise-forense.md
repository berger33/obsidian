---
id: software.seguranca.tranche12.001106
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

# Extração Bruta e Conversão de Artefatos (**`$MFT`**, Hives de Registro e Bancos ESE) para JSON com **`chainsaw dump`**

## Em uma frase
Muitas vezes o perito forense precisa inspecionar entradas específicas da **Master File Table (`$MFT`)** do sistema de arquivos NTFS (para detectar *timestomping* comparando os atributos `$STANDARD_INFORMATION` e `$FILE_NAME`, ou recuperar pequenos arquivos residentes diretamente na `$MFT`), ou transformar um hive de Registro inteiro (`SAM`, `SECURITY`, `NTUSER.DAT`, `UsrClass.dat`) em JSON estruturado para processamento automatizado com `jq` ou Python.

## Por que importa
O subcomando **`chainsaw dump`** atua como um extrator universal de artefatos forenses do Windows: ele detecta automaticamente o formato binário do artefato fornecido (`.evtx`, `$MFT`, hive de Registro Windows `regf` ou banco de dados ESE `.dat`/`.edb`) e converte 100% dos seus registros internos para **JSON** (`--json`) ou JSON Lines (`--jsonl`)!

## Como funciona
Ao fazer o dump de uma `$MFT` com `chainsaw dump $MFT --json`, o parser Rust `mft` decodifica cada entrada de arquivo/diretório com seus timestamps de criação, modificação, alteração de MFT e acesso de ambos os atributos (`StandardInfo` e `FileName`), tamanhos de arquivo e flags residentes!

## Exemplo
```bash
# Converter uma Master File Table ($MFT) ou um hive NTUSER.DAT diretamente para JSON estruturado e filtrar com jq
chainsaw dump ./artefatos_ntfs/\$MFT \
  --json -q -o ./mft_dump.json
```

## Limites e trade-offs
Por que ter os dois conjuntos de timestamps (`$STANDARD_INFORMATION` e `$FILE_NAME`) no dump da `$MFT` é essencial em DFIR? Porque ferramentas de anti-forense usadas por invasores (*timestomping*, como o `timestomp` do Meterpreter ou `Set-ItemProperty`) alteram facilmente os timestamps de `$STANDARD_INFORMATION`, mas **os timestamps do atributo `$FILE_NAME` só são modificados pelo próprio kernel do Windows** — revelando imediatamente a fraude temporal!

## Como verificar
Use `-q` (*quiet*) e `-o <arquivo>` ao fazer dump de uma `$MFT` grande (que pode conter centenas de milhares de registros) para gravar direto em disco sem sobrecarga de renderização no terminal.

## Conexões
- [[chainsaw-analise-srum-srudb-dat-telemetria-rede-processos-exfiltracao]] — Veja também: Forense de Exfiltração de Dados e Consumo de Rede por Processo com **`chainsaw analyse srum`** (**`SRUDB.dat`** + Hive **`SOFTWARE`**).
- [[chainsaw-regras-nativas-av-alerts-defender-sophos-kaspersky-evtx]] — Veja também: Triagem de Alertas de Antivírus/EDR (**Windows Defender, Sophos, F-Secure e Kaspersky**) e Limpeza de Logs com as Regras Nativas do Chainsaw.
- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Referência cruzada direta com chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust.
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Referência cruzada direta com chainsaw-analise-shimcache-amcache-timeline-execucao-binarios.

## Fontes
- [WithSecure Chainsaw Official GitHub — Rapidly Search and Hunt Through Windows Forensic Artefacts](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/README.md) — repositório oficial do Chainsaw cobrindo triagem forense (`hunt`, `search`, `analyse shimcache`, `analyse srum`, `dump`), regras Sigma e motor TAU; consultado em 2026-10-03.
- [WithSecure Chainsaw Official Rust Package Specification (`Cargo.toml`)](https://raw.githubusercontent.com/WithSecureLabs/chainsaw/master/Cargo.toml) — especificação oficial das bibliotecas forenses em Rust do Chainsaw 2.16+ (`evtx`, `mft`, `notatin`, `libesedb`, `tau-engine`, `aho-corasick`, `rayon`); consultado em 2026-10-03.
