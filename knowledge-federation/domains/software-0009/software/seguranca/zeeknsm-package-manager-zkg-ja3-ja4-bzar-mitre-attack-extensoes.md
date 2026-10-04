---
id: software.seguranca.tranche03.000209
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Package Manager (`zkg`): instalação de pacotes comunitários (`JA3`, `JA4`, `MITRE ATT&CK BZAR`, `hassh`, `cve-detectors`)

## Em uma frase
O utilitário oficial **`zkg` (Zeek Package Manager)** gerencia a descoberta, instalação, teste, atualização e carregamento de pacotes do diretório oficial **[packages.zeek.org](https://packages.zeek.org)** — incluindo pacotes consagrados de detecção como **`ja3`**, **`ja4`** (fingerprinting TLS/QUIC), **`hassh`** (fingerprinting de clientes/servidores SSH), **`bzar`** (*Bro/Zeek ATT&CK-based Analytics and Reporting* para detecção de movimentação lateral SMB/DCE-RPC/WMI mapeada ao MITRE ATT&CK) e detectores de CVEs.

## Por que importa
Copiar scripts `.zeek` avulsos da internet para dentro de `/opt/zeek/share/zeek/site/` sem controle de versão, sem rodar a suíte de testes (`btest`) do pacote e sem rastrear dependências dificulta a manutenção do sensor.

## Como funciona
Com o `zkg`, você instala pacotes validados (`zkg install <pacote>`), congela versões em um manifesto (`zkg bundle` para ambientes air-gapped sem acesso à internet) e carrega todos os pacotes instalados adicionando `@load packages` ao seu `local.zeek`!

## Exemplo
```bash
# Instalando pacotes de fingerprinting SSH (HASSH) e detecção MITRE ATT&CK (BZAR) via zkg:
zkg refresh
zkg install salesforce/hassh
zkg install mitre-attack/bzar
zkg list
```

## Limites e trade-offs
Para sensores NSM em redes isoladas (*air-gapped*), execute `zkg bundle meu-pacote.bundle ...` em uma máquina conectada e transfira o arquivo `.bundle` para instalar offline no sensor com `zkg unbundle`.

## Como verificar
Verifique os pacotes ativos com `zkg list` e confirme a presença de `@load packages` em `site/local.zeek`.

## Conexões
- [[zeeknsm-spicy-parser-generator-gramaticas-seguras-protocolos-arquivos]] — Veja também: Zeek `Spicy`: gerador moderno de parsers seguros em C++ para protocolos de rede e formatos de arquivo customizados.
- [[zeeknsm-summary-statistics-sumstats-deteccao-anomalias-scans-exfiltracao]] — Veja também: Zeek `SumStats` (Summary Statistics Framework): agregação estatística distribuída para detectar Port Scans, DGA e Beaconing.

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
