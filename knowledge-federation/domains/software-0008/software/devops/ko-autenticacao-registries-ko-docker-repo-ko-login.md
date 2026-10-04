---
id: software.devops.tranche09.000862
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/ko-build/ko/main/README.md", "https://ko.build/get-started/", "https://ko.build/features/k8s/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ko: autenticação transparente em registries (GCR/GAR, ECR, ACR, GHCR e ko login) e variável KO_DOCKER_REPO

## Em uma frase
O `ko` reutiliza automaticamente as credenciais de `~/.docker/config.json`, inclui o comando `ko login` para ambientes sem Docker e possui autenticação nativa embutida para Google Artifact Registry/GCR, Amazon ECR, Azure ACR e GitHub Container Registry (`GITHUB_TOKEN`).

## Por que importa
Em runners leves de CI/CD (onde o daemon Docker não está instalado), configurar helpers externos de credenciais apenas para autenticar no registry de containers da nuvem adiciona passos extras ao pipeline. A seção `Authenticate` e `Choose Destination` de `ko.build/get-started/` documenta o suporte nativo de autenticação do `ko`.

## Como funciona
Se você já consegue fazer `docker push`, já está autenticado para o `ko` (pois ele lê `~/.docker/config.json`). Em máquinas sem Docker, **`ko login <registry> -u <user> -p <pass>`** grava as credenciais diretamente. Além disso, mesmo sem nenhuma configuração prévia no Docker config, o `ko` autentica automaticamente nos quatro grandes registries usando credenciais do ambiente: (1) **GCR e Google Artifact Registry**: via Application Default Credentials (ADC) ou `gcloud`; (2) **Amazon ECR**: via credenciais padrão da AWS (`AWS_ACCESS_KEY_ID` / IAM Role); (3) **Azure Container Registry (ACR)**: via variáveis de ambiente do Azure; e (4) **GitHub Container Registry (`ghcr.io`)**: via variável de ambiente `GITHUB_TOKEN`. O destino do push é controlado por **`KO_DOCKER_REPO`**.

## Exemplo
```bash
# Autenticar e publicar no GitHub Container Registry (ghcr.io) em um runner sem Docker usando apenas GITHUB_TOKEN
export GITHUB_TOKEN="ghp_exemploTokenSegredoCI"
export KO_DOCKER_REPO="ghcr.io/minha-org/meu-servico"
ko build ./cmd/server
```

## Limites e trade-offs
A variável `KO_DOCKER_REPO` é obrigatória para comandos que publicam imagens; se `KO_DOCKER_REPO` não estiver definida no ambiente (nem for um destino local especial como `ko.local` ou `kind.local`), o `ko build` falhará solicitando que você especifique o repositório de destino.

## Como verificar
Verifique a autenticação executando `ko login ghcr.io -u $USER --password-stdin` (ou exportando `GITHUB_TOKEN`) e confirmando o push bem-sucedido de `ko build`.

## Conexões
- [[ko-construtor-imagens-containers-go-sem-docker]] — Veja também: ko: construtor rápido de imagens de container para aplicações Go sem necessidade de Docker.
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Veja também: ko: integração nativa com manifestos Kubernetes via referências ko://, ko resolve, ko apply e ko delete.
- [[ko-desenvolvimento-local-ko-local-kind-local-minikube]] — Referência cruzada direta com ko-desenvolvimento-local-ko-local-kind-local-minikube.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
