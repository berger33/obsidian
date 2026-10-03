---
id: software.seguranca.tranche11.001030
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
fontes: ["https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md", "https://github.com/RhinoSecurityLabs/pacu/wiki/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Engenharia de Detecção (**Purple Team AWS**) com Pacu: Como Validar Regras **Sigma (`aws_cloudtrail`)** e Alertas do **Amazon GuardDuty**

## Em uma frase
A aplicação mais produtiva do **Pacu** dentro de uma equipe corporativa de Segurança é como motor de **Purple Team e Validação Contínua de Detecção em Nuvem**: em vez de apenas assumir que o seu SIEM (Splunk, Elastic, Sentinel, Panther) e o **Amazon GuardDuty** detectarão um ataque na AWS, você executa módulos selecionados do Pacu em uma conta de homologação (`sandbox-purple-team`) e mede o **MTTD (*Mean Time to Detect*)** real das suas regras!

## Por que importa
Cada execução de módulo no Pacu registra no arquivo **`cmd_log.txt`** e no **`api_calls.txt`** da pasta da sessão (`~/.local/share/pacu/<sessao>/`) os timestamps exatos e os serviços invocados.

## Como funciona
Cruze esse log do Pacu com os eventos `aws.cloudtrail` ingeridos no seu SIEM e com o conjunto oficial de regras **Sigma para CloudTrail (`rules/cloud/aws/cloudtrail/`)** para provar que cada etapa da cadeia de ataque (reconhecimento IAM -> escalação de privilégio -> download de `UserData` -> tentativa de `StopLogging`) dispara um alerta acionável no SOC!

## Exemplo
```bash
# Executar um teste controlado de Purple Team no Pacu e inspecionar o log de auditoria da sessao para correlacionar com o CloudTrail
pacu --session purple-team-drill \
  --module-name detection__enum_services \
  --exec
ls -la ~/.local/share/pacu/purple-team-drill/
```

## Limites e trade-offs
Ao documentar o exercício de Purple Team, anexe os logs da sessão do Pacu (`~/.local/share/pacu/<sessao>/`) junto com os IDs dos eventos do CloudTrail (`eventID`) e os UUIDs das regras **Sigma** que dispararam.

## Como verificar
Sempre destrua ou reverta imediatamente quaisquer recursos de teste criados na conta de laboratório após o término da bateria de validação.

## Conexões
- [[pacu-persistencia-aws-backdoor-iam-roles-users-lambda-remediacao]] — Veja também: Análise de Técnicas de **Persistência em AWS IAM** Mapeadas pelo Pacu (`iam__backdoor_*`) e Playbook de **Erradicação e Resposta a Incidentes (DFIR)**.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[pacu-auditoria-monitoramento-cloudtrail-guardduty-config-deteccao]] — Referência cruzada direta com pacu-auditoria-monitoramento-cloudtrail-guardduty-config-deteccao.
- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — Referência cruzada direta com sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
