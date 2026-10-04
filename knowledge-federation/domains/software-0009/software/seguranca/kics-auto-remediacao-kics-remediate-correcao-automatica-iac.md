---
id: software.seguranca.tranche09.000803
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

# KICS **`remediate`**: Auto-Remediação Determinística de Misconfigurations em Infraestrutura como Código (`remediation` + `remediationType`)

## Em uma frase
Além de apontar a linha exata de uma falha de segurança, muitas consultas do KICS incluem nos seus resultados os campos **`remediation`** e **`remediationType`** (`addition`, `replacement` ou `removal`), permitindo que o subcomando **`kics remediate`** aplique a correção diretamente no código-fonte de IaC!

## Por que importa
O fluxo de auto-remediação opera em dois passos: **(1)** executar **`kics scan -p ./infra -o ./out --report-formats json`** para gerar o relatório `results.json` contendo as instruções de remediação; e **(2)** executar **`kics remediate --results ./out/results.json`** (podendo filtrar quais correções aplicar com **`--include-ids <similarity_id>`**)!

## Como funciona
Isso permite que um bot de Pull Request no GitHub/GitLab gere sugestões automáticas de código (*Suggested Changes*) para adicionar `encrypted = true` em volumes EBS ou `runAsNonRoot: true` em Deployments Kubernetes.

## Exemplo
```bash
# Executar o scan do KICS gerando results.json e aplicar auto-remediacao verificando o diff no Git
kics scan -p /cases/iac/terraform -t Terraform --report-formats json -o /cases/iac/out --output-name scan_res
kics remediate --results /cases/iac/out/scan_res.json -v
git -C /cases/iac/terraform diff
```

## Limites e trade-offs
Nunca aplique `kics remediate` diretamente na branch `main` sem revisão humana ou sem rodar **`terraform plan` / `kubectl diff`**, pois adicionar um atributo de criptografia em um recurso de banco de dados ou disco que já existe em produção pode forçar o Terraform a destruir e recriar (`forces replacement`) o recurso!

## Como verificar
Verifique no `results.json` quais achados possuem o campo `"remediation"` preenchido antes de invocar `kics remediate`.

## Conexões
- [[kics-desenvolvimento-queries-customizadas-rego-cxpolicy-metadata]] — Veja também: KICS: Criação de **Consultas Customizadas em `Rego` (`CxPolicy [ result ]`)**, Metadados `metadata.json` e `kics generate-id`.
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — Veja também: KICS: Governança de Exceções — Comentários Inline (**`# kics-scan ignore`**) e Exclusão por **`similarityID` (`-x` / `--exclude-results`)**.
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — Referência cruzada direta com kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
