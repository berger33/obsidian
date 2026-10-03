---
id: software.devops.tranche14.001342
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

# Porter: Ciclo de Vida de Instalações de Bundles (install, upgrade, uninstall, list e show)

## Em uma frase
O Porter gerencia o ciclo de vida completo das instalações de aplicações por meio das ações padronizadas do CNAB: **`porter install`**, **`porter upgrade`**, **`porter uninstall`**, além dos comandos de inspeção **`porter list`** e **`porter show`**.

## Por que importa
Quando um instalador executa apenas um script de criação inicial, atualizar a aplicação para a versão `2.0` ou remover todos os recursos criados em múltiplos provedores exige rastrear manualmente o que foi provisionado.

## Como funciona
Cada execução de `porter install <nome> --reference <oci-ref>` registra os metadados da instalação (nome, versão do bundle, timestamps de criação/modificação e histórico de `Run ID` com status e logs), consultáveis com `porter list` e `porter show <nome>`, permitindo posteriormente rodar `porter upgrade <nome>` e `porter uninstall <nome>` de forma determinística.

## Exemplo
```bash
porter install porter-hello --reference ghcr.io/getporter/examples/porter-hello:v0.2.0
porter list
porter show porter-hello
porter upgrade porter-hello
porter uninstall porter-hello
```

## Limites e trade-offs
Apagar o banco de estado local do Porter antes de executar `porter uninstall` faz com que o Porter perca o registro dos parâmetros e outputs da instalação necessários para desprovisionar os recursos remotos.

## Como verificar
Use sempre um Plugin de armazenamento remoto (como Kubernetes ou MongoDB/Azure) para persistir o estado das instalações compartilhadas pela equipe antes de rodar `porter install`.

## Conexões
- [[porter-arquitetura-cnab-cloud-native-application-bundle-cncf]] — Veja também: Porter: Arquitetura de Empacotamento CNAB (Cloud Native Application Bundle) na CNCF.
- [[porter-mixins-helm-terraform-kubernetes-exec-cloud-clis]] — Veja também: Porter: Ecossistema de Mixins (Helm, Terraform, Kubernetes, Docker, AWS, Azure, GCloud e exec).

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://porter.sh/docs/quickstart/) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
