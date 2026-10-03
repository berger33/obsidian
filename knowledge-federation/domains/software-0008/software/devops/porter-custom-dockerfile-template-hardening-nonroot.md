---
id: software.devops.tranche14.001349
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/getporter/porter/main/README.md", "https://porter.sh/docs/quickstart/", "https://github.com/getporter/porter"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Porter: Customização da Imagem de Invocação com Dockerfile Template e Execução Non-Root

## Em uma frase
Quando os Mixins padrão do Porter não cobrem um pacote de sistema operacional específico, certificado CA corporativo ou biblioteca nativa, o Porter permite usar um **`Dockerfile.tmpl`** customizado (`dockerfile: Dockerfile.tmpl` no `porter.yaml`) preservando o comentário especial `# PORTER_MIXINS`.

## Por que importa
Construir uma imagem totalmente manual sem a diretiva `# PORTER_MIXINS` perde a injeção automática dos binários dos mixins e a configuração do usuário não-privilegiado (`nonroot`, UID `65532`) gerenciada pelo Porter.

## Como funciona
Executando `porter create`, o Porter gera um `Dockerfile.tmpl` pronto onde o comentário `# PORTER_MIXINS` indica exatamente o ponto em que o compilador do Porter inserirá as camadas dos mixins declarados e configurará o ambiente de execução seguro.

## Exemplo
```dockerfile
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates jq && rm -rf /var/lib/apt/lists/*
# PORTER_MIXINS
COPY . ${BUNDLE_DIR}
```

## Limites e trade-offs
Remover a linha `# PORTER_MIXINS` ou `COPY . ${BUNDLE_DIR}` do `Dockerfile.tmpl` impede que os binários dos mixins (`helm3`, `terraform`, `kubectl`) e os arquivos do diretório do bundle sejam copiados para a imagem de invocação.

## Como verificar
Mantenha sempre o marcador `# PORTER_MIXINS` e a cópia para `${BUNDLE_DIR}` intactos ao customizar o `Dockerfile.tmpl`.

## Conexões
- [[porter-archive-air-gapped-thick-bundles-relocacao-imagens]] — Veja também: Porter: Exportação e Relocação de Thick Bundles para Ambientes Air-Gapped (porter archive).
- [[porter-operator-kubernetes-execucao-bundles-in-cluster-gitops]] — Veja também: Porter: Execução In-Cluster e Automação CI/CD de Bundles com o Plugin Kubernetes.

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
