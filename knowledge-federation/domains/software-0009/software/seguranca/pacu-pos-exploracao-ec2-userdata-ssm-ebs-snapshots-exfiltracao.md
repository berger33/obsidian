---
id: software.seguranca.tranche11.001026
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

# Pós-Exploração em **Amazon EC2, SSM e EBS** com Pacu: Extração de Segredos de **`UserData` (`ec2__download_userdata`)**, Snapshots EBS e Execução via **Systems Manager**

## Em uma frase
Muitos engenheiros de infraestrutura acham que, para roubar dados de uma instância EC2, um atacante precisa ter a chave privada SSH (`.pem`) e acesso de rede na porta `22`. Os módulos de pós-exploração EC2/EBS/SSM do Pacu demonstram três caminhos pela **API do Plano de Controle da AWS** que ignoram completamente o firewall de rede e o SSH!

## Por que importa
Primeiro, **`ec2__download_userdata`**: busca e decodifica em Base64/Gzip os scripts de inicialização **`UserData`** (`ec2:DescribeInstanceAttribute`) de todas as instâncias EC2 e Launch Templates da conta — onde administradores frequentemente deixam senhas de banco de dados, tokens de registro de runners CI/CD ou chaves de API em texto claro!

## Como funciona
Segundo, **`ebs__explore_snapshots`**: lista snapshots de volumes EBS, compartilha ou clona um volume a partir do snapshot da instância alvo e lê o disco inteiro sem tocar na VM em produção! E terceiro, **`systems_manager__rce_ec2`**: se a instância EC2 roda o agente **AWS Systems Manager (`ssm-agent`)** (padrão na Amazon Linux 2/2023 e Ubuntu AMIs), qualquer identidade com permissão **`ssm:SendCommand`** executa comandos como `root` dentro da instância via API da AWS sem abrir nenhuma porta de rede!

## Exemplo
```bash
# Auditar scripts UserData de todas as instancias EC2 da sessao em busca de segredos hardcoded (ec2__download_userdata)
pacu --session pentest-aws-lab \
  --module-name ec2__download_userdata \
  --exec
```

## Limites e trade-offs
Como defender suas instâncias EC2 e volumes EBS contra esses três vetores do Plano de Controle? **(1)** Nunca coloque segredos em `UserData` (faça o script buscar o segredo em tempo de boot no **AWS Secrets Manager** ou **SSM Parameter Store `SecureString`**); **(2)** Criptografe 100% dos volumes EBS e snapshots com chaves **AWS KMS Customer Managed Keys (CMK)** com políticas de chave restritas (mesmo que alguém compartilhe um snapshot, sem permissão `kms:Decrypt` na CMK o disco é ilegível!); e **(3)** Trate a permissão `ssm:SendCommand` e `ssm:StartSession` no IAM com o mesmo rigor de acesso `root` SSH!

## Como verificar
Monitore no CloudTrail chamadas incomuns a `DescribeInstanceAttribute` (`attribute=userData`) e `ModifySnapshotAttribute` (`createVolumePermission`).

## Conexões
- [[pacu-auditoria-monitoramento-cloudtrail-guardduty-config-deteccao]] — Veja também: Pacu vs Monitoramento AWS (**CloudTrail, GuardDuty, Config & CloudWatch**): Módulos de Enumeração (`detection__enum_services`) e Controles de Blindagem (SCPs).
- [[pacu-auditoria-lambda-env-vars-codigo-backdoor-api-gateway]] — Veja também: Auditoria e Pós-Exploração de **AWS Lambda (`lambda__enum`)** no Pacu: Extração de Código-Fonte, Variáveis de Ambiente e Riscos de `UpdateFunctionCode`.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Referência cruzada direta com pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque.
- [[cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3]] — Referência cruzada direta com cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
