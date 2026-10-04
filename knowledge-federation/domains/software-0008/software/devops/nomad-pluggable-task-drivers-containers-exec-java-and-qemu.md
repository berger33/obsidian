---
id: software.devops.tranche06.000591
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
fontes: ["https://raw.githubusercontent.com/hashicorp/nomad/main/README.md", "https://developer.hashicorp.com/nomad/docs", "https://github.com/hashicorp/nomad"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Orquestração unificada de contêineres (Docker, Podman), binários (exec, Java) e VMs (QEMU) via Task Drivers no Nomad

## Em uma frase
O HashiCorp Nomad (`developer.hashicorp.com/nomad`), suportado em **Linux, Windows e macOS**, é um orquestrador de cargas de trabalho simples e flexível para implantar e gerenciar tanto **contêineres** quanto **aplicações não containerizadas** e **máquinas virtuais** em infraestrutura on-premises e na nuvem em larga escala. Conforme destaca o README oficial, essa flexibilidade vem da sua arquitetura de **Task Drivers plugáveis**: o Nomad orquestra nativamente contêineres (**`docker`** e **`podman`**), aplicações executáveis diretamente no sistema operacional (**`exec`** / `raw_exec` e **`java`** para aplicações JAR/JVM) e máquinas virtuais (**`qemu`**), permitindo executar aplicações legadas, processos em lote (batch) e microsserviços modernos juntos na mesma infraestrutura sem exigir containerização prévia.

## Por que importa
Em muitas empresas de manufatura, finanças, jogos ou telecomunicações, existem binários C++, serviços Windows, aplicações Java legadas ou daemons de hardware que não podem ou não devem ser empacotados em imagens Docker, mas ainda assim precisam de agendamento automatizado, health checks, rolling updates e failover.

## Como funciona
Utilize o driver `docker` ou `podman` no arquivo de job HCL do Nomad para cargas containerizadas e utilize os drivers `exec`, `java` ou `qemu` para trazer benefícios completos de orquestração declarativa a binários nativos e máquinas virtuais no mesmo cluster.

## Exemplo
Uma empresa executa no mesmo cluster Nomad seus novos microsserviços via driver `podman`/`docker`, um motor legado de processamento financeiro em Java via driver `java` e agentes de monitoramento de baixo nível via driver `exec`.

## Limites e trade-offs
Ao utilizar drivers que executam binários diretamente no host (como `exec` no Linux, que usa isolamento de `chroot`/cgroups do sistema operacional), garanta que as bibliotecas compartilhadas ou o runtime Java exigidos pela tarefa estejam presentes nos nós clientes elegíveis (usando `constraint` no job).

## Como verificar
Execute `nomad node status -self` em um nó cliente do Nomad e verifique na seção `Driver Status` quais task drivers (`docker`, `podman`, `exec`, `java`, `qemu`) estão detectados e saudáveis (`healthy = true`).

## Conexões
- [[nomad-single-binary-self-contained-architecture]] — Veja também: Arquitetura de binário único autocontido do Nomad sem serviços externos de armazenamento ou coordenação.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
