---
id: software.devops.tranche09.000861
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

# ko: construtor rápido de imagens de container para aplicações Go sem necessidade de Docker

## Em uma frase
O `ko` (`ko-build/ko`, projeto CNCF Sandbox) é um construtor simples e rápido de imagens de container para aplicações Go que executa `go build` localmente e monta a imagem OCI diretamente no registry sem exigir `docker` nem `Dockerfile`.

## Por que importa
A imensa maioria dos microsserviços e operadores Kubernetes escritos em Go compila para um único binário estático sem dependências de sistema operacional (`CGO_ENABLED=0`); manter um `Dockerfile` multi-stage e iniciar um daemon Docker pesado em runners de CI apenas para colocar um binário Go dentro de uma imagem `distroless` é lento e desnecessário. O README oficial do `ko` e o guia `Get Started` (`ko.build/get-started/`) explicam como o `ko` elimina essa camada.

## Como funciona
Quando o desenvolvedor define a variável de ambiente **`KO_DOCKER_REPO`** (por exemplo, `KO_DOCKER_REPO=ghcr.io/minha-org/meu-repo`) e executa **`ko build ./cmd/app`** (onde `./cmd/app` é um pacote `main` com `func main()`), o `ko` invoca `go build` na máquina local, pega uma imagem base mínima (por padrão `cgr.dev/chainguard/static:latest`), adiciona uma nova camada OCI contendo o binário compilado em **`/ko-app/app`** (definindo-o como `ENTRYPOINT` da imagem), faz o push diretamente via API HTTP do registry OCI e imprime o digest completo (`registry.../app@sha256:...`) no `stdout`.

## Exemplo
```bash
# Definir o repositório de destino e construir/publicar uma imagem OCI de um pacote Go sem usar Docker
export KO_DOCKER_REPO="ghcr.io/minha-org/meu-projeto"
ko build ./cmd/app
```

## Limites e trade-offs
Conforme destaca o README oficial do `ko`, a ferramenta é ideal para casos onde a imagem contém uma única aplicação Go sem dependências de pacotes do sistema operacional base (sem `cgo` complexo ou binários externos); se a sua aplicação Go invocar utilitários CLI externos via `os/exec` (como `git`, `ffmpeg` ou `bash`), você precisará configurar uma imagem base que já contenha esses utilitários no `.ko.yaml`.

## Como verificar
Execute `ko version` e teste uma construção local sem push para registry remoto usando `ko build ./cmd/app --push=false --tarball=/tmp/image.tar` verificando o tarball OCI gerado.

## Conexões
- [[ko-autenticacao-registries-ko-docker-repo-ko-login]] — Veja também: ko: autenticação transparente em registries (GCR/GAR, ECR, ACR, GHCR e ko login) e variável KO_DOCKER_REPO.
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Referência cruzada direta com ko-integracao-kubernetes-ko-resolve-apply-delete-uri.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
