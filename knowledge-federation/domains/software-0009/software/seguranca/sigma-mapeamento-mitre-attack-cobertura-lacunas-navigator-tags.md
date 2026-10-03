---
id: software.seguranca.tranche11.001089
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

# Governança de Cobertura de Detecção com Sigma: Mapeamento de **Tags MITRE ATT&CK (`attack.tXXXX`)**, CVEs (`cve.YYYY.NNNN`) e **ATT&CK Navigator**

## Em uma frase
Como um líder de SOC ou Engenheiro de Detecção responde com dados objetivos à pergunta da diretoria: *"Qual é a nossa cobertura real de detecção contra as técnicas da matriz MITRE ATT&CK usadas por grupos de Ransomware modernos?"*

## Por que importa
Em todas as regras do repositório oficial `SigmaHQ/sigma` (e nas suas regras internas), o atributo **`tags`** segue uma taxonomia padronizada de namespaces: **(1) Táticas do MITRE ATT&CK** (ex.: `attack.initial_access`, `attack.execution`, `attack.persistence`, `attack.privilege_escalation`, `attack.credential_access`, `attack.lateral_movement`); **(2) Técnicas e Sub-técnicas do MITRE ATT&CK** (ex.: `attack.t1003.001` para *LSASS Memory Dumping*, `attack.t1059.001` para *PowerShell*); **(3) Vulnerabilidades Específicas** (`cve.2024.21626`); e **(4) Escopo de Detecção** (`detection.emerging_threats`, `detection.threat_hunting`, `tlp.amber`)!

## Como funciona
Extraindo as tags `attack.t*` de todas as regras Sigma ativas no seu SIEM, você gera automaticamente uma camada JSON (**Layer File**) para o **MITRE ATT&CK Navigator**, colorindo no mapa de calor quais técnicas possuem 0, 1 ou múltiplas regras independentes!

## Exemplo
```bash
# Extrair e contabilizar o ranking das tecnicas MITRE ATT&CK (attack.tXXXX) cobertas por um diretorio de regras Sigma YAML
grep -rhoE "attack\.t[0-9]{4}(\.[0-9]{3})?" rules/ 2>/dev/null | \
  sort | uniq -c | sort -nr | head -n 15
```

## Limites e trade-offs
Dica estratégica para avaliação de maturidade do SOC: não olhe apenas se uma técnica `attack.tXXXX` tem pelo menos 1 regra — verifique o **`level` (`informational`, `low`, `medium`, `high`, `critical`)** e o **`status` (`stable`, `test`, `experimental`)** das regras daquela técnica, e se elas dependem apenas de `CommandLine` (fácil de contornar por um atacante!) ou também de eventos de telemetria profunda de kernel/Sysmon (`ProcessAccess` EventID 10, `ImageLoad` EventID 7, `PipeEvent` EventID 17/18)!

## Como verificar
Consulte também a plataforma oficial da comunidade **Phoenix (`sigma.nasbench.dev`)** citada no `README.md` do SigmaHQ para explorar o mapeamento ATT&CK das 3.000+ regras.

## Conexões
- [[sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo]] — Veja também: Uso de **Placeholders (`%variavel%` eModificador `|expand`)** no Sigma para Parametrizar Domínios VIP, Sub-redes de Servidores e Contas de Administração.
- [[sigma-pipeline-detection-as-code-cicd-validacao-schema-testes]] — Veja também: Implantando **Detection-as-Code (DaC)** com Sigma em CI/CD: Validação de JSON Schema (`sigma check`), Linting, Conversão Automatizada e Deploy no SIEM.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao]] — Referência cruzada direta com pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
