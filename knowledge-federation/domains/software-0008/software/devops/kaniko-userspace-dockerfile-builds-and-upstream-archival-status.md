---
id: software.devops.tranche06.000551
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

# Execução de Dockerfile em userspace no Kaniko e seu status de projeto arquivado upstream

## Em uma frase
O `kaniko` (`github.com/GoogleContainerTools/kaniko`), licenciado sob Apache-2.0, é uma ferramenta criada para construir imagens de contêiner a partir de um `Dockerfile` dentro de um contêiner ou cluster Kubernetes **sem depender de um daemon Docker**, executando cada comando do `Dockerfile` inteiramente em **userspace**. Ao mesmo tempo, o topo do README oficial registra um aviso fundamental de governança atual: **`This project is archived and no longer developed or maintained. The code remains available for historic purposes`** (além da nota de que não é um produto oficialmente suportado pelo Google).

## Por que importa
Milhares de pipelines legados em Kubernetes (GitLab CI, Jenkins, Tekton e Argo Workflows) ainda utilizam a imagem `gcr.io/kaniko-project/executor`; por isso, engenheiros DevOps precisam tanto dominar a arquitetura e flags do Kaniko para manter e operar esses pipelines quanto planejar a estratégia de ciclo de vida diante do arquivamento upstream do repositório `GoogleContainerTools/kaniko`.

## Como funciona
Ao manter pipelines que utilizam o Kaniko, siga rigorosamente as práticas documentadas no README oficial e planeje no roadmap de engenharia de plataforma a avaliação gradual de construtores ativamente mantidos (como **BuildKit rootless** ou **Buildah**) para novas cargas.

## Exemplo
Uma equipe de plataforma audita seus pipelines de CI no Kubernetes, documenta o funcionamento atual dos jobs baseados em `gcr.io/kaniko-project/executor` e inicia a homologação de runners BuildKit rootless/Buildah em razão do arquivamento oficial de `GoogleContainerTools/kaniko`.

## Limites e trade-offs
Não confie na etiqueta `:latest` de um projeto arquivado esperando novas correções de CVEs upstream; monitore vulnerabilidades na imagem do executor e avalie a migração planejada para ferramentas ativamente mantidas.

## Como verificar
Inspecione os manifestos de CI/CD da organização para inventariar onde `gcr.io/kaniko-project/executor` é utilizado e validar suas flags de segurança e cache.

## Conexões
- [[kaniko-how-kaniko-works-base-image-extraction-and-userspace-snapshotting]] — Veja também: Como o Kaniko funciona: extração da imagem base e snapshotting do sistema de arquivos em userspace.

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
