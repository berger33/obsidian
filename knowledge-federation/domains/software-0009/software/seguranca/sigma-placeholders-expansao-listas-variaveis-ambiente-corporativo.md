---
id: software.seguranca.tranche11.001088
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

# Uso de **Placeholders (`%variavel%` eModificador `|expand`)** no Sigma para Parametrizar Domínios VIP, Sub-redes de Servidores e Contas de Administração

## Em uma frase
Como escrever uma regra Sigma compartilhável que verifica se alguém acessou um **Servidor Crítico (Domain Controller / Cofre de Senhas)** ou tentou logar com uma **Conta VIP / Tier-0**, sem colocar os hostnames e nomes de usuários reais da sua empresa diretamente dentro do código da regra?

## Por que importa
A especificação Sigma define o mecanismo de **Placeholders (`%nome_do_placeholder%`)** ativado pelo modificador de valor **`|expand`**!

## Como funciona
Na regra Sigma, você escreve **`WorkstationName|expand: '%domain_controllers%'`** ou **`TargetUserName|expand: '%tier0_admins%'`**; e, no seu arquivo de **Processing Pipeline** do `pySigma` (ou na pasta de configuração do **Hayabusa**, que possui o subcomando dedicado `hayabusa expand-list`!), você fornece a lista real de servidores e contas da sua organização que substituirá `%domain_controllers%` no momento da compilação!

## Exemplo
```yaml
title: Logon Interativo de Conta Comum em Controlador de Dominio (Tier-0)
id: 3f4e5d6c-7b8a-4901-8234-56789abcdef0
status: stable
logsource:
    product: windows
    service: security
detection:
    selection_logon:
        EventID: 4624
        LogonType:
            - 2
            - 10
        ComputerName|expand: '%enterprise_domain_controllers%'
    filter_admins:
        TargetUserName|expand: '%tier0_domain_admins%'
    condition: selection_logon and not filter_admins
level: critical
```

## Limites e trade-offs
Além dos placeholders customizados da sua organização, a especificação v2.1 do Sigma documenta os **Standard Placeholders** para variáveis de ambiente do sistema operacional (como `%SystemRoot%`, `%AppData%`, `%Temp%`, `%Public%`), que os pipelines de conversão expandem automaticamente para os caminhos reais de cada versão do Windows!

## Como verificar
Centralizar a lista de IPs de scanners de vulnerabilidade autorizados (`%authorized_vuln_scanners%`) e de Domain Controllers (`%enterprise_domain_controllers%`) em um único arquivo de placeholders evita ter que editar 200 regras toda vez que um servidor novo entra em produção.

## Conexões
- [[sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem]] — Veja também: Compilação de Regras com **`sigma-cli` e `pySigma`**: Backends (**Splunk SPL, Elastic EQL/Lucene, Sentinel KQL, QRadar, Loki**) e Pipelines de Transformação.
- [[sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags]] — Veja também: Governança de Cobertura de Detecção com Sigma: Mapeamento de **Tags MITRE ATT&CK (`attack.tXXXX`)**, CVEs (`cve.YYYY.NNNN`) e **ATT&CK Navigator**.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Referência cruzada direta com sigma-logica-detection-modificadores-valores-base64offset-windash-re.
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Referência cruzada direta com hayabusa-comandos-analise-metricas-logon-summary-critical-systems.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
