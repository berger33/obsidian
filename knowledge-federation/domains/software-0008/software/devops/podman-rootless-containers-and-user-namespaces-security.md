---
id: software.devops.tranche04.000362
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

# Contêineres e pods rootless no Podman com user namespaces e isolamento de privilégios

## Em uma frase
O README oficial destaca que o Podman pode ser executado facilmente como um usuário normal sem exigir nenhum binário `setuid`. Quando executado sem root (**Rootless Podman**), os contêineres usam **user namespaces** do kernel Linux para mapear o usuário `root` dentro do contêiner para o UID desprivilegiado do usuário que iniciou o Podman no host. Mesmo que o usuário passe `--privileged` ao contêiner rootless, o contêiner **nunca terá mais privilégios no sistema host do que o próprio usuário normal que o lançou** — por exemplo, se o usuário montar `/etc/passwd` do host dentro do contêiner, ainda assim será incapaz de alterá-lo porque sua conta de usuário não possui permissão de escrita nesse arquivo no host.

## Por que importa
Caso ocorra uma vulnerabilidade de escape de contêiner em produção ou em uma máquina de desenvolvimento, um contêiner iniciado em modo rootless fica estritamente confinado às permissões do usuário comum no sistema operacional, impedindo comprometimento root do host.

## Como funciona
Configure `subuid` e `subgid` para as contas de usuários e contas de serviço conforme o tutorial oficial (`rootless_tutorial.md`) e execute todas as cargas compatíveis com Podman em modo rootless por padrão.

## Exemplo
Um desenvolvedor executa um contêiner de banco de dados local e um servidor de aplicação com `podman run` usando sua conta de usuário padrão; no host Linux, os processos do banco rodam mapeados sob a faixa de UIDs subordinados do usuário, sem qualquer privilégio administrativo no sistema.

## Limites e trade-offs
Consulte o documento oficial `rootless.md` para conhecer as limitações inerentes a contêineres sem root (como impossibilidade de fazer bind direto em portas privilegiadas abaixo de 1024 sem ajuste de `sysctl` ou montar sistemas de arquivos de kernel restritos).

## Como verificar
Execute `podman unshare cat /proc/self/uid_map` como usuário não-root e confirme o mapeamento do UID `0` do contêiner para o UID do usuário atual no host.

## Conexões
- [[podman-daemonless-architecture-and-libpod-lifecycle]] — Veja também: Arquitetura daemonless do Podman baseada na biblioteca libpod e compatibilidade com Docker CLI.
- [[podman-pods-shared-resources-and-kubernetes-yaml]] — Veja também: Gerenciamento nativo de Pods no Podman e integração com manifestos YAML do Kubernetes.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
