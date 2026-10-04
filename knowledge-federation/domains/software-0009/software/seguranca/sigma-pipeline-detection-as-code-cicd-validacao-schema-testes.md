---
id: software.seguranca.tranche11.001090
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

# Implantando **Detection-as-Code (DaC)** com Sigma em CI/CD: Validação de JSON Schema (`sigma check`), Linting, Conversão Automatizada e Deploy no SIEM

## Em uma frase
Na engenharia moderna de SOC (**Detection-as-Code**), nenhum analista cria ou edita regras de alerta clicando manualmente na interface web do Splunk, Sentinel ou Elastic: todas as detecções vivem como arquivos **Sigma YAML** em um repositório Git, passando por revisão de Pull Request (`CODEOWNERS`), validação automatizada no CI/CD e deploy contínuo via API do SIEM!

## Por que importa
Quais etapas compõem um pipeline de CI/CD de **Detection-as-Code com Sigma**?

## Como funciona
**(1) Validação Sintática e de Schema (`sigma check` + `sigma-detection-rule-schema.json`)** — garante que toda regra nova ou modificada segue a especificação Sigma v2.1, não possui UUIDs duplicados e usa nomes de campos válidos da taxonomia; **(2) Teste contra Logs de Exemplo (*Unit Testing de Detecção*)** — executa o **Hayabusa** ou um motor de teste sobre arquivos `.evtx` / JSON de ataques reais (como o dataset *EVTX-ATTACK-SAMPLES*) para provar que a regra dispara no ataque e não dispara nos logs limpos; e **(3) Compilação (`sigma convert`) e Publicação via API** no SIEM!

## Exemplo
```bash
# No pipeline de CI/CD de Detection-as-Code: validar todas as regras Sigma contra o padrao oficial (sigma check) antes de compilar
sigma check rules/
sigma convert \
  --target splunk \
  --pipeline sysmon \
  --output /tmp/splunk_saved_searches.conf \
  rules/
```

## Limites e trade-offs
Por que incluir a etapa de validação com o **Hayabusa** no mesmo pipeline de CI/CD das suas regras Sigma Windows? Porque o Hayabusa compila e avalia milhares de regras Sigma contra gigabytes de arquivos `.evtx` de baseline em poucos segundos, revelando imediatamente na tela do Pull Request se a nova regra do analista geraria uma tempestade de 50.000 falsos positivos por hora em produção!

## Como verificar
Versione seus `Sigma Filters` e `Processing Pipelines` no mesmo repositório Git das regras para garantir builds determinísticos e auditáveis.

## Conexões
- [[sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags]] — Veja também: Governança de Cobertura de Detecção com Sigma: Mapeamento de **Tags MITRE ATT&CK (`attack.tXXXX`)**, CVEs (`cve.YYYY.NNNN`) e **ATT&CK Navigator**.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem]] — Referência cruzada direta com sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
