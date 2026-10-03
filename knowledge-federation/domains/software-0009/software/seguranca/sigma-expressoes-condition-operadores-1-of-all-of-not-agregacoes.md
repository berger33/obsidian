---
id: software.seguranca.tranche11.001084
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

# Construindo a Cláusula **`condition`** no Sigma: Operadores Booleanos (`and`, `or`, `not`), Seletores Wildcard (**`1 of selection_*`**, **`all of them`**) e Valores Especiais (`null`)

## Em uma frase
Na seção `detection` de uma regra Sigma, você define quantos blocos de busca nomeados (*Search-Identifiers*, como `selection_bin`, `selection_cli`, `filter_legit_updater`, `filter_system`) quiser, e os combina na cláusula obrigatória **`condition`**!

## Por que importa
Dominar a sintaxe da cláusula `condition` permite estruturar regras complexas e legíveis usando: **(1) Operadores Lógicos com Precedência Estrita**: parênteses `(...)` -> **`not`** -> **`and`** -> **`or`**; **(2) Seletores de Grupo com Wildcard**: **`1 of selection_*`** (qualquer um dos blocos que começam com `selection_`), **`all of selection_*`** (todos os blocos `selection_*` devem casar simultaneamente!), **`1 of them`** (qualquer bloco definido em `detection`) e **`all of them`**; e **(3) Exclusão Limpa de Falsos Positivos**: **`and not 1 of filter_*`**!

## Como funciona
Além disso, como verificar no Sigma se um campo no log é nulo (`null`), existe (`exists: true`) ou contém uma string vazia (`''`)? Usando exatamente os valores especiais **`Campo: null`** e **`Campo|exists: true`** (ou `false`) definidos na especificação v2.1!

## Exemplo
```yaml
title: Criacao de Servico Windows a partir de Diretorio Temporario ou Publico
id: 7a1b2c3d-4e5f-4a6b-8c9d-0e1f2a3b4c5d
status: stable
logsource:
    product: windows
    service: system
detection:
    selection_eid:
        Provider_Name: 'Service Control Manager'
        EventID: 7045
    selection_suspicious_path:
        ImagePath|contains:
            - '\Users\Public\'
            - '\AppData\Local\Temp\'
            - '\Windows\Temp\'
            - 'cmd.exe /c'
            - 'powershell'
    filter_known_admin_tool:
        ServiceName: 'PSEXESVC'
        AccountName: 'NT AUTHORITY\SYSTEM'
    condition: all of selection_* and not 1 of filter_*
level: high
```

## Limites e trade-offs
Padronizar a estrutura de nomes dos seus blocos em `detection` usando prefixos **`selection_*`** (para o comportamento malicioso) e **`filter_*`** (para as exceções conhecidas) com a condição universal **`condition: all of selection_* and not 1 of filter_*`** torna suas regras Sigma autoexplicativas e facílimas de manter!

## Como verificar
Atenção ao escapar caracteres especiais em valores de string no Sigma: como `*` e `?` são tratados como *wildcards* na busca Sigma, para procurar um asterisco ou barra invertida literal dentro de um wildcard, use a barra invertida de escape (`\*`, `\?`, `\\`).

## Conexões
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Veja também: Modificadores de Valor (**`Value Modifiers`**) no Sigma: **`contains`**, **`all`**, **`base64offset`**, **`utf16le`**, **`windash`**, **`cidr`** e **`fieldref`**.
- [[sigma-regras-correlacao-v2-event-count-value-count-temporal-ordered]] — Veja também: **Sigma Correlation Rules (Especificação v2.0 / v2.1)**: Correlação Multi-Evento **`event_count`**, **`value_count`**, **`temporal`** e **`temporal_ordered`** (`timespan` & `group-by`).
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork]] — Referência cruzada direta com sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
