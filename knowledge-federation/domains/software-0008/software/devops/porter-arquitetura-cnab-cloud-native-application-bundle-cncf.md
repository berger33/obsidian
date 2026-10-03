---
id: software.devops.tranche14.001341
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

# Porter: Arquitetura de Empacotamento CNAB (Cloud Native Application Bundle) na CNCF

## Em uma frase
O **Porter** (`getporter/porter`, projeto **CNCF Sandbox**) é um instalador e ferramenta de autoria declarativa baseada na especificação **CNAB (Cloud Native Application Bundle)** que empacota uma aplicação, suas ferramentas de cliente (`helm`, `kubectl`, `terraform`, `aws`, `az`), configurações e lógica de implantação em um único **bundle** distribuível via registros OCI.

## Por que importa
Para instalar uma aplicação complexa que combina um banco RDS via Terraform, um segredo no Key Vault e três Helm charts no Kubernetes, o operador normalmente precisa instalar versões exatas de quatro CLIs na máquina e rodar scripts manuais na ordem certa.

## Como funciona
Com o Porter, o autor declara tudo em um arquivo `porter.yaml`; o comando `porter build` constrói uma imagem de invocação autocontida com os binários necessários e `porter publish` envia o bundle para um registro OCI padrão (como `ghcr.io`), permitindo que qualquer pessoa o instale com um único comando `porter install`.

## Exemplo
```bash
porter version
porter explain --reference ghcr.io/getporter/examples/porter-hello:v0.2.0
```

## Limites e trade-offs
Executar scripts bash soltos na máquina do cliente para provisionar infraestrutura em vez de encapsulá-los em um bundle CNAB falha sempre que a máquina do operador possui uma versão incompatível do `terraform`, `helm` ou `kubectl`.

## Como verificar
Empacote as versões exatas das ferramentas de implantação dentro do bundle via Mixins do Porter e publique-o em um registro OCI versionado.

## Conexões
- [[porter-ciclo-vida-bundle-install-upgrade-uninstall-show-list]] — Veja também: Porter: Ciclo de Vida de Instalações de Bundles (install, upgrade, uninstall, list e show).

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
