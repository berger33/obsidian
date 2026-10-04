---
id: software.seguranca.tranche11.001081
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

# **SigmaHQ (`SigmaHQ/sigma`)**: Arquitetura do Padrão Aberto Universal de **Regras de Detecção para Logs e SIEMs** (*Detection-as-Code* em YAML)

## Em uma frase
Criado por Florian Roth e Thomas Patzke e mantido pela comunidade global **SigmaHQ** (`SigmaHQ/sigma`, com mais de **3.000 regras de detecção revisadas por pares**), o **Sigma** é para arquivos de log e SIEMs o que o **Snort/Suricata** é para tráfego de rede e o **YARA** é para arquivos binários: um formato de assinatura aberto, padronizado e agnóstico de fornecedor escrito em **YAML**!

## Por que importa
Qual problema crônico de operações de segurança (SOC) o Sigma resolve? Antes do Sigma, toda vez que um novo ataque, APT ou Zero-Day era publicado, cada empresa precisava traduzir manualmente os indicadores para a linguagem proprietária do seu SIEM (**SPL no Splunk**, **KQL no Microsoft Sentinel / Elastic**, **AQL no QRadar**, **LogScale**, **Loki**), ficando presa ao fornecedor (*Vendor Lock-in*).

## Como funciona
Com o **Sigma (Especificação v2.1.0)**, o engenheiro de detecção escreve a regra **uma única vez em YAML** (nas 5 categorias do repositório oficial: `Generic Detection Rules`, `Threat Hunting Rules`, `Emerging Threats`, `Compliance Rules` e `Placeholder Rules`) e o compilador **`sigma-cli` / `pySigma`** a transpila automaticamente para qualquer SIEM, EDR ou motor forense (como **Hayabusa** e **Velociraptor**)!

## Exemplo
```yaml
title: Execucao Suspeita de Whoami para Reconhecimento de Privilegios
id: 929a690e-bef0-4204-a928-ef5e620d6fcc
status: stable
description: Detecta a execucao do utilitario whoami.exe frequentemente usado apos exploracao inicial
author: Equipe de Engenharia de Deteccao (SecOps)
date: 2026-10-03
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\whoami.exe'
    condition: selection
falsepositives:
    - Scripts administrativos de inventario conhecidos
level: high
tags:
    - attack.discovery
    - attack.t1033
```

## Limites e trade-offs
Conforme define a especificação oficial (`sigma-rules-specification.md` v2.1.0), para garantir interoperabilidade global, arquivos Sigma `.yml` devem usar codificação **UTF-8**, quebras de linha **LF**, indentação de **4 espaços**, chaves em minúsculas e strings delimitadas por aspas simples `'...'`.

## Como verificar
Explore o repositório oficial `SigmaHQ/sigma` para importar imediatamente milhares de detecções mapeadas para o **MITRE ATT&CK (`tags: attack.tXXXX`)**.

## Conexões
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Veja também: Anatomia do Bloco **`logsource`** e **`taxonomy`** na Especificação Sigma v2.1: Abstraindo **Windows Event Logs, Sysmon, Linux `auditd` e CloudTrail**.
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Referência cruzada direta com sigma-logica-detection-modificadores-valores-base64offset-windash-re.
- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — Referência cruzada direta com hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust.

## Fontes
- [SigmaHQ Official Repository — Generic Signature Format for SIEM Systems (3,000+ Detection & Hunting Rules)](https://raw.githubusercontent.com/SigmaHQ/sigma/master/README.md) — repositório principal do SigmaHQ cobrindo categorias de regras, ecossistema `sigma-cli` / `pySigma` e mapeamento MITRE ATT&CK; consultado em 2026-10-03.
- [Sigma Rules Specification v2.1.0 (`SigmaHQ/sigma-specification`)](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/specification/sigma-rules-specification.md) — especificação técnica oficial v2.1.0 das regras Sigma cobrindo estrutura YAML, `logsource`, `detection`, modificadores de valor, `correlation` e `filter`; consultado em 2026-10-03.
