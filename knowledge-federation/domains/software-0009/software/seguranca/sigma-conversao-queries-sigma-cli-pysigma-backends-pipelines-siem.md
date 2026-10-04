---
id: software.seguranca.tranche11.001087
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

# Compilação de Regras com **`sigma-cli` e `pySigma`**: Backends (**Splunk SPL, Elastic EQL/Lucene, Sentinel KQL, QRadar, Loki**) e Pipelines de Transformação

## Em uma frase
Como converter um diretório inteiro de regras YAML do Sigma (junto com seus **Sigma Filters** e **Placeholders**) em consultas prontas para rodar no **Splunk**, **Elasticsearch / Kibana**, **Microsoft Sentinel**, **CrowdStrike LogScale**, **Datadog** ou **Grafana Loki**?

## Por que importa
Através da ferramenta oficial de linha de comando **`sigma-cli`** (`SigmaHQ/sigma-cli`, construída sobre a biblioteca moderna **`pySigma`** que substituiu o antigo `sigmac` legado)!

## Como funciona
No `sigma-cli`, a conversão usa dois componentes plugáveis: **(1) O `Target` (`-t` / `--target`)** — que escolhe o **Backend de Linguagem de Consulta** (ex.: `splunk`, `es-qs`, `eql`, `kusto` / ` sentinel`, `qradar`, `loki`, `sqlite`, `opensearch`); e **(2) O `Pipeline` (`-p` / `--pipeline`)** — que define como mapear os `logsources` e os nomes de campos para o esquema real de ingestão da sua empresa (por exemplo, `sysmon`, `windows-audit`, `ecs_windows` para Elastic Common Schema, ou `crowdstrike_fdr` para dados do Falcon Data Replicator)!

## Exemplo
```bash
# Instalar o sigma-cli, instalar o plugin de backend do Splunk/Elastic e converter uma pasta de regras Sigma aplicando pipeline Sysmon
pip install sigma-cli
sigma plugin install splunk elasticsearch
sigma convert \
  --target splunk \
  --pipeline sysmon \
  rules/windows/process_creation/
```

## Limites e trade-offs
Compreenda por que o conceito de **Processing Pipeline (`-p`)** do `pySigma` é tão importante: uma mesma empresa que usa o **Splunk (`--target splunk`)** pode ingerir logs do Windows no formato XML do Sysmon (`--pipeline sysmon`) ou no formato **CIM / OCSF** — trocando apenas o arquivo YAML de `--pipeline`, o `sigma convert` gera o SPL com os nomes de `index`, `sourcetype` e campos exatos do seu ambiente!

## Como verificar
Use `sigma list targets` e `sigma list pipelines` para consultar todos os plugins disponíveis no ecossistema oficial do `pySigma`.

## Conexões
- [[sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork]] — Veja também: **Sigma Filters (`filter` em Especificação v2.1)**: Como Suprimir Falsos Positivos do Ambiente Local **Sem Modificar as Regras Oficiais do SigmaHQ**.
- [[sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo]] — Veja também: Uso de **Placeholders (`%variavel%` eModificador `|expand`)** no Sigma para Parametrizar Domínios VIP, Sub-redes de Servidores e Contas de Administração.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Referência cruzada direta com sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
