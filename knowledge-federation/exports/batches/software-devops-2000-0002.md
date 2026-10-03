# Lote de escala software-devops-2000-0002

- Data de início: 2026-10-03
- Última atualização: 2026-10-03
- Escopo: engenharia de software — DevOps, GitOps, IaC, observabilidade e runtimes cloud-native
- Tamanho-alvo solicitado: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **100 / 2.000 (5,00%)**
- Gate automatizado: **100/100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 1)
- Revisão factual humana: **0/100**
- Revisão factual por IA: **100/100**
- Contabilizadas como válidas: **100/100**
- Revisor das 100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranche 1 (100 notas, IDs 1–100) foi conferida factualmente por IA e aprovada sob o protocolo atualizado
- Auditoria reproduzível do gate e links: [`note-quality-software-devops-2000-0002.md`](../reports/note-quality-software-devops-2000-0002.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-devops-2000-0002-tranche-01.md`](../reports/batch-reconciliation-software-devops-2000-0002-tranche-01.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-devops-2000-0002-tranche-01.md)
- Navegação: [`MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)

> **Contagem literal:** 2.000 é a meta deste segundo lote de escala, não a quantidade já criada. Existem 100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1900 restantes. A contagem válida só avança com conteúdo substantivo, fontes específicas, gate aprovado e revisão factual humana ou por IA registrada separadamente.

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

## Critérios e próximo passo

Cada tranche é auditada antes de ser adicionada ao lote de escala. A aprovação automática verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e links; não certifica a verdade das afirmações. O protocolo atualizado aceita revisão factual humana ou por IA, registradas separadamente. As 100 notas 1–100 da tranche 1 têm revisão factual por IA registrada no relatório vinculado. O lote continua incompleto: são 100/2.000 notas válidas, restando 1900 notas materiais. Continuar em tranches de conteúdo real, sem contar placeholders, IDs ou progresso parcial como conclusão; cada nota deve ter fontes conferidas e relatório de revisão factual.
