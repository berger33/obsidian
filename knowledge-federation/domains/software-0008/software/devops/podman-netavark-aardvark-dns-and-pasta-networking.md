---
id: software.devops.tranche04.000364
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

# Pilha de rede do Podman: Netavark, servidor DNS Aardvark e rede rootless com pasta

## Em uma frase
A seção de arquitetura OCI do README oficial documenta a pilha moderna de rede do Podman: o gerenciamento completo de redes de contêineres é realizado pelo **Netavark** (`github.com/containers/netavark`) em conjunto com o servidor DNS autoritativo para registros de contêineres **Aardvark** (`github.com/containers/aardvark-dns`), enquanto o suporte de rede para contêineres em modo **rootless** é processado pelo **`pasta`** (`passt.top/passt`), que cria uma interface de rede em espaço de usuário sem exigir privilégios de root no host.

## Por que importa
A transição da antiga pilha CNI/`slirp4netns` para a combinação **Netavark + Aardvark + pasta** trouxe melhor desempenho de throughput, suporte nativo a IPv6, resolução DNS rápida entre contêineres na mesma rede e menor sobrecarga de memória e CPU em contêineres rootless.

## Como funciona
Ao criar redes customizadas com `podman network create`, aproveite a resolução automática de nomes DNS fornecida pelo `aardvark-dns` entre os contêineres conectados àquela rede e utilize o driver `pasta` padrão nas execuções rootless.

## Exemplo
Dois contêineres (`api` e `redis`) conectados a uma rede criada com `podman network create app-net` resolvem os nomes de host um do outro automaticamente via `aardvark-dns`, enquanto em modo rootless o tráfego de saída flui pelo `pasta` sem permissões elevadas.

## Limites e trade-offs
Evite depender da rede bridge padrão quando precisar de resolução automática de nomes DNS entre contêineres; crie sempre uma rede dedicada com `podman network create` onde o `aardvark-dns` é habilitado.

## Como verificar
Execute `podman info` e confirme na seção de rede que `networkBackend` está configurado como `netavark` com `dns` via `aardvark-dns` e rede rootless via `pasta`.

## Conexões
- [[podman-pods-shared-resources-and-kubernetes-yaml]] — Veja também: Gerenciamento nativo de Pods no Podman e integração com manifestos YAML do Kubernetes.
- [[podman-oci-runtime-crun-runc-conmon-and-shared-libraries]] — Veja também: Ecossistema de bibliotecas OCI do Podman: crun, runc, conmon, containers/image e containers/storage.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
