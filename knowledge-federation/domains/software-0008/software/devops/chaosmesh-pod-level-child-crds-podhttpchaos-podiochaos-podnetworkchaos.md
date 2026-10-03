---
id: software.devops.tranche06.000516
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

# Reconciliação de CRDs filhos de nível de Pod (PodHTTPChaos, PodIOChaos e PodNetworkChaos) no Chaos Mesh

## Em uma frase
A tabela de diretórios em `controllers/README.md` revela um mecanismo essencial de coordenação do Chaos Mesh para falhas compartilhadas no mesmo pod: os diretórios **`podhttpchaos/`**, **`podiochaos/`** e **`podnetworkchaos/`** contêm os reconciliadores para os **CRDs filhos de nível de Pod (`PodHTTPChaos`, `PodIOChaos` e `PodNetworkChaos`)**, que são os recursos que efetivamente se comunicam com o **Chaos Daemon** no nó. Quando múltiplos experimentos `NetworkChaos`, `IOChaos` ou `HTTPChaos` de alto nível selecionam o mesmo Pod ao mesmo tempo, eles escrevem suas intenções no recurso filho correspondente daquele Pod, que consolida e aplica o conjunto completo de regras no `Chaos Daemon` sem que um experimento sobrescreva as regras de `iptables`/`tc` ou FUSE do outro.

## Por que importa
Se dois experimentos `NetworkChaos` independentes programassem diretamente o `tc`/`iptables` do mesmo Pod sem um recurso filho consolidador (`PodNetworkChaos`), o segundo experimento apagaria as regras do primeiro ou deixaria regras órfãs ao ser revertido.

## Como funciona
Ao diagnosticar por que uma falha de rede, I/O ou HTTP não foi aplicada ou não foi limpa em um Pod específico, inspecione diretamente o recurso filho `PodNetworkChaos`, `PodIOChaos` ou `PodHTTPChaos` de mesmo nome do Pod alvo no namespace da aplicação.

## Exemplo
Um engenheiro aplica simultaneamente um `NetworkChaos` de latência e outro `NetworkChaos` de perda de pacotes sobre o pod `api-0`; ambos convergem no recurso filho `PodNetworkChaos/api-0`, que instrui o `Chaos Daemon` a aplicar as duas regras combinadas no network namespace do pod.

## Limites e trade-offs
Nunca edite nem exclua manualmente os recursos filhos `PodNetworkChaos`, `PodIOChaos` ou `PodHTTPChaos` enquanto os experimentos pais estiverem ativos; remova sempre o recurso pai de alto nível para acionar a reconciliação limpa.

## Como verificar
Execute `kubectl get podnetworkchaos,podiochaos,podhttpchaos -n <namespace>` durante um experimento ativo para verificar o estado consolidado por pod.

## Conexões
- [[chaosmesh-uber-fx-composition-and-common-reconciliation-pipeline]] — Veja também: Composição modular com Uber Fx (controllers/fx.go) e pipeline comum de reconciliação no Chaos Mesh.
- [[chaosmesh-one-writer-per-field-and-idempotent-level-based-reconciliation]] — Veja também: Regras de engenharia de controladores no Chaos Mesh: One writer per field e reconciliação idempotente baseada em nível.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
