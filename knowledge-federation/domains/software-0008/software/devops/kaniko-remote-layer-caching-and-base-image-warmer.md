---
id: software.devops.tranche06.000555
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

# Cache remoto de camadas (--cache, --cache-repo) e pré-aquecimento local de imagens base (kaniko warmer)

## Em uma frase
A seção *Caching* do README oficial detalha os dois mecanismos complementares de cache do Kaniko: (1) **Caching Layers (cache remoto de camadas)** — habilitado com **`--cache=true`** e **`--cache-repo=<registro/repo/cache>`**, onde o Kaniko armazena e reutiliza camadas criadas por instruções `RUN` (`--cache-run-layers`) e `COPY` (`--cache-copy-layers`) em um repositório de registro remoto; e (2) **Caching Base Images (cache local de imagens base)** — onde um diretório local somente-leitura (`--cache-dir=/cache`) montado no pod do Kaniko é populado previamente pela imagem aquecedora oficial **`gcr.io/kaniko-project/warmer:latest`** (`--cache-dir=/workspace/cache --image=...` ou `--dockerfile=...`).

## Por que importa
Em pods efêmeros de CI no Kubernetes, cada novo build começa com disco vazio; combinar o `warmer` em um volume compartilhado (para evitar baixar gigabytes das imagens base `FROM` a cada job) com `--cache=true --cache-repo=...` (para reutilizar camadas `RUN` já compiladas no registro) acelera drasticamente os builds.

## Como funciona
Ative `--cache=true` (e `--cache-copy-layers` / `--cache-ttl`) apontando `--cache-repo` para um repositório dedicado no seu registro privado e utilize `gcr.io/kaniko-project/warmer` para pré-popular as imagens base corporativas mais usadas em um volume de cache montado nos runners.

## Exemplo
Uma equipe configura `--cache=true --cache-repo=registry.corp/ci/kaniko-cache` nos jobs de build; quando um desenvolvedor altera apenas o código-fonte final sem mudar o `go.mod`, o Kaniko baixa a camada de dependências pronta do `--cache-repo` em vez de recompilar tudo.

## Limites e trade-offs
Observe a regra de invalidação documentada no README: **uma vez que ocorre um *cache miss* em uma camada, o Kaniko não lê mais camadas subsequentes do cache** — todas as camadas seguintes daquele `Dockerfile` são construídas localmente. Ordene sempre seu `Dockerfile` das instruções que mudam menos para as que mudam mais.

## Como verificar
Execute dois builds consecutivos idênticos com `--cache=true` e confirme no segundo build os logs `Foundmanifest at ...` / extração da camada em cache sem reexecutar o comando `RUN`.

## Conexões
- [[kaniko-seven-build-context-sources-and-prefixes]] — Veja também: Os sete contextos de build suportados pelo Kaniko (dir, tar, stdin, gs, s3, https Azure e git).
- [[kaniko-running-kaniko-in-kubernetes-and-gvisor-sandbox]] — Veja também: Execução segura do Kaniko em clusters Kubernetes e dentro do sandbox gVisor (runsc --force).

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
