---
id: software.devops.tranche06.000597
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

# Especificação de Jobs em HCL e os tipos de agendadores do Nomad (service, batch, system e sysbatch)

## Em uma frase
A documentação oficial de conceitos (`developer.hashicorp.com/nomad/docs`) estrutura a unidade declarativa de trabalho do Nomad em uma hierarquia clara escrita em **HCL (HashiCorp Configuration Language)**: um **Job** contém um ou mais **Task Groups (`group`)** — conjunto de tarefas que devem ser co-localizadas no mesmo nó cliente compartilhando rede e volumes —, e cada grupo contém uma ou mais **Tasks (`task`)** executadas por seus respectivos drivers. Cada Job declara seu tipo de agendador (`type`): **`service`** (serviços de longa duração que nunca devem parar e são reagendados se falharem), **`batch`** (tarefas de curta ou média duração que executam até terminar com código de saída 0), **`system`** (roda uma instância em cada nó cliente elegível do cluster, análogo a um DaemonSet) e **`sysbatch`** (executa um trabalho batch uma vez em cada nó elegível, ideal para manutenção de host).

## Por que importa
Reutilizar a mesma sintaxe HCL concisa para serviços web (`service`), jobs agendados via cron (`periodic` + `batch`), agentes de log/monitoramento por nó (`system`) e tarefas de patch de segurança em todos os nós (`sysbatch`) simplifica drasticamente a curva de aprendizado da equipe.

## Como funciona
Escolha o `type` exato na definição do seu Job Nomad (`service`, `batch`, `system` ou `sysbatch`) e agrupe dentro do mesmo `group` apenas as `tasks` que realmente precisam rodar juntas no mesmo nó (como a aplicação principal e um contêiner auxiliar/init).

## Exemplo
Para rodar um agente coletor de logs (como Fluent Bit ou Vector) em todos os servidores Linux do cluster, o engenheiro define um job com `type = "system"`, garantindo que todo novo nó cliente que entrar no cluster receba automaticamente uma alocação do coletor.

## Limites e trade-offs
Não use `type = "service"` para scripts que devem rodar uma tarefa rápida e encerrar com `exit 0`; no agendador `service`, encerrar o processo é tratado como falha inesperada e o Nomad continuará reiniciando a tarefa repetidamente conforme a `restart` policy.

## Como verificar
Valide a sintaxe de um arquivo `.nomad.hcl` com **`nomad job validate <arquivo.nomad.hcl>`** antes de planejar ou submeter o job ao cluster.

## Conexões
- [[nomad-hashicorp-ecosystem-integration-terraform-consul-vault]] — Veja também: Integração nativa do Nomad com o ecossistema HashiCorp: Terraform, Consul e Vault.
- [[nomad-nomad-cli-api-and-plugin-ecosystem-operations]] — Veja também: Operação via Nomad CLI (developer.hashicorp.com/nomad/commands), HTTP API e ecossistema de Plugins.

## Fontes
- [HashiCorp Nomad GitHub — README.md (Pluggable Task Drivers, Single Binary, GPU/Device Plugins, Multi-Region Federation, 10K+ Nodes & BUSL-1.1)](https://raw.githubusercontent.com/hashicorp/nomad/main/README.md) — README oficial do HashiCorp Nomad (licenciado sob BUSL-1.1) detalhando orquestração de contêineres (docker, podman), aplicações não containerizadas (exec, Java) e VMs (qemu) em Linux, Windows e macOS, binário único autocontido sem dependências externas de armazenamento/coordenação, plugins de dispositivos (GPU, FPGAs, TPUs), federação multi-região/multi-cloud nativa, escalabilidade otimista comprovada em clusters de 10K+ nós e integração com Terraform, Consul e Vault.; consultado em 2026-10-03.
- [HashiCorp Nomad Official Documentation — Concepts, User Guides & Reference Architecture](https://developer.hashicorp.com/nomad/docs) — Documentação oficial completa do HashiCorp Nomad incluindo arquitetura de referência para produção, CLI, API e plugins.; consultado em 2026-10-03.
- [HashiCorp Nomad — Official GitHub Repository](https://github.com/hashicorp/nomad) — Repositório oficial do HashiCorp Nomad.; consultado em 2026-10-03.
