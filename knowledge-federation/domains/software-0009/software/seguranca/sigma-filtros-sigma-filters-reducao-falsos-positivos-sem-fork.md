---
id: software.seguranca.tranche11.001086
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

# **Sigma Filters (`filter` em Especificação v2.1)**: Como Suprimir Falsos Positivos do Ambiente Local **Sem Modificar as Regras Oficiais do SigmaHQ**

## Em uma frase
Um dos maiores problemas práticos de equipes de Detection Engineering que consomem o repositório oficial `SigmaHQ/sigma` via Git Submodule ou CI/CD era: *"Se a regra oficial do SigmaHQ dispara para a nossa ferramenta interna de backup `C:\CorpBackup\agent.exe`, e nós editarmos o arquivo `.yml` oficial para adicionar um `filter_backup`, na semana que vem nosso `git pull` do SigmaHQ dará conflito de merge!"*

## Por que importa
A **Especificação Sigma v2.1.0** resolveu esse problema de engenharia criando um novo tipo de documento chamado **Sigma Filter (`filter`)**!

## Como funciona
Um **Sigma Filter** vive em um arquivo `.yml` **100% separado da regra original**: no bloco `filter`, você referencia no array **`rules`** o `id` (ou `name`) da(s) regra(s) oficial(is) do SigmaHQ às quais aquele filtro de ambiente deve ser aplicado, define os seletores locais (ex.: `selection_corp_backup`) e a cláusula `condition: not selection_corp_backup`! Na hora de compilar as queries com o `sigma-cli` / `pySigma`, o compilador injeta automaticamente seus filtros corporativos nas regras referenciadas sem que você precise tocar em uma única linha do repositório upstream do SigmaHQ!

## Exemplo
```yaml
title: Filtro Corporativo para Agente de Backup Interno nas Regras de Criacao de Processo
description: Exclui o binario assinado de backup interno das regras de reconhecimento do SigmaHQ
status: stable
logsource:
    category: process_creation
    product: windows
filter:
    rules:
        - 929a690e-bef0-4204-a928-ef5e620d6fcc
    selection_corp_agent:
        ParentImage: 'C:\Program Files\CorpBackup\BackupService.exe'
        User: 'NT AUTHORITY\SYSTEM'
    condition: not selection_corp_agent
```

## Limites e trade-offs
Olhe a elegância arquitetural de separar **Regras Upstream (`rules/`)** de **Filtros de Ambiente (`filters/`)**: você pode atualizar o repositório `SigmaHQ/sigma` diariamente de forma 100% automatizada no seu pipeline de *Detection-as-Code*, mantendo todas as particularidades e exceções da sua infraestrutura isoladas na sua pasta privada `corp-sigma-filters/`!

## Como verificar
Se você omitir a chave `rules` ou usar regras globais compátiveis com o mesmo `logsource`, o filtro pode ser aplicado a toda uma categoria de regras (ex.: todas as regras de `process_creation`).

## Conexões
- [[sigma-regras-correlacao-v2-event-count-value-count-temporal-ordered]] — Veja também: **Sigma Correlation Rules (Especificação v2.0 / v2.1)**: Correlação Multi-Evento **`event_count`**, **`value_count`**, **`temporal`** e **`temporal_ordered`** (`timespan` & `group-by`).
- [[sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem]] — Veja também: Compilação de Regras com **`sigma-cli` e `pySigma`**: Backends (**Splunk SPL, Elastic EQL/Lucene, Sentinel KQL, QRadar, Loki**) e Pipelines de Transformação.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[sigma-expressoes-condition-operadores-1-of-all-of-not-agregacoes]] — Referência cruzada direta com sigma-expressoes-condition-operadores-1-of-all-of-not-agregacoes.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
