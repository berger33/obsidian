---
id: software.seguranca.tranche09.000801
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

# **Checkmarx KICS (*Keeping Infrastructure as Code Secure*)**: Arquitetura de SAST para **Infraestrutura como Código (IaC)** Baseada em **Open Policy Agent (Rego)**

## Em uma frase
**KICS** (`Checkmarx/kics`, licença Apache-2.0, escrito em Go) é um motor open-source de análise estática de segurança (**IaC SAST**) que detecta vulnerabilidades de segurança, falhas de conformidade e configurações inseguras em mais de **20 plataformas de Infraestrutura como Código** antes que qualquer recurso seja provisionado na nuvem.

## Por que importa
Diferente de scanners acoplados a uma única linguagem de template, a arquitetura do KICS funciona em duas fases desacopladas: **(1) Parsers de Plataforma** convertem arquivos heterogêneos (**Terraform HCL**, **Kubernetes YAML**, **Helm Charts**, **Dockerfile**, **Docker Compose**, **AWS CloudFormation/SAM/CDK**, **Ansible**, **Azure Resource Manager/Bicep**, **OpenAPI 3.0**, **gRPC Protobuf** e **GitHub Actions**) em uma representação intermediária JSON unificada; e **(2) Motor Open Policy Agent (OPA)** avalia mais de **2.000 consultas declarativas escritas em `Rego` (`CxPolicy`)** sobre esse documento normalizado!

## Como funciona
Isso permite auditar um repositório *monorepo* inteiro contendo Terraform, manifestos Kubernetes, Dockerfiles e especificações OpenAPI em uma única execução (`kics scan -p .`).

## Exemplo
```bash
# Verificar a versao do KICS, listar todas as plataformas de IaC suportadas e executar um scan em um repositorio local
kics version
kics list-platforms
kics scan -p /cases/iac/repo -o /cases/iac/reports
```

## Limites e trade-offs
Para evitar que o KICS tente adivinhar parsers de plataformas que você não usa no projeto (economizando memória e tempo de CPU no CI/CD), especifique explicitamente as plataformas desejadas com **`-t` / `--type`** (ex.: **`kics scan -p . -t Terraform,Kubernetes,Dockerfile`**)!

## Como verificar
Verifique no resumo final da execução a contagem de arquivos analisados (`Files scanned`) e as descobertas agrupadas por severidade (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`).

## Conexões
- [[kics-desenvolvimento-queries-customizadas-rego-cxpolicy-metadata]] — Veja também: KICS: Criação de **Consultas Customizadas em `Rego` (`CxPolicy [ result ]`)**, Metadados `metadata.json` e `kics generate-id`.
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — Referência cruzada direta com kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
