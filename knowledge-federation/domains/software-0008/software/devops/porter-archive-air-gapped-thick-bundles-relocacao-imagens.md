---
id: software.devops.tranche14.001348
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

# Porter: Exportação e Relocação de Thick Bundles para Ambientes Air-Gapped (porter archive)

## Em uma frase
O comando `porter archive` empacota um bundle CNAB junto com a sua imagem de invocação e **todas as imagens de containers da aplicação referenciadas** (`images:` no `porter.yaml`) em um único arquivo `.tgz` autocontido (**Thick Bundle**) pronto para transporte e relocação em ambientes desconectados (**air-gapped**).

## Por que importa
Em clientes governamentais, industriais ou financeiros sem acesso à internet, levar apenas o Helm chart falha na hora em que os nós Kubernetes tentam baixar a imagem do instalador e as 10 imagens dos microsserviços do Docker Hub/GHCR.

## Como funciona
Declarando as imagens dos microsserviços com seus digests SHA-256 na seção `images:` do `porter.yaml`, `porter archive my-app-bundle.tgz --reference <oci-ref>` gera o pacote completo; na rede isolada, `porter publish --archive my-app-bundle.tgz --reference <registro-interno/app:v1>` importa todas as imagens para o registry privado e reescreve automaticamente o mapa de relocação (`relocation-mapping.json`) injetado no bundle.

## Exemplo
```bash
porter archive cloud-app-v0.1.0.tgz --reference ghcr.io/org/cloud-app-installer:v0.1.0
porter publish --archive cloud-app-v0.1.0.tgz --reference registry.airgap.local/platform/cloud-app:v0.1.0
```

## Limites e trade-offs
Hardcodar o endereço do registry público (`ghcr.io/org/service:v1`) diretamente nos templates Helm dentro do bundle em vez de usar a variável de imagem relocada do Porter (`${bundle.images.service.repository}`) faz com que os Pods no ambiente air-gapped continuem tentando baixar do `ghcr.io`.

## Como verificar
Declare todas as imagens na seção `images:` do `porter.yaml` e passe as referências interpoladas `${bundle.images.<alias>.*}` para os passos do Helm/Kubernetes.

## Conexões
- [[porter-custom-actions-status-dry-run-operacoes-dia-2]] — Veja também: Porter: Ações Customizadas de Dia 2 (porter invoke --action) para Diagnóstico, Backup e Dry-Run.
- [[porter-custom-dockerfile-template-hardening-nonroot]] — Veja também: Porter: Customização da Imagem de Invocação com Dockerfile Template e Execução Non-Root.

## Fontes
- [Porter GitHub — README.md (CNAB Application Bundles, Porter Mixins for Helm/Terraform/Kubernetes/Cloud CLIs & Porter Plugins for Vault/Azure/K8s)](https://raw.githubusercontent.com/getporter/porter/main/README.md) — README oficial do getporter/porter (CNCF Sandbox) apresentando a especificação CNAB, a matriz oficial de Mixins (Docker, Kubernetes, Helm, GCloud, Terraform, AWS, Azure, exec) e Plugins (HashiCorp, Azure, Kubernetes); consultado em 2026-10-03.
- [Porter Official Documentation — Quickstart (porter install, list, show, upgrade & uninstall)](https://porter.sh/docs/quickstart/) — Guia oficial Quickstart do Porter demonstrando o ciclo de vida completo de instalação, listagem, inspeção de histórico Run ID, upgrade e desinstalação de bundles OCI; consultado em 2026-10-03.
- [Porter — Official GitHub Repository](https://github.com/getporter/porter) — Repositório oficial do Porter na CNCF; consultado em 2026-10-03.
