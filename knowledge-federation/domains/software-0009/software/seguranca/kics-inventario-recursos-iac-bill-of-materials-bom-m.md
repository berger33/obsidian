---
id: software.seguranca.tranche09.000805
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

# KICS: Geração de **Inventário de Recursos de Nuvem Pré-Deploy (*IaC Bill of Materials — BoM*, `-m` / `--bom`)**

## Em uma frase
Muitas vezes, a equipe de Cloud Security sabe o que já está rodando na conta AWS/GCP via Prowler, mas não tem um inventário estruturado de **quais recursos de infraestrutura um Pull Request de Terraform/CloudFormation/Helm está prestes a criar** antes do `apply`.

## Por que importa
Conforme documentado em `docs/commands.md`, passar a flag **`-m` / `--bom`** ao comando `kics scan` instrui o KICS a incluir na saída (`results.json`) uma seção completa de **Bill of Materials (`bom`)** de todos os recursos de infraestrutura declarados no código!

## Como funciona
Cada item do BoM do KICS detalha o tipo do recurso (`aws_db_instance`, `aws_s3_bucket`, `kubernetes_deployment`), a plataforma, o provedor de nuvem, o arquivo/linha de origem, se possui criptografia configurada e quais políticas de acesso se aplicam a ele.

## Exemplo
```bash
# Executar o KICS habilitando a geracao do Bill of Materials (-m / --bom) para inventariar todos os recursos IaC declarados
kics scan -p /cases/iac/terraform \
  --bom \
  --report-formats json \
  -o /cases/iac/out --output-name iac_with_bom
jq '.bom' /cases/iac/out/iac_with_bom.json
```

## Limites e trade-offs
Atenção a um requisito de privacidade documentado pelo KICS: para que um recurso apareça no relatório `--bom`, ele deve seguir boas práticas de isolamento (por exemplo, buckets ou recursos explicitamente marcados como públicos sem restrição são sinalizados nas vulnerabilidades e tratados de forma distinta do BoM privado).

## Como verificar
Integre a saída `.bom` do KICS ao catálogo de ativos da empresa para rastrear desde o Git quais repositórios são donos de quais recursos de nuvem.

## Conexões
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — Veja também: KICS: Governança de Exceções — Comentários Inline (**`# kics-scan ignore`**) e Exclusão por **`similarityID` (`-x` / `--exclude-results`)**.
- [[kics-analise-terraform-variaveis-tfvars-modulos-plan-json]] — Veja também: KICS para **Terraform e OpenTofu**: Resolução de Variáveis (`--terraform-vars-path`), Módulos e Auditoria de `terraform show -json`.
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
