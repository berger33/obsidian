---
id: software.devops.tranche14.001350
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
fontes: ["https://porter.sh/docs/quickstart/", "https://raw.githubusercontent.com/getporter/porter/main/README.md", "https://github.com/getporter/porter"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Porter: Execução In-Cluster e Automação CI/CD de Bundles com o Plugin Kubernetes

## Em uma frase
Combinando o Porter em pipelines de CI/CD ou dentro de um cluster Kubernetes (usando o **Porter Operator** ou Jobs Kubernetes integrados ao plugin `kubernetes`), equipes de plataforma executam instalações de bundles CNAB sem depender de máquinas de desenvolvedores.

## Por que importa
Executar `porter install` ou `porter upgrade` de produção a partir do laptop de um engenheiro depende da conectividade local da estação e dificulta a auditoria centralizada dos logs de execução.

## Como funciona
Em um runner de CI ou Job Kubernetes, configura-se o Porter para utilizar o plugin do Kubernetes (armazenando o estado e lendo `Credential Sets` a partir de `Secrets` do namespace) e executa-se `porter install` / `porter upgrade` de forma totalmente automatizada e auditável via `porter logs`.

## Exemplo
```bash
porter installations list
porter logs --installation porter-hello
```

## Limites e trade-offs
Executar dois jobs concorrentes de `porter upgrade` sobre a mesma instalação simultaneamente causa condição de corrida nos recursos subjacentes (como o lock do estado do Terraform ou release do Helm).

## Como verificar
Serialize as execuções de `porter upgrade` por instalação no pipeline de CI/CD e consulte sempre `porter show` e `porter logs` para auditar o resultado de cada `Run ID`.

## Conexões
- [[porter-custom-dockerfile-template-hardening-nonroot]] — Veja também: Porter: Customização da Imagem de Invocação com Dockerfile Template e Execução Non-Root.

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://porter.sh/docs/quickstart/) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
