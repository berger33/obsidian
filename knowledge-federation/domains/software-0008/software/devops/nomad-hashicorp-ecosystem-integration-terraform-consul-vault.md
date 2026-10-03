---
id: software.devops.tranche06.000596
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

# Integração nativa do Nomad com o ecossistema HashiCorp: Terraform, Consul e Vault

## Em uma frase
A seção *HashiCorp Ecosystem* do README oficial destaca que o Nomad integra-se de forma nativa e contínua com **Terraform, Consul e Vault** para formar uma pilha completa: o **Terraform** provisiona a infraestrutura de rede e as máquinas do cluster (como demonstrado nos manifestos de referência do próprio diretório `terraform/` do repositório); o **Consul** fornece descoberta automática de serviços, health checks e Service Mesh mTLS para as tarefas agendadas pelo Nomad; e o **Vault** fornece gerenciamento dinâmico de segredos, injetando credenciais temporárias diretamente nos templates e variáveis das tarefas em execução.

## Por que importa
Integrar manualmente um orquestrador de cargas de trabalho a um catálogo de serviços externo e a um cofre de segredos costuma exigir dezenas de operadores extras e scripts de init. No Nomad, declarar um bloco `service {}` registra a tarefa no Consul/Nomad automaticamente, e declarar um bloco `vault {}` com `template {}` busca e renova segredos do HashiCorp Vault nativamente pelo próprio agente Nomad Client.

## Como funciona
Em arquiteturas baseadas na pilha HashiCorp, configure a integração com Consul e Vault nos agentes Nomad para que qualquer job HCL possa solicitar identidades de malha (`connect { sidecar_service {} }`) e segredos dinâmicos (`vault {}` + `template {}`) em poucas linhas declarativas.

## Exemplo
Uma tarefa de aplicação declarada no Nomad inclui um bloco `vault` e um bloco `template` que renderiza um arquivo de configuração em memória (`secrets/db.env`) com credenciais dinâmicas de banco de dados geradas pelo Vault, reiniciando ou enviando sinal `SIGHUP` à aplicação automaticamente quando o segredo é rotacionado.

## Limites e trade-offs
Ao renderizar segredos via bloco `template` no Nomad, grave sempre os arquivos resultantes dentro do diretório protegido em memória da alocação (**`secrets/`**, montado em `tmpfs`) em vez de gravá-los no disco persistente local.

## Como verificar
Inspecione uma alocação ativa (`nomad alloc status <alloc-id>`) e confirme o registro do serviço e a renderização limpa dos templates da tarefa.

## Conexões
- [[nomad-optimistically-concurrent-scheduling-at-10k-nodes-scale]] — Veja também: Agendamento concorrente otimista (Optimistic Concurrency) e escalabilidade comprovada em mais de 10.000 nós.
- [[nomad-job-specification-service-batch-and-system-schedulers]] — Veja também: Especificação de Jobs em HCL e os tipos de agendadores do Nomad (service, batch, system e sysbatch).

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
