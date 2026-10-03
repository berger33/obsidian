---
id: software.seguranca.tranche11.001083
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

# Modificadores de Valor (**`Value Modifiers`**) no Sigma: **`contains`**, **`all`**, **`base64offset`**, **`utf16le`**, **`windash`**, **`cidr`** e **`fieldref`**

## Em uma frase
Atacantes raramente executam comandos maliciosos em texto limpo e previsível: no Windows, um comando PowerShell pode ser passado com `-enc`, `/enc`, `–enc` (diferentes caracteres de traço/barra aceitos pelo Windows!) e ter seu payload codificado em **Base64 UTF-16LE** — onde o texto codificado muda completamente dependendo do deslocamento de bytes (*offset* 0, 1 ou 2) em que a string aparece!

## Por que importa
Para que o analista do SOC não precise calcular manualmente as 3 variações de Base64 nem listar todas as barras/traços do Windows, a especificação Sigma fornece **Modificadores de Valor encadeáveis via pipe (`Campo|mod1|mod2`)**!

## Como funciona
Veja os modificadores mais importantes da especificação v2.1: **(1) Strings e Listas**: `|contains`, `|startswith`, `|endswith`, **`|all`** (transforma uma lista que por padrão seria `OR` em uma condição **`AND` — todos os itens devem estar presentes**!) e `|cased` (sensível a maiúsculas/minúsculas); **(2) Ofuscação de Linha de Comando Windows**: **`|windash`** (expande automaticamente `-param` para aceitar `-`, `/`, `–`, `—` e `―`!); **(3) Codificação Base64**: **`|base64`** e **`|base64offset`** (gera automaticamente as 3 permutações de alinhamento Base64 combináveis com `|utf16le` / `|wide`!); e **(4) Rede, Regex e Campos**: **`|cidr`** (sub-redes IPv4/IPv6), **`|re`** (PCRE) e **`|fieldref`** (compara o valor de um campo com outro campo do mesmo evento!)!

## Exemplo
```yaml
title: Execucao de Comando PowerShell Ofuscado com Flags de Bypass ou Base64
id: 4d8f2a1c-9e3b-4c5d-8a7f-1b2c3d4e5f6a
status: stable
logsource:
    category: process_creation
    product: windows
detection:
    selection_img:
        Image|endswith:
            - '\powershell.exe'
            - '\pwsh.exe'
    selection_flags:
        CommandLine|windash|contains:
            - '-EncodedCommand'
            - '-ep bypass'
            - '-w hidden'
    selection_b64_iex:
        CommandLine|base64offset|utf16le|contains:
            - 'Invoke-Expression'
            - 'FromBase64String'
            - 'DownloadString'
    condition: selection_img and (selection_flags or selection_b64_iex)
level: high
```

## Limites e trade-offs
Olhe o poder da combinação **`CommandLine|base64offset|utf16le|contains: 'DownloadString'`** na regra acima: o compilador Sigma calcula sozinho em tempo de compilação as 3 variantes Base64 em UTF-16LE (como o `powershell -enc` codifica strings no Windows!) e injeta os padrões resultantes na query do seu SIEM ou no **Hayabusa**!

## Como verificar
Use também o modificador **`|all`** quando quiser exigir múltiplos argumentos simultâneos na mesma linha de comando (ex.: `CommandLine|contains|all: ['sekurlsa::', 'logonpasswords']`).

## Conexões
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Veja também: Anatomia do Bloco **`logsource`** e **`taxonomy`** na Especificação Sigma v2.1: Abstraindo **Windows Event Logs, Sysmon, Linux `auditd` e CloudTrail**.
- [[sigma-expressoes-condition-operadores-1-of-all-of-not-agregacoes]] — Veja também: Construindo a Cláusula **`condition`** no Sigma: Operadores Booleanos (`and`, `or`, `not`), Seletores Wildcard (**`1 of selection_*`**, **`all of them`**) e Valores Especiais (`null`).
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Referência cruzada direta com hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
