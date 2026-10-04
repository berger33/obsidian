---
id: software.devops.tranche14.001343
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

# Porter: Ecossistema de Mixins (Helm, Terraform, Kubernetes, Docker, AWS, Azure, GCloud e exec)

## Em uma frase
Os **Porter Mixins** são blocos de construção modulares que adicionam automaticamente ao container de invocação do bundle tanto os binários das ferramentas de plataforma quanto uma sintaxe YAML declarativa de alto nível no `porter.yaml` (suportando **Helm**, **Kubernetes**, **Terraform**, **Docker**, **Docker Compose**, **AWS**, **Azure**, **GCloud** e **`exec`**).

## Por que importa
Escrever um `Dockerfile` manual para instalar `helm`, `terraform`, `kubectl` e `aws-cli` com verificação de checksums e depois encadear dezenas de scripts shell para passar outputs de uma ferramenta para outra é trabalhoso e frágil.

## Como funciona
Ao declarar `mixins: [exec, helm3, terraform]` no topo do `porter.yaml`, o Porter injeta automaticamente as instruções de instalação daquelas ferramentas na imagem de invocação durante o `porter build` e valida a sintaxe dos passos declarados em `install:`, `upgrade:` e `uninstall:`.

## Exemplo
```yaml
schemaVersion: 1.0.0
name: cloud-app-installer
version: 0.1.0
registry: ghcr.io/org
mixins:
  - exec
  - terraform
  - helm3
install:
  - terraform:
      description: "Provisionar banco de dados"
  - helm3:
      description: "Implantar aplicacao no cluster"
```

## Limites e trade-offs
Usar o mixin genérico `exec` para invocar binários (`kubectl` ou `helm`) que não foram declarados na lista `mixins:` nem instalados em um `Dockerfile` customizado causa falha `command not found` durante a execução do bundle.

## Como verificar
Liste explicitamente cada ferramenta utilizada na seção `mixins:` (verificando os mixins instalados com `porter mixins list`) antes de executar `porter build`.

## Conexões
- [[porter-ciclo-vida-bundle-install-upgrade-uninstall-show-list]] — Veja também: Porter: Ciclo de Vida de Instalações de Bundles (install, upgrade, uninstall, list e show).
- [[porter-yaml-parameters-credentials-outputs-wiring-entre-steps]] — Veja também: Porter: Declaração de Parameters, Credentials e Outputs no porter.yaml.

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
