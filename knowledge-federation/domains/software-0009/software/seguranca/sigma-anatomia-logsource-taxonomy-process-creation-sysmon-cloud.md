---
id: software.seguranca.tranche11.001082
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
fontes: ["https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md", "https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia do Bloco **`logsource`** e **`taxonomy`** na Especificação Sigma v2.1: Abstraindo **Windows Event Logs, Sysmon, Linux `auditd` e CloudTrail**

## Em uma frase
Como uma única regra Sigma consegue funcionar tanto em uma empresa que usa **Microsoft Sysmon (`EventID 1`)**, quanto em outra que usa **Windows Security Auditing nativo (`EventID 4688`)** ou **CrowdStrike / Microsoft Defender for Endpoint**, se cada fonte usa IDs de evento e nomes de campos diferentes?

## Por que importa
O segredo está na abstração do bloco **`logsource`** (composto pelos atributos `category`, `product` e `service`) combinada com os **Pipelines de Processamento do `pySigma`**!

## Como funciona
Quando você escreve na regra `logsource: { category: process_creation, product: windows }` e usa os nomes de campo da taxonomia padrão Sigma (`Image`, `CommandLine`, `ParentImage`, `User`, `Hashes`, `OriginalFileName`), você não está amarrando a regra ao EventID 1 nem ao EventID 4688: é o **Pipeline de Destino** na hora da conversão com o `sigma-cli` que traduz `category: process_creation` para `EventID=1` (no pipeline `sysmon`) ou `EventID=4688` com `NewProcessName` (no pipeline `windows-audit`)!

## Exemplo
```yaml
# Comparacao de definicoes de logsource padronizadas no Sigma: Criacao de Processos Windows, Linux Auditd e AWS CloudTrail
logsource:
    category: process_creation
    product: windows
---
logsource:
    product: linux
    service: auditd
---
logsource:
    product: aws
    service: cloudtrail
```

## Limites e trade-offs
Além dos logs de sistema operacional (`windows`, `linux`, `macos`), o ecossistema Sigma possui *logsources* padronizados para **Nuvem e Identidade** (`product: aws, service: cloudtrail`, `product: azure, service: signinlogs / auditlogs`, `product: gcp`, `product: okta`, `product: m365`, `product: github`) e **Servidores Web/Proxy/DNS** (`category: webserver`, `category: proxy`, `category: dns`)!

## Como verificar
Na especificação Sigma **v2.1.0**, o atributo opcional **`taxonomy`** (padrão: `sigma`) formaliza o esquema de nomes de campos e categorias utilizado pela regra.

## Conexões
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Veja também: **SigmaHQ (`SigmaHQ/sigma`)**: Arquitetura do Padrão Aberto Universal de **Regras de Detecção para Logs e SIEMs** (*Detection-as-Code* em YAML).
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Veja também: Modificadores de Valor (**`Value Modifiers`**) no Sigma: **`contains`**, **`all`**, **`base64offset`**, **`utf16le`**, **`windash`**, **`cidr`** e **`fieldref`**.
- [[sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem]] — Referência cruzada direta com sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
