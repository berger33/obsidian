---
id: software.devops.tranche06.000532
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
fontes: ["https://raw.githubusercontent.com/containers/buildah/main/README.md", "https://github.com/containers/buildah/tree/main/docs/containertools", "https://github.com/containers/buildah"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Construção programática de imagens sem Dockerfile com buildah from, run, config e commit

## Em uma frase
Um diferencial central destacado no README oficial do Buildah é que seus subcomandos replicam todas as instruções encontradas em um `Dockerfile`, permitindo **construir imagens tanto a partir de `Containerfiles`/`Dockerfiles` (`buildah build`) quanto de forma puramente imperativa e programática sem nenhum `Dockerfile`**, tendo como objetivo fornecer uma interface de baixo nível estilo *coreutils* integrável a qualquer linguagem de script (Bash, Python, Makefiles). O exemplo oficial `examples/lighttpd.sh` demonstra esse fluxo em quatro etapas: criar um contêiner de trabalho com **`ctr1=$(buildah from "${1:-fedora}")`**, executar comandos nele com **`buildah run "$ctr1" -- dnf install -y lighttpd`**, ajustar metadados da imagem com **`buildah config --annotation ... --cmd ... --port 80 "$ctr1"`** e gravar a imagem final com **`buildah commit "$ctr1" "$USER/lighttpd"`**.

## Por que importa
Em um `Dockerfile` tradicional, você fica preso a uma DSL limitada sem loops, condicionais complexas ou integração direta com variáveis e funções do shell. Com `buildah from` + `buildah run` + `buildah copy` + `buildah config` + `buildah commit` dentro de um script Bash, toda a expressividade do shell Linux fica disponível durante o build.

## Como funciona
Adote scripts baseados em `buildah from`, `buildah copy`/`add`, `buildah run`, `buildah config` e `buildah commit` quando precisar de lógica condicional avançada de construção de camadas ou mantenha `buildah build` para `Containerfiles` declarativos padrão.

## Exemplo
Seguindo o exemplo oficial `lighttpd.sh` do README, um script de build cria `ctr1=$(buildah from fedora)`, instala pacotes com `buildah run "$ctr1" -- ...`, injeta o hostname de build na anotação com `buildah config --annotation "com.example.build.host=$(uname -n)" "$ctr1"`, define `--cmd` e `--port 80` e consolida a imagem com `buildah commit`.

## Limites e trade-offs
Lembre-se sempre de remover o contêiner de trabalho temporário ao final do script com **`buildah rm "$ctr1"`** (ou passando `--rm` no `buildah commit`) para não acumular contêineres de trabalho órfãos no armazenamento local.

## Como verificar
Execute a sequência `buildah from`, `buildah config`, `buildah commit` e `buildah rm` em uma imagem de teste (como `alpine` ou `scratch`) e verifique a imagem criada em `buildah images`.

## Conexões
- [[buildah-daemonless-fork-exec-oci-image-builder]] — Veja também: Buildah como construtor de imagens OCI e Docker sem daemon no modelo fork-exec.
- [[buildah-from-scratch-minimal-images-and-host-package-managers]] — Veja também: Criação de imagens mínimas do zero (buildah from scratch) e montagem direta do rootfs com buildah mount.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
