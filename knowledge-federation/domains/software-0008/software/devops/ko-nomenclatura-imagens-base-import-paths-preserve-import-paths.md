---
id: software.devops.tranche09.000868
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

# ko: estratégias de nomenclatura de imagens no registry (--base-import-paths, --preserve-import-paths e --bare)

## Em uma frase
O `ko` oferece quatro estratégias para formar o nome do repositório da imagem a partir de `KO_DOCKER_REPO` e do importpath Go: o modo padrão (com hash MD5 do caminho para evitar colisões), `--preserve-import-paths` (`-P`), `--base-import-paths` (`-B`) e `--bare`.

## Por que importa
Por padrão, conforme mostra o guia `Get Started` (`ko.build/get-started/`), `ko build ./cmd/app` publica uma imagem com um sufixo hash como `registry.example.com/my-project/app-099ba5bcefdead87f92606265fb99ac0@sha256:...`; em registries como Docker Hub ou Amazon ECR (onde cada nome de repositório precisa ser pré-criado ou seguir um nome limpo previsível), a equipe precisa controlar exatamente como a URL final da imagem é gerada.

## Como funciona
Supondo `KO_DOCKER_REPO=ghcr.io/minha-org` e o pacote `github.com/minha-org/repo/cmd/app`: (1) **Padrão (sem flags)**: gera `ghcr.io/minha-org/app-<md5-do-importpath>` (evitando colisão caso o repositório tenha dois binários chamados `app` em pastas diferentes); (2) **`--base-import-paths` (`-B`)**: usa apenas o último segmento do caminho sem o hash MD5, gerando `ghcr.io/minha-org/app`; (3) **`--preserve-import-paths` (`-P`)**: anexa o importpath completo em letras minúsculas, gerando `ghcr.io/minha-org/github.com/minha-org/repo/cmd/app`; e (4) **`--bare`**: usa literalmente apenas o valor de `KO_DOCKER_REPO` sem anexar nada do importpath, ideal para publicar em um repositório único pré-criado no Docker Hub ou AWS ECR (`123456.dkr.ecr.../meu-servico`).

## Exemplo
```bash
# Publicar a imagem usando apenas o nome base do pacote (-B) e definindo tags explícitas (-t) além do digest
export KO_DOCKER_REPO="ghcr.io/minha-org/projeto"
ko build ./cmd/app --base-import-paths --tags=v1.0.0,latest
```

## Limites e trade-offs
A flag `--bare` só deve ser usada quando você está construindo **um único binário** por comando (ou quando cada binário tem seu próprio `KO_DOCKER_REPO`), pois se você usar `ko resolve --bare -f config/` em um YAML que contém dois microsserviços Go diferentes (`ko://.../cmd/api` e `ko://.../cmd/worker`), ambos serão enviados para exatamente o mesmo repositório `KO_DOCKER_REPO` sobrescrevendo a mesma tag `:latest` (embora seus digests `@sha256:...` no YAML resolvido continuem distintos).

## Como verificar
Execute `ko build ./cmd/app --base-import-paths --push=false` e observe na referência impressa no `stdout` que o sufixo de hash MD5 foi removido do nome da imagem.

## Conexões
- [[ko-arquivos-estaticos-kodata-caminho-ko-data-path]] — Veja também: ko: empacotamento de arquivos estáticos sem Dockerfile usando o diretório kodata e KO_DATA_PATH.
- [[ko-origens-bazel-rules-docker-arquitetura-camadas-oci]] — Veja também: ko: herança arquitetural do Bazel (rules_docker / rules_k8s) e montagem direta de camadas OCI com go-containerregistry.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-autenticacao-registries-ko-docker-repo-ko-login]] — Referência cruzada direta com ko-autenticacao-registries-ko-docker-repo-ko-login.
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Referência cruzada direta com ko-integracao-kubernetes-ko-resolve-apply-delete-uri.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
