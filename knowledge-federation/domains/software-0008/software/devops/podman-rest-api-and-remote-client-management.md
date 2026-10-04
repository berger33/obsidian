---
id: software.devops.tranche04.000370
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/containers/podman/main/README.md", "https://docs.podman.io/en/latest/", "https://github.com/containers/podman"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# API REST compatível com Docker e gerenciamento remoto com cliente Podman

## Em uma frase
O Podman fornece uma **API REST** dupla que expõe tanto uma interface compatível com o daemon do Docker (permitindo que ferramentas existentes como Docker Compose, Testcontainers e plugins de IDE funcionem sem modificação) quanto uma interface aprimorada (endpoint `/libpod/...`) que expõe funcionalidades exclusivas do Podman, como gerenciamento de pods e geração de YAML Kubernetes. Além disso, o **cliente remoto do Podman** (`remote_client.md`) permite gerenciar contêineres e pods em servidores Linux remotos de forma segura via conexões SSH sem expor portas TCP abertas sem criptografia.

## Por que importa
Diferentemente de expor um socket TCP Docker na rede, o cliente remoto do Podman usa autenticação SSH padrão do sistema operacional combinada a systemd socket activation no servidor remoto, iniciando o serviço da API apenas enquanto há requisições ativas.

## Como funciona
Para ferramentas locais que exigem socket Docker, habilite `systemctl --user enable --now podman.socket`; para administrar hosts remotos, configure conexões SSH com `podman system connection add` e use `podman --remote`.

## Exemplo
Um engenheiro de plataforma adiciona o servidor de staging com `podman system connection add staging ssh://user@staging.interno/run/user/1000/podman/podman.sock` e inspeciona os pods remotos diretamente de sua estação com `podman --remote pod ps`.

## Limites e trade-offs
Nunca exponha o socket da API REST do Podman diretamente em uma interface TCP de rede sem autenticação; utilize sempre túneis SSH (`podman --remote`) ou sockets Unix locais protegidos por permissões de arquivo do usuário.

## Como verificar
Ative o socket de usuário do Podman e consulte a versão da API local ou via `podman --remote info` confirmando a resposta limpa do serviço sob demanda.

## Conexões
- [[podman-release-cadence-lts-and-pgp-signed-releases]] — Veja também: Cadência trimestral de releases, versões LTS e assinatura PGP no Podman.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
