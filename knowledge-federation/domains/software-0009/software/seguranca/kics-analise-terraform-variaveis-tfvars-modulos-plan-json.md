---
id: software.seguranca.tranche09.000806
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/Checkmarx/kics/master/README.md", "https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md", "https://docs.kics.io/latest/queries/all-queries/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KICS para **Terraform e OpenTofu**: Resolução de Variáveis (`--terraform-vars-path`), Módulos e Auditoria de `terraform show -json`

## Em uma frase
Um desafio clássico da análise estática de Terraform/OpenTofu é o uso intensivo de **variáveis (`var.encryption_enabled`)** cujos valores reais estão definidos em arquivos `.tfvars` separados por ambiente (`prod.tfvars`, `dev.tfvars`): se o scanner analisar apenas o `.tf` sem ler o `prod.tfvars`, ele não saberá qual valor `var.encryption_enabled` assumirá em produção!

## Por que importa
O KICS resolve isso através da flag **`--terraform-vars-path <caminho/prod.tfvars>`**, que interpola os valores reais das variáveis durante a construção da árvore sintática do HCL antes de rodar as queries Rego!

## Como funciona
E para cenários complexos com loops `for_each`, `dynamic` blocks e módulos remotos aninhados, você também pode gerar o plano resolvido do Terraform (`terraform plan -out=tf.plan && terraform show -json tf.plan > plan.json`) e auditar o plano consolidado.

## Exemplo
```bash
# Auditar codigo Terraform injetando os valores reais de producao via --terraform-vars-path
kics scan -p /cases/iac/terraform \
  -t Terraform \
  --terraform-vars-path /cases/iac/terraform/envs/prod.tfvars \
  --fail-on high,critical \
  -o /cases/iac/out
```

## Limites e trade-offs
Quando o seu projeto Terraform referencia submódulos ou especifica provedores específicos (`aws`, `gcp`, `azure`), use **`--cloud-provider aws`** para restringir o carregamento de queries apenas ao provedor de nuvem utilizado, acelerando o scan.

## Como verificar
Compare o resultado do `kics scan` usando `dev.tfvars` vs `prod.tfvars` para garantir que configurações permissivas de desenvolvimento não vazem para o arquivo de produção.

## Conexões
- [[kics-inventario-recursos-iac-bill-of-materials-bom-m]] — Veja também: KICS: Geração de **Inventário de Recursos de Nuvem Pré-Deploy (*IaC Bill of Materials — BoM*, `-m` / `--bom`)**.
- [[kics-auditoria-kubernetes-helm-dockerfile-pod-security-containers]] — Veja também: KICS para **Kubernetes, Helm Charts e Dockerfiles**: Auditoria Integrada da Imagem (`Dockerfile`) até o Manifesto do Pod (`Deployment`).
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — Referência cruzada direta com kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
