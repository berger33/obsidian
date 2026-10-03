---
id: software.devops.tranche14.001345
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

# Porter: Plugins de Armazenamento e Segredos (HashiCorp Vault, Azure Key Vault e Kubernetes)

## Em uma frase
Os **Porter Plugins** estendem o runtime do Porter para persistir os dados de instalação do Porter e buscar segredos dinamicamente em serviços externos, com plugins oficiais disponíveis para **HashiCorp Vault**, **Azure (Key Vault / Blob / CosmosDB)** e **Kubernetes**.

## Por que importa
Por padrão, quando um engenheiro executa o Porter em seu laptop sem configurar plugins externos, os metadados da instalação ficam restritos à máquina local e os segredos precisam estar presentes no ambiente do cliente.

## Como funciona
Configurando no arquivo `~/.porter/config.toml` (ou `.yaml`) um plugin de segredos (como `hashicorp.vault`, `azure.keyvault` ou `kubernetes.secrets`), os conjuntos de credenciais (`Credential Sets`) e parâmetros (`Parameter Sets`) referenciam apenas o nome da chave no cofre remoto, que o Porter resolve em memória no momento da execução.

## Exemplo
```bash
porter plugins list
porter credentials generate my-app-creds --reference ghcr.io/org/cloud-app:v1.0.0
porter credentials list
```

## Limites e trade-offs
Armazenar valores literais de produção diretamente dentro dos arquivos JSON/YAML de `Credential Sets` versionados no Git expõe credenciais críticas.

## Como verificar
Nos arquivos de `Credential Set`, utilize sempre a fonte `secret` apontando para o plugin configurado (HashiCorp Vault, Azure Key Vault ou Kubernetes Secrets).

## Conexões
- [[porter-yaml-parameters-credentials-outputs-wiring-entre-steps]] — Veja também: Porter: Declaração de Parameters, Credentials e Outputs no porter.yaml.
- [[porter-build-publish-explain-inspecao-contrato-bundle]] — Veja também: Porter: Construção, Publicação OCI e Auto-Documentação de Bundles (build, publish e explain).

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
