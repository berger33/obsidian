---
id: software.seguranca.tranche11.001025
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

# Pacu vs Monitoramento AWS (**CloudTrail, GuardDuty, Config & CloudWatch**): Módulos de Enumeração (`detection__enum_services`) e Controles de Blindagem (SCPs)

## Em uma frase
Quando um invasor compromete uma credencial com altas permissões na AWS, uma de suas primeiras ações é mapear os controles de monitoramento da conta (**`detection__enum_services`**) e tentar cegar ou alterar o **AWS CloudTrail**, o **Amazon GuardDuty**, o **AWS Config** ou os alarmes do **CloudWatch** (**`detection__disruption`**).

## Por que importa
Estudar os módulos da categoria `detection__*` do Pacu mostra exatamente por que **controles de log nunca devem poder ser modificados ou desativados de dentro da própria conta monitorada**!

## Como funciona
Veja os 4 ataques contra telemetria que o Pacu simula e como **blindar estruturalmente sua AWS Organizations contra todos eles**: **(1)** Parar a trilha (`cloudtrail:StopLogging`) ou deletá-la (`cloudtrail:DeleteTrail`); **(2)** Minimizar a trilha (`cloudtrail:UpdateTrail` desativando `IncludeGlobalServiceEvents` ou `IsMultiRegionTrail`, ou adicionando Event Selectors que excluem eventos de leitura/escrita!); **(3)** Desativar ou deletar o detector do GuardDuty (`guardduty:DeleteDetector` / `UpdateDetector`) ou criar um filtro de supressão (`guardduty:CreateFilter`) para esconder todos os alertas!; e **(4)** Deletar regras de eventos do EventBridge (`events:DeleteRule`)!

## Exemplo
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ProtectCloudTrailAndGuardDutyFromTampering",
      "Effect": "Deny",
      "Action": [
        "cloudtrail:StopLogging",
        "cloudtrail:DeleteTrail",
        "cloudtrail:UpdateTrail",
        "cloudtrail:PutEventSelectors",
        "guardduty:DeleteDetector",
        "guardduty:DisassociateFromMasterAccount",
        "guardduty:UpdateDetector",
        "guardduty:CreateFilter",
        "config:StopConfigurationRecorder",
        "config:DeleteConfigurationRecorder"
      ],
      "Resource": "*"
    }
  ]
}
```

## Limites e trade-offs
Quando você aplica a **Service Control Policy (SCP)** acima na raiz da sua **AWS Organizations** e utiliza um **Organization Trail** gravando em um bucket S3 central de uma conta dedicada de *Log Archive* (com **S3 Object Lock em modo Compliance**), **nem mesmo um atacante que conquiste `AdministratorAccess` total na conta comprometida consegue parar, alterar ou apagar um único log do CloudTrail ou alerta do GuardDuty**!

## Como verificar
Use `pacu --module-name detection__enum_services --exec` em auditorias Purple Team para validar se seus agentes de monitoramento estão ativos em todas as regiões da AWS.

## Conexões
- [[pacu-enumeracao-externa-sem-autenticacao-iam-roles-users-account-id]] — Veja também: Reconhecimento AWS **Sem Credenciais na Conta Alvo** no Pacu: Enumeração de Roles e Usuários via Validação de `AssumeRolePolicy` e `S3/KMS` Cross-Account.
- [[pacu-pos-exploracao-ec2-userdata-ssm-ebs-snapshots-exfiltracao]] — Veja também: Pós-Exploração em **Amazon EC2, SSM e EBS** com Pacu: Extração de Segredos de **`UserData` (`ec2__download_userdata`)**, Snapshots EBS e Execução via **Systems Manager**.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — Referência cruzada direta com steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
