---
id: software.seguranca.tranche09.000808
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

# KICS para **OpenAPI (v2/v3) e gRPC (`.proto`)**: *Shift-Left API Security* desde o Contrato da API (`--enable-openapi-refs`)

## Em uma frase
A maioria das equipes só testa a segurança de uma API REST ou gRPC depois que o código já foi escrito e implantado em homologação; porém, falhas graves de design de API — como endpoints sem esquema `security` global/por operação, transporte `http://` não cifrado, parâmetros numéricos/strings sem limites (`maxLength`, `maximum`, `pattern` contra DoS/Injeção) ou códigos de resposta mal especificados — já estão visíveis no contrato **OpenAPI (`openapi.yaml` / `swagger.json`)** e **gRPC (`service.proto`)**!

## Por que importa
O KICS inclui plataformas dedicadas **`OpenAPI`** e **`GRPC`** com dezenas de queries baseadas no **OWASP API Security Top 10** que auditam os arquivos de especificação da API durante o design!

## Como funciona
Quando a especificação OpenAPI utiliza referências externas (`$ref: "./schemas/user.yaml"`), passe a flag **`--enable-openapi-refs`** para que o KICS resolva e inspecione todos os esquemas referenciados.

## Exemplo
```bash
# Auditar contratos OpenAPI 3.0 (resolvendo $ref externos) e arquivos gRPC Protobuf contra falhas do OWASP API Top 10
kics scan -p /cases/iac/api-contracts \
  -t OpenAPI,GRPC \
  --enable-openapi-refs \
  --fail-on high,critical \
  -o /cases/iac/out
```

## Limites e trade-offs
Adicione um step `kics scan -t OpenAPI --enable-openapi-refs` em todo repositório que contém contratos Swagger/OpenAPI: isso impede que um desenvolvedor publique uma nova rota REST esquecendo de declarar a exigência de autenticação `BearerAuth`/`OAuth2` ou limites de tamanho de array (`maxItems`).

## Como verificar
Confira no relatório do KICS os achados da categoria `Access Control` e `Input Validation` sobre os seus arquivos `openapi.yaml`.

## Conexões
- [[kics-auditoria-kubernetes-helm-dockerfile-pod-security-containers]] — Veja também: KICS para **Kubernetes, Helm Charts e Dockerfiles**: Auditoria Integrada da Imagem (`Dockerfile`) até o Manifesto do Pod (`Deployment`).
- [[kics-deteccao-segredos-embutidos-passwords-keys-regex-rules]] — Veja também: KICS: Detecção Integrada de **Segredos e Credenciais Hardcoded** em IaC (`passwords_and_secrets`, `--secrets-regexes-path` e `--disable-secrets`).
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[wapiti-varredura-apis-rest-openapi-swagger-json-payloads]] — Referência cruzada direta com wapiti-varredura-apis-rest-openapi-swagger-json-payloads.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
