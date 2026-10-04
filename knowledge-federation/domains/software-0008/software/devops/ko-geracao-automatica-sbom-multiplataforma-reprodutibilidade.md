---
id: software.devops.tranche09.000864
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

# ko: builds multiplataforma (--platform=all), geração de SBOM por padrão e reprodutibilidade

## Em uma frase
O `ko` produz **Software Bills of Materials (SBOMs)** por padrão a partir dos metadados do módulo Go (`go.mod`) anexando-os ao registry OCI, constrói imagens multi-arquitetura (`linux/amd64`, `linux/arm64`, etc.) via cross-compilation nativa do Go com `--platform=all` e gera camadas reprodutíveis.

## Por que importa
Construir imagens multi-arquitetura com `docker buildx` frequentemente recorre à emulação lenta via QEMU, e gerar SBOMs precisos exige ferramentas adicionais no pipeline. Como destacado no README oficial do `ko`, a ferramenta resolve builds multiplataforma, geração de SBOM por padrão e determinismo nativamente porque compreende a estrutura de compilação do Go.

## Como funciona
(1) **Multi-platform builds**: como o compilador Go faz cross-compilation nativa instantaneamente apenas variando `GOOS` e `GOARCH` sem precisar de emulador QEMU, passar **`ko build ./cmd/app --platform=linux/amd64,linux/arm64`** (ou `--platform=all` para todas as plataformas suportadas pela imagem base) compila os binários em paralelo e publica um OCI Image Index / Docker Manifest List multi-arch; (2) **SBOMs por padrão**: o `ko` lê as informações de dependências compiladas pelo toolchain Go, gera um SBOM (formato SPDX por padrão, ou CycloneDX, desativável com `--sbom=none`) e faz upload do artefato `.sbom` no registry ao lado da imagem (inspecionável com `cosign download sbom`); e (3) **Reprodutibilidade**: zera timestamps na camada tar do binário Go para produzir digests determinísticos.

## Exemplo
```bash
# Construir e publicar uma imagem multi-arquitetura (amd64 e arm64) com geração automática de SBOM SPDX
ko build ./cmd/app --platform=linux/amd64,linux/arm64 --sbom=spdx
```

## Limites e trade-offs
O suporte a cross-compilation instantânea com `--platform=all` funciona perfeitamente porque o `ko` compila com `CGO_ENABLED=0` por padrão; se você habilitar `CGO_ENABLED=1` nas configurações de build do `.ko.yaml`, a compilação cruzada para outra arquitetura exigirá toolchains C de cross-compilation (`gcc-aarch64-linux-gnu`) instalados na máquina host.

## Como verificar
Construa uma imagem com `ko build ./cmd/app --sbom-dir=/tmp/ko-sbom` e inspecione o arquivo SPDX gerado em `/tmp/ko-sbom` contendo a lista completa de módulos Go compilados no binário.

## Conexões
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Veja também: ko: integração nativa com manifestos Kubernetes via referências ko://, ko resolve, ko apply e ko delete.
- [[ko-configuracao-ko-yaml-imagens-base-flags-ldflags]] — Veja também: ko: customização de imagem base (defaultBaseImage), flags de compilação e ldflags com .ko.yaml.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[buildpacks-metadados-sbom-labels-oci-deprecacao-stacks]] — Referência cruzada direta com buildpacks-metadados-sbom-labels-oci-deprecacao-stacks.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
