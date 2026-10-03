---
id: software.devops.tranche06.000592
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

# Arquitetura de binário único autocontido do Nomad sem serviços externos de armazenamento ou coordenação

## Em uma frase
Na seção *Simple & Reliable*, o README oficial destaca um dos maiores diferenciais operacionais do Nomad em relação a orquestradores mais pesados: **o Nomad executa como um único binário (`nomad`) e é inteiramente autocontido — combinando gerenciamento de recursos e agendamento em um único sistema**. O Nomad **não exige nenhum serviço externo para armazenamento ou coordenação** (como um cluster etcd ou ZooKeeper separado): os servidores Nomad formam seu próprio quórum distribuído e resiliente usando **eleição de líder (Raft) e replicação de estado integrada** para oferecer alta disponibilidade e tratar automaticamente falhas de aplicação, de nó e de driver.

## Por que importa
Operar um plano de controle distribuído onde o banco de estado (etcd), o API server, o controller-manager e o scheduler são múltiplos componentes independentes exige alta carga operacional para clusters de borda, filiais ou equipes enxutas de SRE. No Nomad, o mesmo executável `nomad` roda no modo `server` (plano de controle Raft + agendador) ou no modo `client` (agente de execução no nó).

## Como funciona
Implante um cluster de servidores Nomad (tipicamente 3 ou 5 nós com `server { enabled = true, bootstrap_expect = 3 }`) e aponte a frota de nós trabalhadores (`client { enabled = true }`) para esses servidores, obtendo um orquestrador completo sem instalar bancos de coordenação externos.

## Exemplo
Uma rede de varejo implanta clusters leves de 3 pequenos servidores em suas filiais usando o binário único do Nomad para orquestrar serviços locais de caixa e logística com failover automático e sobrecarga mínima de memória.

## Limites e trade-offs
Mesmo sendo um binário único, em ambientes de produção siga a arquitetura de referência oficial (`developer.hashicorp.com/nomad/docs/deploy/production/reference-architecture`) separando os nós que rodam como **Nomad Server** dos nós que rodam cargas pesadas como **Nomad Client**, protegendo a latência de disco e CPU do consenso Raft dos servidores.

## Como verificar
Execute `nomad server members` e `nomad operator raft list-peers` para confirmar o quórum autocontido dos servidores Nomad.

## Conexões
- [[nomad-pluggable-task-drivers-containers-exec-java-and-qemu]] — Veja também: Orquestração unificada de contêineres (Docker, Podman), binários (exec, Java) e VMs (QEMU) via Task Drivers no Nomad.
- [[nomad-device-plugins-gpu-fpga-and-tpu-workloads]] — Veja também: Suporte nativo a cargas de IA/ML com Device Plugins para GPUs, FPGAs e TPUs no Nomad.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
