---
id: software.devops.tranche06.000502
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
fontes: ["https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md", "https://docs.litmuschaos.io/docs/introduction/what-is-litmus", "https://github.com/litmuschaos/litmus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# O recurso customizado ChaosExperiment e o modelo Bring-Your-Own-Chaos (BYOC) no LitmusChaos

## Em uma frase
No coração da plataforma LitmusChaos estão três Custom Resources (CRs) do Kubernetes, sendo o primeiro o **`ChaosExperiment`**. Conforme documenta o README oficial, o `ChaosExperiment` agrupa os parâmetros de configuração de uma falha específica: esses CRs funcionam como **templates instaláveis** que descrevem a biblioteca executora da falha, indicam as permissões RBAC necessárias para rodá-la e definem os valores padrão de operação. Através do `ChaosExperiment`, o Litmus suporta nativamente **BYOC (Bring-Your-Own-Chaos)**, permitindo integrar qualquer ferramenta de terceiros ou script customizado para realizar a injeção de falha.

## Por que importa
Nem toda falha de negócio ou infraestrutura específica de uma empresa está pronta em ferramentas genéricas de mercado; o suporte a **BYOC** no `ChaosExperiment` permite empacotar scripts internos de simulação de falha em imagem de contêiner e executá-los com a mesma governança declarativa dos experimentos oficiais.

## Como funciona
Instale os manifestos `ChaosExperiment` homologados a partir do Chaos Hub no namespace de teste ou empacote seus próprios injetores de falha customizados seguindo o contrato BYOC do `ChaosExperiment`.

## Exemplo
Uma equipe de banco de dados empacota uma ferramenta própria de simulação de latência de replicação como imagem OCI e a declara em um `ChaosExperiment` BYOC, reutilizando toda a validação de estado estável e coleta de métricas do LitmusChaos.

## Limites e trade-offs
Ao instalar um `ChaosExperiment`, revise sempre a lista de permissões RBAC exigidas pelo experimento na especificação do CR para conceder à `ServiceAccount` executora apenas os verbos estritamente necessários.

## Como verificar
Execute `kubectl get chaosexperiments -n <namespace>` e inspecione o YAML instalado para validar a imagem executora, variáveis de ambiente padrão e permissões declaradas.

## Conexões
- [[litmus-control-plane-chaos-center-and-execution-plane]] — Veja também: Arquitetura do LitmusChaos: Chaos Control Plane (chaos-center) e Chaos Execution Plane.
- [[litmus-chaosengine-steady-state-probes-and-chaos-operator]] — Veja também: Vinculação de alvo, validação de hipótese de estado estável via probes e Chaos-Operator no ChaosEngine.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
