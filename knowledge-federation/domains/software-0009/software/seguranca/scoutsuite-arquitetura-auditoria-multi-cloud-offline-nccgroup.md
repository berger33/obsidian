---
id: software.seguranca.tranche11.001011
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
fontes: ["https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md", "https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **NCC Group Scout Suite (`nccgroup/ScoutSuite`)**: Arquitetura de Auditoria de Postura de Segurança Multi-Cloud Assíncrona e **Inspeção 100% Offline**

## Em uma frase
Desenvolvido pelos consultores e auditores de segurança de nuvem do **NCC Group** (`nccgroup/ScoutSuite`, escrito em Python assíncrono com `asyncio`, `ThreadPoolExecutor` e `asyncio_throttle`), o **Scout Suite** é uma ferramenta open-source de auditoria de postura de segurança multi-cloud (**CSPM point-in-time**) com suporte a **Amazon Web Services (AWS)**, **Microsoft Azure**, **Google Cloud Platform (GCP)**, **Alibaba Cloud (`aliyun`)**, **Oracle Cloud Infrastructure (`oci`)**, **DigitalOcean (`do`)** e **Kubernetes**!

## Por que importa
Qual é a filosofia operacional central do Scout Suite destacada na documentação oficial? **"Coletar uma única vez via APIs da nuvem e conduzir toda a análise de segurança 100% offline"**: em vez de forçar o auditor a clicar por dezenas de páginas lentas nos consoles web da AWS/Azure/GCP ou manter conexões ativas com a conta do cliente, o Scout Suite baixa toda a árvore de metadados de configuração dos serviços (`scoutsuite-results/scoutsuite_results_<report>.js`), processa o motor de regras (`ProcessingEngine` + `Ruleset`) e gera um **Painel Web Interativo Autônomo em HTML/JS (`report.html`)** que funciona localmente no navegador sem internet!

## Como funciona
Além disso, a flag **`--fetch-local`** permite reexecutar novos conjuntos de regras (`--ruleset`) e arquivos de exceção (`--exceptions`) sobre os dados já coletados no disco **sem fazer nenhuma nova chamada de API na nuvem**!

## Exemplo
```bash
# Executar uma auditoria completa de seguranca na AWS com o Scout Suite usando um perfil nomeado e sem abrir navegador automaticamente
scout aws \
  --profile auditoria-secops \
  --report-dir /cases/cloud-audit/scout-aws \
  --report-name aws-prod-2026 \
  --no-browser
```

## Limites e trade-offs
Para testar o Scout Suite em laboratório, o próprio NCC Group mantém o repositório **`nccgroup/sadcloud`** (scripts Terraform que provisionam intencionalmente configurações inseguras para validação de ferramentas CSPM!).

## Como verificar
Verifique que o arquivo `/cases/cloud-audit/scout-aws/aws-prod-2026.html` e o payload `scoutsuite-results/scoutsuite_results_aws-prod-2026.js` foram gerados com sucesso.

## Conexões
- [[scoutsuite-auditoria-aws-iam-s3-ec2-rds-cloudtrail-vpc]] — Veja também: Scout Suite na **AWS (`scout aws`)**: Escopo de Serviços (`--services`), Regiões (`--regions`), Controle de Taxa (`--max-rate`) e Mínimo Privilégio IAM.
- [[scoutsuite-auditoria-azure-rbac-entra-storage-network-keyvault]] — Referência cruzada direta com scoutsuite-auditoria-azure-rbac-entra-storage-network-keyvault.

## Fontes
- [NCC Group Scout Suite Official GitHub — Multi-Cloud Security Auditing Tool](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/README.md) — repositório oficial do Scout Suite cobrindo auditoria point-in-time offline para AWS, Azure, GCP, Alibaba Cloud, OCI, DigitalOcean e Kubernetes; consultado em 2026-10-03.
- [Scout Suite Official CLI & Engine Implementation (`ScoutSuite/__main__.py`)](https://raw.githubusercontent.com/nccgroup/ScoutSuite/master/ScoutSuite/__main__.py) — implementação oficial dos provedores, parâmetros de autenticação, `--fetch-local`, `--update`, `--ruleset`, `--exceptions` e `--ip-ranges`; consultado em 2026-10-03.
