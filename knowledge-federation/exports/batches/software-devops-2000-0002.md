# Lote de escala software-devops-2000-0002

- Data de início: 2026-10-03
- Última atualização: 2026-10-03
- Escopo: engenharia de software — DevOps, GitOps, IaC, observabilidade e runtimes cloud-native
- Tamanho-alvo solicitado: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **200 / 2.000 (10,00%)**
- Gate automatizado: **200/200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 2)
- Revisão factual humana: **0/200**
- Revisão factual por IA: **200/200**
- Contabilizadas como válidas: **200/200**
- Revisor das 200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranches 1–2 (200 notas, IDs 1–200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado
- Auditoria reproduzível do gate e links: [`note-quality-software-devops-2000-0002.md`](../reports/note-quality-software-devops-2000-0002.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-02.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-02.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md), [`tranche 2`](../reports/ai-review-software-devops-2000-0002-tranche-02.md)
- Navegação: [`MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)

> **Contagem literal:** 2.000 é a meta deste segundo lote de escala, não a quantidade já criada. Existem 200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1800 restantes. A contagem válida só avança com conteúdo substantivo, fontes específicas, gate aprovado e revisão factual humana ou por IA registrada separadamente.

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

## Critérios e próximo passo

Cada tranche é auditada antes de ser adicionada ao lote de escala. A aprovação automática verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e links; não certifica a verdade das afirmações. O protocolo atualizado aceita revisão factual humana ou por IA, registradas separadamente. As 200 notas 1–200 das tranches 1–2 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 200/2.000 notas válidas, restando 1800 notas materiais. Continuar em tranches de conteúdo real, sem contar placeholders, IDs ou progresso parcial como conclusão; cada nota deve ter fontes conferidas e relatório de revisão factual.
