---
id: software.seguranca.tranche11.001085
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

# **Sigma Correlation Rules (Especificação v2.0 / v2.1)**: Correlação Multi-Evento **`event_count`**, **`value_count`**, **`temporal`** e **`temporal_ordered`** (`timespan` & `group-by`)

## Em uma frase
Nas versões antigas do Sigma (v1.x), as agregações `| near` ou `| count()` eram limitadas e marcadas como obsoletas. A **Especificação Sigma v2.0 / v2.1** introduziu um modelo formal e poderoso de **Regras de Correlação Multi-Evento (`correlation`)** (suportado pelo `pySigma` e nativamente em Rust pelo **Hayabusa**)!

## Por que importa
Como funciona uma Regra de Correlação Sigma v2?

## Como funciona
Você define as regras base (com um atributo `name` ou `id` em documentos separados pelo delimitador YAML `---`) e cria um documento de correlação com o bloco **`correlation`** especificando um dos **4 tipos oficiais**: **(1) `type: event_count`** — dispara quando uma regra ocorre `>= N` vezes dentro da janela **`timespan`** (ex.: 50 falhas de login EventID 4625 em `5m` para o mesmo `TargetUserName`); **(2) `type: value_count`** — dispara quando um campo assume `>= N` **valores distintos** na janela (ex.: 1 usuário tentando autenticar em `>= 20` `WorkstationName` diferentes ou enumerando 30 buckets S3 — *Password Spraying / Recon*!); **(3) `type: temporal`** — dispara quando **múltiplas regras distintas** ocorrem dentro do mesmo `timespan` agrupadas por **`group-by`**; e **(4) `type: temporal_ordered`** — exige que as regras ocorram **na ordem cronológica exata** listada em `rules`!

## Exemplo
```yaml
title: Falha de Logon no Windows
name: failed_windows_logon
status: stable
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4625
    condition: selection
---
title: Ataque de Password Spraying Detectado (Multiplos Usuarios a partir do Mesmo IP)
id: 8c9d0e1f-2a3b-4c5d-9e0f-1a2b3c4d5e6f
status: stable
correlation:
    type: value_count
    rules:
        - failed_windows_logon
    group-by:
        - IpAddress
    timespan: 10m
    condition:
        gte: 25
        field: TargetUserName
level: high
```

## Limites e trade-offs
Compare na regra acima a diferença entre **`event_count`** e **`value_count`**: um ataque de **Brute Force** contra 1 único usuário gera 25 eventos para o mesmo `TargetUserName` (`event_count >= 25` agrupado por `TargetUserName`); já um ataque furtivo de **Password Spraying** testa 1 senha contra 25 usuários diferentes a partir do mesmo `IpAddress` — que é capturado com precisão cirúrgica por **`type: value_count` com `field: TargetUserName` e `group-by: [IpAddress]`**!

## Como verificar
Quando campos têm nomes diferentes entre as regras correlacionadas (ex.: `SubjectUserName` na regra A e `TargetUserName` na regra B), use o mapeamento **`aliases`** dentro do bloco `correlation`!

## Conexões
- [[sigma-expressoes-condition-operadores-1-of-all-of-not-agregacoes]] — Veja também: Construindo a Cláusula **`condition`** no Sigma: Operadores Booleanos (`and`, `or`, `not`), Seletores Wildcard (**`1 of selection_*`**, **`all of them`**) e Valores Especiais (`null`).
- [[sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork]] — Veja também: **Sigma Filters (`filter` em Especificação v2.1)**: Como Suprimir Falsos Positivos do Ambiente Local **Sem Modificar as Regras Oficiais do SigmaHQ**.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
