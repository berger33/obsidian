---
id: software.seguranca.tranche09.000807
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

# KICS para **Kubernetes, Helm Charts e Dockerfiles**: Auditoria Integrada da Imagem (`Dockerfile`) até o Manifesto do Pod (`Deployment`)

## Em uma frase
Em ambientes Cloud-Native, uma falha de segurança de container frequentemente nasce da combinação entre o **`Dockerfile`** (ex.: imagem sem `USER` não-root, pacotes instalados sem pinning, segredos em `ENV`/`ARG` ou `ADD` de URL remota) e o **manifesto Kubernetes / Helm Chart** (ex.: ausência de `securityContext.runAsNonRoot`, `allowPrivilegeEscalation: true`, falta de limites de CPU/memória ou montagem de `hostPath` / `docker.sock`).

## Por que importa
O KICS analisa nativamente tanto **Dockerfiles / Docker Compose** quanto **manifestos Kubernetes, Kustomize e Helm Charts** (renderizando templates Helm diretamente sem precisar de um cluster Kubernetes ativo!) na mesma execução.

## Como funciona
Isso permite validar a conformidade com os padrões **Kubernetes Pod Security Standards (Baseline / Restricted)** e **CIS Docker / Kubernetes Benchmark** antes mesmo do build da imagem OCI.

## Exemplo
```bash
# Auditar simultaneamente Dockerfiles, manifestos Kubernetes e Helm Charts em um repositorio de microsservico
kics scan -p /cases/iac/k8s-microservice \
  -t Dockerfile,Kubernetes,Helm \
  --exclude-severities info,trace \
  --report-formats sarif,json \
  -o /cases/iac/out
```

## Limites e trade-offs
Ao auditar **Helm Charts**, aponte `-p` para o diretório raiz do Chart (onde está o `Chart.yaml` e `values.yaml`): o parser de Helm embutido no KICS renderiza os templates Go (`templates/*.yaml`) com os valores do `values.yaml` e mapeia qualquer vulnerabilidade encontrada de volta para a linha exata do template original!

## Como verificar
Verifique no relatório gerado se algum container roda como `root` (`Container Running As Root`) ou sem `readOnlyRootFilesystem: true`.

## Conexões
- [[kics-analise-terraform-variaveis-tfvars-modulos-plan-json]] — Veja também: KICS para **Terraform e OpenTofu**: Resolução de Variáveis (`--terraform-vars-path`), Módulos e Auditoria de `terraform show -json`.
- [[kics-auditoria-especificacoes-openapi-swagger-grpc-protobuf-apis]] — Veja também: KICS para **OpenAPI (v2/v3) e gRPC (`.proto`)**: *Shift-Left API Security* desde o Contrato da API (`--enable-openapi-refs`).
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Referência cruzada direta com clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
