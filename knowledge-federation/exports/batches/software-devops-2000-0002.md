# Lote de escala software-devops-2000-0002

- Data de início: 2026-10-03
- Última atualização: 2026-10-03
- Escopo: engenharia de software — DevOps, GitOps, IaC, observabilidade e runtimes cloud-native
- Tamanho-alvo solicitado: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **400 / 2.000 (20,00%)**
- Gate automatizado: **400/400 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 4)
- Revisão factual humana: **0/400**
- Revisão factual por IA: **400/400**
- Contabilizadas como válidas: **400/400**
- Revisor das 400 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranches 1–4 (400 notas, IDs 1–400) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado
- Auditoria reproduzível do gate e links: [`note-quality-software-devops-2000-0002.md`](../reports/note-quality-software-devops-2000-0002.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-04.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-04.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md), [`tranche 3`](../reports/ai-review-software-devops-2000-0002-tranche-03.md), [`tranche 4`](../reports/ai-review-software-devops-2000-0002-tranche-04.md)
- Navegação: [`MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)

> **Contagem literal:** 2.000 é a meta deste segundo lote de escala, não a quantidade já criada. Existem 400 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1600 restantes. A contagem válida só avança com conteúdo substantivo, fontes específicas, gate aprovado e revisão factual humana ou por IA registrada separadamente.

## Tranche 1 — OpenTelemetry Collector, Argo CD, Helm, OpenTofu, Ansible, Flux v2, Kustomize, containerd, Jaeger e Tekton Pipelines (100 notas; revisão factual por IA registrada)

### OpenTelemetry Collector — recepção, processamento e exportação de telemetria agnóstica a fornecedor

1. [OpenTelemetry Collector: implementação agnóstica a fornecedor para receber, processar e exportar telemetria](../../domains/software-0008/software/devops/otelcol-what-it-is.md)
2. [Os cinco objetivos de projeto: Usable, Performant, Observable, Extensible e Unified](../../domains/software-0008/software/devops/otelcol-five-core-objectives.md)
3. [Suporte nativo ao protocolo OTLP v1.10.0 e definição de estabilidade do protocolo](../../domains/software-0008/software/devops/otelcol-otlp-protocol-version-stability.md)
4. [Política de suporte a versões menores do Go (N e N-1, remoção de N-2) quando usado como biblioteca](../../domains/software-0008/software/devops/otelcol-go-minor-version-compatibility-policy.md)
5. [Verificação criptográfica de assinaturas das imagens oficiais com Sigstore Cosign](../../domains/software-0008/software/devops/otelcol-cosign-image-signature-verification.md)
6. [Os seis níveis de estabilidade de componentes por sinal: Development a Unmaintained](../../domains/software-0008/software/devops/otelcol-component-stability-tiers-per-signal.md)
7. [Garantias de configuração em Beta e Stable: depreciação com WARN e prazo N+2 ou 6 meses](../../domains/software-0008/software/devops/otelcol-beta-and-stable-configuration-deprecation-rules.md)
8. [Os três requisitos obrigatórios de testes para graduação de um componente a Stable](../../domains/software-0008/software/devops/otelcol-stable-component-testing-requirements.md)
9. [Auto-observabilidade, práticas de segurança e verificação contínua via OSS-Fuzz](../../domains/software-0008/software/devops/otelcol-internal-telemetry-and-security-best-practices.md)
10. [Governança do SIG OpenTelemetry Collector: rotação de horários e GitHub como fonte da verdade](../../domains/software-0008/software/devops/otelcol-sig-governance-and-github-source-of-truth.md)

### Argo CD — entrega contínua declarativa e GitOps para Kubernetes

11. [Argo CD: entrega contínua declarativa GitOps para Kubernetes e seus dois princípios centrais](../../domains/software-0008/software/devops/argocd-what-it-is-and-why.md)
12. [Instalação com `kubectl apply --server-side --force-conflicts` e o limite de 262 KB dos CRDs](../../domains/software-0008/software/devops/argocd-install-server-side-apply-262kb-limit.md)
13. [Instalação enxuta (`core`) sem UI/SSO e autenticação padrão do Redis em `argocd-redis`](../../domains/software-0008/software/devops/argocd-core-install-and-redis-secret.md)
14. [Instalação da CLI `argocd` e acesso direto via `--port-forward-namespace argocd` / `ARGOCD_OPTS`](../../domains/software-0008/software/devops/argocd-cli-installation-and-port-forward-opts.md)
15. [Três modos de expor o `argocd-server`: Service `LoadBalancer`, Ingress e Port Forwarding](../../domains/software-0008/software/devops/argocd-exposing-server-loadbalancer-ingress.md)
16. [Senha inicial em `argocd-initial-admin-secret`, rotação e exclusão recomendada do Secret](../../domains/software-0008/software/devops/argocd-initial-admin-secret-and-password-rotation.md)
17. [Registro de clusters externos (`argocd cluster add`), `argocd-manager` e privilégios mínimos de RBAC](../../domains/software-0008/software/devops/argocd-external-cluster-registration-and-rbac.md)
18. [Criação de aplicações a partir do repositório `argocd-example-apps` e compatibilidade de arquitetura](../../domains/software-0008/software/devops/argocd-guestbook-example-and-multi-arch-note.md)
19. [Integração no ecossistema Argo e GitOps: Rollouts, Workflows, Events, ApplicationSet e Crossplane](../../domains/software-0008/software/devops/argocd-ecosystem-rollouts-workflows-events-crossplane.md)
20. [Comunidade, lista oficial de adotantes `USERS.md` e reuniões sob o Código de Conduta da CNCF](../../domains/software-0008/software/devops/argocd-community-governance-and-meetings.md)

### Helm — gerenciador de pacotes e Charts para aplicações Kubernetes

21. [Helm: gerenciador de pacotes de recursos Kubernetes pré-configurados (Charts)](../../domains/software-0008/software/devops/helm-what-it-is-and-five-uses.md)
22. [Anatomia mínima de um Chart (`Chart.yaml` e `templates/`) e o fluxo de renderização para a API Kubernetes](../../domains/software-0008/software/devops/helm-chart-structure-and-rendering-flow.md)
23. [Ciclo de vida de versões: Helm v4 estável na branch `main` e calendário de fim de suporte do Helm v3](../../domains/software-0008/software/devops/helm-v4-stable-vs-v3-support-timeline.md)
24. [Instalação oficial do cliente Helm: binários de release e os sete gerenciadores de pacotes suportados](../../domains/software-0008/software/devops/helm-installation-seven-package-managers.md)
25. [Descoberta e distribuição de Charts públicos pelo Artifact HUB](../../domains/software-0008/software/devops/helm-artifacthub-discovery-and-chart-sharing.md)
26. [Uso do Helm v4 como biblioteca Go (`helm.sh/helm/v4`) e documentação GoDoc](../../domains/software-0008/software/devops/helm-sdk-go-package-v4-reference.md)
27. [Builds reproduzíveis e gerenciamento do ciclo de vida de releases Kubernetes](../../domains/software-0008/software/devops/helm-reproducible-builds-and-release-lifecycle.md)
28. [Rastreamento de roadmap por GitHub Milestones e automação de releases](../../domains/software-0008/software/devops/helm-roadmap-milestones-and-release-workflow.md)
29. [Postura de segurança e saúde do projeto: CII Best Practices, OpenSSF Scorecard e LFX Health Score](../../domains/software-0008/software/devops/helm-openssf-scorecard-cii-and-lfx-health.md)
30. [Canais oficiais no Kubernetes Slack (`#helm-users`, `#helm-dev`, `#charts`), lista de e-mail e Developer Call](../../domains/software-0008/software/devops/helm-community-slack-channels-and-dev-call.md)

### OpenTofu — infraestrutura como código aberta com planos de execução e grafo de recursos

31. [OpenTofu: ferramenta open-source para construir, alterar e versionar infraestrutura com segurança](../../domains/software-0008/software/devops/opentofu-what-it-is.md)
32. [Infraestrutura como Código (IaC): sintaxe declarativa de alto nível, versionamento e reutilização](../../domains/software-0008/software/devops/opentofu-declarative-infrastructure-as-code.md)
33. [Planos de execução (`Execution Plans`): separação entre planejar e aplicar mudanças](../../domains/software-0008/software/devops/opentofu-execution-plans-safety-step.md)
34. [Grafo de recursos (`Resource Graph`) e paralelização automática de operações independentes](../../domains/software-0008/software/devops/opentofu-resource-dependency-graph-parallelism.md)
35. [Automação de mudanças (`Change Automation`): aplicação previsível de changesets complexos](../../domains/software-0008/software/devops/opentofu-change-automation-minimal-human-error.md)
36. [Builds noturnos (`nightlies.opentofu.org`), retenção de 30 dias e automação via `latest.json`](../../domains/software-0008/software/devops/opentofu-nightly-builds-and-latest-json.md)
37. [Políticas formais de reporte de vulnerabilidades de segurança e questões de copyright](../../domains/software-0008/software/devops/opentofu-security-policy-and-copyright-liaison.md)
38. [Acesso ao OpenTofu Registry e transparência da Registry Inclusion Policy](../../domains/software-0008/software/devops/opentofu-registry-access-and-inclusion-policy.md)
39. [Governança aberta: reuniões semanais da comunidade e quinzenais do Technical Steering Committee (TSC)](../../domains/software-0008/software/devops/opentofu-tsc-and-community-meetings.md)
40. [Onde buscar suporte técnico e contribuir: GitHub Discussions, Issues e `#opentofu` no Slack da CNCF](../../domains/software-0008/software/devops/opentofu-support-channels-discussions-issues-slack.md)

### Ansible — automação de TI sem agentes, gerência de configuração e orquestração multi-nó

41. [Ansible: sistema de automação de TI para configuração, deploy, nuvem, tarefas ad-hoc, rede e orquestração](../../domains/software-0008/software/devops/ansible-what-it-is-and-six-domains.md)
42. [Arquitetura sem agentes sobre SSH e os nove princípios de design do Ansible](../../domains/software-0008/software/devops/ansible-agentless-ssh-and-nine-design-principles.md)
43. [Instalação de versões lançadas via `pip` ou gerenciador de pacotes do sistema versus uso da branch `devel`](../../domains/software-0008/software/devops/ansible-installation-pip-pkg-and-devel-branch.md)
44. [Modelo de branches do repositório: `devel` ativa, linhas `stable-2.X` e ciclo de manutenção](../../domains/software-0008/software/devops/ansible-branch-model-devel-vs-stable-2x.md)
45. [Diretrizes de desenvolvimento de módulos: diretório `context/`, checklist e boas práticas](../../domains/software-0008/software/devops/ansible-module-development-guidelines-and-context.md)
46. [Canais oficiais de comunicação: Ansible Forum (tags `ansible`, `ansible-core`, `playbook`), Matrix e newsletter The Bullhorn](../../domains/software-0008/software/devops/ansible-forum-matrix-and-bullhorn-newsletter.md)
47. [Planejamento público por versão no Ansible Roadmap e influência da comunidade](../../domains/software-0008/software/devops/ansible-roadmap-and-community-feedback.md)
48. [Segurança e auditabilidade nos princípios do Ansible: leitura humana e execução não-root](../../domains/software-0008/software/devops/ansible-security-auditability-and-nonroot-operation.md)
49. [Gerenciamento paralelo de frotas e provisionamento instantâneo sem etapa de bootstrap](../../domains/software-0008/software/devops/ansible-parallel-execution-and-zero-bootstrap.md)
50. [Origem com Michael DeHaan, mais de 5.000 contribuidores, patrocínio Red Hat e licença GPL v3.0+](../../domains/software-0008/software/devops/ansible-history-authors-sponsorship-and-gplv3.md)

### Flux v2 — sincronização GitOps para Kubernetes e controladores do GitOps Toolkit

51. [Flux v2: sincronização contínua de clusters Kubernetes com fontes Git e artefatos OCI](../../domains/software-0008/software/devops/fluxcd-what-it-is-and-v2-architecture.md)
52. [O GitOps Toolkit: conjunto de APIs componíveis e controladores especializados em Kubernetes](../../domains/software-0008/software/devops/fluxcd-gitops-toolkit-composable-apis.md)
53. [Source Controller e seus sete CRDs de origem: de `GitRepository` e `OCIRepository` a `ArtifactGenerator`](../../domains/software-0008/software/devops/fluxcd-source-controller-seven-crds.md)
54. [Kustomize Controller e o CRD `Kustomization` para reconciliação de manifestos e overlays](../../domains/software-0008/software/devops/fluxcd-kustomize-controller-and-crd.md)
55. [Helm Controller e o CRD `HelmRelease` para gerenciamento declarativo de charts Helm](../../domains/software-0008/software/devops/fluxcd-helm-controller-and-helmrelease-crd.md)
56. [Notification Controller: eventos de saída e webhooks de entrada com `Provider`, `Alert` e `Receiver`](../../domains/software-0008/software/devops/fluxcd-notification-controller-provider-alert-receiver.md)
57. [Automação de atualização de imagens no Git: `ImageRepository`, `ImagePolicy` e `ImageUpdateAutomation`](../../domains/software-0008/software/devops/fluxcd-image-automation-controllers-three-crds.md)
58. [Estruturação de repositórios GitOps e gestão de segredos Kubernetes com Mozilla SOPS](../../domains/software-0008/software/devops/fluxcd-repository-structure-and-mozilla-sops-guides.md)
59. [Multi-tenancy, integração nativa com Prometheus e avaliação de segurança SLSA Level 3](../../domains/software-0008/software/devops/fluxcd-multi-tenancy-prometheus-and-slsa3.md)
60. [Diretrizes de suporte comunitário (`fluxcd.io/support`), GitHub Discussions, `#flux` e roadmap](../../domains/software-0008/software/devops/fluxcd-community-support-guidelines-and-roadmap.md)

### Kustomize — customização declarativa e livre de templates para manifestos YAML do Kubernetes

61. [Kustomize: customização de YAML bruto e livre de templates com a semântica de `make` e `sed`](../../domains/software-0008/software/devops/kustomize-what-it-is-make-and-sed-analogy.md)
62. [Integração nativa no `kubectl`: histórico de versões embutidas e verificação com `kubectl version --client`](../../domains/software-0008/software/devops/kustomize-embedded-in-kubectl-version-matrix.md)
63. [Anatomia de um `kustomization.yaml` base: `resources`, `labels` (`includeSelectors`) e `configMapGenerator`](../../domains/software-0008/software/devops/kustomize-base-kustomization-file-anatomy.md)
64. [Geração de YAML customizado com `kustomize build` e aplicação em pipe com `kubectl apply -f -`](../../domains/software-0008/software/devops/kustomize-build-and-kubectl-apply-pipeline.md)
65. [Gerenciamento de variantes (`development`, `staging`, `production`) com `base` e `overlays`](../../domains/software-0008/software/devops/kustomize-variants-with-base-and-overlays.md)
66. [Aplicação declarativa de `patches` em overlays: ajustando réplicas e limites de CPU por ambiente](../../domains/software-0008/software/devops/kustomize-patches-replica-and-cpu-count-example.md)
67. [Fluxo Git com repositórios irmãos em disco: consumindo bases upstream sem precisar de Git submodules](../../domains/software-0008/software/devops/kustomize-git-workflow-sibling-repos-without-submodules.md)
68. [Propagação de rótulos com `labels:` e o efeito de `includeSelectors: true` na base e no overlay](../../domains/software-0008/software/devops/kustomize-labels-with-include-selectors.md)
69. [Conceitos formais do glossário Kustomize: Declarative Application Management, Base, Overlay, Variant e Resource](../../domains/software-0008/software/devops/kustomize-glossary-declarative-application-management.md)
70. [Governança no `sig-cli`, testes presubmit no Prow e fluxo para bugs, features e propostas maiores](../../domains/software-0008/software/devops/kustomize-community-bug-reporting-and-proposals.md)

### containerd — runtime de contêineres padrão da indústria, snapshotters e plugin CRI para Kubernetes

71. [containerd: runtime de contêineres graduado na CNCF desenhado para ser embutido em sistemas maiores](../../domains/software-0008/software/devops/containerd-what-it-is-and-embedded-design.md)
72. [Documentação operacional central: `docs/ops.md`, isolamento em `docs/namespaces.md` e `docs/client-opts.md`](../../domains/software-0008/software/devops/containerd-ops-namespaces-and-client-opts-guides.md)
73. [Requisitos de runtime: `runc` no Linux, `hcsshim` no Windows e versões mínimas de kernel para snapshotters](../../domains/software-0008/software/devops/containerd-runtime-requirements-runc-hcsshim-and-kernel.md)
74. [Checkpoint e Restore de contêineres em Linux com o requisito do `criu`](../../domains/software-0008/software/devops/containerd-checkpoint-restore-with-criu.md)
75. [Suporte a qualquer registry compatível com a OCI Distribution Specification e configuração em `docs/hosts.md`](../../domains/software-0008/software/devops/containerd-oci-distribution-registries-and-hosts-config.md)
76. [Estabilidade de API (`RELEASES.md`, `FEATURES.MD`) e autocompletar de shell para o cliente `ctr`](../../domains/software-0008/software/devops/containerd-releases-stability-and-ctr-autocompletion.md)
77. [O plugin nativo `cri` (GA): integração direta com a Container Runtime Interface do Kubernetes](../../domains/software-0008/software/devops/containerd-cri-plugin-ga-kubernetes-integration.md)
78. [Validação e depuração de setups CRI com `cri-tools`: `critest` e `crictl`](../../domains/software-0008/software/devops/containerd-cri-validation-critest-and-crictl-debugging.md)
79. [Builds noturnos para Linux e Windows via GitHub Actions e restrição estrita contra uso em produção](../../domains/software-0008/software/devops/containerd-nightly-builds-and-production-warning.md)
80. [Auditorias de segurança públicas (`containerd.io/security`), repositório `containerd/project` e `ADOPTERS.md`](../../domains/software-0008/software/devops/containerd-security-audits-governance-and-adopters.md)

### Jaeger — rastreamento distribuído graduado na CNCF, ingestão OTLP e políticas de suporte a storage

81. [Jaeger: plataforma de rastreamento distribuído criada na Uber e graduada na CNCF (com Jaeger v2)](../../domains/software-0008/software/devops/jaeger-what-it-is-and-cncf-history.md)
82. [Quick Start com a imagem `jaegertracing/jaeger:latest`: UI na porta `16686` e OTLP em `4317` (gRPC) e `4318` (HTTP)](../../domains/software-0008/software/devops/jaeger-docker-all-in-one-quickstart-ports.md)
83. [Arquitetura de componentes do Jaeger: OpenTelemetry SDK, Collector, Storage/Plugin, Query Service e UI](../../domains/software-0008/software/devops/jaeger-architecture-components-and-data-flow.md)
84. [Garantia de compatibilidade de configuração: carência mínima de 3 meses ou duas versões menores](../../domains/software-0008/software/devops/jaeger-config-deprecation-grace-period-policy.md)
85. [Política de versões do Go (N como mínimo e remoção de N-1) e pacotes movidos para `internal`](../../domains/software-0008/software/devops/jaeger-go-version-policy-and-internal-packages.md)
86. [Princípios da política de suporte a backends de armazenamento e a diferença entre suporte e presença no CI](../../domains/software-0008/software/devops/jaeger-storage-backend-support-policy-principles.md)
87. [Suporte oficial a Elasticsearch e OpenSearch no Jaeger: alinhamento às políticas de EOL e manutenção](../../domains/software-0008/software/devops/jaeger-elasticsearch-and-opensearch-support-matrix.md)
88. [Suporte oficial a Apache Cassandra e ClickHouse no Jaeger: versões maiores mantidas e foco em releases LTS](../../domains/software-0008/software/devops/jaeger-cassandra-and-clickhouse-lts-support-matrix.md)
89. [Auditorias de segurança independentes (`jaegertracing/security-audits`) e resumo de mecanismos de segurança](../../domains/software-0008/software/devops/jaeger-security-audits-and-mechanisms.md)
90. [Governança aberta (`GOVERNANCE.md`, `MAINTAINERS.md`), reuniões de status e canais `#jaeger` e `jaeger-tracing`](../../domains/software-0008/software/devops/jaeger-governance-maintainers-and-community-channels.md)

### Tekton Pipelines — recursos nativos em estilo Kubernetes para declarar pipelines de CI/CD

91. [Tekton Pipelines: recursos em estilo Kubernetes para declarar pipelines de CI/CD (Cloud Native, Decoupled e Typed)](../../domains/software-0008/software/devops/tekton-what-it-is-and-three-pillars.md)
92. [As entidades de base `Task` e `TaskRun`: definição de passos em contêineres vs. instanciação de execução](../../domains/software-0008/software/devops/tekton-task-and-taskrun-entities.md)
93. [Orquestração de ponta a ponta com `Pipeline` e `PipelineRun`](../../domains/software-0008/software/devops/tekton-pipeline-and-pipelinerun-entities.md)
94. [Evolução do modelo de entidades: depreciação de `PipelineResource` e introdução de Custom Tasks (`Run` / `CustomRun`)](../../domains/software-0008/software/devops/tekton-deprecated-pipelineresource-and-custom-runs.md)
95. [Matriz oficial de versão mínima do Kubernetes exigida pelo Tekton Pipelines (até `v0.61.x` -> Kubernetes 1.28+)](../../domains/software-0008/software/devops/tekton-kubernetes-minimum-version-progression.md)
96. [Governança de evolução da API: `api_compatibility_policy.md`, `docs/deprecations.md` e guias de migração `v1`](../../domains/software-0008/software/devops/tekton-api-compatibility-and-deprecations-table.md)
97. [Compartilhamento de dados, credenciais e parametrização: Workspaces, Authentication e Variable Substitutions](../../domains/software-0008/software/devops/tekton-workspaces-auth-and-variable-substitution.md)
98. [Observabilidade de execuções de CI/CD no Tekton: `labels.md`, `logs.md` e `metrics.md`](../../domains/software-0008/software/devops/tekton-observability-labels-logs-and-metrics.md)
99. [Reutilização remota e segurança da cadeia de suprimentos: `resolution.md` e `trusted-resources.md`](../../domains/software-0008/software/devops/tekton-remote-resolution-and-trusted-resources.md)
100. [Guia de contribuição, arquitetura interna (`docs/developers/README.md`) e duplo licenciamento CC-BY-4.0 / Apache 2.0](../../domains/software-0008/software/devops/tekton-contributing-development-and-licenses.md)

## Tranche 2 — Crossplane, Velero, Cilium, Linkerd, Harbor, Thanos, Grafana Loki, Fluent Bit, Vector e Skaffold (100 notas; revisão factual por IA registrada)

### Crossplane — framework de control planes cloud-native e composição declarativa de recursos (itens 101–110)

101. [Definição do Crossplane como framework de control planes sem escrever código](../../domains/software-0008/software/devops/crossplane-cloud-native-control-plane-framework.md)
102. [Arquitetura dual de backend extensível e frontend declarativo configurável](../../domains/software-0008/software/devops/crossplane-extensible-backend-and-declarative-frontend.md)
103. [Ponto de partida oficial e guia de início com Composition](../../domains/software-0008/software/devops/crossplane-get-started-and-composition-docs.md)
104. [Tabela de versões mantidas e cronograma de End-of-Life (EOL)](../../domains/software-0008/software/devops/crossplane-maintained-releases-and-eol-schedule.md)
105. [Fim de suporte da série v1.20 e transição para o Crossplane v2](../../domains/software-0008/software/devops/crossplane-v1-20-eol-and-v2-migration.md)
106. [Roadmap público, triagem comunitária e natureza estimativa dos milestones](../../domains/software-0008/software/devops/crossplane-public-roadmap-and-triage-process.md)
107. [Reuniões comunitárias a cada quatro semanas e canais de colaboração](../../domains/software-0008/software/devops/crossplane-community-meetings-and-channels.md)
108. [Papel consultivo dos Special Interest Groups (SIGs) sem autoridade decisória](../../domains/software-0008/software/devops/crossplane-special-interest-groups-governance.md)
109. [Frentes técnicas dos 14 SIGs: composição, provedores, Upjet e observabilidade](../../domains/software-0008/software/devops/crossplane-sig-composition-and-provider-ecosystems.md)
110. [Registro público de adotantes em ADOPTERS.md e conformidade OpenSSF](../../domains/software-0008/software/devops/crossplane-adopters-and-open-governance.md)

### Velero — backup, restauração, migração de clusters Kubernetes e proteção de volumes (itens 111–120)

111. [Visão geral do Velero: backup, restauração, migração e replicação de clusters](../../domains/software-0008/software/devops/velero-backup-restore-and-cluster-migration.md)
112. [Arquitetura cliente-servidor: controladores em réplica única no cluster e CLI local](../../domains/software-0008/software/devops/velero-server-controllers-and-local-cli.md)
113. [Movimentação de dados de volumes: file-system backup, data mover CSI e plugins de provedor](../../domains/software-0008/software/devops/velero-file-system-backup-and-csi-data-mover.md)
114. [Matriz de compatibilidade do Velero 1.14 a 1.18 com versões do Kubernetes](../../domains/software-0008/software/devops/velero-kubernetes-compatibility-matrix.md)
115. [Garantia de restauração de backups entre versões N-2 menores do Velero](../../domains/software-0008/software/devops/velero-n-minus-2-upgrade-restore-guarantee.md)
116. [Suporte a ambientes IPv4, IPv6 e dual-stack no Velero](../../domains/software-0008/software/devops/velero-ipv4-ipv6-and-dual-stack-support.md)
117. [Processo de propostas de design em design/ e histórico em design/Implemented/](../../domains/software-0008/software/devops/velero-design-proposals-and-implemented-archive.md)
118. [Seletor de versão na documentação e fluxo de troubleshooting do Velero](../../domains/software-0008/software/devops/velero-versioned-docs-and-troubleshooting.md)
119. [Reuniões quinzenais em dois fusos horários e governança em velero-io/.github](../../domains/software-0008/software/devops/velero-community-meetings-and-governance.md)
120. [Status na CNCF, séries LF Projects e guia Start contributing](../../domains/software-0008/software/devops/velero-cncf-sandbox-and-contributing-workflow.md)

### Cilium — rede CNI baseada em eBPF, segurança por identidade, service mesh e Hubble (itens 121–130)

121. [Dataplane baseado em eBPF para rede, observabilidade e segurança graduado na CNCF](../../domains/software-0008/software/devops/cilium-ebpf-dataplane-networking-security-observability.md)
122. [Modos de operação CNI: overlay (VXLAN/Geneve), roteamento nativo e BGP/L2](../../domains/software-0008/software/devops/cilium-cni-overlay-native-routing-and-bgp.md)
123. [Balanceamento de carga eBPF L4, substituição do kube-proxy, XDP, DSR e Maglev](../../domains/software-0008/software/devops/cilium-ebpf-load-balancing-kube-proxy-replacement.md)
124. [Cluster Mesh: descoberta global de serviços e identidade unificada entre clusters](../../domains/software-0008/software/devops/cilium-cluster-mesh-multicluster-service-discovery.md)
125. [Políticas de rede L3–L7 e DNS baseadas em identidade de segurança](../../domains/software-0008/software/devops/cilium-identity-based-l3-l7-and-dns-network-policy.md)
126. [Service Mesh sem sidecars tradicionais: criptografia IPsec/WireGuard/ztunnel e Gateway API](../../domains/software-0008/software/devops/cilium-service-mesh-encryption-and-gateway-api.md)
127. [Observabilidade integrada com Hubble, métricas Prometheus e motivos de descarte](../../domains/software-0008/software/devops/cilium-hubble-observability-and-drop-reasons.md)
128. [Política de manutenção das três últimas versões menores estáveis do Cilium](../../domains/software-0008/software/devops/cilium-stable-releases-and-three-minor-support-policy.md)
129. [Distribuição de imagens AMD64/AArch64 e SBOM em formato SPDX desde a v1.13.0](../../domains/software-0008/software/devops/cilium-multi-arch-images-and-spdx-sbom.md)
130. [Licenciamento Apache 2.0 em espaço de usuário e duplo licenciamento GPL-2.0/BSD-2-Clause em BPF](../../domains/software-0008/software/devops/cilium-dual-licensing-userspace-and-bpf-templates.md)

### Linkerd — service mesh ultraleve e security-first para Kubernetes com proxy em Rust (itens 131–140)

131. [Definição do Linkerd como service mesh ultraleve e security-first na CNCF](../../domains/software-0008/software/devops/linkerd-ultralight-security-first-service-mesh.md)
132. [Organização dos cinco repositórios do Linkerd e divisão entre Rust, Go e React](../../domains/software-0008/software/devops/linkerd-five-repositories-and-rust-go-react-split.md)
133. [Componentes nucleares do control plane: destination, proxy-injector e identity](../../domains/software-0008/software/devops/linkerd-control-plane-destination-injector-identity.md)
134. [Extensão viz: metrics-api, tap, tap-injector e dashboard web](../../domains/software-0008/software/devops/linkerd-viz-extension-metrics-tap-and-web.md)
135. [Extensão multicluster: linkerd-gateway e controlador linkerd-service-mirror](../../domains/software-0008/software/devops/linkerd-multicluster-gateway-and-service-mirror.md)
136. [Fluxo de instalação em duas etapas (--crds e control plane), linkerd check e linkerd inject](../../domains/software-0008/software/devops/linkerd-install-crds-check-and-inject-workflow.md)
137. [Habilitação de rastreamento distribuído nos componentes do control plane](../../domains/software-0008/software/devops/linkerd-control-plane-distributed-tracing-flag.md)
138. [Registro oficial cr.l5d.io/linkerd e fluxo de build local com k3d e buildx](../../domains/software-0008/software/devops/linkerd-container-registry-and-k3d-dev-workflow.md)
139. [Auditorias periódicas de segurança por terceiros e política em SECURITY.md](../../domains/software-0008/software/devops/linkerd-third-party-security-audits-and-policy.md)
140. [Reuniões do Steering Committee, listas da CNCF e canais comunitários](../../domains/software-0008/software/devops/linkerd-steering-committee-and-community-channels.md)

### Harbor — registro cloud-native de imagens e Helm charts com assinatura, scan e replicação (itens 141–150)

141. [Definição do Harbor como registro cloud-native que armazena, assina e escaneia artefatos](../../domains/software-0008/software/devops/harbor-trusted-cloud-native-registry-overview.md)
142. [Controle de acesso baseado em papéis (RBAC) por projeto e autenticação LDAP/AD e OIDC](../../domains/software-0008/software/devops/harbor-rbac-projects-ldap-and-oidc-identity.md)
143. [Replicação baseada em políticas com filtros, retentativa automática e adaptadores](../../domains/software-0008/software/devops/harbor-policy-based-replication-multi-registry.md)
144. [Scan regular de vulnerabilidades e políticas para impedir o deploy de imagens vulneráveis](../../domains/software-0008/software/devops/harbor-vulnerability-scanning-and-deployment-policies.md)
145. [Exclusão de imagens e jobs de garbage collection para liberar manifests e blobs órfãos](../../domains/software-0008/software/devops/harbor-image-deletion-and-garbage-collection.md)
146. [Portal gráfico, trilha de auditoria de operações e API RESTful com Swagger UI embutido](../../domains/software-0008/software/devops/harbor-portal-auditing-and-restful-swagger-api.md)
147. [Opções de implantação: Docker Compose, Helm Chart (harbor-helm) e Harbor Operator](../../domains/software-0008/software/devops/harbor-deployment-options-docker-compose-helm-operator.md)
148. [Verificação criptográfica de instaladores do Harbor com Cosign a partir da v2.15.0](../../domains/software-0008/software/devops/harbor-cosign-release-signature-verification.md)
149. [Testes de conformidade OCI Distribution e matriz de compatibilidade de adaptadores](../../domains/software-0008/software/devops/harbor-oci-distribution-conformance-and-compatibility.md)
150. [Visão arquitetural na wiki oficial e reuniões comunitárias quinzenais em dois fusos](../../domains/software-0008/software/devops/harbor-architecture-overview-and-community-calls.md)

### Thanos — métricas Prometheus em alta disponibilidade, visão global de consulta e armazenamento ilimitado (itens 151–160)

151. [Definição do Thanos e os três objetivos centrais sobre o Prometheus 2.0](../../domains/software-0008/software/devops/thanos-ha-prometheus-global-query-unlimited-storage.md)
152. [Formato de armazenamento do Prometheus 2.0 e Object Storage como única dependência opcional](../../domains/software-0008/software/devops/thanos-prometheus-2-storage-format-and-object-storage.md)
153. [Visão global de consulta, deduplicação de pares Prometheus HA e federação multi-cluster](../../domains/software-0008/software/devops/thanos-global-query-view-and-ha-deduplication.md)
154. [Downsampling de dados históricos para aceleração massiva de consultas](../../domains/software-0008/software/devops/thanos-downsampling-historical-data-query-speedup.md)
155. [API gRPC Store API simples para acesso unificado a dados e provedores customizados](../../domains/software-0008/software/devops/thanos-grpc-store-api-unified-data-access.md)
156. [Arquiteturas de implantação no Kubernetes: modelo com Sidecar versus modelo com Receive](../../domains/software-0008/software/devops/thanos-sidecar-versus-receive-architectures.md)
157. [Filosofia UNIX e Go no design do Thanos: um binário com subcomandos coesos](../../domains/software-0008/software/devops/thanos-unix-and-golang-design-philosophy.md)
158. [Cadência de releases menores a cada seis semanas e imagens em Quay.io e Docker Hub](../../domains/software-0008/software/devops/thanos-release-cadence-six-weeks-and-container-registries.md)
159. [Documentação de partida: Getting Started, Design, Proposals e Integrations](../../domains/software-0008/software/devops/thanos-design-docs-proposals-and-integrations.md)
160. [Comunidade no CNCF Slack, lista de adotantes em adopters.yml e MAINTAINERS.md](../../domains/software-0008/software/devops/thanos-community-adopters-and-maintainers-governance.md)

### Grafana Loki — agregação de logs multi-tenant indexada por labels no estilo Prometheus (itens 161–170)

161. [Definição do Loki: agregação de logs inspirada no Prometheus que indexa apenas labels](../../domains/software-0008/software/devops/loki-prometheus-inspired-label-indexed-log-aggregation.md)
162. [Correlação direta entre métricas e logs usando os mesmos labels do Prometheus e de Pods Kubernetes](../../domains/software-0008/software/devops/loki-shared-prometheus-and-kubernetes-pod-labels.md)
163. [Pilha de três componentes (Alloy, Loki e Grafana) e transição do Promtail para o Grafana Alloy](../../domains/software-0008/software/devops/loki-three-component-stack-alloy-loki-grafana.md)
164. [Diferença entre o modelo push do Loki e o pull do Prometheus, em binário único ou microsserviços](../../domains/software-0008/software/devops/loki-push-model-and-single-binary-or-microservices.md)
165. [Migração do Helm chart do Grafana Loki em março de 2026 para grafana-community/helm-charts](../../domains/software-0008/software/devops/loki-helm-chart-migration-march-2026.md)
166. [Seções essenciais da documentação: API de ingestão, Labels, Docker Driver Client e Grafana](../../domains/software-0008/software/devops/loki-api-labels-docker-driver-and-grafana-datasource.md)
167. [Operação e verificação: interface de linha de comando LogCLI e monitoramento com Loki Canary](../../domains/software-0008/software/devops/loki-logcli-and-loki-canary-auditing.md)
168. [Compilação a partir do código-fonte em Go e execução local sem dependências](../../domains/software-0008/software/devops/loki-building-from-source-and-local-no-dependencies-mode.md)
169. [Documento original de design do Loki e referências históricas de arquitetura](../../domains/software-0008/software/devops/loki-design-doc-and-architecture-reading.md)
170. [Canais de suporte da comunidade e separação entre issues do Loki e issues de UI no Grafana](../../domains/software-0008/software/devops/loki-community-support-and-grafana-ui-issue-routing.md)

### Fluent Bit — agente de telemetria leve e de alta performance para logs, métricas e traces (itens 171–180)

171. [Definição do Fluent Bit como agente leve para Logs, Métricas e Traces graduado na CNCF](../../domains/software-0008/software/devops/fluentbit-lightweight-telemetry-agent-logs-metrics-traces.md)
172. [Suporte multi-plataforma (Linux, Windows, macOS, BSD e sistemas embarcados) e escala de produção](../../domains/software-0008/software/devops/fluentbit-multi-platform-and-embedded-footprint.md)
173. [Cadência de releases maiores a cada 3–4 meses, série v5.1 e guia MAINTENANCE.md](../../domains/software-0008/software/devops/fluentbit-release-cadence-v5-1-and-maintenance-policy.md)
174. [Arquitetura modular plugável com mais de 70 plugins de Inputs, Filters e Outputs](../../domains/software-0008/software/devops/fluentbit-pluggable-inputs-filters-outputs-architecture.md)
175. [Processamento de streams com consultas SQL para análise e transformação em trânsito](../../domains/software-0008/software/devops/fluentbit-sql-stream-processing-analytics.md)
176. [Rede segura com TLS/SSL, I/O assíncrono e exposição de métricas internas para Prometheus](../../domains/software-0008/software/devops/fluentbit-tls-async-io-and-prometheus-self-monitoring.md)
177. [Extensibilidade poliglota: plugins em C, filtros em Lua e outputs em Go](../../domains/software-0008/software/devops/fluentbit-extensibility-in-c-lua-and-go.md)
178. [Requisitos de compilação (CMake, Flex, Bison, YAML e OpenSSL) e quickstart via CLI](../../domains/software-0008/software/devops/fluentbit-cmake-build-requirements-and-cli-quickstart.md)
179. [Fluxos de CI no GitHub Actions: testes unitários, testes de integração, builds Arm e release](../../domains/software-0008/software/devops/fluentbit-ci-workflows-and-arm-builds.md)
180. [Guia do desenvolvedor, diretrizes de contribuição e canal #fluent-bit no Slack](../../domains/software-0008/software/devops/fluentbit-developer-guide-and-community-channels.md)

### Vector — pipeline de dados de observabilidade ponta a ponta em Rust para agentes e agregadores (itens 181–190)

181. [Definição do Vector como pipeline de dados de observabilidade ponta a ponta construído em Rust](../../domains/software-0008/software/devops/vector-high-performance-rust-observability-pipeline.md)
182. [Os três princípios arquiteturais do Vector: Reliable (Rust), End-to-end (Agent/Aggregator) e Unified](../../domains/software-0008/software/devops/vector-three-principles-reliable-end-to-end-unified.md)
183. [Cinco casos de uso: redução de custos, transição de fornecedores, qualidade e consolidação de agentes](../../domains/software-0008/software/devops/vector-five-use-cases-vendor-transition-and-agent-consolidation.md)
184. [Escala comprovada na comunidade: mais de 100 mil downloads diários e 500 TB/dia no maior usuário](../../domains/software-0008/software/devops/vector-community-scale-500tb-daily-and-production-users.md)
185. [Benchmarks de performance no vector-test-harness: TCP, File e HTTP](../../domains/software-0008/software/devops/vector-performance-benchmarks-test-harness.md)
186. [Testes de corretude: persistência de buffer em disco, rotação de arquivos, truncamento, SIGHUP e JSON](../../domains/software-0008/software/devops/vector-correctness-tests-disk-buffer-logrotate-sighup.md)
187. [Modelo declarativo do pipeline: coleta em sources, processamento em transforms e entrega em sinks](../../domains/software-0008/software/devops/vector-sources-transforms-sinks-pipeline-model.md)
188. [Verificação contínua no repositório: Nightly, Integration/E2E Test Suite e Component Features](../../domains/software-0008/software/devops/vector-ci-workflows-nightly-integration-component-features.md)
189. [Políticas formais do projeto: Releases, Versioning, Security, Privacy e Code of Conduct](../../domains/software-0008/software/devops/vector-policies-releases-versioning-security-privacy.md)
190. [Posicionamento arquitetural: como combinar ou escolher entre Vector, Fluent Bit e OpenTelemetry Collector](../../domains/software-0008/software/devops/vector-choosing-between-vector-fluentbit-and-otelcol.md)

### Skaffold — desenvolvimento contínuo client-side e blocos de CI/CD para aplicações Kubernetes (itens 191–200)

191. [Definição do Skaffold como ferramenta de linha de comando para desenvolvimento contínuo no Kubernetes](../../domains/software-0008/software/devops/skaffold-continuous-development-kubernetes-cli.md)
192. [Ciclo otimizado source-to-deploy, tagueamento baseado em políticas e feedback contínuo](../../domains/software-0008/software/devops/skaffold-source-to-deploy-and-policy-image-tagging.md)
193. [Portabilidade de projeto (`git clone` e `skaffold run`) e perfis sensíveis ao contexto](../../domains/software-0008/software/devops/skaffold-project-portability-and-profiles.md)
194. [Blocos de construção de CI/CD e geração de manifestos hidratados com skaffold render para GitOps](../../domains/software-0008/software/devops/skaffold-cicd-building-blocks-and-skaffold-render-gitops.md)
195. [Descoberta com skaffold init, aplicações multi-componente e arquitetura plugável de build/deploy](../../domains/software-0008/software/devops/skaffold-init-multi-component-and-pluggable-tools.md)
196. [Arquitetura 100% client-side sem componentes instalados nem manutenção no cluster](../../domains/software-0008/software/devops/skaffold-client-side-only-lightweight-architecture.md)
197. [Integração gerenciada com IDEs via extensões Google Cloud Code para VS Code e JetBrains](../../domains/software-0008/software/devops/skaffold-cloud-code-ide-integrations-vscode-jetbrains.md)
198. [Maturidade GA pronta para produção e política formal de depreciação](../../domains/software-0008/software/devops/skaffold-production-readiness-and-deprecation-policy.md)
199. [Catálogo oficial de exemplos no repositório e guia de contribuição](../../domains/software-0008/software/devops/skaffold-examples-catalog-and-contribution-guide.md)
200. [Processo de divulgação de segurança (SECURITY.md), avisos no GitHub e canais da comunidade](../../domains/software-0008/software/devops/skaffold-security-disclosures-and-community-channels.md)

## Tranche 3 — cert-manager, ExternalDNS, Kyverno, OPA Gatekeeper, Falco, KEDA, Karpenter, Envoy Proxy, CoreDNS e etcd (100 notas; revisão factual por IA registrada)

### cert-manager — certificados X.509 e emissores nativos como recursos do Kubernetes

201. [Certificados e emissores de certificados como recursos nativos do Kubernetes](../../domains/software-0008/software/devops/certmanager-x509-certificates-and-issuers-resources.md)
202. [Fontes de emissão suportadas: Let's Encrypt (ACME), HashiCorp Vault, CyberArk e emissão local](../../domains/software-0008/software/devops/certmanager-acme-vault-cyberark-and-in-cluster-sources.md)
203. [Renovação automática antes da expiração para reduzir indisponibilidades e trabalho manual](../../domains/software-0008/software/devops/certmanager-automated-renewal-before-expiry.md)
204. [Guias oficiais para emissão automática de TLS em Ingress (nginx-ingress) e primeiro certificado](../../domains/software-0008/software/devops/certmanager-nginx-ingress-and-getting-started-guides.md)
205. [Requisitos de build em Linux e macOS e convenções de código para contribuidores](../../domains/software-0008/software/devops/certmanager-linux-macos-development-and-coding-conventions.md)
206. [Ausência de garantia de compatibilidade como módulo Go em pkg/ versus estabilidade de APIs Kubernetes](../../domains/software-0008/software/devops/certmanager-go-module-no-compatibility-guarantee.md)
207. [Transição do caminho de importação Go na versão 1.8: jetstack para cert-manager](../../domains/software-0008/software/devops/certmanager-go-import-path-v1-8-transition.md)
208. [Fluxo de troubleshooting oficial e canais #cert-manager e #cert-manager-dev no Slack](../../domains/software-0008/software/devops/certmanager-troubleshooting-and-slack-channels.md)
209. [Relato de vulnerabilidades em SECURITY.md, grupo cert-manager-dev e reuniões públicas](../../domains/software-0008/software/devops/certmanager-security-reporting-and-community-governance.md)
210. [Origem histórica do projeto: evolução a partir do kube-lego e do kube-cert-manager](../../domains/software-0008/software/devops/certmanager-history-kube-lego-and-kube-cert-manager.md)

### ExternalDNS — sincronização agnóstica de Services e Ingresses do Kubernetes com provedores DNS

211. [Sincronização declarativa e agnóstica de recursos Kubernetes com provedores DNS](../../domains/software-0008/software/devops/externaldns-provider-agnostic-kubernetes-dns-sync.md)
212. [Isolamento seguro de zonas não vazias com --domain-filter e --txt-owner-id](../../domains/software-0008/software/devops/externaldns-domain-filter-and-txt-owner-id-safety.md)
213. [Validação prévia com --dry-run e --once e configuração por variáveis EXTERNAL_DNS_*](../../domains/software-0008/software/devops/externaldns-dry-run-once-and-environment-variables.md)
214. [Anotações external-dns.kubernetes.io/hostname e external-dns.kubernetes.io/ttl em Services](../../domains/software-0008/software/devops/externaldns-hostname-and-ttl-service-annotations.md)
215. [Registros DNS apontando para ClusterIP com internal-hostname e --publish-internal-services](../../domains/software-0008/software/devops/externaldns-internal-hostname-and-publish-internal-services.md)
216. [Políticas de ciclo de vida de registros: --policy=sync versus --policy=upsert-only](../../domains/software-0008/software/devops/externaldns-policy-sync-versus-upsert-only.md)
217. [Uso obrigatório de --txt-prefix com registros CNAME e risco de perda de propriedade](../../domains/software-0008/software/devops/externaldns-txt-prefix-cname-conflict-prevention.md)
218. [Precedência da lista externalIPs em clusters bare-metal atrás de NAT ou com MetalLB](../../domains/software-0008/software/devops/externaldns-external-ips-bare-metal-nat-metallb.md)
219. [Arquitetura de provedores via Webhook (PR 3063) e fim de novos provedores in-tree](../../domains/software-0008/software/devops/externaldns-webhook-provider-architecture-pr3063.md)
220. [Verificação prática de resolução com dig +short e escopo de namespaces no FAQ](../../domains/software-0008/software/devops/externaldns-verification-with-dig-and-faq-namespaces.md)

### Kyverno — motor de políticas nativo para Kubernetes, admissão, mutação, geração e segurança da cadeia de suprimentos

221. [Motor de políticas nativo para Kubernetes sem exigir linguagem de programação nova](../../domains/software-0008/software/devops/kyverno-kubernetes-native-policy-engine-overview.md)
222. [As cinco ações do Kyverno: validar, mutar, gerar, limpar recursos e verificar assinaturas de imagens](../../domains/software-0008/software/devops/kyverno-validate-mutate-generate-cleanup-and-image-verify.md)
223. [Limites formais (Non-Goals): vulnerabilidades do API Server e manutenção ativa de políticas](../../domains/software-0008/software/devops/kyverno-non-goals-api-server-flaws-and-explicit-policies.md)
224. [Complementaridade do Kyverno com o RBAC do Kubernetes e com Validating/MutatingAdmissionPolicies](../../domains/software-0008/software/devops/kyverno-complementarity-with-rbac-and-native-admission-policies.md)
225. [Ecossistema de projetos companheiros: Chainsaw, Policy Reporter, Kyverno JSON e Kyverno Envoy Plugin](../../domains/software-0008/software/devops/kyverno-companion-projects-chainsaw-reporter-json-envoy.md)
226. [Casos de uso de Segurança e Conformidade: Pod Security Standards, contextos de segurança e CIS Benchmarks](../../domains/software-0008/software/devops/kyverno-security-compliance-pod-security-and-cis.md)
227. [Excelência operacional e guardrails para desenvolvedores: auto-labeling, NetworkPolicies e probes](../../domains/software-0008/software/devops/kyverno-operational-excellence-and-developer-guardrails.md)
228. [Otimização de custos no cluster: quotas, labels de alocação, tipos de instância e limpeza de recursos](../../domains/software-0008/software/devops/kyverno-cost-optimization-quotas-labels-and-cleanup.md)
229. [Biblioteca oficial de políticas prontas para produção e Kyverno Playground](../../domains/software-0008/software/devops/kyverno-policy-library-and-interactive-playground.md)
230. [SBOM em formato CycloneDX (ghcr.io/kyverno/sbom), SLSA 3 e política de uso de IA em contribuições](../../domains/software-0008/software/devops/kyverno-cyclonedx-sbom-slsa3-and-ai-usage-policy.md)

### OPA Gatekeeper — controle de admissão e auditoria no Kubernetes com Constraint Framework e Rego

231. [Diferenças arquiteturais do Gatekeeper em relação ao OPA clássico com sidecar kube-mgmt](../../domains/software-0008/software/devops/gatekeeper-evolution-beyond-opa-kube-mgmt-sidecar.md)
232. [Uso do OPA Constraint Framework para validação na admissão, auditoria e mutação](../../domains/software-0008/software/devops/gatekeeper-opa-constraint-framework-and-targets.md)
233. [Estrutura do ConstraintTemplate (`templates.gatekeeper.sh/v1`): esquema openAPIV3Schema e código Rego](../../domains/software-0008/software/devops/gatekeeper-constrainttemplate-openapi-schema-and-rego.md)
234. [Instanciação declarativa de Constraints (`constraints.gatekeeper.sh/v1beta1`) e inspeção com kubectl get constraints](../../domains/software-0008/software/devops/gatekeeper-constraint-instantiation-and-listing.md)
235. [Os sete seletores do campo match e suporte a globs baseados em prefixo](../../domains/software-0008/software/devops/gatekeeper-match-field-selectors-and-glob-support.md)
236. [Armadilha de escopo: match vazio (inclusivo para tudo) e impacto sobre recursos Cluster-scoped](../../domains/software-0008/software/devops/gatekeeper-empty-matcher-and-cluster-scoped-gotcha.md)
237. [Validação de tipos de spec.parameters pelo API Server e objeto input.review no Rego](../../domains/software-0008/software/devops/gatekeeper-parameters-validation-and-input-review.md)
238. [Modos de ação em violações (`enforcementAction`): deny, dryrun e warn](../../domains/software-0008/software/devops/gatekeeper-enforcement-action-deny-dryrun-warn.md)
239. [Biblioteca oficial Gatekeeper Policy Library e suporte a dados externos](../../domains/software-0008/software/devops/gatekeeper-policy-library-and-external-data.md)
240. [Governança sob o Código de Conduta da CNCF, processo de segurança e versão do motor OPA](../../domains/software-0008/software/devops/gatekeeper-cncf-governance-security-and-opa-version.md)

### Falco — segurança em tempo de execução (runtime security) no kernel Linux e detecção de ameaças na CNCF

241. [Detecção de comportamento anormal em tempo real no kernel Linux graduada na CNCF](../../domains/software-0008/software/devops/falco-cloud-native-linux-runtime-security-overview.md)
242. [Observação de syscalls no kernel enriquecida com metadados de container runtime e Kubernetes](../../domains/software-0008/software/devops/falco-syscall-monitoring-and-kubernetes-metadata-enrichment.md)
243. [Arquitetura modular da organização falcosecurity: libs, rules, plugins, falcoctl e charts](../../domains/software-0008/software/devops/falco-five-core-repositories-modular-ecosystem.md)
244. [Extensão além de syscalls com falcosecurity/plugins e gerenciamento via falcoctl](../../domains/software-0008/software/devops/falco-plugins-beyond-syscalls-and-falcoctl-management.md)
245. [Recomendações oficiais antes do deploy em produção: compatibilidade, metas, performance e SIEM](../../domains/software-0008/software/devops/falco-production-deployment-checklist-and-setup.md)
246. [Ambiente de demonstração com Docker Compose: Falco, Falcosidekick, Falcosidekick-UI e Redis](../../domains/software-0008/software/devops/falco-demo-environment-falcosidekick-ui-and-redis.md)
247. [Compilação a partir do código-fonte com CMake, driver Modern BPF (`BUILD_FALCO_MODERN_BPF`) e testes](../../domains/software-0008/software/devops/falco-cmake-modern-bpf-build-and-unit-tests.md)
248. [Auditorias independentes em ./audits/ e relato de vulnerabilidades em falco e libs](../../domains/software-0008/software/devops/falco-security-audits-and-vulnerability-reporting.md)
249. [Motivação arquitetural do uso de C++ no motor do Falco e nas bibliotecas de captura](../../domains/software-0008/software/devops/falco-cpp-architecture-and-performance-rationale.md)
250. [Comunidade no Slack #falco, lista cncf-falco-dev e governança em falcosecurity/evolution](../../domains/software-0008/software/devops/falco-community-channels-and-evolution-governance.md)

### KEDA — escalonamento automático orientado a eventos (inclusive até zero) para cargas no Kubernetes

251. [Escalonamento automático fino orientado a eventos — inclusive para e a partir de zero — graduado na CNCF](../../domains/software-0008/software/devops/keda-event-driven-autoscaling-and-scale-to-zero.md)
252. [Integração nativa com o Horizontal Pod Autoscaler na nuvem ou na borda sem dependências externas](../../domains/software-0008/software/devops/keda-hpa-native-integration-cloud-and-edge.md)
253. [Exemplos oficiais de QuickStart: RabbitMQ, Azure Functions, Kafka e ScaledJob](../../domains/software-0008/software/devops/keda-quickstarts-rabbitmq-azure-kafka-and-scaledjob.md)
254. [Métodos oficiais de implantação do KEDA: Helm, Operator Hub e manifestos YAML](../../domains/software-0008/software/devops/keda-deployment-methods-helm-operatorhub-and-yaml.md)
255. [Construção sobre o Operator SDK, dev containers e variáveis GOPROXY e GOSUMDB](../../domains/software-0008/software/devops/keda-operator-sdk-build-and-goproxy-gosumdb.md)
256. [Execução local do operador fora do cluster, geração de certificados em /certs e --zap-log-level](../../domains/software-0008/software/devops/keda-local-operator-outside-cluster-and-certs.md)
257. [Publicação de imagens customizadas (IMAGE_REGISTRY e IMAGE_REPO) e verificação dos pods do KEDA](../../domains/software-0008/software/devops/keda-custom-images-publish-and-pod-log-verification.md)
258. [Pontos de entrada em Go: cmd/operator/main.go e cmd/adapter/main.go](../../domains/software-0008/software/devops/keda-architecture-entrypoints-operator-and-metrics-adapter.md)
259. [Workflows de build principal e testes end-to-end noturnos (TESTING.md)](../../domains/software-0008/software/devops/keda-ci-workflows-and-testing-strategy.md)
260. [Governança em kedacore/governance, política de suporte em keda.sh/support e ROADMAP.md](../../domains/software-0008/software/devops/keda-governance-support-policy-and-roadmap.md)

### Karpenter — provisionamento e consolidação de nós Kubernetes orientados a pods não agendáveis

261. [Ciclo de quatro etapas do Karpenter: Watching, Evaluating, Provisioning e Removing](../../domains/software-0008/software/devops/karpenter-four-step-node-lifecycle-optimization.md)
262. [Avaliação conjunta das cinco restrições de agendamento de pods pelo Karpenter](../../domains/software-0008/software/devops/karpenter-evaluating-five-pod-scheduling-constraints.md)
263. [Provisionamento sem grupos de nós (Groupless Autoscaling) e consolidação de cargas](../../domains/software-0008/software/devops/karpenter-groupless-provisioning-versus-cluster-autoscaler.md)
264. [Arquitetura multi-cloud e as 16 implementações de provedores de nuvem e infraestrutura](../../domains/software-0008/software/devops/karpenter-multi-cloud-provider-implementations.md)
265. [Distinção entre implementações oficiais e comunitárias em provedores como OCI e UpCloud](../../domains/software-0008/software/devops/karpenter-oci-and-upcloud-dual-provider-variants.md)
266. [Extensão do Karpenter para ambientes híbridos e on-premises com Cluster API e Proxmox](../../domains/software-0008/software/devops/karpenter-cluster-api-and-proxmox-hybrid-providers.md)
267. [Automação de atualizações de nós do cluster sem indisponibilidade (Zero Downtime Updates)](../../domains/software-0008/software/devops/karpenter-zero-downtime-node-updates-and-drift.md)
268. [Canais de suporte e design no Slack do Kubernetes: #karpenter versus #karpenter-dev](../../domains/software-0008/software/devops/karpenter-slack-channels-users-versus-developers.md)
269. [Calendário de reuniões do Working Group (quintas) e Issue Triage (segundas) em dois repositórios](../../domains/software-0008/software/devops/karpenter-working-group-and-issue-triage-meetings.md)
270. [Guia de contribuição, issues para iniciantes e Código de Conduta do Kubernetes](../../domains/software-0008/software/devops/karpenter-contributing-guide-and-code-of-conduct.md)

### Envoy Proxy — proxy de borda, intermediário e de serviço em C++ moderno para arquiteturas cloud-native

271. [Definição do Envoy como proxy cloud-native de alta performance para borda, meio e malha de serviços](../../domains/software-0008/software/devops/envoy-cloud-native-edge-middle-service-proxy.md)
272. [Pilares arquiteturais documentados no README: threading model, hot restart, stats e universal data plane API](../../domains/software-0008/software/devops/envoy-core-architecture-threading-hot-restart-stats-xds.md)
273. [Repositórios relacionados: data-plane-api, envoy-perf e envoy-filter-example](../../domains/software-0008/software/devops/envoy-related-repositories-dataplane-api-perf-and-filters.md)
274. [Cinco listas de comunicação oficial e política de resposta no Slack versus envoy-users](../../domains/software-0008/software/devops/envoy-mailing-lists-and-slack-best-effort-policy.md)
275. [Desenvolvimento em C++ moderno, quick start de build/teste via Docker (ci/) e toolchain de suporte](../../domains/software-0008/software/devops/envoy-modern-cpp-contributing-and-docker-ci-quickstart.md)
276. [Reuniões comunitárias duas vezes por mês e regra de cancelamento em 24h sem pauta confirmada](../../domains/software-0008/software/devops/envoy-community-meeting-agenda-cancellation-rule.md)
277. [Auditorias de segurança independentes: Cure53 (2018) e Ada Logics sobre fuzzing (2021)](../../domains/software-0008/software/devops/envoy-third-party-security-audits-cure53-and-adalogics.md)
278. [Canal preferencial de relato de vulnerabilidades via GitHub Security Advisory e SECURITY.md](../../domains/software-0008/software/devops/envoy-vulnerability-reporting-and-security-release-process.md)
279. [Integração contínua com OSS-Fuzz e exclusão da arquitetura ppc64le da política de segurança](../../domains/software-0008/software/devops/envoy-oss-fuzzing-and-ppc64le-security-policy-exclusion.md)
280. [Processo formal de lançamento e governança de versões em RELEASES.md](../../domains/software-0008/software/devops/envoy-release-process-and-lifecycle-governance.md)

### CoreDNS — servidor e encaminhador DNS em Go baseado em cadeia de plugins graduado na CNCF

281. [Servidor e encaminhador DNS em Go baseado em cadeia de plugins graduado na CNCF](../../domains/software-0008/software/devops/coredns-plugin-chained-dns-server-cncf-graduated.md)
282. [Protocolos de transporte DNS suportados: UDP/TCP, DoT (RFC 7858), DoH (RFC 8484), DoH3, DoQ (RFC 9250) e gRPC](../../domains/software-0008/software/devops/coredns-transport-protocols-dot-doh-doh3-doq-grpc.md)
283. [Plugins de autoridade e transferência de zonas: file, auto, secondary (AXFR), dnssec, transfer e loadbalance](../../domains/software-0008/software/devops/coredns-zone-serving-dnssec-axfr-and-loadbalance.md)
284. [Plugins de backend e integração cloud-native: kubernetes, etcd (substituindo SkyDNS), route53, forward e cache](../../domains/software-0008/software/devops/coredns-kubernetes-etcd-route53-and-forward-backends.md)
285. [Plugins de observabilidade, diagnóstico e manipulação: prometheus, log, errors, pprof, rewrite, template, any e dns64](../../domains/software-0008/software/devops/coredns-observability-security-and-query-manipulation-plugins.md)
286. [Compilação a partir do código-fonte (Go 1.26.0+), variável COREDNS_PLUGINS e build via Docker](../../domains/software-0008/software/devops/coredns-source-and-docker-compilation-coredns-plugins-env.md)
287. [Logging operacional estruturado em JSON com -log-format=json e campos time, level, msg e plugin](../../domains/software-0008/software/devops/coredns-json-logging-format-and-structured-fields.md)
288. [Comportamento padrão sem Corefile (plugins whoami e log na porta 53) e substituição com -dns.port](../../domains/software-0008/software/devops/coredns-default-whoami-behavior-and-dns-port-override.md)
289. [Diretiva import com globs e expansão de variáveis {$VARIABLE} como token único no Corefile](../../domains/software-0008/software/devops/coredns-corefile-import-globs-and-env-var-single-token.md)
290. [Verificação contínua com CodeQL, Go Tests, CircleCI e OpenSSF Best Practices](../../domains/software-0008/software/devops/coredns-security-scorecard-and-codeql-verification.md)

### etcd — banco de chave-valor distribuído e consistente via consenso Raft para sistemas críticos

291. [Banco chave-valor distribuído baseado em Raft e os quatro pilares: Simple, Secure, Fast e Reliable](../../domains/software-0008/software/devops/etcd-distributed-raft-key-value-store-pillars.md)
292. [Uso em produção pelo Kubernetes e garantia de confiabilidade com testes de robustez (tests/robustness)](../../domains/software-0008/software/devops/etcd-kubernetes-state-store-and-robustness-testing.md)
293. [Os sete pacotes Go v3 fundamentais do etcd e instalação do cliente go.etcd.io/etcd/client/v3](../../domains/software-0008/software/devops/etcd-v3-go-packages-and-client-library.md)
294. [Portas TCP oficiais registradas na IANA: 2379 para clientes e 2380 para comunicação entre pares](../../domains/software-0008/software/devops/etcd-official-iana-tcp-ports-2379-and-2380.md)
295. [Cluster local de 3 membros (infra1, infra2, infra3), grpc-proxy e nó learner com goreman e Procfile](../../domains/software-0008/software/devops/etcd-local-multi-member-cluster-goreman-procfile-and-learner.md)
296. [Guias operacionais essenciais: clustering multi-máquina, configuração, segurança TLS e tuning](../../domains/software-0008/software/devops/etcd-operational-guides-clustering-security-and-tuning.md)
297. [Binários pré-compilados multi-plataforma (macOS, Linux, Windows e Docker) e cliente etcdctl](../../domains/software-0008/software/devops/etcd-prebuilt-releases-and-etcdctl-cli.md)
298. [Cultura de manutenção em OWNERS e responsabilidades em community-membership.md](../../domains/software-0008/software/devops/etcd-maintainers-culture-and-community-membership.md)
299. [Reuniões semanais às quintas-feiras (11:00 AM PT) alternando comunidade e triagem de issues](../../domains/software-0008/software/devops/etcd-weekly-thursday-meetings-and-issue-triage.md)
300. [Verificação contínua no repositório: workflows de testes, Codecov, CodeQL e OpenSSF Scorecard](../../domains/software-0008/software/devops/etcd-ci-verification-codeql-coverage-and-scorecard.md)

## Tranche 4 — Rook, Longhorn, Cosign, Syft, Grype, BuildKit, Podman, CRI-O, Packer e Terragrunt (100 notas; revisão factual por IA registrada)

### Rook (orquestrador cloud-native de armazenamento Ceph para Kubernetes)

301. [Rook como orquestrador cloud-native de armazenamento Ceph no Kubernetes](../../domains/software-0008/software/devops/rook-orchestrator-for-ceph-on-kubernetes.md)
302. [Versões do Kubernetes v1.31 a v1.37 e arquiteturas amd64 e arm64 suportadas pelo Rook](../../domains/software-0008/software/devops/rook-kubernetes-versions-and-cpu-architectures.md)
303. [Pré-requisitos de dispositivos brutos, partições, LVM e PVs em modo block para OSDs no Rook](../../domains/software-0008/software/devops/rook-raw-devices-lvm-and-block-pvc-prerequisites.md)
304. [Implantação do Rook Operator com crds.yaml, common.yaml, csi-operator.yaml e operator.yaml](../../domains/software-0008/software/devops/rook-operator-deployment-crds-common-and-csi-operator.md)
305. [Manifestos de cluster Rook para bare-metal (cluster.yaml), nuvem dinâmica (cluster-on-pvc.yaml) e teste (cluster-test.yaml)](../../domains/software-0008/software/devops/rook-cluster-manifests-bare-metal-on-pvc-and-test.md)
306. [Arquitetura de pods mon, mgr, osd e plugins CSI no namespace rook-ceph](../../domains/software-0008/software/devops/rook-mon-mgr-osd-and-csi-pods-architecture.md)
307. [Verificação de saúde HEALTH_OK com Rook Toolbox e plugin kubectl rook-ceph](../../domains/software-0008/software/devops/rook-ceph-toolbox-and-kubectl-plugin-verification.md)
308. [Consumo de armazenamento Block (RBD RWO), Shared Filesystem (CephFS RWX) e Object (RGW S3) no Rook](../../domains/software-0008/software/devops/rook-block-rbd-shared-filesystem-cephfs-and-object-rgw.md)
309. [Ceph Dashboard, coletores Prometheus nativos e telemetria anônima no Rook](../../domains/software-0008/software/devops/rook-dashboard-prometheus-monitoring-and-telemetry.md)
310. [Desmontagem limpa (teardown) de clusters Rook e limpeza de metadados nos discos dos hosts](../../domains/software-0008/software/devops/rook-cluster-teardown-and-disk-cleanup-safety.md)

### Longhorn (sistema de armazenamento de bloco distribuído cloud-native para Kubernetes)

311. [Longhorn e arquitetura de controlador dedicado por volume com replicação síncrona](../../domains/software-0008/software/devops/longhorn-distributed-block-storage-microservice-controller.md)
312. [Snapshots incrementais e backups para NFSv4 ou S3 com detecção eficiente de blocos alterados](../../domains/software-0008/software/devops/longhorn-incremental-snapshots-and-change-block-backups.md)
313. [Upgrade automatizado e não disruptivo da pilha de software do Longhorn](../../domains/software-0008/software/devops/longhorn-automated-non-disruptive-software-upgrades.md)
314. [Componentes Longhorn Manager, Instance Manager, Share Manager e Backing Image Manager](../../domains/software-0008/software/devops/longhorn-manager-instance-manager-and-share-manager-components.md)
315. [Motores de dados Longhorn Engine V1 (iSCSI) e Longhorn SPDK Engine V2 (SPDK)](../../domains/software-0008/software/devops/longhorn-v1-engine-iscsi-and-v2-spdk-data-engines.md)
316. [Ciclo de suporte de releases ativas (1.11, 1.12, 1.13) e política de EOL de um ano no Longhorn](../../domains/software-0008/software/devops/longhorn-release-support-window-and-eol-policy.md)
317. [Gerenciamento de imagens base com Longhorn Backing Image Manager](../../domains/software-0008/software/devops/longhorn-backing-image-manager-disk-synchronization.md)
318. [Instalação do Longhorn via kubectl apply, Helm Chart e Rancher App Marketplace](../../domains/software-0008/software/devops/longhorn-installation-methods-kubectl-helm-and-rancher.md)
319. [Operação visual e por linha de comando com Longhorn UI e Longhorn CLI](../../domains/software-0008/software/devops/longhorn-ui-dashboard-and-cli-operations.md)
320. [Coleta de Support Bundle para diagnóstico de bugs e reporte de vulnerabilidades no Longhorn](../../domains/software-0008/software/devops/longhorn-support-bundle-diagnostics-and-security-reporting.md)

### Sigstore Cosign (assinatura e verificação de contêineres OCI, blobs e atestações)

321. [Assinatura keyless de contêineres OCI no Cosign com OIDC, Fulcio e Rekor](../../domains/software-0008/software/devops/cosign-keyless-signing-fulcio-oidc-and-rekor.md)
322. [Obrigatoriedade de assinar imagens pelo digest SHA-256 em vez de tags mutáveis no Cosign](../../domains/software-0008/software/devops/cosign-always-sign-by-digest-not-mutable-tag.md)
323. [Verificação keyless com --certificate-identity e --certificate-oidc-issuer no Cosign](../../domains/software-0008/software/devops/cosign-verify-certificate-identity-and-oidc-issuer.md)
324. [Assinatura e verificação com par de chaves cosign.key/cosign.pub, KMS, hardware tokens e PKI própria](../../domains/software-0008/software/devops/cosign-keypair-kms-and-byo-pki-signing-modes.md)
325. [Verificação offline e air-gapped no Cosign com cosign initialize, cosign save e trusted_root.json](../../domains/software-0008/software/devops/cosign-air-gapped-offline-verification-and-tuf-trusted-root.md)
326. [Assinatura e verificação keyless de arquivos arbitrários com cosign sign-blob, verify-blob e bundles](../../domains/software-0008/software/devops/cosign-sign-blob-and-verify-blob-bundles.md)
327. [Publicação e assinatura de Blobs, Tekton Bundles, módulos WASM e programas eBPF em registros OCI](../../domains/software-0008/software/devops/cosign-oci-registry-artifacts-blobs-tekton-wasm-ebpf.md)
328. [Suporte a atestações in-toto e uso da imagem oficial ghcr.io/sigstore/cosign/cosign](../../domains/software-0008/software/devops/cosign-in-toto-attestations-and-chainguard-container-image.md)
329. [Diagnóstico de falhas de verificação no Cosign: RFC3161 timestamps, Rekor v2 e resiliência de serviços](../../domains/software-0008/software/devops/cosign-troubleshooting-rfc3161-timestamps-and-rekor-v2.md)
330. [Estabilidade da série Cosign 2.x e evolução arquitetural sobre sigstore-go](../../domains/software-0008/software/devops/cosign-sigstore-go-architecture-and-v2-stability-roadmap.md)

### Anchore Syft (geração de Software Bill of Materials SBOM para contêineres e sistemas de arquivos)

331. [Syft como CLI e biblioteca Go para geração de SBOM de contêineres, diretórios e arquivos](../../domains/software-0008/software/devops/syft-sbom-generation-cli-and-go-library.md)
332. [Catalogação multi-ecossistema de pacotes de SO e linguagens de programação no Syft](../../domains/software-0008/software/devops/syft-os-and-language-packaging-ecosystems.md)
333. [Emissão simultânea de múltiplos formatos de SBOM: SPDX, CycloneDX, Syft JSON e tabela](../../domains/software-0008/software/devops/syft-spdx-cyclonedx-and-syft-json-multi-output.md)
334. [Inspeção de pacotes em SPDX e CycloneDX com jq e formatação SYFT_FORMAT_PRETTY=true](../../domains/software-0008/software/devops/syft-jq-inspection-and-pretty-printing-sboms.md)
335. [Escopo padrão squashed versus análise de todas as camadas com --scope all-layers no Syft](../../domains/software-0008/software/devops/syft-squashed-default-versus-all-layers-scope.md)
336. [Criação de atestações de SBOM assinadas segundo a especificação in-toto com Syft](../../domains/software-0008/software/devops/syft-in-toto-signed-sbom-attestations.md)
337. [Execução 100% local sem telemetria externa e enriquecimento opcional com --enrich no Syft](../../domains/software-0008/software/devops/syft-offline-execution-privacy-and-enrich-flag.md)
338. [Autenticação em registros privados e variedade de alvos de scan suportados pelo Syft](../../domains/software-0008/software/devops/syft-private-registry-authentication-and-scan-targets.md)
339. [Integração direta entre Syft e Grype para desacoplar geração de SBOM e scan de vulnerabilidades](../../domains/software-0008/software/devops/syft-seamless-pipeline-integration-with-grype.md)
340. [Verificação de licenças de dependências e conversão entre formatos de SBOM no Syft](../../domains/software-0008/software/devops/syft-license-scanning-and-format-conversion-workflows.md)

### Anchore Grype (scanner de vulnerabilidades para imagens de contêiner, filesystems e SBOMs)

341. [Grype como scanner de vulnerabilidades para imagens de contêiner, diretórios e SBOMs](../../domains/software-0008/software/devops/grype-vulnerability-scanner-for-containers-filesystems-and-sboms.md)
342. [Suporte do Grype a pacotes de sistemas operacionais e dependências de linguagens](../../domains/software-0008/software/devops/grype-os-and-language-specific-package-scanning.md)
343. [Priorização de ameaças e risco no Grype com EPSS, KEV e pontuação de risco (risk scoring)](../../domains/software-0008/software/devops/grype-epss-kev-and-risk-scoring-prioritization.md)
344. [Filtragem e enriquecimento de resultados de scan com suporte a OpenVEX no Grype](../../domains/software-0008/software/devops/grype-openvex-filtering-and-result-augmentation.md)
345. [Varredura ultrarrápida de SBOMs existentes via grype sbom:arquivo ou pipe Unix](../../domains/software-0008/software/devops/grype-fast-sbom-scanning-and-unix-piping.md)
346. [Geração de relatórios de vulnerabilidade em JSON (--output json) com progresso separado em stderr](../../domains/software-0008/software/devops/grype-json-vulnerability-reports-and-stderr-progress.md)
347. [Gerenciamento do banco de dados de vulnerabilidades e operação offline no Grype](../../domains/software-0008/software/devops/grype-vulnerability-database-management-and-offline-scanning.md)
348. [Privacidade estrita no Grype: execução 100% local sem envio de dados externos](../../domains/software-0008/software/devops/grype-strict-local-privacy-zero-external-telemetry.md)
349. [Gates de severidade em pipelines CI/CD e distinção entre vulnerabilidades fixed e not-fixed no Grype](../../domains/software-0008/software/devops/grype-ci-cd-severity-gates-and-fixed-status-filtering.md)
350. [Suporte a registros privados e formatos de imagem Docker, OCI e Singularity no Grype](../../domains/software-0008/software/devops/grype-private-registries-and-singularity-oci-formats.md)

### Moby BuildKit (toolkit concorrente e baseado em LLB para construção de artefatos e imagens OCI)

351. [Representação intermediária binária LLB e resolução concorrente de dependências no BuildKit](../../domains/software-0008/software/devops/buildkit-llb-intermediate-format-and-concurrent-solver.md)
352. [Arquitetura buildkitd e buildctl com workers OCI (runc/crun) e containerd](../../domains/software-0008/software/devops/buildkit-buildkitd-daemon-buildctl-client-and-worker-backends.md)
353. [Frontends extensíveis no BuildKit: dockerfile.v0, gateway.v0 e linguagens alternativas para LLB](../../domains/software-0008/software/devops/buildkit-dockerfile-v0-and-gateway-v0-extensible-frontends.md)
354. [Montagens avançadas RUN --mount=type=(bind, cache, tmpfs, secret, ssh) no BuildKit](../../domains/software-0008/software/devops/buildkit-dockerfile-run-mounts-bind-cache-tmpfs-secret-ssh.md)
355. [Exportação de imagens no BuildKit: compressão gzip/estargz/zstd, oci-mediatypes e SOURCE_DATE_EPOCH](../../domains/software-0008/software/devops/buildkit-image-output-compression-estargz-zstd-and-reproducibility.md)
356. [Exportação de artefatos para diretório local (type=local) e tarballs OCI ou Docker no BuildKit](../../domains/software-0008/software/devops/buildkit-local-directory-and-tarball-outputs.md)
357. [Exportação e importação de cache de build (inline, registry, local, GitHub Actions, S3 e Azure Blob)](../../domains/software-0008/software/devops/buildkit-cache-import-export-inline-registry-local-and-cloud.md)
358. [Coleta de lixo automática (automatic garbage collection) do cache interno no BuildKit](../../domains/software-0008/software/devops/buildkit-automatic-garbage-collection-and-storage-management.md)
359. [Execução rootless do BuildKit sem privilégios de root e implantação em Kubernetes](../../domains/software-0008/software/devops/buildkit-rootless-execution-and-containerized-kubernetes-deployments.md)
360. [Construção de imagens multi-plataforma e rastreamento distribuído com OpenTelemetry no BuildKit](../../domains/software-0008/software/devops/buildkit-multi-platform-builds-and-opentelemetry-tracing.md)

### Podman (gerenciador daemonless e rootless de contêineres OCI, imagens, volumes e pods)

361. [Arquitetura daemonless do Podman baseada na biblioteca libpod e compatibilidade com Docker CLI](../../domains/software-0008/software/devops/podman-daemonless-architecture-and-libpod-lifecycle.md)
362. [Contêineres e pods rootless no Podman com user namespaces e isolamento de privilégios](../../domains/software-0008/software/devops/podman-rootless-containers-and-user-namespaces-security.md)
363. [Gerenciamento nativo de Pods no Podman e integração com manifestos YAML do Kubernetes](../../domains/software-0008/software/devops/podman-pods-shared-resources-and-kubernetes-yaml.md)
364. [Pilha de rede do Podman: Netavark, servidor DNS Aardvark e rede rootless com pasta](../../domains/software-0008/software/devops/podman-netavark-aardvark-dns-and-pasta-networking.md)
365. [Ecossistema de bibliotecas OCI do Podman: crun, runc, conmon, containers/image e containers/storage](../../domains/software-0008/software/devops/podman-oci-runtime-crun-runc-conmon-and-shared-libraries.md)
366. [Relação complementar e diferenças de conceito de contêiner entre Podman e Buildah](../../domains/software-0008/software/devops/podman-buildah-and-podman-specialization-and-storage.md)
367. [Checkpoint e restauração de contêineres em execução no Podman via CRIU](../../domains/software-0008/software/devops/podman-criu-container-checkpoint-and-restore.md)
368. [Execução multiplataforma no Windows e macOS com podman machine e Podman Desktop](../../domains/software-0008/software/devops/podman-podman-machine-and-podman-desktop-multi-os.md)
369. [Cadência trimestral de releases, versões LTS e assinatura PGP no Podman](../../domains/software-0008/software/devops/podman-release-cadence-lts-and-pgp-signed-releases.md)
370. [API REST compatível com Docker e gerenciamento remoto com cliente Podman](../../domains/software-0008/software/devops/podman-rest-api-and-remote-client-management.md)

### CRI-O (implementação leve baseada em OCI da Container Runtime Interface do Kubernetes)

371. [CRI-O como implementação OCI dedicada da Container Runtime Interface (CRI) do Kubernetes](../../domains/software-0008/software/devops/crio-kubernetes-cri-implementation-and-scope.md)
372. [Matriz de compatibilidade CRI-O 1.x.y com o Kubernetes e política de version skew n-2](../../domains/software-0008/software/devops/crio-kubernetes-version-matching-and-n-minus-2-skew-policy.md)
373. [Arquitetura interna do CRI-O: runc, container-libs/image, container-libs/storage e CNI](../../domains/software-0008/software/devops/crio-oci-components-runc-container-libs-and-cni.md)
374. [Arquivos de configuração do CRI-O: crio.conf, policy.json, registries.conf e storage.conf](../../domains/software-0008/software/devops/crio-configuration-files-crio-conf-policy-registries-and-storage.md)
375. [Inspeção de runtime com crio status e API HTTP sobre socket Unix /var/run/crio/crio.sock](../../domains/software-0008/software/devops/crio-http-status-api-and-crio-status-cli.md)
376. [Verificação nativa de assinaturas de imagem no nó Kubernetes com policy.json no CRI-O](../../domains/software-0008/software/devops/crio-signature-verification-policy-json-enforcement.md)
377. [Suporte a OCI Hooks e guia de migração de anotações no CRI-O](../../domains/software-0008/software/devops/crio-oci-hooks-injection-and-annotations-migration.md)
378. [Configuração do Kubelet com CRI-O via endpoint unix:///var/run/crio/crio.sock e systemd cgroup](../../domains/software-0008/software/devops/crio-running-kubernetes-with-crio-socket-and-systemd.md)
379. [Observabilidade do CRI-O com métricas Prometheus, tracing distribuído e Evented PLEG](../../domains/software-0008/software/devops/crio-metrics-tracing-and-evented-pleg-observability.md)
380. [Validação contínua em GitHub Actions e OpenShift Prow e pacotes DEB/RPM do CRI-O](../../domains/software-0008/software/devops/crio-ci-prow-validation-and-packaging-ecosystem.md)

### HashiCorp Packer (construção automatizada e paralela de imagens de máquina idênticas a partir de fonte única)

381. [Packer para construção paralela de imagens de máquina idênticas a partir de configuração única](../../domains/software-0008/software/devops/packer-multi-platform-parallel-machine-image-builder.md)
382. [Arquitetura de integrações via plugins externos no Packer (developer.hashicorp.com/packer/integrations)](../../domains/software-0008/software/devops/packer-external-plugin-integrations-architecture.md)
383. [Rastreamento de ciclo de vida de imagens com HCP Packer Registry e integração com Terraform](../../domains/software-0008/software/devops/packer-hcp-packer-image-metadata-registry-and-terraform.md)
384. [Desenvolvimento e teste local de templates Packer com imagens Docker e Vagrant boxes](../../domains/software-0008/software/devops/packer-local-docker-and-vagrant-box-workflows.md)
385. [Depuração detalhada com PACKER_LOG=1 packer build template.pkr.hcl e revisão de chaves sensíveis](../../domains/software-0008/software/devops/packer-packer-log-debugging-and-secret-sanitization.md)
386. [Política oficial do Packer para plugins comunitários não mantidos e arquivados](../../domains/software-0008/software/devops/packer-unmaintained-and-archived-plugins-policy.md)
387. [Templates HCL2 (template.pkr.hcl) e criação de casos de teste mínimos reproduzíveis no Packer](../../domains/software-0008/software/devops/packer-hcl2-templates-and-reproducible-test-cases.md)
388. [Compilação do Packer a partir do código-fonte com Go >= v1.20 e verificação de binários de PR](../../domains/software-0008/software/devops/packer-building-packer-from-source-and-go-requirements.md)
389. [Repositório unificado de documentação (hashicorp/web-unified-docs) e licença BUSL-1.1 no Packer](../../domains/software-0008/software/devops/packer-unified-documentation-and-license-governance.md)
390. [Fluxo de infraestrutura imutável combinando Golden Images do Packer com provisionamento IaC](../../domains/software-0008/software/devops/packer-immutable-infrastructure-pipeline-with-packer-and-iac.md)

### Terragrunt (orquestrador flexível para escalar código de infraestrutura em OpenTofu e Terraform)

391. [Terragrunt como orquestrador flexível para escalar projetos em OpenTofu e Terraform](../../domains/software-0008/software/devops/terragrunt-orchestration-for-opentofu-and-terraform-at-scale.md)
392. [Configuração terragrunt.hcl, recurso Auto-init e controle de saída com --log-format bare](../../domains/software-0008/software/devops/terragrunt-terragrunt-hcl-auto-init-and-bare-log-format.md)
393. [Unidades (units), módulos compartilhados e eliminação de main.tf redundantes com blocos terraform e inputs](../../domains/software-0008/software/devops/terragrunt-units-shared-modules-and-inputs-blocks.md)
394. [Funcionamento do diretório .terragrunt-cache e uso da função built-in get_terragrunt_dir()](../../domains/software-0008/software/devops/terragrunt-terragrunt-cache-scratch-directory-and-get-terragrunt-dir.md)
395. [Gerenciamento de Stacks e execução concorrente com terragrunt run --all e --non-interactive](../../domains/software-0008/software/devops/terragrunt-stacks-and-concurrent-run-all-execution.md)
396. [Grafo Acíclico Direcionado (DAG) no Terragrunt para ordenação automática de runs na stack](../../domains/software-0008/software/devops/terragrunt-directed-acyclic-graph-dag-and-execution-order.md)
397. [Passagem dinâmica de outputs entre unidades com o bloco dependency no Terragrunt](../../domains/software-0008/software/devops/terragrunt-dependency-blocks-and-dynamic-cross-unit-inputs.md)
398. [Tratamento de dependências ainda não aplicadas durante o plan com mock_outputs e mock_outputs_allowed_terraform_commands](../../domains/software-0008/software/devops/terragrunt-unapplied-dependencies-and-mock-outputs-in-plan.md)
399. [Automação GitOps em CI/CD (plan no PR e apply no merge) e Terragrunt Scale](../../domains/software-0008/software/devops/terragrunt-ci-cd-gitops-workflows-and-terragrunt-scale.md)
400. [Adoção incremental do Terragrunt e uso das fixtures oficiais test/fixtures/docs/01-quick-start](../../domains/software-0008/software/devops/terragrunt-documentation-fixtures-and-incremental-adoption.md)

## Critérios e próximo passo

Cada tranche é auditada antes de ser adicionada ao lote de escala. A aprovação automática verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e links; não certifica a verdade das afirmações. O protocolo atualizado aceita revisão factual humana ou por IA, registradas separadamente. As 400 notas 1–400 das tranches 1–4 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 400/2.000 notas válidas, restando 1600 notas materiais. Continuar em tranches de conteúdo real, sem contar placeholders, IDs ou progresso parcial como conclusão; cada nota deve ter fontes conferidas e relatório de revisão factual.
