---
id: software.devops.tranche06.000536
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

# Adição de arquivos, diretórios e URLs ao contêiner de trabalho com buildah copy e buildah add

## Em uma frase
Na tabela de comandos do README oficial, os subcomandos **`buildah-copy(1)`** (`buildah copy`) e **`buildah-add(1)`** (`buildah add`) espelham e expandem as instruções `COPY` e `ADD` de um `Dockerfile`: `buildah copy` copia o conteúdo de um arquivo, URL ou diretório para dentro do diretório de trabalho do contêiner, enquanto `buildah add` adiciona o conteúdo de um arquivo, URL ou diretório (extraindo automaticamente arquivos tar locais comprimidos quando aplicável). Ambos podem ser chamados repetidamente sobre um working container criado com `buildah from`.

## Por que importa
Em builds multi-etapas ou scripts de montagem de imagem, copiar apenas os artefatos finais compilados para um novo working container limpo (criado a partir de uma imagem base mínima ou `scratch`) sem carregar os compiladores e caches intermediários reduz drasticamente o tamanho da imagem final.

## Como funciona
Em scripts Buildah, use um primeiro working container `builder` para compilar o código e, em seguida, copie os artefatos resultantes para um segundo working container de runtime limpo antes de rodar `buildah commit`.

## Exemplo
Após compilar a aplicação estática, o script usa `buildah copy --chown 1000:1000 "$runtime_ctr" ./bin/server /usr/local/bin/server` para injetar o binário já com as permissões corretas do usuário não-root antes do commit.

## Limites e trade-offs
Prefira `buildah copy` para cópias diretas e previsíveis de arquivos e diretórios, reservando `buildah add` especificamente para quando desejar o comportamento de extração automática de arquivos tar locais.

## Como verificar
Crie um working container de teste, copie um arquivo com `buildah copy`, verifique sua presença com `buildah run "$ctr" -- ls -l` e remova o contêiner com `buildah rm`.

## Conexões
- [[buildah-buildah-versus-podman-specialization-and-working-containers]] — Veja também: Diferença arquitetural entre Buildah e Podman e o conceito de Working Containers.
- [[buildah-image-metadata-configuration-with-buildah-config]] — Veja também: Configuração de metadados OCI (entrypoint, cmd, env, port, user, labels e annotations) com buildah config.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
