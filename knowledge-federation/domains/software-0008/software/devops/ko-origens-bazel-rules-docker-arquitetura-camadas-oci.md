---
id: software.devops.tranche09.000869
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

# ko: herança arquitetural do Bazel (rules_docker / rules_k8s) e montagem direta de camadas OCI com go-containerregistry

## Em uma frase
Conforme documentado nos agradecimentos do README oficial, o `ko` nasceu da experiência dos autores em construir `rules_docker` e `rules_k8s` para o Bazel, trazendo a montagem direta de camadas OCI em memória (via biblioteca `google/go-containerregistry`) para projetos Go padrão sem exigir Bazel.

## Por que importa
No Bazel (`rules_docker` / `rules_oci` e `rules_k8s`), a comunidade descobriu que para linguagens compiladas não faz sentido iniciar uma máquina virtual ou container completo só para criar um arquivo `.tar` contendo um binário e dar `PUT` de blobs em um registry HTTP; o `ko` democratizou essa velocidade para qualquer projeto que use apenas `go.mod` padrão.

## Como funciona
Internamente, o `ko` utiliza a biblioteca Go **`google/go-containerregistry`**. Em vez de falar com o socket de um daemon Docker (`/var/run/docker.sock`), o `ko` atua como um cliente HTTP direto da especificação OCI Distribution: ele baixa apenas o manifesto JSON da imagem base remota (sem sequer precisar baixar os blobs das camadas da imagem base para a máquina local!), compila o binário Go localmente em um stream tar em memória com permissões fixas (`/ko-app/<binario>`), faz upload (`BLOB UPLOAD`) apenas da camada nova do binário para o registry e publica o novo manifesto JSON combinando os digests das camadas da imagem base com o digest da nova camada do binário.

## Exemplo
```bash
# Construir e publicar uma imagem em segundos (transferindo pela rede apenas a camada do binário Go compilado)
KO_DOCKER_REPO="ghcr.io/minha-org/projeto" ko build ./cmd/controller
```

## Limites e trade-offs
Como o `ko` monta a camada do binário Go em memória e faz streaming direto para o registry sem baixar nem executar a imagem base na máquina local, ele nunca executa instruções `RUN` dentro da imagem; qualquer preparação do sistema operacional base já deve vir pronta na `defaultBaseImage` escolhida.

## Como verificar
Observe o tempo de execução de `ko build` em um runner de CI limpo e note que os blobs da imagem base não precisam ser baixados localmente quando já existem no registry de destino (cross-repository blob mounting / manifest referencing).

## Conexões
- [[ko-nomenclatura-imagens-base-import-paths-preserve-import-paths]] — Veja também: ko: estratégias de nomenclatura de imagens no registry (--base-import-paths, --preserve-import-paths e --bare).
- [[ko-cicd-github-actions-assinatura-cosign-slsa-seguranca]] — Veja também: ko: pipelines leves de CI/CD, integração com Sigstore Cosign e segurança com imagens base Chainguard nonroot.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.
- [[gvisor-build-bazel-docker-testes-macos]] — Referência cruzada direta com gvisor-build-bazel-docker-testes-macos.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
