---
id: software.devops.tranche04.000365
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

# Ecossistema de bibliotecas OCI do Podman: crun, runc, conmon, containers/image e containers/storage

## Em uma frase
O Podman constrói sua arquitetura combinando projetos OCI e bibliotecas especializadas compartilhadas com o Buildah e o CRI-O: configuração de runtime gerada via `opencontainers/runtime-tools` para qualquer runtime compatível com OCI como **`crun`** (escrito em C, rápido e leve) e **`runc`**; gerenciamento de imagens via biblioteca **`containers/image`**; armazenamento de camadas e contêineres via **`containers/storage`**; monitoramento do processo do runtime OCI via **`conmon`** (`github.com/containers/conmon`); suporte a **OCI Hooks**; e uma política unificada de **Seccomp** (`seccomp.json`) compartilhada entre Podman, Buildah e CRI-O.

## Por que importa
Como o Podman não tem um daemon persistente, o pequeno utilitário C **`conmon`** permanece anexado a cada contêiner em execução para monitorar o processo do runtime (`crun`/`runc`), segurar os descritores de arquivos de `stdout`/`stderr`, gravar logs e capturar o código de saída quando o contêiner termina.

## Como funciona
Prefira o runtime `crun` em distribuições Linux modernas com cgroups v2 pelo menor consumo de memória e inicialização mais rápida, e mantenha a política Seccomp padrão ativa para restringir chamadas de sistema perigosas do kernel.

## Exemplo
Quando o comando `podman run -d` retorna imediatamente no terminal, o processo `conmon` correspondente permanece ativo em segundo plano gerenciando o console e o ciclo de vida do contêiner executado pelo `crun`.

## Limites e trade-offs
Nunca mate manualmente processos `conmon` no host achando que são processos órfãos, pois encerrar o `conmon` interrompe o monitoramento e o controle do contêiner que ele supervisiona.

## Como verificar
Consulte `podman info` para verificar o `ociRuntime` ativo (`crun` ou `runc`), a versão do `conmon` e a configuração do `containers/storage`.

## Conexões
- [[podman-netavark-aardvark-dns-and-pasta-networking]] — Veja também: Pilha de rede do Podman: Netavark, servidor DNS Aardvark e rede rootless com pasta.
- [[podman-buildah-and-podman-specialization-and-storage]] — Veja também: Relação complementar e diferenças de conceito de contêiner entre Podman e Buildah.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
