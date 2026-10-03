---
id: software.devops.tranche06.000598
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

# Operação via Nomad CLI (developer.hashicorp.com/nomad/commands), HTTP API e ecossistema de Plugins

## Em uma frase
O README oficial aponta diretamente para as quatro referências centrais de operação e extensão do Nomad: a documentação de comandos do **CLI** (`developer.hashicorp.com/nomad/commands`), a referência completa da **HTTP API** (`developer.hashicorp.com/nomad/api-docs`), a documentação de **Nomad Plugins** (`developer.hashicorp.com/nomad/plugins` — cobrindo Task Drivers externos como o plugin `podman`, Device Plugins e plugins de armazenamento **CSI — Container Storage Interface**) e os tutoriais práticos (`developer.hashicorp.com/nomad/tutorials`).

## Por que importa
O suporte a plugins **CSI (Container Storage Interface)** e **CNI (Container Network Interface)** dentro do ecossistema de plugins do Nomad permite que o Nomad consuma os mesmos drivers de armazenamento em nuvem/on-premises (EBS, Ceph, NFS) e plugins de rede do ecossistema cloud-native mantendo a simplicidade operacional do Nomad.

## Como funciona
Utilize o CLI do Nomad (`nomad job`, `nomad alloc`, `nomad node`, `nomad volume`, `nomad acl`) para operações e pipelines GitOps, instale plugins adicionais de task drivers (como `nomad-driver-podman`) no diretório `plugin_dir` dos nós clientes e gerencie volumes persistentes via CSI.

## Exemplo
Para executar contêineres sem daemon Docker nos nós clientes Linux, a equipe instala o plugin oficial do Podman (`developer.hashicorp.com/nomad/plugins/drivers/podman`) nos agentes Nomad e passa a agendar tarefas com `driver = "podman"`.

## Limites e trade-offs
Ao atualizar versões de plugins externos (`podman`, plugins CSI ou Device Plugins) nos nós clientes, drene o nó com segurança primeiro (**`nomad node drain -enable <node-id>`**) para migrar as alocações ativas antes de reiniciar o serviço do agente Nomad.

## Como verificar
Execute `nomad version`, `nomad status` e `nomad plugin status` para verificar a saúde da API, dos jobs e dos plugins CSI/dispositivos registrados.

## Conexões
- [[nomad-job-specification-service-batch-and-system-schedulers]] — Veja também: Especificação de Jobs em HCL e os tipos de agendadores do Nomad (service, batch, system e sysbatch).
- [[nomad-local-dev-agent-and-terraform-cloud-reference-manifests]] — Veja também: Desenvolvimento local (nomad agent -dev), manifestos Terraform de referência e arquitetura de produção.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
