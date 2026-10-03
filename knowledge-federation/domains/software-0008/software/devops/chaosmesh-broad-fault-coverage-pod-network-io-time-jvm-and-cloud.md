---
id: software.devops.tranche06.000512
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
fontes: ["https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md", "https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md", "https://github.com/chaos-mesh/chaos-mesh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cobertura abrangente de falhas no Chaos Mesh: Pod, Rede, DNS, HTTP, I/O, Clock Skew, Kernel, JVM, Bare-Metal e Nuvens

## Em uma frase
Na seção *Features*, o README oficial destaca a ampla cobertura de falhas nativas do Chaos Mesh: **Pod (`PodChaos`), rede (`NetworkChaos`), DNS (`DNSChaos`), HTTP (`HTTPChaos`), entrada/saída de arquivos (`IOChaos`), tempo/desvio de relógio (`TimeChaos`), estresse de CPU/memória (`StressChaos`), kernel (`KernelChaos`), dispositivos de bloco (`BlockChaos`), máquina virtual Java (`JVMChaos`), máquinas físicas (`PhysicalMachineChaos`) e falhas em provedores de nuvem pública (`AWSChaos`, `AzureChaos` e `GCPChaos`)**.

## Por que importa
Problemas complexos em sistemas distribuídos — como bugs de expiração de certificado ou consenso Raft causados por desvio de relógio (*clock skew*), lentidão de disco (`IOChaos`) ou exceções internas de métodos Java (`JVMChaos`) — não podem ser reproduzidos apenas matando pods (`PodChaos`). O Chaos Mesh simula todas essas camadas no nível do contêiner sem afetar outros contêineres vizinhos no mesmo nó.

## Como funciona
Selecione o tipo exato de CRD de falha para a hipótese que deseja testar: use `TimeChaos` para testar sensibilidade a *clock skew* em tokens JWT/TLS ou bancos distribuídos, `IOChaos`/`HTTPChaos` para testar timeouts de dependências e `JVMChaos` para injetar exceções ou latência de bytecode em serviços Java.

## Exemplo
Para validar como um banco de dados distribuído reage a um desvio de relógio de +5 minutos em apenas uma réplica sem alterar o relógio do host nem dos demais pods do nó, o engenheiro aplica um recurso `TimeChaos` direcionado ao pod daquela réplica.

## Limites e trade-offs
Restrinja tipos de falha altamente intrusivos no kernel do host (como `KernelChaos`) a clusters de teste dedicados, pois falhas injetadas no nível do kernel compartilhado podem impactar todo o nó trabalhador.

## Como verificar
Aplique um manifesto `PodChaos` ou `NetworkChaos` em ambiente de teste (ou no playground interativo Killercoda referenciado no README) e verifique nos eventos do recurso a transição para a fase `Injected` e posterior recuperação.

## Conexões
- [[chaosmesh-three-runtime-components-controller-daemon-and-dashboard]] — Veja também: Arquitetura de runtime do Chaos Mesh: Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.
- [[chaosmesh-schedule-workflow-and-statuscheck-orchestration]] — Veja também: Orquestração de experimentos recorrentes, fluxos seriados/paralelos e verificações de saúde com Schedule, Workflow e StatusCheck.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
