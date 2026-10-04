---
id: software.devops.tranche04.000367
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

# Checkpoint e restauração de contêineres em execução no Podman via CRIU

## Em uma frase
No escopo de gerenciamento completo do ciclo de vida do contêiner, o README oficial do Podman inclui a capacidade de **checkpointing e restoring** de contêineres através do **CRIU** (Checkpoint/Restore In Userspace). Esse recurso permite congelar um contêiner stateful em execução, serializar o estado completo de seus processos em memória, conexões e arquivos abertos para o disco, e restaurá-lo posteriormente no mesmo host ou migrá-lo para outro nó sem perder o estado em memória.

## Por que importa
Aplicações que levam vários minutos para aquecer caches em memória ou carregar modelos pesados na inicialização podem ter seu estado pós-inicialização salvo em um checkpoint CRIU e restaurado em frações de segundo, além de permitir manutenção de host preservando sessões em memória.

## Como funciona
Utilize `podman container checkpoint` e `podman container restore` em hosts Linux configurados com suporte ao CRIU quando precisar suspender, clonar ou migrar o estado em memória de contêineres compatíveis.

## Exemplo
Para acelerar a inicialização de um serviço Java pesado, a plataforma inicia o contêiner, aguarda o aquecimento completo da JVM, gera um checkpoint via CRIU no Podman e restaura novas instâncias diretamente a partir da imagem de estado em memória.

## Limites e trade-offs
Verifique a compatibilidade do kernel, versão do CRIU e runtime OCI (como `crun`/`runc`) antes de depender de checkpoint/restore em produção, pois processos que mantêm recursos específicos de hardware ou sockets externos incompatíveis podem falhar no congelamento.

## Como verificar
Em um host com CRIU instalado, execute o ciclo de checkpoint e restore em um contêiner de teste com contador em memória e confirme que o processo retoma a contagem exatamente do ponto em que foi congelado.

## Conexões
- [[podman-buildah-and-podman-specialization-and-storage]] — Veja também: Relação complementar e diferenças de conceito de contêiner entre Podman e Buildah.
- [[podman-podman-machine-and-podman-desktop-multi-os]] — Veja também: Execução multiplataforma no Windows e macOS com podman machine e Podman Desktop.

## Fontes
- [Podman GitHub — README.md (Architecture, libpod, Rootless, OCI Projects & Buildah Relationship)](https://raw.githubusercontent.com/containers/podman/main/README.md) — README oficial do Podman descrevendo arquitetura sem daemon baseada em libpod, suporte a contêineres e pods rootless com user namespaces, bibliotecas OCI (crun/runc, containers/image, containers/storage, Netavark, Aardvark, pasta, Conmon), checkpoint/restore com CRIU, podman machine e relação complementar com Buildah e Skopeo.; consultado em 2026-10-03.
- [Podman Documentation — Official Docs & API Reference](https://docs.podman.io/en/latest/) — Documentação técnica oficial do Podman cobrindo comandos compatíveis com Docker CLI, gerenciamento de pods, geração e execução de YAML Kubernetes e API REST.; consultado em 2026-10-03.
- [Podman — Official GitHub Repository](https://github.com/containers/podman) — Repositório oficial Apache-2.0 do Podman e da biblioteca libpod.; consultado em 2026-10-03.
