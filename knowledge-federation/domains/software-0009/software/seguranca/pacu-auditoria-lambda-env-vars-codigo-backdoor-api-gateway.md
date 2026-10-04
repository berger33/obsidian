---
id: software.seguranca.tranche11.001027
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

# Auditoria e Pós-Exploração de **AWS Lambda (`lambda__enum`)** no Pacu: Extração de Código-Fonte, Variáveis de Ambiente e Riscos de `UpdateFunctionCode`

## Em uma frase
Funções Serverless no **AWS Lambda** são um dos alvos mais valiosos em pentests de nuvem por dois motivos: primeiro, cada função Lambda possui sua própria **Execution Role (`IAM Role`)**; segundo, qualquer identidade com a permissão de leitura **`lambda:GetFunction`** recebe uma URL pré-assinada do S3 para **baixar o pacote `.zip` completo do código-fonte da função junto com todas as suas Variáveis de Ambiente!**

## Por que importa
No Pacu, o módulo **`lambda__enum`** automatiza a enumeração de todas as funções Lambda em todas as regiões configuradas na sessão, extraindo metadados, variáveis de ambiente (`Environment.Variables`), políticas de recursos, versões e URLs de código!

## Como funciona
Além disso, se uma função Lambda for acionada por eventos IAM/CloudTrail ou tiver uma Execution Role privilegiada e o atacante possuir `lambda:UpdateFunctionCode` ou `lambda:UpdateFunctionConfiguration` (por exemplo, injetando uma *Lambda Layer* maliciosa!), ele consegue executar código sob a identidade da Execution Role daquela Lambda!

## Exemplo
```bash
# Enumerar todas as funcoes AWS Lambda e suas variaveis de ambiente nas regioes ativas da sessao no Pacu
pacu --session pentest-aws-lab \
  --module-name lambda__enum \
  --exec
pacu --session pentest-aws-lab --data Lambda
```

## Limites e trade-offs
Após rodar o `lambda__enum`, você pode passar os arquivos e variáveis extraídos diretamente pelo **Gitleaks**, **TruffleHog** ou **`detect-secrets`** para identificar chaves de terceiros (Stripe, SendGrid, Slack, bancos externos) deixadas nas variáveis de ambiente das funções!

## Como verificar
Ative o **AWS Code Signing for Lambda** em produção para garantir que apenas pacotes `.zip` assinados digitalmente pela sua pipeline oficial de CI/CD possam ser implantados em funções Lambda (`UpdateFunctionCode`).

## Conexões
- [[pacu-pos-exploracao-ec2-userdata-ssm-ebs-snapshots-exfiltracao]] — Veja também: Pós-Exploração em **Amazon EC2, SSM e EBS** com Pacu: Extração de Segredos de **`UserData` (`ec2__download_userdata`)**, Snapshots EBS e Execução via **Systems Manager**.
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Veja também: Detecção de **Honeytokens / Canarytokens AWS** (`iam__detect_honeytokens`) e Como Projetar **Decoys de Credenciais AWS Indetectáveis** para o Blue Team.
- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — Referência cruzada direta com pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos.
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Referência cruzada direta com pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque.

## Fontes
- [Rhino Security Labs Pacu Official GitHub — Open-Source AWS Exploitation Framework](https://raw.githubusercontent.com/RhinoSecurityLabs/pacu/master/README.md) — repositório oficial do Pacu cobrindo arquitetura de sessões SQLite, comandos interativos e CLI (`--session`, `--module-name`, `--exec`, `--whoami`, `--data`); consultado em 2026-10-03.
- [Rhino Security Labs Pacu Official Wiki — Architecture, Modules & Usage Reference](https://github.com/RhinoSecurityLabs/pacu/wiki/) — wiki oficial do Pacu detalhando categorias de módulos de enumeração IAM, escalação de privilégio, pós-exploração EC2/Lambda/EBS e logs de auditoria; consultado em 2026-10-03.
