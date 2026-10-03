---
id: software.devops.tranche04.000369
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

# Cadência trimestral de releases, versões LTS e assinatura PGP no Podman

## Em uma frase
O README oficial documenta a governança de releases do Podman: o projeto lança uma nova versão major ou minor **4 vezes por ano**, durante a **segunda semana de fevereiro, maio, agosto e novembro**, enquanto patch releases saem com maior frequência conforme necessário para corrigir bugs. Todas as releases são **assinadas com PGP** (chaves públicas oficiais em `github.com/containers/release-keys/tree/main/podman`), e por padrão apenas a release mais recente recebe suporte upstream, com exceções documentadas como versões **LTS (Long Term Support)** em `SUPPORT.md`.

## Por que importa
Saber que apenas a release upstream mais recente (ou uma versão LTS explícita ou suportada pela distribuição Linux corporativa) recebe correções ativas evita que equipes fiquem presas em versões intermediárias sem patches de segurança.

## Como funciona
Alinhe o calendário de atualização de ferramentas de contêiner às janelas trimestrais do Podman (fevereiro, maio, agosto e novembro) ou utilize versões LTS / pacotes mantidos por distribuições corporativas com suporte estendido, validando sempre a assinatura PGP dos artefatos baixados diretamente.

## Exemplo
Uma equipe de infraestrutura que compila pacotes internos do Podman verifica a assinatura PGP da tag de release contra as chaves públicas do repositório `containers/release-keys` antes de promover a nova versão trimestral de maio.

## Limites e trade-offs
Não assuma que uma versão minor antiga do Podman continuará recebendo backports upstream indefinidamente se ela não estiver listada como versão LTS em `SUPPORT.md`.

## Como verificar
Verifique a versão instalada com `podman --version` e valide a assinatura PGP da release oficial contra as chaves publicadas em `github.com/containers/release-keys/tree/main/podman`.

## Conexões
- [[podman-podman-machine-and-podman-desktop-multi-os]] — Veja também: Execução multiplataforma no Windows e macOS com podman machine e Podman Desktop.
- [[podman-rest-api-and-remote-client-management]] — Veja também: API REST compatível com Docker e gerenciamento remoto com cliente Podman.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
