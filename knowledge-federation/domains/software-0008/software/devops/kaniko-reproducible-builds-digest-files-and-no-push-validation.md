---
id: software.devops.tranche06.000558
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md", "https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md", "https://github.com/GoogleContainerTools/kaniko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Builds reprodutíveis (--reproducible), captura de digests (--digest-file) e validação sem push (--no-push, --tar-path)

## Em uma frase
Na seção *Additional Flags*, o README oficial documenta flags essenciais para governança de CI/CD e segurança da cadeia de suprimentos: **`--reproducible`** (remove timestamps variáveis dos metadados e arquivos das camadas construídas para produzir uma imagem bit-a-bit reprodutível com o mesmo digest SHA-256 para os mesmos inputs), **`--digest-file`** / **`--image-name-with-digest-file`** / **`--image-name-tag-with-digest-file`** (grava o digest exato da imagem construída em um arquivo local para encadeamento com etapas seguintes do pipeline), **`--no-push`** (valida e constrói o `Dockerfile` sem enviar a nenhum registro, ideal para pull requests), **`--tar-path`** e **`--oci-layout-path`**.

## Por que importa
Em pipelines modernos de CI/CD, pull requests de branches não confiáveis precisam apenas validar se o `Dockerfile` compila (`--no-push`) ou exportar o tarball (`--tar-path`) para escaneamento de vulnerabilidades com Syft/Grype antes de publicar no registro, enquanto builds de release precisam do digest exato (`--image-name-with-digest-file`) para assinar com Cosign.

## Como funciona
Em jobs de validação de Pull Request, passe `--no-push` (ou `--no-push --tar-path=/workspace/image.tar` para escanear com Trivy/Grype); em jobs de release, passe `--reproducible` e `--image-name-with-digest-file=/workspace/image-digest.txt`.

## Exemplo
No pipeline de Tekton, o step do Kaniko constrói a imagem com `--reproducible` e grava `registry.corp/app@sha256:...` via `--image-name-with-digest-file=$(results.IMAGE_DIGEST.path)`, que é lido diretamente pelo step seguinte do Cosign e pelo atualizador GitOps.

## Limites e trade-offs
Combine também a flag **`--skip-unused-stages`** em `Dockerfiles` multi-stage grandes quando usar `--target=<stage>`, evitando que o Kaniko gaste tempo processando estágios do `Dockerfile` que não fazem parte da árvore de dependências do alvo escolhido.

## Como verificar
Execute o Kaniko com `--no-push --tar-path=/tmp/out.tar` e confirme que o arquivo tar da imagem é gerado localmente sem realizar chamadas de escrita a nenhum registro remoto.

## Conexões
- [[kaniko-registry-authentication-docker-hub-gcr-ecr-and-acr]] — Veja também: Configuração de autenticação do Kaniko para Docker Hub, Google GCR, Amazon ECR, Azure ACR e JFrog.
- [[kaniko-multi-arch-container-manifests-with-manifest-tool]] — Veja também: Construção de imagens multi-arquitetura (multi-arch) combinando Kaniko e manifest-tool.

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
