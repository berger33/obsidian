---
id: software.devops.tranche06.000559
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

# Construção de imagens multi-arquitetura (multi-arch) combinando Kaniko e manifest-tool

## Em uma frase
A seção *Creating Multi-arch Container Manifests Using Kaniko and Manifest-tool* do README oficial explica o fluxo de trabalho recomendado e suas limitações ao construir imagens multi-arquitetura (`linux/amd64`, `linux/arm64`, etc.) com o Kaniko: como cada instância do Kaniko executa os binários da instrução `RUN` na arquitetura do nó/contêiner em que está rodando, o fluxo geral consiste em (1) **construir as imagens de cada arquitetura separadamente** em paralelo nos respectivos runners (por exemplo, publicando tags sufixadas pela arquitetura como `image:v1-amd64` e `image:v1-arm64`, usando `--custom-platform` quando aplicável); e (2) **mesclar os manifestos das arquiteturas** em um único *manifest list* OCI/Docker (ex.: `image:v1`) usando o **`manifest-tool`** em uma etapa subsequente do pipeline.

## Por que importa
Diferente de um builder que oculta o manifesto multi-arch em um único passo, no Kaniko é fundamental evitar que dois jobs paralelos (`amd64` e `arm64`) façam push para exatamente a mesma tag `--destination` sem sufixo de arquitetura, pois o segundo job sobrescreveria o manifesto do primeiro.

## Como funciona
Configure uma matriz de jobs no seu pipeline de CI (um job em nó `amd64` publicando `:<tag>-amd64` e outro em nó `arm64` publicando `:<tag>-arm64`) e adicione um job final dependente que executa `manifest-tool push from-args` (ou `skopeo` / `crane`) para publicar a manifest list unificada `:<tag>`.

## Exemplo
Em um pipeline GitLab CI multi-arch seguindo o exemplo oficial do README, dois jobs paralelos do Kaniko geram as variantes `amd64` e `arm64` e o estágio de merge consolida ambas sob a tag de versão semântica da release.

## Limites e trade-offs
Ao usar `--cache=true` em builds multi-arch do Kaniko, separe o `--cache-repo` por arquitetura (ou garanta isolamento por plataforma) para evitar conflitos de cache entre arquiteturas distintas.

## Como verificar
Inspecione a tag final mesclada com `skopeo inspect --raw docker://<imagem>:<tag>` e confirme que o manifesto retornado é uma lista (`manifest.list.v2` / `image.index.v1`) contendo os descritores de ambas as arquiteturas.

## Conexões
- [[kaniko-reproducible-builds-digest-files-and-no-push-validation]] — Veja também: Builds reprodutíveis (--reproducible), captura de digests (--digest-file) e validação sem push (--no-push, --tar-path).
- [[kaniko-custom-ca-certificates-and-registry-mirrors-configuration]] — Veja também: Configuração de certificados CA privados (/kaniko/ssl/certs/), mTLS de registro e registry mirrors no Kaniko.

## Fontes
- [Kaniko GitHub — README.md (Archival Notice, Userspace Dockerfile Execution, Build Contexts, Caching & Known Issues)](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md) — README oficial do Kaniko (GoogleContainerTools/kaniko) registrando o aviso no topo de que o projeto está arquivado e não é mais mantido, seu funcionamento por extração do rootfs e snapshotting em userspace sem daemon Docker dentro de gcr.io/kaniko-project/executor, os 7 contextos de build suportados, cache de camadas (--cache, --cache-repo) e cache de imagens base (gcr.io/kaniko-project/warmer), execução em Kubernetes/gVisor e limitações conhecidas.; consultado em 2026-10-03.
- [Kaniko GitHub — Getting Started Tutorial (docs/tutorial.md)](https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md) — Tutorial histórico oficial de uso do Kaniko em clusters Kubernetes.; consultado em 2026-10-03.
- [Kaniko — Official GitHub Repository (Archived)](https://github.com/GoogleContainerTools/kaniko) — Repositório oficial Apache-2.0 arquivado do Kaniko em GoogleContainerTools.; consultado em 2026-10-03.
