---
id: software.devops.tranche09.000870
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

# ko: pipelines leves de CI/CD, integração com Sigstore Cosign e segurança com imagens base Chainguard nonroot

## Em uma frase
Por não exigir daemon Docker nem privilégios de `root` no runner, o `ko` encaixa-se em pipelines leves de CI/CD (GitHub Actions `ko-build/setup-ko`, GitLab CI, Tekton) e encadeia sua saída diretamente com o **Sigstore Cosign** (`cosign sign $(ko build ...)`) sobre imagens base mínimas sem shell.

## Por que importa
Em pipelines de CI/CD modernos no Kubernetes (como Tekton ou GitHub Actions Runners em pods sem privilégios), rodar Docker-in-Docker (`dind`) introduz riscos severos de segurança; além disso, como `ko build` imprime exclusivamente a referência imutável `imagem@sha256:...` no `stdout`, ele foi desenhado para composição UNIX com ferramentas de assinatura criptográfica como o `cosign`.

## Como funciona
Como a imagem base padrão do `ko` (`cgr.dev/chainguard/static:latest`) é uma imagem *distroless* mínima que **não contém shell (`/bin/sh`), não contém gerenciador de pacotes e roda como usuário não-privilegiado (`nonroot`, UID 65532)**, a superfície de ataque da imagem gerada é reduzida ao próprio binário Go em `/ko-app/<nome>`. Em um pipeline de CI, o comando `DIGEST=$(ko build ./cmd/app)` captura a URI exata com `@sha256:...` da imagem publicada (e seu SBOM anexado automaticamente), permitindo assinar imediatamente a imagem e o SBOM sem chave estática (keyless OIDC) via `cosign sign --yes "${DIGEST}"`.

## Exemplo
```bash
# Construir e publicar a imagem com ko capturando o digest imutável no stdout para assinatura ou deploy imediato
IMAGE_URI=$(KO_DOCKER_REPO=ghcr.io/minha-org/app ko build ./cmd/app --base-import-paths)
echo "Imagem publicada com digest imutável: ${IMAGE_URI}"
```

## Limites e trade-offs
Como a imagem base padrão do `ko` não possui shell (`/bin/sh` ou `/bin/bash`) nem utilitários como `ls` ou `curl`, se um operador tentar executar `kubectl exec -it <pod> -- /bin/sh` em produção receberá erro de executável não encontrado; para depurar um pod construído com `ko` em Kubernetes, utilize containers efêmeros de debug (`kubectl debug -it <pod> --image=busybox --target=<container>`).

## Como verificar
Inspecione o usuário e o entrypoint da imagem gerada com `docker inspect <imagem> --format '{{.Config.User}} {{.Config.Entrypoint}}'` confirmando o execução não-root e o caminho `/ko-app/<binario>`.

## Conexões
- [[ko-origens-bazel-rules-docker-arquitetura-camadas-oci]] — Veja também: ko: herança arquitetural do Bazel (rules_docker / rules_k8s) e montagem direta de camadas OCI com go-containerregistry.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
