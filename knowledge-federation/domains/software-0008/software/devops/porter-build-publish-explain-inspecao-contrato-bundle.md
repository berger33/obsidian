---
id: software.devops.tranche14.001346
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

# Porter: Construção, Publicação OCI e Auto-Documentação de Bundles (build, publish e explain)

## Em uma frase
Os comandos `porter build`, `porter publish` e `porter explain` cobrem o fluxo de engenharia do pacote CNAB: compilar a imagem de invocação e o manifesto `bundle.json`, enviá-los para um registro OCI e inspecionar toda a interface do bundle antes de instalá-lo.

## Por que importa
Quando uma equipe recebe a referência de uma imagem de instalador (`ghcr.io/org/installer:v1.2.0`), rodar a imagem às cegas sem saber quais parâmetros, credenciais e ações ela aceita é arriscado.

## Como funciona
O comando `porter explain --reference <oci-ref>` lê os metadados CNAB do bundle diretamente do registro e imprime uma documentação estruturada (ou JSON/YAML) detalhando descrição, versão, todos os parâmetros (tipos, defaults, obrigatoriedade), credenciais requeridas, ações customizadas e outputs.

## Exemplo
```bash
porter build
porter publish --registry ghcr.io/org
porter explain --reference ghcr.io/org/cloud-app-installer:v0.1.0
```

## Limites e trade-offs
Fazer alterações no `porter.yaml` e executar `porter publish` sem rodar `porter build` novamente (ou sem incrementar a versão do bundle) publica metadados desatualizados ou sobrescreve tags em uso.

## Como verificar
Execute sempre `porter build` seguido de `porter explain` localmente para validar o contrato de parâmetros e credenciais antes de publicar uma nova versão com `porter publish`.

## Conexões
- [[porter-plugins-secrets-storage-hashicorp-vault-azure-kubernetes]] — Veja também: Porter: Plugins de Armazenamento e Segredos (HashiCorp Vault, Azure Key Vault e Kubernetes).
- [[porter-custom-actions-status-dry-run-operacoes-dia-2]] — Veja também: Porter: Ações Customizadas de Dia 2 (porter invoke --action) para Diagnóstico, Backup e Dry-Run.

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://porter.sh/docs/quickstart/) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
