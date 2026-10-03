---
id: software.seguranca.tranche09.000802
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

# KICS: Criação de **Consultas Customizadas em `Rego` (`CxPolicy [ result ]`)**, Metadados `metadata.json` e `kics generate-id`

## Em uma frase
Toda regra de segurança do KICS consiste em uma pasta contendo dois arquivos: **`metadata.json`** (que define o UUID único gerado por **`kics generate-id`**, `queryName`, `severity`, `category`, `descriptionText`, `platform` e `cwe`) e **`query.rego`** (no pacote `package Cx`, que define a regra **`CxPolicy[result]`**).

## Por que importa
Quando a condição de falha de segurança é satisfeita no documento JSON normalizado (`input.document[i]`), a regra `CxPolicy[result]` retorna um objeto estruturado contendo **`documentId`**, **`resourceType`**, **`resourceName`**, **`searchKey`** (o caminho exato no arquivo IaC para o KICS apontar o número da linha!), **`issueType`** (`"MissingAttribute"`, `"IncorrectValue"` ou `"RedundantAttribute"`), **`keyExpectedValue`** e **`keyActualValue`**!

## Como funciona
Com a flag **`-q` / `--queries-path`**, sua equipe pode carregar um diretório de políticas corporativas internas (ex.: exigir tags obrigatórias `CostCenter`/`DataClassification` ou proibir regiões fora de `sa-east-1`) junto com as queries oficiais.

## Exemplo
```rego
package Cx

# Query KICS Rego customizada: exigir tag 'DataClassification' em todos os buckets AWS S3 no Terraform
CxPolicy[result] {
    resource := input.document[i].resource.aws_s3_bucket[name]
    not resource.tags.DataClassification
    result := {
        "documentId": input.document[i].id,
        "resourceType": "aws_s3_bucket",
        "resourceName": name,
        "searchKey": sprintf("aws_s3_bucket[%s].tags", [name]),
        "issueType": "MissingAttribute",
        "keyExpectedValue": sprintf("aws_s3_bucket[%s].tags.DataClassification deve estar definido", [name]),
        "keyActualValue": sprintf("aws_s3_bucket[%s].tags.DataClassification esta ausente", [name]),
    }
}
```

## Limites e trade-offs
Use sempre **`kics generate-id`** ao criar uma nova query customizada para garantir um UUID v4 válido no `metadata.json` sem colisão com as queries oficiais do KICS.

## Como verificar
Execute `kics scan -p ./terraform -q ./custom_queries --include-queries <UUID>` para testar isoladamente sua nova regra Rego.

## Conexões
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Veja também: **Checkmarx KICS (*Keeping Infrastructure as Code Secure*)**: Arquitetura de SAST para **Infraestrutura como Código (IaC)** Baseada em **Open Policy Agent (Rego)**.
- [[kics-auto-remediacao-kics-remediate-correcao-automatica-iac]] — Veja também: KICS **`remediate`**: Auto-Remediação Determinística de Misconfigurations em Infraestrutura como Código (`remediation` + `remediationType`).
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — Referência cruzada direta com kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
