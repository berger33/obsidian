---
id: moc-seguranca-software-0009
titulo: "MOC — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM"
dominio: software
subdominio: seguranca
lote: software-seguranca-2000-0003
tipo_nota: moc
created: 2026-10-03
updated: 2026-10-04
---

# MOC — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM (`software-0009`)

Mapa de conteúdo das **1700 notas substantivas (Tranches 1–17, IDs `1–1700`)** do lote [`software-seguranca-2000-0003`](../../exports/batches/software-seguranca-2000-0003.md) em `knowledge-federation/domains/software-0009/software/seguranca/`.

## Estado do lote

- Progresso atual: **1700 / 2.000 notas válidas (85,00%)** (`status: in_progress`)
- Revisão factual humana: **0 / 1700**
- Revisão factual por IA (`Arena.ai Agent Mode`): **1700 / 1700** ([Tranche 1](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [Tranche 2](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md), [Tranche 3](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md), [Tranche 4](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md), [Tranche 5](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md), [Tranche 6](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md), [Tranche 7](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md), [Tranche 8](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md), [Tranche 9](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md), [Tranche 10](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md), [Tranche 11](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), [Tranche 12](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md), [Tranche 13](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md), [Tranche 14](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md), [Tranche 15](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md), [Tranche 16](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md), [Tranche 17](../../exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md))
- Auditoria de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../../exports/reports/note-quality-software-seguranca-2000-0003.md)
- Reconciliação mais recente: [`batch-reconciliation-software-seguranca-2000-0003-tranche-17.md`](../../exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-17.md)

## Tranche 1 (IDs 1–100)

### Gitleaks (varredura determinística de segredos em repositórios Git, diretórios e streams, hierarquia `gitleaks.toml`, `[extend]`, `[allowlist]`, `.gitleaksignore` e `--baseline-path`)

- [[gitleaks-arquitetura-deteccao-segredos-git-dir-stdin]] — Gitleaks: arquitetura de detecção rápida de segredos em repositórios `git`, diretórios `dir` e `stdin`
- [[gitleaks-configuracao-toml-precedencia-rules-keywords-entropy]] — Gitleaks `gitleaks.toml`: ordem de precedência da configuração e anatomia de tabelas `rules` (`regex`, `keywords`, `entropy`)
- [[gitleaks-pre-commit-hook-prevencao-commits-locais-skip]] — Gitleaks com `pre-commit`: bloqueio preventivo de segredos na máquina do desenvolvedor antes do `git commit`
- [[gitleaks-allowlists-gitleaksignore-fingerprints-comentarios-allow]] — Gitleaks Controle de Falsos Positivos: `[allowlist]`, comentários `gitleaks:allow` e arquivo `.gitleaksignore` por `Fingerprint`
- [[gitleaks-baseline-scanning-adocao-repositorios-legados-baseline-path]] — Gitleaks Baseline Scanning (`--baseline-path`): adoção incremental em repositórios legados sem bloquear o CI com dívida antiga
- [[gitleaks-decodificacao-recursiva-arquivos-compactados-max-decode-archive-depth]] — Gitleaks Inspeção Profunda: decodificação recursiva (`--max-decode-depth`) e varredura de arquivos compactados (`--max-archive-depth`)
- [[gitleaks-formatos-relatorio-sarif-junit-json-csv-template]] — Gitleaks Relatórios e Integração DevSecOps: geração de saídas `sarif`, `junit`, `json`, `csv` e templates Go (`--report-template`)
- [[gitleaks-allowlist-global-paths-regexes-stopwords-padroes]] — Gitleaks Anatomia da `[allowlist]` Global: exclusão de lockfiles (`go.sum`, `package-lock.json`), binários e `stopwords`
- [[gitleaks-varredura-commits-especificos-git-log-options-ci-pr]] — Gitleaks no CI/CD (`gitleaks git` + opções `git log`): varredura rápida apenas dos commits de um Pull Request
- [[gitleaks-diagnostico-performance-pprof-cpu-mem-trace-betterleaks]] — Gitleaks Diagnóstico de Performance (`--diagnostics`) e Governança: profiling `cpu`/`mem`/`trace`/`http` e evolução para `Betterleaks`

### TruffleHog (descoberta, classificação, validação ativa em tempo real de mais de 800 tipos de credenciais, `trufflehog analyze`, filtros `--results=verified,unknown` e detectores customizados)

- [[trufflehog-arquitetura-discovery-classification-validation-analysis]] — TruffleHog: arquitetura dos 4 pilares (`Discovery`, `Classification`, `Validation` e `Analysis`) para credenciais vazadas
- [[trufflehog-fontes-varredura-git-github-gitlab-s3-gcs-docker-filesystem]] — TruffleHog Fontes de Varredura: inspeção nativa de `git`, `github`, `gitlab`, `s3`, `gcs`, `docker` (camadas OCI) e `filesystem`
- [[trufflehog-verificacao-ativa-credenciais-results-verified-unverified-no-verification]] — TruffleHog Políticas de Verificação: controle de `--results=verified,unknown,unverified` e modo offline `--no-verification`
- [[trufflehog-analise-profunda-credenciais-analyze-iam-permissions]] — TruffleHog Credential Analysis (`trufflehog analyze`): mapeamento de identidade, recursos acessíveis e permissões de chaves vazadas
- [[trufflehog-ci-cd-github-actions-gitlab-ci-since-commit-branch-fail]] — TruffleHog em Pipelines CI/CD: varredura diferencial com `--since-commit`, `--branch` e código de saída `--fail` (`183`)
- [[trufflehog-verificacao-assinatura-cosign-checksums-supply-chain]] — TruffleHog Supply Chain Security: verificação criptográfica de binários e `checksums.txt` com Sigstore `cosign verify-blob`
- [[trufflehog-custom-regex-detectors-webhook-verification-config]] — TruffleHog Custom Detectors (`--config`): criação de detectores Regex customizados com verificação via servidor Webhook
- [[trufflehog-arquitetura-concorrencia-process-flow-chunks-decoders-detectors]] — TruffleHog Arquitetura Interna de Concorrência: pipeline de `Sources`, `Chunks`, `Decoders`, `Aho-Corasick` e `Detectors`
- [[trufflehog-filtros-exclusao-include-paths-exclude-paths-archive-limits]] — TruffleHog Filtragem de Escopo e Limites de Arquivos: `--include-paths`, `--exclude-paths` e controle de archives
- [[trufflehog-varredura-postman-jenkins-elasticsearch-jira-slack-enterprise]] — TruffleHog Além do Git: varredura de `Postman`, `Jenkins`, `Elasticsearch`, `Syslog` e ecossistema colaborativo

### Google OSV-Scanner V2 (análise de composição de software sobre `OSV.dev` e `OSV-Scalibr`, varredura de containers, análise de alcançabilidade *Call Analysis* e remediação guiada `osv-scanner fix`)

- [[osvscanner-arquitetura-osv-dev-osv-scalibr-extracao-matching]] — OSV-Scanner V2: arquitetura em duas fases (*Package Extraction* via `OSV-Scalibr` e *Vulnerability Matching* via `OSV.dev`)
- [[osvscanner-scan-source-lockfiles-sbom-cyclonedx-spdx-git-commits]] — OSV-Scanner `scan source`: varredura de 19+ lockfiles, manifestos SBOM (`CycloneDX`/`SPDX`) e hashes de commits Git (`C/C++`)
- [[osvscanner-scan-image-containers-layer-aware-distros-artifacts]] — OSV-Scanner `scan image`: varredura *layer-aware* de imagens de container (pacotes Alpine/Debian/Ubuntu e artefatos Go/Java/Node/Python)
- [[osvscanner-call-analysis-reachability-go-rust-reducao-falsos-positivos]] — OSV-Scanner Call Analysis (*Reachability*): análise de grafo de chamadas para verificar se a função vulnerável é realmente invocada
- [[osvscanner-guided-remediation-fix-in-place-relax-override-pom-npm]] — OSV-Scanner Guided Remediation (`osv-scanner fix`): estratégias `in-place`, `relax` e `override` para atualização segura de dependências
- [[osvscanner-license-scanning-deps-dev-spdx-allowlist-compliance]] — OSV-Scanner License Scanning (`--licenses`): auditoria de licenças de software livre via `deps.dev` e validação contra allowlist SPDX
- [[osvscanner-offline-scanning-download-offline-databases-air-gapped]] — OSV-Scanner Modo Offline (`--offline-vulnerabilities` e `--download-offline-databases`): operação em redes isoladas e *air-gapped*
- [[osvscanner-configuracao-osv-scanner-toml-ignoredvulns-packageoverrides]] — OSV-Scanner `osv-scanner.toml`: supressão auditável (`IgnoredVulns` com `ignoreUntil`) e sobrescrita (`PackageOverrides`)
- [[osvscanner-formatos-saida-sarif-cyclonedx-html-gh-annotations-pre-commit]] — OSV-Scanner Formatos de Saída (`--format`) e Integração `pre-commit` / GitHub Actions (`sarif`, `cyclonedx-1-5`, `gh-annotations`)
- [[osvscanner-extensibilidade-osv-scalibr-plugins-arquitetura-v2]] — OSV-Scanner e `OSV-Scalibr`: arquitetura modular de extratores e detectores na versão V2

### OWASP Dependency-Track (plataforma contínua API-first de análise de SBOM CycloneDX, correlação de vulnerabilidades com pontuação EPSS, triagem VEX e Policy Engine)

- [[deptrack-arquitetura-owasp-dependency-track-sbom-cyclonedx-api-first]] — OWASP Dependency-Track: arquitetura da plataforma contínua de análise de risco de cadeia de suprimentos baseada em SBOM `CycloneDX`
- [[deptrack-ingestao-sbom-api-rest-bom-upload-ci-cd-auto-create]] — OWASP Dependency-Track Ingestão de SBOM em CI/CD: endpoint `/api/v1/bom`, autenticação `X-Api-Key` e criação automática de projetos
- [[deptrack-vex-vulnerability-exploitability-exchange-cyclonedx-triagem]] — OWASP Dependency-Track e `CycloneDX VEX`: consumo e exportação de *Vulnerability Exploitability Exchange* para triagem auditável
- [[deptrack-fontes-inteligencia-vulnerabilidades-nvd-osv-github-epss]] — OWASP Dependency-Track Inteligência de Vulnerabilidades e `EPSS`: correlação multi-fonte e priorização preditiva de exploração
- [[deptrack-policy-engine-seguranca-licencas-risco-operacional]] — OWASP Dependency-Track Policy Engine: políticas globais e por projeto para risco de segurança, conformidade de licenças e risco operacional
- [[deptrack-impact-analysis-portfolio-busca-componentes-afetados-log4shell]] — OWASP Dependency-Track Portfolio Impact Analysis: resposta imediata a incidentes (*"O que está afetado, e onde?"*) via PURL e CPE
- [[deptrack-monitoramento-servicos-externos-apis-trust-boundary-cyclonedx]] — OWASP Dependency-Track Inventário de Serviços e APIs: rastreamento de provedores externos, classificação de dados e *Trust Boundaries*
- [[deptrack-notificacoes-webhooks-slack-jira-defectdojo-integracoes]] — OWASP Dependency-Track Notificações e Integrações: alertas em tempo real (`Slack`, `Teams`, `Jira`, `Webhooks`) e sincronização com `DefectDojo`
- [[deptrack-autenticacao-oidc-oauth2-ldap-teams-rbac-permissions]] — OWASP Dependency-Track Autenticação e RBAC (`OIDC`, `LDAP`, `API Keys` e *Portfolio Access Control*): governança multi-equipe
- [[deptrack-repositorio-outdated-components-private-vuln-db-operacao-v5]] — OWASP Dependency-Track Risco de Desatualização, Banco Privado de Vulnerabilidades e Evolução Arquitetural (`v4` -> `v5`)

### OWASP ZAP / Zed Attack Proxy (DAST declarativo com Automation Framework YAML, `spider`/`spiderAjax`, importação `openapi`/`graphql`, `passiveScan-wait`, `activeScan`, `alertFilter` e `exitStatus`)

- [[zaproxy-arquitetura-zed-attack-proxy-dast-passive-active-scanner]] — OWASP ZAP (Zed Attack Proxy): arquitetura de proxy interceptador, `Passive Scanner` e `Active Scanner` para DAST
- [[zaproxy-automation-framework-yaml-env-jobs-substituicao-packaged-scans]] — ZAP Automation Framework (`zap.sh -cmd -autorun`): controle declarativo em arquivo YAML único para CI/CD
- [[zaproxy-descoberta-superficie-spider-spiderajax-spiderclient-spas]] — ZAP Crawling e Descoberta (`spider`, `spiderAjax` e `spiderClient`): mapeamento de aplicações tradicionais e SPAs modernas
- [[zaproxy-importacao-schemas-apis-openapi-graphql-soap-postman]] — ZAP Segurança de APIs (`openapi`, `graphql`, `soap` e `postman`): importação de contratos para DAST de APIs REST e GraphQL
- [[zaproxy-autenticacao-browser-auth-autodetect-replacer-bearer-tokens]] — ZAP Autenticação no Automation Framework: `browser` auth, `autodetect` de sessão e injeção de tokens com o job `replacer`
- [[zaproxy-passive-scan-config-passive-scan-wait-fila-assincrona]] — ZAP `passiveScan-config` e `passiveScan-wait`: ajuste de regras passivas e sincronização obrigatória da fila de análise
- [[zaproxy-active-scan-policy-strength-threshold-technologies-tuning]] — ZAP `activeScan`, `activeScan-policy` e `activeScan-config`: sintonia de *Attack Strength*, *Alert Threshold* e tecnologias do alvo
- [[zaproxy-alert-filter-triagem-falsos-positivos-rebaixamento-risco]] — ZAP `alertFilter`: supressão e reklasificação declarativa de falsos positivos por `ruleId`, `url` e `parameter`
- [[zaproxy-job-tests-assertions-exitstatus-report-sarif-quality-gates]] — ZAP Quality Gates em CI/CD: *Job Tests* (`alert`, `stats`, `url`), geração de relatórios (`report`) e `exitStatus`
- [[zaproxy-requestor-sequence-har-import-prune-fluxos-multi-step]] — ZAP Fluxos Multi-Step e Customizados: jobs `requestor`, `sequence-import` (arquivos HAR), `sequence-activeScan` e `prune`

### ProjectDiscovery Nuclei (scanner de vulnerabilidades de alta performance baseado em templates YAML multi-protocolo, workflows condicionais, detecção OAST via Interactsh e exportação SARIF)

- [[nuclei-arquitetura-scanner-vulnerabilidades-templates-yaml-zero-false-positives]] — ProjectDiscovery Nuclei: arquitetura do scanner de vulnerabilidades de alta performance baseado em templates YAML
- [[nuclei-anatomia-template-yaml-info-http-matchers-extractors]] — Nuclei Anatomia de um Template YAML: metadados `info` (`severity`, `classification`, `tags`), `matchers` e `extractors`
- [[nuclei-filtragem-templates-tags-severity-author-template-condition]] — Nuclei Seleção e Filtragem de Templates: `-tags`, `-etags`, `-severity` (`critical,high`), `-tc` (Template Condition) e `-as` (Automatic Scan)
- [[nuclei-multi-protocolo-dns-ssl-tcp-websocket-whois-network-scans]] — Nuclei Além do HTTP: templates multi-protocolo para auditoria de `DNS`, `SSL/TLS`, `TCP`, `WHOIS` e serviços de rede
- [[nuclei-workflows-multi-step-flow-engine-variaveis-dinamicas]] — Nuclei Workflows e `flow:` Engine: orquestração condicional multi-step e encadeamento de variáveis entre requisições
- [[nuclei-interactsh-oast-out-of-band-blind-ssrf-rce-log4shell]] — Nuclei OAST com `Interactsh` (`{{interactsh-url}}`): detecção *Out-of-Band* sem falsos positivos para Blind SSRF, XXE e RCE
- [[nuclei-authenticated-scans-secrets-file-headers-variables-ci-cd]] — Nuclei Varreduras Autenticadas (`-H`, `-var` e arquivo de `secrets` com `pre-condition`): autenticação dinâmica em APIs e aplicações
- [[nuclei-controle-taxa-concorrencia-rate-limit-bulk-size-request-clustering]] — Nuclei Performance, *Request Clustering* e Rate Limiting (`-rl`, `-c`, `-bs`): proteção do alvo e otimização de tráfego
- [[nuclei-headless-browser-dast-fuzzing-code-templates-assinatura]] — Nuclei Modo Headless (`-headless`), Fuzzing DAST (`-dast`) e Assinatura Criptográfica de Templates `code:`
- [[nuclei-relatorios-exportacao-sarif-jsonl-markdown-integracao-jira-github]] — Nuclei Exportação e Integração CI/CD (`-sarif-export`, `-jsonl`, `-markdown-export` e `-rc` Report Config para Jira/GitHub/Splunk)

### OpenFGA (motor de autorização CNCF Incubating inspirado no Google Zanzibar para ReBAC/ABAC, DSL `schema 1.1`/`1.2`, Conditions CEL, APIs `Check`/`ListObjects`, `fga model test` e PostgreSQL)

- [[openfga-arquitetura-cncf-google-zanzibar-rebac-abac-engine]] — OpenFGA: arquitetura CNCF Incubating do motor de autorização ReBAC/ABAC de alta performance inspirado no Google Zanzibar
- [[openfga-conceitos-fundamentais-store-type-object-user-relation-tuple]] — OpenFGA Conceitos Fundamentais: `Store`, `Type`, `Object`, `User` (`userset` e wildcard `*`), `Relation` e `Relationship Tuple`
- [[openfga-configuration-language-dsl-schema-1-1-operadores-or-and-but-not-from]] — OpenFGA Configuration Language (DSL `schema 1.1`): relações diretas, herança hierárquica (`from`) e operadores `or`, `and` e `but not`
- [[openfga-abac-conditions-cel-contextual-tuples-atributos-tempo-execucao]] — OpenFGA ABAC Híbrido: combinação de grafos ReBAC com `Conditions` (Google CEL) e `Contextual Tuples`
- [[openfga-queries-check-batchcheck-listobjects-listusers-expand]] — OpenFGA APIs de Consulta: diferenças e casos de uso entre `Check`, `BatchCheck`, `ListObjects`, `ListUsers` e `Expand`
- [[openfga-testes-unitarios-modelos-fga-model-test-ci-cd]] — OpenFGA Testes Automatizados de Modelos (`fga model test`): validação declarativa de `.fga.yaml` em pipelines de CI/CD
- [[openfga-modular-models-fga-mod-divisao-dominios-equipes]] — OpenFGA Modular Models (`fga.mod`): divisão de modelos de autorização complexos em módulos por equipe e domínio
- [[openfga-armazenamento-producao-postgres-mysql-migrations-read-replicas]] — OpenFGA em Produção (`openfga migrate` e Storage Engines): operação com PostgreSQL/MySQL, conexões e Unix Domain Socket
- [[openfga-performance-caching-consistency-higher-consistency-minimize-latency]] — OpenFGA Consistência e Cache (`ConsistencyPreference`): equilíbrio entre `MINIMIZE_LATENCY` e `HIGHER_CONSISTENCY` (*Zookie* / Problema do Novo Inimigo)
- [[openfga-automacao-terraform-provider-sdks-embedded-go-library]] — OpenFGA Ecossistema e Automação: Terraform Provider (`openfga/openfga`), SDKs oficiais e uso embarcado como biblioteca Go

### AuthZed SpiceDB (banco de dados de permissões distribuído inspirado no Google Zanzibar, linguagem de schema `.zed`, Caveats CEL, consistência `ZedToken`, `zed validate` e cluster dispatch)

- [[spicedb-arquitetura-authzed-google-zanzibar-permissions-database]] — SpiceDB: arquitetura do banco de dados de permissões distribuído inspirado no Google Zanzibar (`spicedb` e CLI `zed`)
- [[spicedb-schema-language-zed-definitions-relations-permissions]] — SpiceDB Schema Language (`.zed`): separação estrita entre `definition`, `relation` (substantivos) e `permission` (verbos computados)
- [[spicedb-operadores-permissao-union-intersection-exclusion-arrows-precedencia]] — SpiceDB Operações de Permissão (`+`, `&`, `-` e `->`): travessia de hierarquias com Arrows e a armadilha de precedência do `+`
- [[spicedb-caveats-abac-relacoes-condicionais-cel-contexto]] — SpiceDB `Caveats`: combinando ReBAC e ABAC com relacionamentos condicionais avaliados em tempo de execução
- [[spicedb-consistencia-zedtoken-zookies-at-least-as-fresh-new-enemy]] — SpiceDB Consistência Global e `ZedToken`: prevenção do *New Enemy Problem* com `at_least_as_fresh`, `minimize_latency` e `fully_consistent`
- [[spicedb-reverse-indexes-lookupresources-lookupsubjects-paginacao]] — SpiceDB Índices Reversos (`LookupResources` e `LookupSubjects`): listagem eficiente de recursos acessíveis e auditoria de sujeitos
- [[spicedb-validacao-testes-schema-zed-validate-assertions-ci]] — SpiceDB Validação e Testes em CI/CD (`zed validate`): arquivos YAML de schema, relacionamentos de teste, `assertions` e `expected_relations`
- [[spicedb-datastores-postgres-cockroachdb-spanner-mysql-migrate]] — SpiceDB Datastores de Produção e `spicedb migrate`: escolha entre `postgres`, `cockroachdb`, `spanner` e `mysql`
- [[spicedb-dispatch-cluster-consistent-hashing-kubernetes-caching]] — SpiceDB Dispatching Distribuído em Cluster Kubernetes: roteamento por *Consistent Hashing* entre réplicas para maximizar Cache Hit
- [[spicedb-watch-api-bulk-import-export-backup-auditoria-eventos]] — SpiceDB `Watch` API e Operações em Massa (`zed backup` / `zed restore` / `zed import`): streaming de mudanças e migração de dados

### Cerbos PDP (Policy Decision Point stateless para autorização PBAC/ABAC/RBAC, os 6 tipos de política YAML, `Derived Roles`, APIs `CheckResources` e `PlanResources` AST, `cerbos compile` e JWKS)

- [[cerbos-arquitetura-stateless-pdp-pbac-abac-rbac-cloud-native]] — Cerbos: arquitetura do Policy Decision Point (`PDP`) stateless para autorização PBAC/ABAC/RBAC declarativa em YAML
- [[cerbos-seis-tipos-politicas-resource-derived-roles-principal-role-export]] — Cerbos Taxonomia das 6 Políticas: `Resource Policies`, `Derived Roles`, `Principal Policies`, `Role Policies`, `Exported Variables` e `Constants`
- [[cerbos-derived-roles-evolucao-rbac-para-abac-condicoes-cel]] — Cerbos `Derived Roles`: evolução limpa de RBAC estático para ABAC contextual usando expressões CEL
- [[cerbos-api-checkresources-batch-avaliacao-multiplos-recursos-acoes]] — Cerbos API `CheckResources`: avaliação em lote de múltiplos recursos e múltiplas ações em uma única requisição
- [[cerbos-api-planresources-query-plan-ast-filtros-banco-orm]] — Cerbos API `PlanResources` (*Query Plan*): geração de AST de filtros (`CONDITIONAL`) para consultas diretas no banco de dados (Prisma/SQLAlchemy/GORM)
- [[cerbos-scoped-policies-hierarquia-multi-tenant-heranca-escopos]] — Cerbos Scoped Policies: herança hierárquica de políticas para SaaS multi-tenant (`acme.corp.uk`) sem duplicar regras
- [[cerbos-compilacao-testes-unitarios-cerbos-compile-schemas-json]] — Cerbos `cerbos compile` e Validação de Schemas: testes unitários de políticas e checagem de tipos de atributos (`schemas`)
- [[cerbos-auxdata-jwt-verificacao-claims-contexto-criptografico]] — Cerbos `auxData` e Verificação Nativa de JWT: uso de claims autenticadas do token diretamente nas expressões de política
- [[cerbos-audit-logs-decision-logs-outputs-mascaramento-campos-sensiveis]] — Cerbos Decision Audit Logs e Policy Outputs: trilha de auditoria de decisões e retorno de obrigações/máscaras para a aplicação
- [[cerbos-implantacao-kubernetes-sidecar-vs-service-storage-git-blob-disk]] — Cerbos Topologias de Deploy e Storage Drivers: `sidecar` vs `service` no Kubernetes e sincronização via `git`, `blob` ou `disk`

### OpenSSF Scorecard (avaliação automatizada de postura de segurança em repositórios open-source e supply chain, `Branch-Protection` em 5 Tiers, `Pinned-Dependencies`, `Token-Permissions` e Probes V5)

- [[scorecard-arquitetura-openssf-avaliacao-seguranca-open-source-supply-chain]] — OpenSSF Scorecard: arquitetura de avaliação automatizada de postura de segurança em repositórios open-source e supply chain
- [[scorecard-check-branch-protection-tiers-1-a-5-code-review]] — OpenSSF Scorecard `Branch-Protection` e `Code-Review`: pontuação em 5 Tiers contra injeção maliciosa na branch principal
- [[scorecard-check-binary-artifacts-reproducible-builds-supply-chain]] — OpenSSF Scorecard `Binary-Artifacts`: detecção de executáveis e binários não revisáveis commitados no repositório de código-fonte
- [[scorecard-checks-token-permissions-dangerous-workflows-github-actions]] — OpenSSF Scorecard `Token-Permissions` e `Dangerous-Workflows`: prevenção de escalação de privilégio e injeção em GitHub Actions
- [[scorecard-check-pinned-dependencies-hash-sha-imutavel-containers-actions]] — OpenSSF Scorecard `Pinned-Dependencies`: fixação de GitHub Actions, imagens Docker e downloads por hash criptográfico SHA
- [[scorecard-checks-signed-releases-packaging-slsa-provenance-cosign]] — OpenSSF Scorecard `Signed-Releases` e `Packaging`: assinatura de artefatos, atestados de proveniência SLSA e pacotes oficiais
- [[scorecard-checks-sast-fuzzing-vulnerabilities-dependency-update-tool]] — OpenSSF Scorecard Código Seguro: checks `SAST`, `Fuzzing`, `Vulnerabilities` (OSV) e `Dependency-Update-Tool`
- [[scorecard-checks-maintained-cii-best-practices-security-policy-license]] — OpenSSF Scorecard Governança e Saúde do Projeto: `Maintained`, `Security-Policy` (`SECURITY.md`), `License` e `CII-Best-Practices`
- [[scorecard-github-action-sarif-code-scanning-badge-monitoramento-continuo]] — OpenSSF Scorecard GitHub Action (`ossf/scorecard-action`): publicação de alertas SARIF no GitHub Code Scanning e Badge oficial
- [[scorecard-probes-structured-results-bigquery-api-rest-avaliacao-escala]] — OpenSSF Scorecard em Escala: *Probes* estruturadas (V5), API REST (`api.scorecard.dev`) e dataset público no BigQuery

## Tranche 2 (IDs 101–200)

### OWASP Coraza WAF (motor de Web Application Firewall em Go, 5 fases de transação HTTP, linguagem SecLang, `SecRuleEngine`, `SecRequestBodyAccess`, `SecAuditLogFormat JSON` e proxy-wasm)

- [[coraza-arquitetura-owasp-waf-go-seclang-compatibilidade-crs-v4]] — OWASP Coraza WAF: arquitetura do Web Application Firewall em Go compatível com `SecLang` e OWASP CRS v4
- [[coraza-ciclo-vida-transacao-cinco-fases-processamento-http]] — Coraza Ciclo de Vida de Transação (`tx`): as 5 fases de avaliação (`Request Headers`, `Request Body`, `Response Headers`, `Response Body`, `Logging`)
- [[coraza-diretivas-seclang-secruleengine-request-response-body-access]] — Coraza Diretivas Essenciais `SecLang`: `SecRuleEngine`, `SecRequestBodyAccess`, `SecResponseBodyAccess` e limites de memória
- [[coraza-audit-logging-secauditengine-parts-abcfhz-formatos-json-ocsf]] — Coraza Audit Logging (`SecAuditEngine`, `SecAuditLogParts` e `SecAuditLogFormat`): saída estruturada em `JSON`, `OCSF` e `Native`
- [[coraza-integracoes-cloud-native-proxy-wasm-envoy-istio-caddy-traefik]] — Coraza em Proxies Cloud-Native: `coraza-proxy-wasm` (Envoy / Istio), `coraza-caddy`, Traefik e HAProxy SPOA
- [[coraza-build-tags-otimizacao-memoization-multiphase-rx-prefilter]] — Coraza Otimização de Performance e Build Tags: memoização de regex/Aho-Corasick, `WAF.Close()`, `SecRxPreFilter` e `no_regex_multiline`
- [[coraza-modo-fips-140-3-restricao-transformacoes-md5-sha1]] — Coraza em Modo `FIPS 140-3` (`GODEBUG=fips140=on`): detecção em tempo de execução e restrição automática de `t:md5` e `t:sha1`
- [[coraza-body-processors-json-xml-urlencoded-multipart-inspecao]] — Coraza Body Processors (`JSON`, `XML`, `URLENCODED`, `MULTIPART`): parsing estruturado de payloads de APIs modernas na Fase 1 e Fase 2
- [[coraza-extensibilidade-plugins-operators-actions-audit-loggers-go]] — Coraza SDK de Extensibilidade (`plugins`): registro de Operadores (`RegisterOperator`), Ações, Transformações e Audit Loggers customizados em Go
- [[coraza-testes-regressao-regras-ftw-go-ftw-playground-ci-cd]] — Coraza Testes de Regressão de WAF (`go-ftw` e Coraza Playground): validação automatizada de regras SecLang em CI/CD

### OWASP Core Rule Set — CRS v4 (conjunto de regras genéricas de detecção para WAFs, *Anomaly Scoring*, `blocking_paranoia_level` vs `detection_paranoia_level`, exclusões e `crs-toolchain`)

- [[owaspcrs-arquitetura-core-rule-set-v4-protecao-owasp-top-ten]] — OWASP CRS (Core Rule Set v4): arquitetura do conjunto de regras de detecção genérica para ModSecurity e Coraza
- [[owaspcrs-anomaly-scoring-mode-collaborative-detection-delayed-blocking]] — OWASP CRS Anomaly Scoring Mode: detecção colaborativa (`setvar`) e bloqueio adiado em `949` (Inbound) e `959` (Outbound)
- [[owaspcrs-thresholds-severidades-critical-error-warning-notice-calibragem]] — OWASP CRS Limiares de Anomalia e Severidades (`CRITICAL=5`, `ERROR=4`, `WARNING=3`, `NOTICE=2`): por que a meta de produção é Threshold `5`
- [[owaspcrs-paranoia-levels-pl1-a-pl4-blocking-vs-detection-paranoia-level]] — OWASP CRS Níveis de Paranoia (`PL1` a `PL4`): uso combinado de `tx.blocking_paranoia_level` e `tx.detection_paranoia_level`
- [[owaspcrs-taxonomia-arquivos-regras-request-911-a-949-response-950-a-959]] — OWASP CRS Taxonomia Numerada de Regras (`901–999`): organização modular de `REQUEST-911..949` e `RESPONSE-950..959`
- [[owaspcrs-tratamento-falsos-positivos-ctl-ruleremovetargetbyid-before-after]] — OWASP CRS Tuning de Falsos Positivos: `ctl:ruleRemoveTargetById` em tempo de execução (`BEFORE-CRS`) vs `SecRuleUpdateTargetById` (`AFTER-CRS`)
- [[owaspcrs-exclusion-packages-pre-construidos-wordpress-nextcloud-dokuwiki]] — OWASP CRS Rule Exclusion Packages e CRS v4 Plugins: perfis oficiais de exclusão para WordPress, Nextcloud, Drupal e cPanel
- [[owaspcrs-validacao-protocolo-http-911-920-metodos-content-type-charset]] — OWASP CRS Políticas de Protocolo HTTP (`900200–900250` e `REQUEST-911`/`920`): restrição de métodos HTTP, `Content-Type` e versões TLS/HTTP
- [[owaspcrs-inspecao-outbound-response-950-a-959-prevencao-vazamento-dados]] — OWASP CRS Inspeção de Resposta Outbound (`RESPONSE-950` a `959`): bloqueio de vazamento de erros SQL, stack traces e web shells
- [[owaspcrs-sampling-percentage-rollout-gradual-crs-setup-900400]] — OWASP CRS Sampling Mode (`tx.sampling_percentage`, Regra `900400`) e `coreruleset-cli`: rollout gradual por amostragem de tráfego

### Ory Hydra (servidor OAuth 2.0 e OpenID Connect Certified headless em Go, arquitetura *Login & Consent Flow* em 6 passos, `prompt=none`, revogação/introspecção RFC 7662 e rotação JWKS)

- [[oryhydra-arquitetura-oauth2-openid-connect-certified-headless-server]] — Ory Hydra: arquitetura do servidor OAuth 2.0 e OpenID Connect Certificado (*OpenID Certified*) desacoplado de banco de usuários
- [[oryhydra-fluxo-login-consent-challenge-verifier-delegacao-ui]] — Ory Hydra Login & Consent Flow: orquestração via `login_challenge`, `consent_challenge` e `skip` com sua própria UI
- [[oryhydra-gerenciamento-oauth2-clients-pkce-auth-methods-scopes]] — Ory Hydra Gerenciamento de OAuth 2.0 Clients: `token_endpoint_auth_method`, obrigatoriedade de `PKCE` e escopos granulares
- [[oryhydra-estrategias-access-token-opaque-vs-jwt-token-introspection-rfc7662]] — Ory Hydra Estratégias de Access Token (`opaque` vs `jwt`) e Token Introspection (`RFC 7662`)
- [[oryhydra-client-credentials-rfc6749-rfc7523-jwt-bearer-m2m]] — Ory Hydra Autenticação Machine-to-Machine (`M2M`): `client_credentials` (`RFC 6749`) e `jwt-bearer` (`RFC 7523`)
- [[oryhydra-jwks-gerenciamento-chaves-assimetricas-rotacao-zero-downtime]] — Ory Hydra Gerenciamento e Rotação de Chaves Criptográficas (`JWKS`): conjuntos `hydra.openid.id-token` e `hydra.jwt.access-token`
- [[oryhydra-oidc-frontchannel-backchannel-logout-revogacao-sessao]] — Ory Hydra Logout Federado OpenID Connect: `RP-Initiated`, `Front-Channel Logout 1.0` e `Back-Channel Logout 1.0`
- [[oryhydra-deteccao-reuso-refresh-token-rotacao-mitigacao-roubo]] — Ory Hydra Segurança de `Refresh Tokens`: rotação automática a cada uso e invalidação de toda a família em caso de *Replay*
- [[oryhydra-operacao-producao-postgres-cockroachdb-migrate-janitor]] — Ory Hydra em Produção: `hydra migrate sql`, limpeza de tokens expirados com `hydra janitor` e escalabilidade stateless
- [[oryhydra-integracao-ory-kratos-arquitetura-idp-completo-drop-in]] — Ory Hydra + Ory Kratos: arquitetura combinada de Identidade (`Kratos`) e Provedor OAuth2/OIDC (`Hydra`) como substituto de Auth0/Okta

### Ory Kratos (sistema cloud-native e headless de gerenciamento de identidades e usuários, JSON Schemas de `traits`, Self-Service Flows `Browser`/`API`, Passkeys/WebAuthn, MFA e Webhooks)

- [[orykratos-arquitetura-api-first-identity-user-management-cloud-native]] — Ory Kratos: arquitetura API-first de gerenciamento de identidades, credenciais e fluxos de autoatendimento (*Self-Service*)
- [[orykratos-modelo-identidade-json-schema-traits-metadata-public-admin]] — Ory Kratos Modelo de Identidade e `JSON Schema`: validação de `traits`, `credentials`, `metadata_public` e `metadata_admin`
- [[orykratos-fluxos-self-service-browser-vs-api-ui-nodes-csrf]] — Ory Kratos Self-Service Flows (`login`, `registration`, `recovery`, `verification`, `settings`): arquitetura *Headless UI Nodes* para Browser e API
- [[orykratos-sessoes-whoami-cookies-session-token-caching-tokenizer]] — Ory Kratos Gerenciamento de Sessões (`/sessions/whoami`): validação por Cookie (`ory_kratos_session`), `X-Session-Token` e conversão para JWT
- [[orykratos-mfa-aal1-aal2-webauthn-passkeys-totp-lookup-secrets]] — Ory Kratos Multi-Factor Authentication (`AAL1` vs `AAL2`): `Passkeys`, `WebAuthn` (FIDO2), `TOTP` e `lookup_secret` (códigos de backup)
- [[orykratos-seguranca-senhas-argon2id-haveibeenpwned-k-anonymity]] — Ory Kratos Segurança de Credenciais `password`: hashing `Argon2id` (ou `bcrypt`), política de similaridade e checagem *Have I Been Pwned* (`k-Anonymity`)
- [[orykratos-recovery-verification-one-time-codes-link-anti-enumeration]] — Ory Kratos Fluxos de `Recovery` e `Verification`: códigos OTP (`code`) vs `link`, `courier` SMTP/HTTP e prevenção de enumeração de contas
- [[orykratos-webhooks-actions-before-after-hooks-jsonnet-sincronizacao]] — Ory Kratos Actions & Webhooks (`before` / `after` hooks): interceptação e enriquecimento de fluxos com templates `Jsonnet`
- [[orykratos-social-sign-in-oidc-federation-jsonnet-data-mapping]] — Ory Kratos Social Sign-In e Federação OIDC: mapeamento de claims de provedores externos (`Google`, `GitHub`, `Microsoft`, `GitLab`) via `Jsonnet`
- [[orykratos-importacao-migracao-identidades-hashes-bcrypt-argon2-pbkdf2]] — Ory Kratos Migração de Identidades sem Reset de Senha (`POST /admin/identities`): importação de hashes `bcrypt`, `argon2`, `pbkdf2` e `scrypt`

### Authelia (portal open-source de Single Sign-On e 2FA/WebAuthn acoplado a Reverse Proxies, motor de Access Control em 7 dimensões de especificidade, `bypass`/`one_factor`/`two_factor` e OIDC)

- [[authelia-arquitetura-portal-autenticacao-autorizacao-forwardauth-oidc]] — Authelia: arquitetura do servidor open-source de autenticação, 2FA, controle de acesso (`ForwardAuth`) e provedor OpenID Connect 1.0
- [[authelia-access-control-policies-deny-bypass-one-factor-two-factor]] — Authelia `access_control`: políticas `deny`, `bypass`, `one_factor` e `two_factor` e avaliação sequencial *first-match*
- [[authelia-criterios-regras-domain-regex-resources-subject-methods-query]] — Authelia Critérios Granulares de Regra: `domain`, `domain_regex`, `resources`, `subject` (`AND`/`OR`), `methods` e `query`
- [[authelia-teste-politicas-cli-access-control-check-policy-ci]] — Authelia `authelia access-control check-policy`: validação determinística de regras de autorização na linha de comando e CI/CD
- [[authelia-backends-autenticacao-ldap-active-directory-file-argon2id]] — Authelia Backends de Autenticação (`authentication_backend`): integração com `LDAP` (Active Directory / OpenLDAP / FreeIPA) e `file` (`Argon2id`)
- [[authelia-mfa-webauthn-passkeys-totp-duo-push-configuracao]] — Authelia Segundo Fator (`2FA`): configuração de `WebAuthn` (FIDO2 / YubiKey / Passkeys), `TOTP` e notificações `Duo Push`
- [[authelia-session-redis-sentinel-cluster-storage-postgres-encryption-key]] — Authelia Sessões e Persistência de Produção: `session.redis` (HA Sentinel/Cluster) e `storage.postgres` com `encryption_key`
- [[authelia-regulation-protecao-forca-bruta-max-retries-find-time-ban-time]] — Authelia `regulation`: proteção integrada contra ataques de força bruta com `max_retries`, `find_time` e `ban_time`
- [[authelia-openid-connect-provider-clients-authorization-policies-pkce]] — Authelia como Provedor OpenID Connect 1.0 (`identity_providers.oidc`): proteção de aplicações nativas OIDC (Grafana, Argo CD, GitLab)
- [[authelia-gestao-segredos-variaveis-ambiente-file-filters-templates-k8s]] — Authelia Gestão Segura de Segredos (`_FILE` e Templates): injeção de credenciais via arquivos Kubernetes Secrets sem expor texto claro

### FiloSottile `age` (ferramenta, formato `age-encryption.org/v1` e biblioteca Go `filippo.io/age` para criptografia moderna de arquivos com `X25519`, `ChaCha20-Poly1305` `STREAM`, chaves SSH, `scrypt` e plugins)

- [[agecrypt-arquitetura-filosottile-age-criptografia-arquivos-x25519-chacha20]] — FiloSottile `age`: arquitetura da ferramenta e formato moderno de criptografia de arquivos (`X25519`, `ChaCha20-Poly1305` e `STREAM`)
- [[agecrypt-chaves-nativas-age-keygen-bech32-multiplos-destinatarios-recipients-file]] — `age` Gerenciamento de Chaves (`age-keygen`) e Múltiplos Destinatários (`-r` e `-R recipients.txt`)
- [[agecrypt-criptografia-chaves-ssh-ed25519-rsa-github-keys]] — `age` Criptografia para Chaves SSH Existentes (`ssh-ed25519` e `ssh-rsa`): envio seguro usando `~/.ssh/id_ed25519.pub` ou `github.com/<user>.keys`
- [[agecrypt-passphrase-scrypt-protecao-chaves-identidade-em-repouso]] — `age` Criptografia por Passphrase (`-p` / `--passphrase` com `scrypt`) e Identidades Protegidas por Senha
- [[agecrypt-ascii-armor-pem-strict-base64-protecao-tty]] — `age` ASCII Armor (`-a` / `--armor`): codificação PEM canônica estrita (`AGE ENCRYPTED FILE`) e proteção de TTY
- [[agecrypt-criptografia-simetrica-com-arquivo-identidade-encrypt-i]] — `age` Criptografia Simétrica para Arquivo de Identidade (`age --encrypt -i key.txt`): backups sem gerenciar chave pública separada
- [[agecrypt-plugins-hardware-yubikey-fido2-kms-arquitetura-extensivel]] — `age` Sistema de Plugins (`age-plugin-*` e `-j`): chaves em hardware com `age-plugin-yubikey`, Secure Enclave e TPM
- [[agecrypt-suporte-pos-quantico-pq-ml-kem-x25519-especificacao-c2sp]] — `age` Criptografia Pós-Quântica Híbrida e Verificação de Binários com `Sigsum`: proteção contra *Harvest Now, Decrypt Later*
- [[agecrypt-biblioteca-go-filippo-io-age-encrypt-decrypt-streams]] — `age` como Biblioteca Nativa em Go (`filippo.io/age`): `age.Encrypt`, `age.Decrypt` e `armor` em aplicações sem processos externos
- [[agecrypt-integracao-gitops-sops-flux-argocd-chezmoi-pass]] — `age` em Pipelines GitOps e Dotfiles: integração com `SOPS` (`SOPS_AGE_KEY_FILE`), `Flux CD`, `Argo CD`, `passage` e `chezmoi`

### OWASP DefectDojo (plataforma open-source de ASPM e gestão unificada de vulnerabilidades com 500+ parsers, hierarquia `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding`, `reimport-scan` e deduplicação)

- [[defectdojo-arquitetura-owasp-aspm-vulnerability-management-500-parsers]] — OWASP DefectDojo: arquitetura da plataforma open-source de ASPM e gestão unificada de vulnerabilidades com 500+ parsers
- [[defectdojo-modelo-hierarquico-product-type-product-engagement-test-finding]] — DefectDojo Modelo de Dados Hierárquico: `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding` e `Endpoint`
- [[defectdojo-api-v2-import-scan-vs-reimport-scan-ciclo-vida-ci-cd]] — DefectDojo `import-scan` vs `reimport-scan`: automação de pipelines CI/CD com fechamento automático de vulnerabilidades corrigidas
- [[defectdojo-deduplicacao-algoritmos-hash-code-unique-id-from-tool]] — DefectDojo Algoritmos de Deduplicação (`HASH_CODE`, `UNIQUE_ID_FROM_TOOL`, `LEGACY`): eliminação de duplicatas intra-scanner e cross-scanner
- [[defectdojo-triagem-findings-verified-false-positive-out-of-scope-risk-acceptance]] — DefectDojo Fluxo de Triagem e `Risk Acceptance`: estados `Active`, `Verified`, `False Positive`, `Out of Scope` e Aceite Formal de Risco
- [[defectdojo-sla-configuration-enforcement-severidade-notificacoes-atraso]] — DefectDojo SLA Engine (`SLA Configuration`): prazos de remediação por severidade (`Critical`, `High`, `Medium`, `Low`) e alertas de violação
- [[defectdojo-integracao-bidirecional-jira-sincronizacao-status-comentarios]] — DefectDojo Integração Bidirecional com Jira: criação automática de Issues, sincronização de comentários e fechamento por resolução
- [[defectdojo-arquitetura-servicos-nginx-uwsgi-celery-beat-worker-postgres-redis]] — DefectDojo Arquitetura de Produção: papéis dos componentes `nginx`, `uwsgi` (Django), `celeryworker`, `celerybeat`, `postgres` e `redis`/`valkey`
- [[defectdojo-universal-parser-sarif-conectores-customizados-ingestao]] — DefectDojo Ingestão Universal: uso nativo de relatórios `SARIF` e criação de parsers customizados para ferramentas internas
- [[defectdojo-rbac-product-members-groups-sso-oidc-saml-governanca]] — DefectDojo Governança de Acesso (`RBAC`, `Product Type Members` e `SSO` OIDC/SAML/LDAP): isolamento de visibilidade por equipe

### Prowler (plataforma open-source de Cloud Security Posture Management — CSPM multi-cloud para AWS, Azure, GCP, Kubernetes, M365 e GitHub, *Attack Paths* com Cartography/Neo4j, `Mutelist` e saída OCSF)

- [[prowler-arquitetura-open-cloud-security-platform-cspm-multi-cloud]] — Prowler: arquitetura da plataforma open-source de segurança e conformidade multi-cloud (`AWS`, `Azure`, `GCP`, `Kubernetes`, `M365`, `GitHub`)
- [[prowler-compliance-frameworks-cis-nist-pci-dss-soc2-iso27001-nis2-ens]] — Prowler Frameworks de Conformidade (`--compliance`) e `Prowler ThreatScore`: auditoria automatizada `CIS`, `NIST`, `PCI-DSS`, `SOC2`, `ISO 27001` e `MITRE ATT&CK`
- [[prowler-attack-paths-cartography-neo4j-amazon-neptune-grafos]] — Prowler `Attack Paths`: análise de caminhos de ataque combinando inventário `Cartography` com achados do Prowler em `Neo4j` ou `Amazon Neptune`
- [[prowler-selecao-granular-checks-services-severities-categories-regions]] — Prowler Filtragem Granular de Execução: `--checks`, `--services`, `--severity`, `--category` e `--region` / `--excluded-checks`
- [[prowler-mutelist-yaml-supressao-excecoes-accounts-regions-resources-tags]] — Prowler `Mutelist` (`-w` / `--mutelist-file`): gerenciamento declarativo de exceções por conta, região, check, recurso e tags
- [[prowler-auditoria-kubernetes-clusters-kubeconfig-in-cluster-rbac-pss]] — Prowler para Kubernetes (`prowler kubernetes`): auditoria CIS Kubernetes Benchmark, RBAC, Pod Security e NetworkPolicies
- [[prowler-saas-github-m365-googleworkspace-okta-iac-containers]] — Prowler SaaS, IaC e Containers (`github`, `m365`, `googleworkspace`, `okta`, `iac`, `image`): postura unificada além da IaaS
- [[prowler-formatos-saida-ocsf-asff-security-hub-s3-defectdojo]] — Prowler Formatos de Saída (`json-ocsf`, `json-asff`, `html`, `csv`) e Integração Nativa com `AWS Security Hub` e `S3`
- [[prowler-multi-account-aws-organizations-assume-role-azure-subscriptions-gcp]] — Prowler Varreduras Multi-Conta em Escala: `AWS AssumeRole` (`-R`), `AWS Organizations` (`-O`), Subscrições Azure e Projetos GCP
- [[prowler-custom-checks-python-metadata-guidelines-prowler-mcp-ai]] — Prowler Extensibilidade: criação de Checks Customizados (`--checks-folder`), `Check Metadata Guidelines` e servidor `Prowler MCP`

### osquery (instrumentação e monitoramento de sistema operacional orientado a SQL para Linux, macOS e Windows, `osqueryi` vs `osqueryd`, logs diferenciais via RocksDB, `Query Packs`, `FIM` e `Watchdog`)

- [[osquery-arquitetura-sistema-operacional-banco-relacional-sql-sqlite]] — osquery: arquitetura do framework que expõe o sistema operacional (`Linux`, `macOS`, `Windows`) como um banco relacional SQL
- [[osquery-osqueryi-vs-osqueryd-shell-interativo-daemon-agendamento]] — osquery `osqueryi` vs `osqueryd`: exploração interativa ad-hoc versus monitoramento contínuo agendado por daemon
- [[osquery-differential-logs-added-removed-vs-snapshot-queries-rocksdb]] — osquery Logs Diferenciais (`added` / `removed` via RocksDB) vs `snapshot: true`: como o `osqueryd` detecta mudanças de estado sem inundar o SIEM
- [[osquery-query-packs-organizacao-modular-discovery-queries-platform-version]] — osquery `Query Packs`: agrupamento modular de queries de detecção com filtros `platform`, `version`, `shard` e `discovery`
- [[osquery-evented-tables-file-integrity-monitoring-fim-process-socket-events]] — osquery Evented Tables e File Integrity Monitoring (`FIM`): captura em tempo real via `auditd`/`ebpf`/`inotify`/`EndpointSecurity`
- [[osquery-watchdog-protecao-recursos-cpu-memoria-denylist-queries]] — osquery Resource Watchdog e Auto-Denylist: garantia de que o agente nunca degrade a CPU ou a memória do host de produção
- [[osquery-auditoria-containers-docker-namespaces-systemd-linux-secops]] — osquery para Segurança de Containers e Servidores Linux: tabelas `docker_containers`, `docker_images`, `process_namespaces` e `iptables`
- [[osquery-gerenciamento-frota-tls-enrollment-fleet-osctrl-zentral]] — osquery Gerenciamento Centralizado de Frota (`TLS Enrollment`, `Fleet`, `osctrl` e `Zentral`): distribuição remota de configuração e Live Queries
- [[osquery-integracao-yara-tabelas-yara-yara-events-varredura-memoria-arquivos]] — osquery + `YARA` (`yara` e `yara_events`): busca de assinaturas de malware sob demanda e acoplada ao File Integrity Monitoring
- [[osquery-extensoes-thrift-sdk-go-python-logger-plugins-aws-kinesis-kafka]] — osquery Extensions (`Thrift` API) e Logger Plugins (`filesystem`, `syslog`, `aws_kinesis`, `aws_firehose`, `kafka_producer`)

### OISF Suricata (motor multi-threaded de alta performance para `IDS`, `IPS` inline e `Network Security Monitoring — NSM`, telemetria unificada `eve.json`, `suricata-update`, *Sticky Buffers*, `JA3`/`JA4` e `file-store`)

- [[suricata-arquitetura-oisf-network-ids-ips-nsm-multithreaded]] — OISF Suricata: arquitetura multi-thread de alta performance para `IDS`, `IPS` e `Network Security Monitoring (NSM)`
- [[suricata-eve-json-log-unificado-alert-flow-dns-http-tls-fileinfo]] — Suricata `EVE JSON` (`eve.json`): telemetria unificada de alertas, fluxos (`flow`), `dns`, `http`, `tls`, `ssh`, `smb` e `fileinfo`
- [[suricata-gerenciamento-regras-suricata-update-et-open-fontes]] — Suricata Gerenciamento de Regras (`suricata-update`): atualização automatizada do *Emerging Threats Open (ET Open)* e tuning via `enable.conf`/`disable.conf`/`modify.conf`
- [[suricata-anatomia-regras-assinaturas-sticky-buffers-http-dns-tls]] — Suricata Linguagem de Regras e *Sticky Buffers*: escrita de assinaturas de camada 7 (`http.uri`, `http.user_agent`, `dns.query`, `tls.sni`)
- [[suricata-inspecao-tls-fingerprinting-ja3-ja4-sni-certificados-c2]] — Suricata Inspeção de Tráfego Criptografado TLS: fingerprinting de clientes/servidores (`JA3`, `JA3S`, `JA4`), `tls.sni` e certificados X.509
- [[suricata-modo-ips-inline-af-packet-nfqueue-acao-drop-reject]] — Suricata em Modo IPS Inline (`AF_PACKET` Layer 2 Bridge e `NFQUEUE`): bloqueio ativo de ataques com ações `drop` e `reject`
- [[suricata-file-extraction-file-store-sha256-deteccao-malware-rede]] — Suricata File Extraction e Hashing (`file-store` v2 e `fileinfo`): cálculo de SHA-256 em tempo real e captura forense de arquivos trafegados
- [[suricata-tuning-performance-runmodes-workers-af-packet-ebpf-hyperscan]] — Suricata Performance Multi-Gigabit (`runmode: workers`, `AF_PACKET`, `eBPF` Bypass e `Hyperscan`): eliminação de perda de pacotes (`kernel_drops`)
- [[suricata-analise-offline-pcap-replay-regressao-ci-unix-socket]] — Suricata Análise Forense de `PCAP` (`-r`) e Automação via Unix Socket (`suricatasc`): processamento em lote de capturas de tráfego
- [[suricata-datasets-thresholding-suppress-rate-filter-correlacao-ioc]] — Suricata `Datasets`, `Thresholds`, `Suppress` e `Flowbits`: correlação de estado entre pacotes, listas dinâmicas e controle de ruído

## Tranche 3 (IDs 201–300)

### Zeek Network Security Monitor (arquitetura em duas camadas *Event Engine* e *Script Interpreter*, logs transacionais interligados por `uid`/`fuid`, `FAF`, `Notice`, `Intel`, `Spicy`, `zkg` e `SumStats`)

- [[zeeknsm-arquitetura-event-engine-script-interpreter-nsm]] — Zeek Network Security Monitor: arquitetura em duas camadas (*Event Engine* e *Script Interpreter*) para análise semântica de rede
- [[zeeknsm-logs-transacionais-conn-dns-http-ssl-files-x509-uid]] — Zeek Logs Transacionais e Correlação por `uid` (`conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log`): pivotamento forense no SOC
- [[zeeknsm-linguagem-scripts-eventos-tipos-nativos-addr-subnet-port-table]] — Zeek Scripting Language: programação orientada a eventos com tipos nativos de rede (`addr`, `subnet`, `port`, `interval`, `set` e `table`)
- [[zeeknsm-file-analysis-framework-faf-extracao-arquivos-hashing-mime]] — Zeek File Analysis Framework (`FAF`): dissecção agnóstica de protocolo, detecção de MIME (`file_sniff`) e cálculo de hashes (`MD5`, `SHA1`, `SHA256`)
- [[zeeknsm-notice-framework-alertas-notice-log-action-alarm-hook]] — Zeek Notice Framework (`notice.log`): geração de alertas contextuais (`NOTICE`), deduplicação por `suppress_for` e hooks de resposta
- [[zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif]] — Zeek Intelligence Framework (`intel.log`): ingestão em tempo real de Indicadores de Comprometimento (`ADDR`, `DOMAIN`, `URL`, `FILE_HASH`, `CERT_HASH`)
- [[zeeknsm-arquitetura-cluster-zeekctl-manager-logger-proxy-workers]] — Zeek Arquitetura de Cluster (`zeekctl` / `node.cfg`): papéis de `Manager`, `Logger`, `Proxy` e `Workers` com `AF_PACKET` e `lb_procs`
- [[zeeknsm-spicy-parser-generator-gramaticas-seguras-protocolos-arquivos]] — Zeek `Spicy`: gerador moderno de parsers seguros em C++ para protocolos de rede e formatos de arquivo customizados
- [[zeeknsm-package-manager-zkg-ja3-ja4-bzar-mitre-attack-extensoes]] — Zeek Package Manager (`zkg`): instalação de pacotes comunitários (`JA3`, `JA4`, `MITRE ATT&CK BZAR`, `hassh`, `cve-detectors`)
- [[zeeknsm-summary-statistics-sumstats-deteccao-anomalias-scans-exfiltracao]] — Zeek `SumStats` (Summary Statistics Framework): agregação estatística distribuída para detectar Port Scans, DGA e Beaconing

### CNCF KubeArmor (sistema cloud-native de segurança em runtime com bloqueio inline via Linux Security Modules `AppArmor`/`BPF-LSM`/`SELinux` e telemetria `eBPF`, CRDs `ksp`/`csp`/`hsp` e CLI `karmor`)

- [[kubearmor-arquitetura-cncf-runtime-security-enforcement-lsm-ebpf]] — CNCF KubeArmor: arquitetura de segurança em runtime com bloqueio inline no kernel via `Linux Security Modules (LSMs)` e `eBPF`
- [[kubearmor-crd-kubearmorpolicy-especificacao-selector-process-file-network]] — KubeArmor `KubeArmorPolicy` (`ksp`): anatomia da política para Pods/Containers (`selector`, `process`, `file`, `network`, `capabilities`, `action`)
- [[kubearmor-restricao-processos-fromsource-owneronly-recursive]] — KubeArmor Controle Fino de Execução de Processos: `fromSource`, `ownerOnly` e `matchDirectories` recursivos
- [[kubearmor-protecao-arquivos-sensi-readonly-fromsource-serviceaccount-token]] — KubeArmor Proteção de Arquivos e Segredos (`file`): `readOnly: true`, vínculo `fromSource` e blindagem do Token da ServiceAccount
- [[kubearmor-restricao-rede-capabilities-socket-icmp-tcp-udp-por-processo]] — KubeArmor Controle de Rede (`network`) e Linux Capabilities (`capabilities`) por Executável (`fromSource`)
- [[kubearmor-politicas-default-posture-allow-whitelist-least-permissive]] — KubeArmor Postura *Zero-Trust Whitelisting* (`action: Allow` + `kubearmor-file-posture` / `kubearmor-Visibility`): modelo de privilégio mínimo
- [[kubearmor-cluster-security-policy-csp-governanca-multi-namespace]] — KubeArmor `KubeArmorClusterPolicy` (`csp`): políticas de segurança em nível de cluster através de múltiplos namespaces
- [[kubearmor-host-security-policy-hsp-protecao-nodes-vms-systemd-kubelet]] — KubeArmor `KubeArmorHostPolicy` (`hsp`): hardening de Nós Kubernetes e Servidores Linux Bare-Metal/VM
- [[kubearmor-cli-karmor-logs-profile-recommend-telemetria-tempo-real]] — KubeArmor CLI (`karmor`): streaming de telemetria e alertas (`karmor logs`), perfilamento (`karmor profile`) e `karmor recommend`
- [[kubearmor-matriz-lsm-bpf-lsm-apparmor-selinux-gke-eks-aks]] — KubeArmor Matriz de LSMs (`BPF-LSM` vs `AppArmor` vs `SELinux`): escolha de sistema operacional de nó em `EKS`, `GKE`, `AKS` e `RKE`

### Aqua Security Tracee (segurança em runtime e investigação forense para Linux e Kubernetes com `eBPF`, arquitetura *Everything is an Event*, políticas CRD/YAML, captura forense e modelo de segurança)

- [[tracee-arquitetura-aqua-security-ebpf-runtime-security-forensics]] — Aqua Security Tracee: arquitetura unificada *"Everything is an Event"* para segurança em runtime e forense com `eBPF`
- [[tracee-policies-yaml-kubernetes-crd-vs-plain-format-64-policies]] — Tracee Políticas de Detecção (`Policies`): intercambiabilidade entre formato `Kubernetes CRD` (`tracee.aquasec.com/v1beta1`) e `Plain YAML`
- [[tracee-policy-scopes-container-not-container-tree-pid-executable]] — Tracee Escopos de Política (`scope`): filtragem no kernel por `container`, `host`, árvore de processos (`tree`), `executable` e `uid`
- [[tracee-event-filters-data-args-retval-context-operators-prefix-suffix]] — Tracee Filtros de Eventos (`rules[].filters`): operadores sobre `data.*`, `retval`, `uid`, `comm` e wildcards `*` de prefixo/sufixo
- [[tracee-built-in-security-events-signatures-fileless-rootkit-escape]] — Tracee Assinaturas de Segurança Embutidas: detecção de execução *Fileless* (`mem_prot_alert`), *Rootkits* (` hooked_syscall`), `anti_debugging` e Escape
- [[tracee-forensic-capture-artifacts-executables-memory-pcap-files]] — Tracee Captura Forense Automática (`--capture` / `output.artifacts`): coleta de binários executados, dumps de memória, arquivos e `PCAP`
- [[tracee-eventos-rede-ebpf-dns-http-net-packet-flow-visibilidade]] — Tracee Visibilidade de Rede via eBPF (`net_packet_dns`, `net_packet_http`, `net_flow_tcp_begin`): inspeção sem proxy ou sidecar
- [[tracee-assinaturas-customizadas-golang-cel-extensibilidade-deteccao]] — Tracee Criação de Assinaturas Customizadas: escrita de detectores próprios consumindo o pipeline de eventos do Tracee
- [[tracee-implantacao-kubernetes-helm-daemonset-postee-webhook-siem]] — Tracee em Kubernetes: implantação via Helm DaemonSet, CRDs `Policy` (`tracee.aquasec.com/v1beta1`) e roteamento de saída (`json`, `webhook`, `forward`)
- [[tracee-modelo-seguranca-adversario-userspace-vs-kernel-garantias]] — Tracee Modelo de Ameaças e Segurança (*Security Model*): resistência contra adversários em *userspace* e detecção de ameaças em *kernel*

### CNCF Dex (provedor OpenID Connect federado baseado em `Connectors` para LDAP, GitHub, GitLab e OIDC upstream, autenticação `kube-apiserver`, `staticClients`/`trustedPeers` e CRDs Kubernetes)

- [[dexidp-arquitetura-cncf-federated-openid-connect-provider-connectors]] — CNCF Dex: arquitetura do provedor OpenID Connect federado (*Identity Broker*) baseado em `Connectors`
- [[dexidp-autenticacao-kubernetes-apiserver-oidc-kubectl-kubelogin-rbac]] — Dex + Kubernetes API Server: autenticação OIDC para `kubectl` (`kubelogin`) com mapeamento de grupos para `ClusterRoleBinding`
- [[dexidp-conector-ldap-active-directory-usersearch-groupsearch-starttls]] — Dex Conector `LDAP` (`ldap`): integração segura com Active Directory / OpenLDAP via `userSearch`, `groupSearch` e `startTLS` / `rootCA`
- [[dexidp-conectores-github-gitlab-orgs-teams-groups-filtragem]] — Dex Conectores `GitHub` e `GitLab`: controle de acesso baseado em Organizações, Teams (`org:team`) e Grupos de engenharia
- [[dexidp-conector-oidc-upstream-okta-entra-google-alerta-saml]] — Dex Conector `OIDC` Upstream vs Alerta de Segurança sobre o Conector `SAML 2.0`
- [[dexidp-staticclients-trustedpeers-cross-client-trust-aud-azp]] — Dex `staticClients` e `trustedPeers`: delegação de tokens entre serviços (*Cross-Client Trust*) com claims `aud` e `azp`
- [[dexidp-scopes-offline-access-refresh-tokens-expiry-rotation]] — Dex Escopos (`offline_access`, `groups`, `federated:id`) e Políticas de Expiração (`expiry`): controle de sessão e `refreshTokens`
- [[dexidp-storage-backends-kubernetes-crd-postgres-sqlite-etcd]] — Dex Backends de Armazenamento (`storage`): `kubernetes` (CRDs nativos) vs `postgres` / `mysql` / `etcd` em Alta Disponibilidade
- [[dexidp-grpc-api-mtls-gerenciamento-dinamico-clientes-revogacao]] — Dex API Administrativa `gRPC` com `mTLS`: criação dinâmica de clientes OAuth2 e revogação de Refresh Tokens
- [[dexidp-token-exchange-rfc8693-aws-sts-irsa-workload-identity]] — Dex como Emissor OIDC para `AWS STS` (`AssumeRoleWithWebIdentity`) e Federação de Identidades Multi-Serviço

### Pomerium (proxy de acesso Zero-Trust sensível à identidade e ao contexto inspirado no Google BeyondCorp, linguagem `PPL`, `X-Pomerium-Jwt-Assertion`, `mTLS` downstream/upstream e túneis TCP)

- [[pomerium-arquitetura-identity-aware-access-proxy-beyondcorp-zero-trust]] — Pomerium: arquitetura do *Identity-Aware Access Proxy* baseado nos princípios Google BeyondCorp e NIST Zero Trust
- [[pomerium-policy-language-ppl-operadores-allow-deny-and-or-not-nor]] — Pomerium Policy Language (`PPL`): autorização declarativa com operadores lógicos (`allow`/`deny`, `and`, `or`, `not`, `nor`) e critérios de contexto
- [[pomerium-jwt-assertion-header-x-pomerium-jwt-assertion-verificacao-upstream]] — Pomerium Identity Propagation (`X-Pomerium-Jwt-Assertion`): assinatura criptográfica da identidade do usuário para a aplicação backend
- [[pomerium-mtls-downstream-upstream-client-certificates-device-identity]] — Pomerium `mTLS` Downstream (Certificados de Cliente/Dispositivo) e Upstream (Criptografia Mútua Proxy -> Backend)
- [[pomerium-acesso-tcp-ssh-rdp-postgres-tunelamento-autenticado]] — Pomerium Rotas `TCP` (`tcp+https://`): acesso Zero-Trust a bancos de dados (`PostgreSQL`, `Redis`), `SSH` e `RDP` sem VPN
- [[pomerium-kubernetes-ingress-controller-gateway-api-crd-annotations]] — Pomerium Kubernetes Ingress Controller e Gateway API: definição declarativa de rotas e políticas via `Ingress` Annotations e CRDs
- [[pomerium-arquitetura-distribuida-authenticate-authorize-proxy-databroker]] — Pomerium Arquitetura de Serviços Distribuídos (`Authenticate`, `Authorize`, `Proxy` e `Databroker`): isolamento e escalabilidade
- [[pomerium-integracao-kubernetes-dashboard-api-impersonation-serviceaccount]] — Pomerium para Acesso Zero-Trust a `Kubernetes API` e Dashboards Internos: injeção de credenciais upstream e cabeçalhos `Impersonate-*`
- [[pomerium-cors-websocket-timeout-headers-seguranca-hsts-csp]] — Pomerium Controles de Tráfego HTTP/WebSockets (`allow_websockets`, `timeout`, `idle_timeout`) e Cabeçalhos de Segurança (`set_response_headers`)
- [[pomerium-auditoria-continua-authorize-logs-otel-metricas-prometheus]] — Pomerium Verificação Contínua e Observabilidade (`authorize_log`, `access_log`, `Prometheus` e `OpenTelemetry` Tracing)

### CNCF in-toto (framework de integridade da cadeia de suprimentos de software, `root.layout`, `functionaries`, *Artifact Rules* `MATCH`/`CREATE`/`DISALLOW`, `in-toto-run`/`verify` e *Attestation Framework v1*)

- [[intoto-arquitetura-cncf-supply-chain-integrity-layout-functionaries-links]] — CNCF in-toto: arquitetura de integridade fim-a-fim da cadeia de suprimentos (`Layout`, `Functionaries`, `Steps`, `Links` e `Inspections`)
- [[intoto-artifact-rules-materials-products-match-create-disallow]] — in-toto Artifact Rules (`MATCH`, `CREATE`, `MODIFY`, `DELETE`, `ALLOW`, `DISALLOW`, `REQUIRE`): encadeamento criptográfico entre etapas
- [[intoto-run-vs-intoto-record-geracao-metadados-link-assinados]] — in-toto Execução de Etapas (`in-toto-run` vs `in-toto-record start`/`stop`): captura de hashes de `materials`, comando e `products`
- [[intoto-inspections-verificacao-final-in-toto-verify-untar]] — in-toto `Inspections` e `in-toto-verify`: desempacotamento e validação criptográfica no momento da instalação pelo cliente
- [[intoto-attestation-framework-v1-statement-subject-predicate-dsse]] — in-toto Attestation Framework (`v1`): arquitetura das camadas `Envelope (DSSE)`, `Statement`, `subject` e `predicate`
- [[intoto-predicates-catalogo-slsa-provenance-cyclonedx-spdx-vuln-vsa]] — in-toto Attestation Predicates: catálogo oficial de predicados (`SLSA Provenance`, `SPDX`/`CycloneDX SBOM`, `Vuln Scan`, `VSA` e `Test Result`)
- [[intoto-dsse-dead-simple-signing-envelope-pae-prevencao-ambiguidade]] — in-toto Envelope de Assinatura `DSSE` (*Dead Simple Signing Envelope*) e `PAE`: proteção contra ataques de confusão de parser e tipo
- [[intoto-sign-assinatura-multiplas-chaves-thresholds-gpg-ssh-ed25519]] — in-toto Assinaturas e Quorum (`in-toto-sign` e `threshold`): exigência de múltiplas assinaturas independentes em `Layout` e `Steps`
- [[intoto-bindings-go-python-rust-java-protobuf-validacao-programatica]] — in-toto SDKs e Protobuf Bindings (`in-toto-golang`, `in-toto-rs`, `Python`, `Java`): geração e validação de atestados em código
- [[intoto-interseccao-slsa-witness-archivista-sigstore-admission-control]] — in-toto + `SLSA`, `Witness` e `Sigstore`: implementação prática de cadeias verificáveis do commit ao Kubernetes

### PyCQA Bandit (analisador estático de segurança `SAST` para Python baseado em `AST`, configuração em `pyproject.toml`/`bandit.yaml`, supressão granular `# nosec Bxxx`, plugins `B1xx`–`B7xx` e baseline)

- [[bandit-arquitetura-pycqa-sast-python-ast-nodes-plugins]] — PyCQA Bandit: arquitetura do analisador estático de segurança (`SAST`) para Python baseado na árvore sintática (`AST`)
- [[bandit-configuracao-pyproject-toml-bandit-yaml-ini-tests-skips]] — Bandit Configuração Declarativa (`pyproject.toml`, `bandit.yaml` e `.bandit`): controle de `exclude_dirs`, `tests` e `skips`
- [[bandit-supressao-granular-nosec-id-especifico-prevencao-cegueira]] — Bandit Supressão Segura de Falsos Positivos (`# nosec B602, B607`): por que nunca usar `# nosec` genérico sem ID
- [[bandit-injecao-comandos-subprocess-shell-true-b602-b605-os-system]] — Bandit Prevenção de Command Injection (`B602`–`B607`): `subprocess` com `shell=True`, `os.system` e customização do plugin
- [[bandit-desserializacao-insegura-pickle-yaml-load-marshal-b301-b506]] — Bandit Desserialização Insegura e XML (`B301` `pickle`, `B506` `yaml.load`, `B314`–`B320` XXE `defusedxml`)
- [[bandit-criptografia-fraca-random-hashes-md5-sha1-tls-b303-b311-b501]] — Bandit Criptografia, PRNG e TLS (`B303`/`B324` MD5/SHA1, `B311` `random` vs `secrets`, `B501` `verify=False` e `B502` SSL/TLS)
- [[bandit-sql-injection-jinja2-xss-flask-debug-hardcoded-passwords]] — Bandit AppSec Web (`B608` SQL Injection, `B701` Jinja2 `autoescape`, `B201` Flask Debug, `B104` Bind `0.0.0.0` e `B105`–`B107` Senhas)
- [[bandit-filtragem-severidade-confianca-ll-ii-baseline-legado]] — Bandit Filtragem por Severidade (`-l`/`-ll`/`-lll`), Confiança (`-i`/`-ii`/`-iii`) e Adoção Incremental com `--baseline` (`-b`)
- [[bandit-formatos-relatorio-sarif-json-custom-pre-commit-ci]] — Bandit Formatos de Saída (`json`, `sarif`, `xml`, `html`, `custom`) e Integração com `pre-commit` e GitHub Code Scanning
- [[bandit-escrita-plugins-ast-customizados-entry-points-blacklist]] — Bandit Extensibilidade: criação de Plugins AST Customizados (`@test.checks('Call')`) para regras internas de segurança

### Securego `gosec` (analisador de segurança para Go combinando regras `AST`, analisadores `SSA` e *Taint Analysis* `G701`–`G710`, categorias `G1xx`–`G7xx`, configuração JSON, `#nosec` e SARIF)

- [[gosec-arquitetura-securego-ast-ssa-taint-analysis-golang]] — Securego `gosec`: arquitetura em três motores (`AST`, `SSA` e `Taint Analysis`) para análise estática de segurança em Go
- [[gosec-taint-analysis-g701-a-g710-sqli-cmdi-ssrf-xss-path-traversal]] — `gosec` Motor de *Taint Analysis* (`G701`–`G710`): rastreamento de fluxo de dados de entradas HTTP até sinks perigosos
- [[gosec-analisadores-ssa-g113-http-smuggling-g115-integer-overflow-g118-context]] — `gosec` Analisadores `SSA`: detecção de *HTTP Smuggling* (`G113`), *Integer Overflow* (`G115`), *Context Leak* (`G118`) e *TOCTOU* (`G122`)
- [[gosec-seguranca-http-cookies-serializacao-segredos-g117-g120-g124]] — `gosec` Hardening de Serviços Web e Serialização: exposição de segredos em JSON/YAML (`G117`), `ParseMultipartForm` (`G120`) e Cookies (`G124`)
- [[gosec-seguranca-filesystem-permissoes-zip-slip-decompression-bomb-g110-g301-g307]] — `gosec` Segurança de Sistema de Arquivos (`G110` *Decompression Bomb*, `G301`–`G307` Permissões Octais e `G305` *Zip Slip*)
- [[gosec-criptografia-tls-ssh-g401-a-g408-math-rand-vs-crypto-rand]] — `gosec` Criptografia, TLS e SSH (`G401`–`G408` e `G501`–`G507`): `crypto/rand`, `MinVersion: tls.VersionTLS13`, IVs hardcoded e SSH
- [[gosec-configuracao-regras-json-g101-entropia-g104-erros-allowlist]] — `gosec` Configuração Fina por Regra (`-conf config.json`): ajuste de entropia em `G101`, allowlist de erros em `G104` e permissões em `G301`/`G306`
- [[gosec-supressao-anotacoes-nosec-justificativa-tracking-suppressions]] — `gosec` Supressões Auditáveis (`// #nosec Gxxx -- justificativa`) e Rastreamento com `-track-suppressions`
- [[gosec-filtragem-severity-confidence-include-exclude-tests-build-tags]] — `gosec` Seleção de Escopo na CLI: `-severity`, `-confidence`, `-include`/`-exclude`, `-tests` e `-tags` de compilação
- [[gosec-integracao-github-actions-sarif-private-modules-golangci-lint]] — `gosec` em Pipelines CI/CD: GitHub Actions com `SARIF`, módulos privados (`GOPRIVATE`) e integração com `golangci-lint` / Bazel `nogo`

### VirusTotal YARA e YARA-X (motor de *Pattern Matching* para pesquisa de malware e Threat Hunting, strings hexadecimais com jumps/wildcards/not, modificadores `xor`/`base64`, módulos `pe`/`elf`/`math` e `yarac`)

- [[yarasig-arquitetura-virustotal-yara-yara-x-anatomia-regras-meta-strings-condition]] — VirusTotal YARA e YARA-X: arquitetura do motor de *Pattern Matching* para pesquisa de malware e anatomia de regras (`meta`, `strings`, `condition`)
- [[yarasig-hexadecimal-strings-wildcards-not-jumps-alternatives]] — YARA Hexadecimal Strings (`{ ... }`): uso de *nibble wildcards* (`?`), operador *not* (`~`), *jumps* (`[X-Y]`) e alternativas (`( A | B )`)
- [[yarasig-text-strings-modificadores-nocase-wide-ascii-xor-base64-fullword]] — YARA Text Strings e Modificadores de Ofuscação: `nocase`, `wide`, `ascii`, `fullword`, `xor(min-max)`, `base64` e `base64wide`
- [[yarasig-conditions-contadores-offsets-at-in-filesize-entrypoint-uint]] — YARA Expressões em `condition`: contadores (`#a`), offsets (`@a[i]`), `at`, `in`, `of them`, `filesize` e leitura de inteiros (`uint16`, `uint32`)
- [[yarasig-modulos-pe-elf-math-hash-cuckoo-dotnet-inspecao-estrutural]] — YARA Módulos Embutidos (`import "pe"`, `"elf"`, `"math"`, `"hash"`, `"dotnet"`): inspeção de imports, seções, entropia, imphash e assinaturas Authenticode
- [[yarasig-private-rules-global-rules-tags-anonymous-strings-modularizacao]] — YARA Organização Modular de Rulesets: `private rule`, `global rule`, Strings Anônimas (`$`) e `include`
- [[yarasig-compilacao-binaria-yarac-external-variables-d-varredura-processos-pid]] — YARA Execução Avançada na CLI: pré-compilação com `yarac`, variáveis externas (`-d var=valor`) e varredura de Memória de Processos (`yara rules.yar <PID>`)
- [[yarasig-otimizacao-performance-atoms-aho-corasick-regex-bounded-profiling]] — YARA Engenharia de Performance: escolha de *Atoms* para o motor Aho-Corasick, perigos de Regex abertas (`.*`) e `short-circuit`
- [[yarasig-automacao-python-yara-python-yara-x-callbacks-timeout]] — YARA Automação em Python (`yara-python` e `yara_x`): compilação em memória, callbacks de `matches` e proteção por `timeout`
- [[yarasig-ecossistema-yarahq-yara-forge-yargen-yara-ci-integracoes]] — YARA no Ecossistema DFIR/SOC: integração com `Velociraptor`, `osquery`, `ClamAV`, `LimaCharlie` e curadoria com `YARA-CI` / `YARA Forge`

### Rapid7 Velociraptor (plataforma open-source de `DFIR` e visibilidade de endpoints movida por `VQL` — *Velociraptor Query Language*, `Artifacts`, `Hunts`, *Offline Collector*, `ETW`/`eBPF`/`Sigma`, `$MFT` e API `gRPC`)

- [[velociraptor-arquitetura-dfir-endpoint-visibility-vql-client-server]] — Rapid7 Velociraptor: arquitetura da plataforma open-source de `DFIR` e visibilidade de endpoints movida por `VQL`
- [[velociraptor-vql-velociraptor-query-language-plugins-functions-foreach]] — Velociraptor Query Language (`VQL`): consultas reativas com plugins geradores de linhas (`pslist`, `glob`, `parse_mft`, `yara`) e `foreach()`
- [[velociraptor-artifacts-yaml-client-server-events-artifact-exchange]] — Velociraptor `Artifacts` e `Artifact Exchange`: empacotamento YAML de queries VQL (`CLIENT`, `SERVER`, `CLIENT_EVENT`, `SERVER_EVENT`)
- [[velociraptor-hunting-at-scale-controle-recursos-cpu-iops-rate-limiting]] — Velociraptor `Hunts` em Escala e Controle de Recursos no Endpoint: `ops_per_second`, limite de CPU (`max_cpu`) e `timeout`
- [[velociraptor-offline-collector-triagem-sem-agente-zip-criptografado-s3]] — Velociraptor `Offline Collector`: geração de binário autônomo pré-configurado para triagem forense com upload cifrado (`ZIP` / `S3` / `Azure`)
- [[velociraptor-monitoramento-tempo-real-client-events-etw-ebpf-sigma]] — Velociraptor Detecção em Tempo Real (`CLIENT_EVENT`): monitoramento contínuo via `ETW` (Windows), `eBPF` (Linux) e regras `Sigma`
- [[velociraptor-pericia-ntfs-raw-accessor-mft-usnjrnl-vss-virtual-client]] — Velociraptor Perícia Forense de Disco (`ntfs`, `raw_ntfs`, `$MFT`, `$UsnJrnl` e Análise de Imagens de Disco via `remapping`)
- [[velociraptor-notebooks-interativos-pos-processamento-vql-timesketch-siem]] — Velociraptor `Notebooks` Colaborativos e Exportação (`Timesketch`, `Splunk`, `Elastic` e `S3`): análise pós-coleta sem reinterrogar o host
- [[velociraptor-orquestracao-ferramentas-externas-thor-hayabusa-cybertriage-quarantine]] — Velociraptor Orquestração de Ferramentas de Terceiros (`Tools`) e Resposta Ativa (`Windows.Remediation.Quarantine`)
- [[velociraptor-automacao-grpc-api-pyvelociraptor-rbac-orgs-multi-tenant]] — Velociraptor Automação SOAR via `gRPC API` (`pyvelociraptor`), `Orgs` Multi-Tenant e Governança `RBAC` / `OIDC`

## Tranche 4 (IDs 301–400)

### OpenZiti (plataforma open-source de rede Zero-Trust, *Dark Services* e *Dark Routers* sem portas inbound expostas, *Controller*, *Fabric Mesh*, *SDKs Application-Embedded* e *Tunnelers* `ziti-edge-tunnel`)

- [[ziti-arquitetura-openziti-malha-zero-trust-controller-fabric-edge]] — OpenZiti: Arquitetura da Malha Zero Trust com Controller, Fabric Mesh e Edge Components
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — OpenZiti: Dark Services e Dark Routers sem Portas de Escuta Inbound Expostas
- [[ziti-identities-enrollment-jwt-ott-certificados-x509-mutuos]] — OpenZiti: Identidades, Enrollment via One-Time Token (OTT) JWT e mTLS X.509
- [[ziti-politicas-service-policies-edge-router-policies-bind-dial]] — OpenZiti: Modelo de Autorização com Service Policies (`Bind`/`Dial`) e Attribute Roles
- [[ziti-sdks-application-embedded-zero-trust-go-c-python-jvm]] — OpenZiti: SDKs Application-Embedded Zero Trust (Go, C, Python, JVM e Node.js)
- [[ziti-tunnelers-ziti-edge-tunnel-intercept-host-tproxy-dns]] — OpenZiti: Tunnelers (`ziti-edge-tunnel`) com Interceptação DNS/TPROXY (`intercept.v1`) e Hosting (`host.v1`)
- [[ziti-criptografia-ponta-a-ponta-libsodium-kx-chacha20-poly1305]] — OpenZiti: Criptografia Ponta a Ponta (`libsodium` Curve25519 / ChaCha20-Poly1305) Acima do mTLS
- [[ziti-posture-checks-mfa-os-process-mac-domain-avaliacao-continua]] — OpenZiti: Posture Checks Contínuos (OS, Processos, MAC, Domínio e MFA TOTP)
- [[ziti-smart-routing-fabric-mesh-terminators-load-balancing-ha]] — OpenZiti: Smart Routing na Fabric Mesh, Terminators, Custos Dinâmicos e Alta Disponibilidade
- [[ziti-operacao-kubernetes-helm-ziti-controller-router-zrok-browzer]] — OpenZiti: Implantação em Kubernetes via Helm, `ziti-host` para ClusterIPs, `zrok` e BrowZer

### Cisco ClamAV (motor antivírus open-source `libclamav`, daemon multi-thread `clamd`, atualização segura `freshclam`, varredura *On-Access* `clamonacc` via `fanotify`, assinaturas `.hsb`/`.ndb`/`.ldb`/`.cbc` e `clamav-milter`)

- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — ClamAV: Arquitetura do Motor `libclamav`, Daemon `clamd`, `clamscan` e `freshclam`
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — ClamAV: Configuração do `clamd.conf`, Protocolo `INSTREAM` e Limites Anti-Zip-Bomb
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — ClamAV: Atualização Segura de Bases (`freshclam`), Arquivos `.cvd`/`.cld` e Mirrors Privados
- [[clamav-varredura-tempo-real-clamonacc-fanotify-on-access-linux]] — ClamAV: Varredura On-Access em Tempo Real (`clamonacc`) via Linux `fanotify`
- [[clamav-assinaturas-customizadas-hdb-ndb-ldb-yara-sigtool]] — ClamAV: Escrita de Assinaturas Customizadas (`.hdb`, `.hsb`, `.ndb`, `.ldb`, `.yar`) e `sigtool`
- [[clamav-bytecode-signatures-bc-clambc-llvm-runtime-sandbox]] — ClamAV: Assinaturas de Bytecode (`.cbc`), Sandbox Runtime e Depuração com `clambc`
- [[clamav-heuristicas-dlp-macros-ole2-pdf-encrypted-archives]] — ClamAV: Alertas Heurísticos, Bloqueio de Macros OLE2, Arquivos Criptografados e Prevenção de DLP
- [[clamav-integracao-pipelines-upload-api-milter-icap-s3]] — ClamAV: Integração em Gateways de E-mail (`clamav-milter`), Servidores ICAP e Eventos S3/API
- [[clamav-monitoramento-performance-clamdtop-filas-threads-memoria]] — ClamAV: Monitoramento Operacional com `clamdtop`, Pool de Memória e Dimensionamento em Containers
- [[clamav-gerenciamento-falsos-positivos-ign2-fp-clamsubmit]] — ClamAV: Supressão Auditável de Falsos Positivos (`.ign2` e `.fp`) e Submissão com `clamsubmit`

### Brakeman (analisador estático de segurança `SAST` *whole-program* para aplicações Ruby on Rails, níveis de confiança `High`/`Medium`/`Weak`, `CheckSQL`, `CheckCrossSiteScripting`, `CheckMassAssignment`, `config/brakeman.ignore` e SARIF)

- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Brakeman: Arquitetura de Análise Estática *Whole-Program* para Aplicações Ruby on Rails
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Brakeman: Níveis de Confiança (`High`, `Medium`, `Weak`) e Sensibilidade de Fluxo (`--branch-limit`)
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Brakeman: Detecção de SQL Injection (`CheckSQL`) em ActiveRecord, Interpolação de Strings e Arel
- [[brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to]] — Brakeman: Detecção de Cross-Site Scripting (`CheckCrossSiteScripting`, `raw`, `html_safe` e `link_to`)
- [[brakeman-mass-assignment-strong-parameters-permit-attr-accessible]] — Brakeman: Detecção de Mass Assignment e Abuso de Strong Parameters (`permit!` e Chaves Sensíveis)
- [[brakeman-command-injection-ssrf-open-redirect-dynamic-render]] — Brakeman: Command Injection (`CheckExecute`), SSRF, Path Traversal (`CheckSendFile`) e Dynamic Render
- [[brakeman-desserializacao-insegura-yaml-marshal-oj-eval-send]] — Brakeman: Desserialização Insegura (`YAML.load`, `Marshal.load`, `CSV`), `eval` e `send` Dinâmico
- [[brakeman-csrf-forgery-protection-sessoes-cookies-ssl-headers]] — Brakeman: Auditoria de CSRF (`protect_from_forgery`), Sessões, Cookies, `force_ssl` e Regex (`\A...\z`)
- [[brakeman-gerenciamento-falsos-positivos-brakeman-ignore-interativo]] — Brakeman: Gestão Auditável de Falsos Positivos com `config/brakeman.ignore` (`-I` e `--show-ignored`)
- [[brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml]] — Brakeman: Configuração Declarativa (`config/brakeman.yml`), Comparação Delta (`--compare`) e SARIF no CI/CD

### `ffuf` — Fuzz Faster U Fool (web fuzzer de alta performance em Go para descoberta de diretórios, *Virtual Hosts* e parâmetros, *Auto-Calibration* `-ac`/`-ach`, *Matchers* `-mc`/`-ms`/`-mw`/`-ml` e *Filters* `-fc`/`-fs`/`-fw`/`-fl`)

- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — ffuf: Arquitetura de Web Fuzzing Rápido em Go, Keyword `FUZZ` e Descoberta de Conteúdo (`-e` e `-D`)
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — ffuf: Precisão com Matchers (`-mc`, `-ms`, `-mw`, `-ml`, `-mr`, `-mt`) e Filters (`-fc`, `-fs`, `-fw`, `-fl`, `-fr`, `-ft`)
- [[ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404]] — ffuf: Auto-Calibration (`-ac`, `-acs`, `-acc` e `-ach`) para Eliminação Automática de Falso Positivo
- [[ffuf-descoberta-virtual-hosts-vhost-host-header-sni]] — ffuf: Descoberta de Virtual Hosts (`Host: FUZZ`) sem Registros DNS Públicos e TLS SNI (`-sni`)
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — ffuf: Fuzzing de Parâmetros GET, Payloads POST JSON, Headers Customizados e Requisições Raw (`-request`)
- [[ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders]] — ffuf: Modos Multi-Wordlist (`clusterbomb`, `pitchfork`, `sniper`) e Encoders (`-enc`)
- [[ffuf-recursao-automatica-recursion-depth-strategy-maxtime-job]] — ffuf: Varredura Recursiva (`-recursion`, `-recursion-depth`, `-recursion-strategy`) e `-maxtime-job`
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — ffuf: Controle de Taxa (`-rate`, `-p`, `-t`), Circuit Breakers (`-sf`, `-se`, `-sa`) e Modo Interativo
- [[ffuf-mutadores-externos-input-cmd-radamsa-ffuf-num]] — ffuf: Geração Dinâmica de Payloads e Fuzzing Mutacional com `--input-cmd`, `--input-num` e `$FFUF_NUM`
- [[ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc]] — ffuf: Padronização com `ffufrc` (`-config`), Artefatos de Resposta (`-od`), Relatórios (`-of all`) e `-replay-proxy`

### ProjectDiscovery Subfinder (enumeração passiva rápida de subdomínios para `EASM`, configuração de provedores e rotação de chaves em `provider-config.yaml`, resolução ativa e eliminação de *wildcards* `-nW`, rate-limiting `-rls` e SDK Go)

- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Subfinder: Arquitetura de Enumeração Passiva de Subdomínios e Descoberta de Superfície Externa (EASM)
- [[subfinder-configuracao-provedores-api-keys-provider-config-yaml]] — Subfinder: Configuração de Chaves de API e Rotação de Credenciais em `provider-config.yaml` (`-pc`)
- [[subfinder-selecao-fontes-recursive-all-exclude-sources-max-results]] — Subfinder: Seleção Granular de Fontes (`-s`, `-es`, `-all`, `-recursive`) e Paginação (`-mr`)
- [[subfinder-resolucao-ativa-eliminacao-wildcards-nw-resolvers-ip]] — Subfinder: Resolução DNS Ativa (`-nW` / `-active`), Eliminação de Wildcards e Extração de IPs (`-oI`)
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Subfinder: Rate-Limiting Global (`-rl`) e por Provedor (`-rls`), Timeouts e Limite de Leitura (`-rsr`)
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Subfinder: Controle de Escopo com Match (`-m`), Filter (`-f`) e Exclusão de IPs (`-ei`)
- [[subfinder-formatos-saida-jsonl-collect-sources-output-dir-audit]] — Subfinder: Saída Estruturada JSONL (`-oJ`), Atribuição de Fontes (`-cs`) e Diretórios por Domínio (`-oD`)
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Subfinder: Encadeamento Unix (`stdin`/`stdout`) em Pipelines de Reconhecimento com `httpx`, `katana` e `nuclei`
- [[subfinder-uso-como-biblioteca-go-sdk-runner-enumerate]] — Subfinder: Integração Programática em Go via SDK (`runner.NewRunner` e `EnumerateSingleDomainWithCtx`)
- [[subfinder-monitoramento-continuo-diff-novos-subdominios-alertas]] — Subfinder: Monitoramento Contínuo de Novos Subdomínios, Detecção de *Shadow IT* e Subdomain Takeover

### ProjectDiscovery `httpx` (toolkit multi-propósito de *probing* HTTP sobre `retryablehttp-go`, detecção de tecnologias Wappalyzer `-td`, hashes `mmh3` de favicon e `JARM`, inspeção TLS/CSP, *screenshots* headless `-ss` e filtros DSL)

- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — ProjectDiscovery `httpx`: Arquitetura de Probing HTTP Multi-Propósito com `retryablehttp-go`
- [[httpxpd-deteccao-tecnologias-wappalyzer-favicon-hash-jarm-tls]] — ProjectDiscovery `httpx`: Fingerprinting de Tecnologias (`-td`), Favicon Hash (`-favicon`), Body Hash e JARM (`-jarm`)
- [[httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports]] — ProjectDiscovery `httpx`: Probes de Infraestrutura (`-ip`, `-cname`, `-asn`, `-cdn`), Portas (`-p`) e Virtual Hosts (`-vhost`)
- [[httpxpd-inspecao-certificados-tls-csp-extract-fqdn-san]] — ProjectDiscovery `httpx`: Inspeção de Certificados TLS (`tls-grab`), Header CSP (`-csp-probe`) e Extração de FQDNs (`-efqdn`)
- [[httpxpd-captura-screenshots-headless-chrome-system-chrome-js]] — ProjectDiscovery `httpx`: Triagem Visual em Escala com Screenshots Headless (`-ss`, `-system-chrome` e `-jsc`)
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — ProjectDiscovery `httpx`: Filtragem Avançada com Matchers (`-mc`, `-ms`, `-mr`, `-mfc`) e Filters (`-fc`, `-fs`, `-fr`, `-fcdn`)
- [[httpxpd-extratores-customizados-er-ep-body-preview-redirect-chain]] — ProjectDiscovery `httpx`: Extratores Regex (`-er`, `-ep`), Body Preview (`-bp`) e Cadeia de Redirecionamento (`-fr` / `- follow-redirects`)
- [[httpxpd-otimizacao-rate-limit-threads-retries-timeout-waf-bypass]] — ProjectDiscovery `httpx`: Controle de Concorrência (`-t`, `-rl`, `-rlm`), Retries, Timeout e Resiliência a WAF
- [[httpxpd-armazenamento-respostas-srd-irh-csv-sqlite-dbs]] — ProjectDiscovery `httpx`: Arquivamento Forense de Respostas (`-srd`, `-irh`, `-irb`) e Relatórios CSV/JSONL
- [[httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei]] — ProjectDiscovery `httpx`: Papel de Filtro e Enriquecimento Entre `subfinder`, `katana` e `nuclei`

### ProjectDiscovery Katana (framework de *web crawling* e *spidering* em modo Standard e Headless Chrome `-hl`, parsing de JavaScript `-jc`/`-jsl` com `jsluice`, preenchimento de formulários `-aff`, deduplicação SimHash `-pcs` e controle de escopo)

- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Katana: Arquitetura de Web Crawling e Spidering (Modo Standard HTTP vs Modo Headless Chrome `-hl`)
- [[katana-analise-javascript-jc-jsluice-known-files-endpoints]] — Katana: Parsing Estático de Arquivos JavaScript (`-jc` e `-jsl`) e Descoberta de `known-files` (`-kf`)
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Katana: Controle Estrito de Escopo (`-fs`, `-cs`, `-cos`, `-do` e `-e`) para Prevenção de Fuga de Crawl
- [[katana-preenchimento-formularios-aff-form-config-estrategias-visita]] — Katana: Preenchimento Automático de Formulários (`-aff`, `-fc`), Extração (`-fx`) e Estratégias de Visita (`-s`)
- [[katana-deduplicacao-similaridade-fsu-pcs-simhash-tfidf-bm25]] — Katana: Deduplicação de URLs Paramétricas (`-fsu`, `-iqp`) e Similaridade de Conteúdo (`-pcs` SimHash/TF-IDF/BM25)
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Katana: Extração Estruturada de Campos (`-f`, `-sf`, `-em`, `-ef`) e `field-config.yaml` (`-flc`)
- [[katana-knowledge-base-classificacao-endpoints-segredos-kb]] — Katana: Knowledge Base (`-kb`), Classificação de Endpoints REST/GraphQL (`-kb-endpoints`) e Detecção de Segredos (`-kb-secrets`)
- [[katana-crawling-autenticado-headers-cookies-chrome-ws-url]] — Katana: Crawling Autenticado com Headers/Cookies (`-H`), Sessão de Navegador (`-cdd`) e Chrome DevTools (`-cwu`)
- [[katana-rate-limiting-concorrencia-parallelism-delay-timeout-resume]] — Katana: Controle de Concorrência (`-c`, `-p`), Rate-Limiting (`-rl`, `-rlm`, `-rd`), TLS Impersonation (`-tlsi`) e `-resume`
- [[katana-integracao-pipelines-dast-nuclei-ffuf-zap-proxy]] — Katana: Integração em Pipelines DAST com Proxy de Auditoria (`-proxy`), `nuclei` e `ffuf`

### OpenSSF GUAC — *Graph for Understanding Artifact Composition* (agregação de `SBOMs` SPDX/CycloneDX, atestações `SLSA`/in-toto `DSSE`, `OSV`, `OpenSSF Scorecard` e `VEX` em grafo de alta fidelidade com API GraphQL e CLI `guacone`)

- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — OpenSSF GUAC: Arquitetura do Grafo de Composição de Artefatos (Collectors, Ingestor, Assembler e GraphQL)
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — OpenSSF GUAC: Ontologia do Grafo — Substantivos (`Package`, `Artifact`, `Source`, `Builder`) e Predicados (`IsDependency`, `HasSLSA`, `CertifyVEX`)
- [[guacsec-ingestao-sboms-spdx-cyclonedx-dsse-intoto-slsa]] — OpenSSF GUAC: Ingestão de Documentos SPDX, CycloneDX, Envelopes DSSE, in-toto ITE-6 e Proveniência SLSA
- [[guacsec-certificadores-automaticos-osv-deps-dev-scorecard-clearlydefined]] — OpenSSF GUAC: Enriquecimento Contínuo com Certifiers (`osv`, `deps_dev`, `scorecard` e `clearlydefined`)
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — OpenSSF GUAC: Rastreamento de Vulnerabilidades Transitivas (`guacone query vuln`) e Filtragem por VEX (`OpenVEX` / `CSAF`)
- [[guacsec-backends-armazenamento-keyvalue-ent-postgresql-redis-tikv]] — OpenSSF GUAC: Backends de Persistência (`keyvalue` In-Memory vs `ent` com PostgreSQL)
- [[guacsec-arquitetura-eventos-nats-jetstream-collectsub-escala]] — OpenSSF GUAC: Pipeline Assíncrono em Escala com NATS JetStream, `collectsub` e `guacingest`
- [[guacsec-governanca-politicas-certifybad-certifygood-pointofcontact]] — OpenSSF GUAC: Governança Proativa da Cadeia de Suprimentos com `CertifyBad`, `CertifyGood` e `PointOfContact`
- [[guacsec-api-graphql-rest-guac-visualizer-integracao]] — OpenSSF GUAC: Consultas Customizadas na API GraphQL, REST API e Exploração Visual no GUAC Visualizer
- [[guacsec-ecossistema-trustify-gateways-admissao-ci-cd]] — OpenSSF GUAC: Integração em Gates de Release CI/CD e Relação com o Ecossistema GUAC / Trustify

### Sigstore Rekor (*Transparency Log* imutável e *append-only* para metadados assinados da cadeia de suprimentos, árvores de Merkle `Trillian` e `rekor-tiles` / `Trillian-Tessera`, *Pluggable Types* `hashedrekord`/`dsse`/`intoto`, `rekor-cli` e `rekor-monitor`)

- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Sigstore Rekor: Arquitetura do Transparency Log Imutável de Cadeia de Suprimentos e Árvores de Merkle
- [[rekor-tipos-pluggable-hashedrekord-intoto-dsse-jar-rpm-tuf]] — Sigstore Rekor: Esquemas Pluggable Types (`hashedrekord`, `rekord`, `intoto`, `dsse`, `jar`, `rpm` e `tuf`)
- [[rekor-operacoes-rekor-cli-upload-get-search-verify]] — Sigstore Rekor: Operação com `rekor-cli` (`upload`, `get`, `search` e `verify`) por Hash, Chave ou E-mail
- [[rekor-provas-criptograficas-inclusion-proof-consistency-proof-sth]] — Sigstore Rekor: Provas Criptográficas de Árvore de Merkle (`Inclusion Proof`, `Consistency Proof`, `STH` e `SET`)
- [[rekor-evolucao-rekor-v2-tile-based-logs-trillian-tessera]] — Sigstore Rekor: Evolução do Rekor v1 (Trillian gRPC + MySQL) para Rekor v2 (`rekor-tiles` e `Trillian-Tessera`)
- [[rekor-monitoramento-continuo-rekor-monitor-checkpoints-identidades]] — Sigstore Rekor: Auditoria e Monitoramento Contínuo com `rekor-monitor` (Consistência e Identidades OIDC)
- [[rekor-integracao-assinatura-ssh-minisign-x509-openpgp]] — Sigstore Rekor: Registro de Assinaturas Não-Fulcio (`ssh-keygen -Y sign`, `minisign` e X.509 Tradicional)
- [[rekor-api-rest-openapi-entries-retrieve-index-search]] — Sigstore Rekor: API REST v1 (`/api/v1/log`, `/api/v1/log/entries`, `/api/v1/index/retrieve`) e Limites Operacionais
- [[rekor-auto-hospedagem-privada-trillian-kms-sharding-offline-bundles]] — Sigstore Rekor: Auto-Hospedagem Privada (`rekor-server`), KMS Signing, Limite `--max_request_body_size` e Sharding
- [[rekor-sigstore-bundle-verificacao-offline-signed-timestamps]] — Sigstore Rekor: Formato Sigstore Bundle (`.sigstore.json`) e Verificação 100% Offline de Inclusão e Tempo

### Sigstore Fulcio (Autoridade Certificadora `CA` gratuita para assinatura de código baseada em identidades `OIDC`, certificados X.509 de curta duração de 10 minutos, extensões `OID 1.3.6.1.4.1.57264.1.*`, *Certificate Transparency Log* `ctfe` e distribuição via `TUF`)

- [[fulcio-arquitetura-sigstore-ca-oidc-short-lived-certificates]] — Sigstore Fulcio: Arquitetura da Autoridade Certificadora (CA) para *Keyless Code Signing* Baseada em OIDC
- [[fulcio-modelo-seguranca-revogacao-timestamps-rekor-verificacao]] — Sigstore Fulcio: Modelo de Segurança de Certificados de 10 Minutos — Por Que Não Há CRL/OCSP nem Re-Assinatura
- [[fulcio-especificacao-certificados-x509-san-critico-subject-vazio]] — Sigstore Fulcio: Especificação RFC 5280 dos Certificados Root, Intermediate (`pathlen:0`) e Leaf (Subject Vazio e SAN Crítico)
- [[fulcio-extensoes-x509-oids-57264-github-actions-ci-claims]] — Sigstore Fulcio: Árvore de OIDs X.509 (`1.3.6.1.4.1.57264.1.*`) para GitHub Actions, GitLab CI e Buildkite
- [[fulcio-provedores-oidc-meta-issuers-kubernetes-spiffe-ci]] — Sigstore Fulcio: Configuração de Provedores OIDC (`config.json`), Meta-Issuers (EKS/GKE/AKS) e SPIFFE/Workload Identity
- [[fulcio-certificate-transparency-log-ctfe-rfc6962-sct-poison]] — Sigstore Fulcio: Certificate Transparency Log (`ctfe`), Precertificates (`OID 1.3.6.1.4.1.11129.2.4.3`) e SCT (`OID 1.3.6.1.4.1.11129.2.4.2`)
- [[fulcio-fluxo-protocolo-create-signing-certificate-proof-possession]] — Sigstore Fulcio: Fluxo Criptográfico da API v2 (`CreateSigningCertificate`) e Prova de Posse da Chave
- [[fulcio-distribuicao-confianca-tuf-root-signing-trustbundle]] — Sigstore Fulcio: Raiz de Confiança com The Update Framework (TUF `sigstore/root-signing`) e `trusted_root.json`
- [[fulcio-implantacao-privada-certificate-maker-kms-pkcs11-tuf]] — Sigstore Fulcio: Implantação Corporativa Privada com `certificate-maker`, Cloud KMS e HSM PKCS#11
- [[fulcio-integracao-ecossistema-cosign-gitsign-policy-controller]] — Sigstore Fulcio: Integração Ponta a Ponta com `cosign`, `gitsign` e Kubernetes `policy-controller` / Kyverno

## Tranche 5 (IDs 401–500)

### sqlmap — Detecção Automatizada de SQL Injection, Técnicas BEUSTQ, Tamper Scripts e Validação de Remediação

- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — sqlmap: Arquitetura do Motor de Detecção de SQL Injection e as Seis Técnicas (`--technique=BEUSTQ`)
- [[sqlmap-calibracao-level-risk-heuristica-falsos-positivos-comparacao]] — sqlmap: Calibração de `--level` (1–5), `--risk` (1–3) e Ancoragem de Comparação (`--string`, `--code`, `--text-only`)
- [[sqlmap-fontes-alvo-request-file-openapi-swagger-burp-logs]] — sqlmap: Ingestão de Alvos via Requisição Raw (`-r`), Especificações `--openapi`, Marcadores `*` e Logs de Proxy (`-l`)
- [[sqlmap-injecao-second-order-csrf-tokens-sessoes-autenticadas]] — sqlmap: Detecção de *Second-Order SQL Injection* (`--second-url`), Renovação de `--csrf-token` e `--eval`
- [[sqlmap-tamper-scripts-avaliacao-regras-waf-normalizacao]] — sqlmap: Scripts de Transformação (`--tamper`) para Avaliação de Regras de WAF e Normalização de Payloads
- [[sqlmap-exfiltracao-out-of-band-dns-domain-time-based-blind]] — sqlmap: Aceleração de Blind SQL Injection via Exfiltração *Out-of-Band* DNS (`--dns-domain`)
- [[sqlmap-auditoria-privilegios-dba-file-system-os-shell-riscos]] — sqlmap: Auditoria de Privilégios Excessivos de SGBD (`--is-dba`, `--privileges`, `--roles` e Vetores de File/OS Access)
- [[sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay]] — sqlmap: Otimização de Rede (`-o`, `--keep-alive`, `--null-connection`, `--predict-output`) e Controle de Taxa (`--delay`)
- [[sqlmap-api-rest-sqlmapapi-automacao-remota-ipc-json]] — sqlmap: Automação Programática com `sqlmapapi.py` (Servidor REST JSON de Tasks Efêmeras)
- [[sqlmap-validacao-remediacao-prepared-statements-ci-non-interactive]] — sqlmap: Validação de Remediação (Prepared Statements / Parameterized Queries) e Regressão em CI/CD (`--batch` e `--results-file`)

### Dalfox — Análise de Parâmetros e Scanner de XSS (Reflected, Stored, DOM/AST), WAF Fingerprinting e CI/CD

- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Dalfox: Arquitetura de Análise de Parâmetros e Varredura de XSS (`dalfox scan`, Tiers `V`/`R`/`A`/`I`)
- [[dalfox-descoberta-mining-parametros-dom-dict-bav-static-analysis]] — Dalfox: Fase de Discovery — Parameter Mining (`--mining-dict`, `--mining-dom`), Análise de Contexto e BAV
- [[dalfox-alvos-multi-localizacao-param-json-graphql-xml-inject-marker]] — Dalfox: Modelagem de Alvos (`--param name:location`, `--inject-marker FUZZ`, `raw-http` e `har`)
- [[dalfox-verificacao-dom-ast-headless-blind-xss-callback]] — Dalfox: Verificação DOM/AST, Stored XSS (`SXSS`) e Blind XSS com Callback (`-b` / `--blind`)
- [[dalfox-monitoramento-sessao-autenticada-session-check-abort]] — Dalfox: Monitoramento Contínuo de Sessão Autenticada (`--session-check`, `--session-check-url` e `--on-session-loss`)
- [[dalfox-controle-escopo-out-of-scope-include-exclude-url]] — Dalfox: Governança de Escopo (`--out-of-scope`, `--out-of-scope-file`, `--include-url`, `--exclude-url` e `--ignore-param`)
- [[dalfox-waf-fingerprinting-evasao-custom-payloads-encoders]] — Dalfox: Fingerprinting de WAF (`--waf-min-confidence`), Rastreamento de Bypass e `--custom-payload`
- [[dalfox-pipeline-mode-katana-dedup-urls-state-file-resume]] — Dalfox: Operação em Pipeline (`--input-type pipe`), Deduplicação (`--dedup-urls signature`) e Retomada (`--state-file`)
- [[dalfox-modos-server-rest-api-mcp-stdio-integracao-automacao]] — Dalfox: Subcomandos `dalfox server` (REST API) e `dalfox mcp` (Model Context Protocol stdio Server)
- [[dalfox-comparacao-baseline-sarif-state-file-ci-cd]] — Dalfox: Gates de CI/CD com Comparação de Baseline (`--baseline`, `--baseline-mode`) e Exportação SARIF (`-f sarif`)

### MISP (Malware Information Sharing Platform) — Threat Intelligence, IOCs, Galaxies, Warninglists, PyMISP e IDS Export

- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — MISP: Arquitetura da Plataforma de Threat Intelligence — Events, Attributes, Objects e Galaxies
- [[mispsoc-motor-correlacao-automatica-ssdeep-cidr-grafos-eventos]] — MISP: Motor de Correlação Automática (Valores Exatos, Sub-redes CIDR e Fuzzy Hashing `ssdeep`)
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — MISP: Taxonomias Padronizadas (`TLP`, `PAP`, `admiralty-scale`), Sharing Groups e Sincronização Federada
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — MISP: Prevenção de Falsos Positivos e Auto-Sabotagem com `misp-warninglists`
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — MISP: Automação em Python com `PyMISP` e Consultas Avançadas na API `/attributes/restSearch`
- [[mispsoc-enriquecimento-misp-modules-hover-expansion-import-export]] — MISP: Enriquecimento e Expansão Automatizada com `misp-modules` (DNS, BGP/ASN, Shodan, VirusTotal, YARA e PDF)
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — MISP: Exportação Automatizada de IOCs para Sensores Suricata, Zeek Intel Framework, DNS RPZ e STIX 2.1
- [[mispsoc-feeds-osint-caching-freetext-import-stix-taxii]] — MISP: Gestão de Feeds OSINT (Caching vs Ingestão Seletiva), Free-Text Import e Integração STIX/TAXII
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — MISP: Motor de Workflows Visuais, Gatilhos (`event-before-publish`) e Governança de Qualidade de CTI
- [[mispsoc-colaboracao-sightings-opinions-decaying-models-ciclo-vida]] — MISP: Ciclo de Vida do IOC com Sightings (Avistamentos), False-Positive Reports e *Decaying Models*

### BloodHound CE (SpecterOps) — Gestão de Caminhos de Ataque em Grafos (Active Directory, Entra ID e OpenGraph)

- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — BloodHound CE: Arquitetura de Gestão de Caminhos de Ataque em Grafos (Go REST API, PostgreSQL e Neo4j)
- [[bloodhound-coletores-sharphound-azurehound-metodos-coleta-furtividade]] — BloodHound CE: Coletores Oficiais `SharpHound` (Active Directory) e `AzureHound` (Microsoft Entra ID / Azure RM)
- [[bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword]] — BloodHound CE: Arestas de Abuso de ACLs no Active Directory (`GenericAll`, `GenericWrite`, `WriteDacl`, `WriteOwner`, `ForceChangePassword`)
- [[bloodhound-movimentacao-lateral-hassession-adminto-dcsync-adminsdholder]] — BloodHound CE: Movimentação Lateral (`AdminTo` + `HasSession`), Roubo de Credenciais e `DCSync` (`GetChanges` + `GetChangesAll`)
- [[bloodhound-delegacao-kerberos-unconstrained-constrained-rbcd]] — BloodHound CE: Mapeamento de Delegações Kerberos (`Unconstrained`, `Constrained` `AllowedToDelegate` e `RBCD` `AllowedToAct`)
- [[bloodhound-escalacao-adcs-certificados-esc1-a-esc13-pkinit]] — BloodHound CE: Caminhos de Escalação via Active Directory Certificate Services (`ADCS ESC1` a `ESC13`)
- [[bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets]] — BloodHound CE: Caminhos de Ataque no Microsoft Entra ID e Ambientes Híbridos (`AZAddSecret`, `AZGlobalAdmin`, `SyncedTo`)
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — BloodHound CE: Governança do Perímetro **Tier Zero** (`admin_tier_0`) e Erradicação de *Chokepoints*
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — BloodHound CE: Consultas `Cypher` Customizadas (`shortestPath`, `allShortestPaths`) e Priorização de Remediação
- [[bloodhound-extensibilidade-opengraph-ingestao-multi-cloud-iam]] — BloodHound CE: Extensibilidade com **BloodHound OpenGraph** para Plataformas Multi-Cloud, SaaS e CI/CD

### CNCF Paralus — Acesso Zero-Trust ao Kubernetes, Kubeconfig Just-in-Time, Federação OIDC/RBAC e Auditoria de kubectl

- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — CNCF Paralus: Arquitetura de Gerenciamento de Acesso Zero-Trust para Frotas de Clusters Kubernetes
- [[paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in]] — CNCF Paralus: Conexão Segura de Clusters Privados via Relay Agent (Túnel mTLS Outbound sem Expor o `kube-apiserver`)
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — CNCF Paralus: Modelo Multi-Tenant com `Projects`, `Groups`, Papéis Pré-Configurados e `Custom Roles` por Namespace
- [[paralus-federacao-sso-oidc-okta-entra-github-mapeamento-grupos]] — CNCF Paralus: Federação SSO com Provedores OIDC (Okta, Microsoft Entra ID, Google, Keycloak e GitHub) e Mapeamento de Grupos
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — CNCF Paralus: Provisionamento *Just-in-Time* de ServiceAccounts, `kubeconfig` Auditado e Revogação Instantânea
- [[paralus-terminal-web-prompt-sessoes-efemeras-browser-kubectl]] — CNCF Paralus: Acesso `kubectl` Browser-Based via Componente `Prompt` (Sessões Efêmeras sem Credenciais no Desktop)
- [[paralus-automacao-cli-pctl-gitops-rbac-as-code-ci-cd]] — CNCF Paralus: Automação Declarativa (*RBAC-as-Code*) com a CLI `pctl` e API REST em Pipelines GitOps
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — CNCF Paralus: Trilhas de Auditoria Imutáveis (`System Audit Logs` e `Kubectl / Relay Audit Logs`) para Conformidade e SIEM
- [[paralus-custom-roles-restricao-verbs-exec-portforward-secrets]] — CNCF Paralus: Criação de `Custom Roles` Restritivas (Bloqueio de `pods/exec`, `pods/portforward` e Leitura de `secrets`)
- [[paralus-hardening-producao-postgres-kratos-tls-networkpolicies]] — CNCF Paralus: Hardening da Própria Instalação do Paralus (Certificados TLS, Isolamento de Rede e Proteção de Segredos)

### CISOfy Lynis — Auditoria de Segurança e Hardening em Linux/Unix, Perfis .prf, Hardening Index e Dockerfiles

- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — CISOfy Lynis: Arquitetura de Auditoria Local e Hardening de Sistemas Linux/Unix (`lynis audit system`)
- [[lynis-interpretacao-relatorios-lynis-log-lynis-report-dat-show-details]] — CISOfy Lynis: Análise de `Warnings` vs `Suggestions`, `/var/log/lynis-report.dat` e `lynis show details <TEST-ID>`
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — CISOfy Lynis: Customização de Políticas com Perfis `custom.prf` (`skip-test`, `config-data` e `--profile`)
- [[lynis-hardening-kernel-sysctl-krnl-6000-aslr-ptrace-bpf-rede]] — CISOfy Lynis: Remediação de `KRNL-6000` — Hardening de Parâmetros `sysctl` de Kernel, Memória e Pilha de Rede
- [[lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites]] — CISOfy Lynis: Remediação de `SSH-7408` e `AUTH-*` — Hardening de OpenSSH (`sshd_config`), PAM e Contas Locais
- [[lynis-auditoria-dockerfiles-lynis-audit-dockerfile-containers]] — CISOfy Lynis: Auditoria Estática de Imagens de Container com `lynis audit dockerfile`
- [[lynis-modo-pentest-nao-privilegiado-enumeracao-escalacao-privilegio]] — CISOfy Lynis: Execução em Modo `--pentest` (Auditoria Não-Privilegiada e Avaliação de Vetores de Escalação Local)
- [[lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot]] — CISOfy Lynis: Hardening de Sistemas de Arquivos (`FILE-*`), Opções de Montagem (`nodev`, `nosuid`, `noexec`), `/proc` `hidepid` e GRUB
- [[lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva]] — CISOfy Lynis: Auditoria Contínua Automatizada (`--cronjob`, `systemd timer`) e Detecção de Deriva de Hardening Index
- [[lynis-desenvolvimento-testes-customizados-lynis-sdk-plugins]] — CISOfy Lynis: Escrita de Testes e Plugins Customizados (`CUST-*`) com Funções Internas (`Register`, `Display`) e `lynis-sdk`

### Linux Audit Framework (auditd / audit-userspace) — Auditoria de Syscalls no Kernel, augenrules, ausearch e Imutabilidade

- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Linux Audit (`auditd`): Arquitetura do Subsistema de Auditoria do Kernel, `auditctl`, `augenrules` e `RefuseManualStop`
- [[auditd-organiazacao-rules-d-buffer-backlog-failure-mode-imutavel-e2]] — Linux Audit (`auditd`): Ordenação `10`–`99` em `/etc/audit/rules.d/`, Backlog (`-b`), Modo de Falha (`-f`) e Trava Imutável (`-e 2`)
- [[auditd-regras-monitoramento-arquivos-identidade-sudoers-ssh-w]] — Linux Audit (`auditd`): Monitoramento de Integridade de Arquivos Críticos (`-w` / `-F path=`) — Identidade, `sudoers`, SSH e Cron
- [[auditd-regras-syscalls-execve-escalacao-privilegio-auid-euid]] — Linux Audit (`auditd`): Auditoria de Syscalls por Arquitetura (`b64`/`b32`), Execução Privilegiada (`auid!=unset`, `uid!=euid`) e Binários SUID
- [[auditd-regras-modulos-kernel-mount-ptrace-time-change-mac]] — Linux Audit (`auditd`): Monitoramento de Carregamento de Módulos do Kernel (`init_module`, `finit_module`), `ptrace`, Alteração de Hora e MAC
- [[auditd-exclusao-ruido-never-exit-cron-containers-alta-performance]] — Linux Audit (`auditd`): Supressão Cirúrgica de Ruído com Regras `never,exit` e `exclude` em `20-dont-audit.rules`
- [[auditd-protecao-disco-particao-dedicada-space-left-action-halt]] — Linux Audit (`auditd`): Partição `/var/log/audit` Dedicada, `space_left_action`, `admin_space_left_action` e `disk_full_action`
- [[auditd-investigacao-forense-ausearch-aureport-auid-correlacao]] — Linux Audit (`auditd`): Investigação Forense e Resposta a Incidentes com `ausearch` (`-i`, `-k`, `-ua`, `--session`) e `aureport`
- [[auditd-streaming-tempo-real-audisp-af-unix-remote-siem]] — Linux Audit (`auditd`): Streaming em Tempo Real com Plugins `audisp` (`/etc/audit/plugins.d/`, `af_unix` e `audisp-remote` TLS/Kerberos)
- [[auditd-rastreamento-containers-audit-container-id-namespaces]] — Linux Audit (`auditd`): Monitoramento de Hosts de Containers, sockets de Runtime (`/run/containerd`, `/var/run/docker.sock`) e Isolamento de `auditd`

### USBGuard — Autorização de Dispositivos USB no Linux, Prevenção contra BadUSB/HID Injection e Linguagem de Regras

- [[usbguard-arquitetura-autorizacao-dispositivos-usb-badusb-daemon]] — USBGuard: Arquitetura de Autorização de Dispositivos USB no Linux e Defesa contra Ataques *BadUSB* / *Rubber Ducky*
- [[usbguard-linguagem-regras-targets-allow-block-reject-atributos]] — USBGuard: Gramática da Linguagem de Regras — Alvos (`allow`, `block`, `reject`), `device_id` e Atributos (`hash`, `serial`, `via-port`)
- [[usbguard-protecao-badusb-operadores-with-interface-hid-storage]] — USBGuard: Prevenção contra Dispositivos Compostos (*BadUSB*) usando Operadores de Conjunto em `with-interface` (`equals`, `none-of`, `one-of`)
- [[usbguard-condicoes-dinamicas-localtime-allowed-matches-rule-applied]] — USBGuard: Condições Contextuais de Regras (`if !allowed-matches(...)`, `localtime(...)` e `rule-applied`)
- [[usbguard-geracao-politica-inicial-generate-policy-port-specific-hash]] — USBGuard: Geração Segura de Política Inicial com `usbguard generate-policy` (`-p`, `-P`, `-H` e `-t`)
- [[usbguard-configuracao-daemon-conf-implicit-policy-present-device]] — USBGuard: Hardening de `/etc/usbguard/usbguard-daemon.conf` (`ImplicitPolicyTarget`, `PresentDevicePolicy`, `PresentControllerPolicy`)
- [[usbguard-controle-acesso-ipc-polkit-dbus-allow-device-temporario]] — USBGuard: Administração Dinâmica (`allow-device`, `block-device`, `append-rule -t`) e Controle de Acesso IPC / Polkit
- [[usbguard-monitoramento-eventos-watch-linux-audit-journald-siem]] — USBGuard: Monitoramento em Tempo Real (`usbguard watch`), Integração com `LinuxAudit` (`AUDIT_USER_DEVICE`) e SIEM
- [[usbguard-integracao-ldap-centralizada-frotas-corporativas-sssd]] — USBGuard: Gerenciamento Centralizado de Políticas USB em Frotas Corporativas via Backend LDAP (`--with-ldap` / `usbguard-ldap`)
- [[usbguard-hardening-daemon-seccomp-libcap-ng-systemd-sandboxing]] — USBGuard: Hardening do Próprio `usbguard-daemon` (Filtro `libseccomp`, Drop de Capabilities `libcap-ng` e Sandboxing `systemd`)

### AppArmor Linux Security Module — MAC Baseado em Caminhos, Perfis Enforce/Complain, Abstrações e Containers/Kubernetes

- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — AppArmor: Arquitetura do Módulo LSM de Controle de Acesso Obrigatório (MAC Baseado em Caminhos e Confinamento de Superusuário)
- [[apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce]] — AppArmor: Modos de Operação de Perfis (`enforce`, `complain`, `unconfined`, `kill`) e Comandos `aa-enforce`, `aa-complain` e `aa-disable`
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — AppArmor: Sintaxe de Regras de Perfil — Permissões de Arquivos (`r`, `w`, `a`, `k`, `l`, `m`), `capability`, `network`, `mount`, `ptrace` e `signal`
- [[apparmor-transicoes-execucao-ix-px-cx-ux-scrubbing-ambiente]] — AppArmor: Modos de Transição de Execução (`ix`, `px`/`Px`, `cx`/`Cx`, `ux`/`Ux`) e Limpeza de Ambiente (*Environment Scrubbing*)
- [[apparmor-abstracoes-tunables-local-overrides-manutencao-perfis]] — AppArmor: Modularização com `abstractions/`, Variáveis `tunables/` e Customizações Seguras em `local/`
- [[apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd]] — AppArmor: Criação e Refinamento Guiado de Perfis com `aa-genprof`, `aa-logprof` e `aa-autodep`
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — AppArmor: Confinamento de Containers e Pods Kubernetes (`securityContext.appArmorProfile` GA no Kubernetes v1.30+)
- [[apparmor-subperfis-change-hat-pam-apparmor-mod-apparmor]] — AppArmor: Mudança Dinâmica de Privilégio Intra-Processo com `aa_change_hat(2)`, `aa_change_profile(2)` e `pam_apparmor`
- [[apparmor-diagnostico-violacoes-apparmor-denied-dmesg-ausearch]] — AppArmor: Diagnóstico de Negativas (`apparmor="DENIED"`), `aa-notify` e Decodificação de Campos `operation`, `requested_mask` e `denied_mask`
- [[apparmor-otimizacao-cache-binario-apparmor-parser-boot-systemd]] — AppArmor: Compilação AOT, Cache Binário (`/var/cache/apparmor/`), Pré-Validação em CI e Hardening de Boot (`apparmor=1 security=apparmor`)

### SELinux (SELinuxProject) — MAC Baseado em Rótulos, Type Enforcement, MCS para Containers, Booleans, semanage e Diagnóstico AVC

- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — SELinux: Arquitetura de Controle de Acesso Obrigatório Baseada em Rótulos (`user:role:type:level`) e *Type Enforcement* (TE)
- [[selinux-modos-enforcing-permissive-booleans-getsebool-setsebool]] — SELinux: Modos `Enforcing` vs `Permissive`, Domínios Permissivos por Processo (`semanage permissive`) e *Booleans* (`getsebool` / `setsebool -P`)
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — SELinux: Persistência de Rótulos de Arquivos com `semanage fcontext` e Aplicação com `restorecon -Rv` (Armadilha do `chcon`)
- [[selinux-gerenciamento-portas-rede-semanage-port-http-ssh]] — SELinux: Controle de Acesso a Portas TCP/UDP com `semanage port` (`http_port_t`, `ssh_port_t`, `mysqld_port_t`)
- [[selinux-isolamento-containers-mcs-svirt-lxc-net-t-container-file-t-z]] — SELinux: Isolamento Multi-Tenant de Containers e Pods Kubernetes com **MCS** (`s0:cX,cY`), `container_t`, `container_file_t` e Montagens `:z` / `:Z`
- [[selinux-diagnostico-violacoes-avc-ausearch-audit2why-sealert]] — SELinux: Diagnóstico Forense de Negativas `AVC` com `ausearch -m AVC`, `audit2why` e `sealert`
- [[selinux-compilacao-modulos-customizados-te-cil-udica-semodule]] — SELinux: Desenvolvimento e Gerenciamento de Módulos de Política (`.te` / `.cil`), `checkmodule`, `semodule_package`, `secilc` e `semodule`
- [[selinux-confinamento-usuarios-semanage-login-user-staff-u-sysadm-u]] — SELinux: Confinamento RBAC de Usuários Humanos e Administradores SSH (`semanage login`, `user_u`, `staff_u`, `sysadm_u` e `sudo -r`)
- [[selinux-analise-politicas-setools-sesearch-seinfo-auditoria]] — SELinux: Auditoria e Consulta Formal da Política Binária com `setools` (`sesearch`, `seinfo` e Desativação Temporária de `dontaudit`)
- [[selinux-exportacao-importacao-customizacoes-semanage-export-ansible]] — SELinux: Backup, Replicação Atômica (`semanage export` / `semanage import`) e Automação Idempotente de Políticas em Frota

## Tranche 6 (IDs 501–600)

### TheHive & Cortex — Plataforma de Resposta a Incidentes (SIRP), Cases, Observables, Analyzers, Responders e Integração MISP

- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — TheHive: Arquitetura da Plataforma de Resposta a Incidentes (SIRP) — Fluxo `Alerts` -> `Cases` -> `Tasks` -> `Observables`
- [[thehive-templates-casos-playbooks-padronizados-metricas-kpis]] — TheHive: Padronização de Playbooks de Resposta a Incidentes com `Case Templates`, `Tasks` Obrigatórias e Métricas Customizadas
- [[thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao]] — TheHive: Ingestão Automatizada de Alertas via `TheHive4py` (`type`, `source`, `sourceRef`), Merge em Casos e Correlação de Observáveis
- [[thehive-governanca-observables-tlp-pap-ioc-sighted-marking]] — TheHive: Governança de `Observables` — Diferença Operacional entre **TLP** (*Traffic Light Protocol*) e **PAP** (*Permissible Actions Protocol*)
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — TheHive & Cortex: Análise em Escala de Observáveis com **Cortex Analyzers** e Guardrails Automáticos de `TLP`/`PAP`
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — TheHive & Cortex: Contenção e Resposta Ativa a Incidentes com **Cortex Responders** (Isolamento EDR, Bloqueio Firewall/RPZ e Revogação IAM)
- [[thehive-sincronizacao-bidirecional-misp-import-export-iocs]] — TheHive: Integração Bidirecional com o **MISP** (Importação Filtrada de Eventos para Alertas e Exportação de IOCs Confirmados)
- [[thehive-desenvolvimento-analyzers-customizados-cortexutils-docker]] — Cortex: Desenvolvimento de `Analyzers` e `Responders` Customizados em Python (`cortexutils`) e Isolamento em Containers Docker
- [[thehive-templates-relatorios-curtos-longos-fusao-casos]] — TheHive: Customização de `Report Templates` do Cortex (Short / Long Reports), Fusão de Casos (`Case Merging`) e Fechamento Auditável
- [[thehive-multi-tenancy-organizacoes-rbac-auditoria-webhooks]] — TheHive & Cortex: Multi-Tenancy por Organizações, RBAC, Autenticação SSO/LDAP/OAuth2 e Notificações via Webhooks

### Filigran OpenCTI — Plataforma de Threat Intelligence em Grafo STIX 2.1, Conectores, Inferência, RBAC Markings e Feeds

- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — OpenCTI: Arquitetura da Plataforma de Threat Intelligence Baseada em Grafo de Conhecimento **STIX 2.1** e API GraphQL
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — OpenCTI: Modelagem com Objetos **STIX 2.1** — Domain Objects (SDOs), Cyber Observables (SCOs), Relationships (SROs) e `Confidence`
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — OpenCTI: Arquitetura dos Cinco Tipos de Conectores (`EXTERNAL_IMPORT`, `INTERNAL_IMPORT_FILE`, `INTERNAL_ENRICHMENT`, `INTERNAL_EXPORT_FILE` e `STREAM`)
- [[opencti-motor-inferencia-regras-deducao-relacoes-transitivas]] — OpenCTI: Motor de Raciocínio e Inferência (`Rule Engine`) para Dedução Automática de Relações Transitivas no Grafo
- [[opencti-ciclo-vida-indicadores-decay-rules-score-revogacao]] — OpenCTI: Ciclo de Vida de Indicadores — **Decay Rules** (Curvas de Decaimento de `x_opencti_score`), Expiração `valid_until` e Revogação
- [[opencti-governanca-rbac-marking-definitions-tlp-confianca-organizacoes]] — OpenCTI: Controle de Acesso Baseado em **Marking Definitions** (`TLP`, `PAP`, `Statement`), Segregação por Organizações e `Max Confidence Level`
- [[opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem]] — OpenCTI: Compartilhamento de Inteligência em Tempo Real — **Live Streams** (SSE), Coleções **TAXII 2.1** e **CSV Feeds** para Firewalls/EDRs
- [[opencti-automacao-playbooks-enriquecimento-notificacoes-triage]] — OpenCTI: Automação de Fluxos de Conhecimento com **Playbooks** (Gatilhos de Stream, Filtros, Enriquecimento, Marcação e Criação de Casos)
- [[opencti-gestao-casos-incident-response-rfi-tasks-workbenches]] — OpenCTI: Módulo de `Cases` (`Incident Response`, `Requests for Information — RFI`, `Requests for Takedown`) e `Analyst Workbenches`
- [[opencti-desenvolvimento-conectores-pycti-stix2-bundles-workers]] — OpenCTI: Desenvolvimento de Conectores Customizados com o SDK Python **`pycti`** (`OpenCTIConnectorHelper` e Envio de Bundles STIX 2.1)

### Google Timesketch & Plaso (log2timeline) — Análise Colaborativa de Super-Timelines Forenses, DFIQ, Analyzers e Sigma

- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Google Timesketch: Arquitetura de Análise Colaborativa de *Super-Timelines* Forenses (Python/Flask, Celery, PostgreSQL e OpenSearch)
- [[timesketch-ingestao-plaso-log2timeline-jsonl-csv-timesketch-importer]] — Timesketch: Geração de *Super-Timelines* com **Plaso (`log2timeline.py`)** e Ingestão via `timesketch_importer` (Plaso, JSONL e CSV)
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Timesketch: Sintaxe de Busca OpenSearch Query String, Filtros de Tipo de Dados (`data_type`), *Context Queries* e *Saved Views*
- [[timesketch-analisadores-automaticos-analyzers-chain-tagger-similarity]] — Timesketch: Execução de **Analyzers** Automatizados em Background (Taggers, Chain Analyzer, Account Finder, Domain/Hash Enrichment)
- [[timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer]] — Timesketch: Caça a Ameaças (*Threat Hunting*) Retroativa em Timelines com Regras **Sigma** e `tsctl`
- [[timesketch-investigacao-guiada-dfiq-questions-facets-approaches]] — Timesketch: Investigação Guiada com **DFIQ** (*Digital Forensics Investigative Questions* — Scenarios, Facets, Questions e Approaches)
- [[timesketch-aba-intelligence-iocs-integracao-yeti-misp-opencti]] — Timesketch: Aba **Intelligence**, Marcação de IOCs na Timeline e Integração com Plataformas de CTI (Yeti, MISP e OpenCTI)
- [[timesketch-narrativa-forense-stories-grafos-relatorios-markdown]] — Timesketch: Construção de Relatórios Forenses Reprodutíveis com **Stories**, Agregações Gráficas e Grafos de Relacionamento
- [[timesketch-automacao-python-timesketch-api-client-notebooks-jupyter]] — Timesketch: Ciência de Dados Forense com **`timesketch-api-client`**, DataFrames `pandas` e Container Jupyter Notebook (`picatrix`)
- [[timesketch-governanca-acls-protecao-delecao-arquivamento-tsctl]] — Timesketch: Governança de Acesso (ACLs de Sketch), Rótulos de Preservação Legal (`protected` / `preserved`), Arquivamento e `tsctl`

### Volatility 3 — Forense de Memória RAM (Windows, Linux, macOS), Tabelas de Símbolos ISF (dwarf2json), Malfind e Rootkits

- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Volatility 3: Arquitetura de Análise Forense de Memória RAM, *Intermediate Symbol Format* (`ISF`) e *Translation Layers*
- [[volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map]] — Volatility 3: Geração de Tabelas de Símbolos **ISF** para Kernels Linux e macOS com `dwarf2json`
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Volatility 3: Análise de Processos Windows (`pslist`, `pstree`, `psscan`, `cmdline`, `envars` e Detecção de *DKOM*)
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Volatility 3: Detecção de Injeção de Código em Memória, *Reflective DLL* e *Process Hollowing* (`malfind`, `vadinfo` e `hollowprocesses`)
- [[volatility3-inspecao-dlls-handles-ldrmodules-mutants-privs]] — Volatility 3: Auditoria de DLLs Desvinculadas (`dlllist` vs `ldrmodules`), *Handles*/Mutexes (`handles`) e Tokens (`privs` / `getsids`)
- [[volatility3-conexoes-rede-windows-netscan-netstat-sockets]] — Volatility 3: Reconstrução de Conexões de Rede e Sockets em Memória (`windows.netscan.NetScan` e `windows.netstat.NetStat`)
- [[volatility3-registro-windows-memoria-hivelist-printkey-userassist-hashdump]] — Volatility 3: Forense de Registro Windows em Memória (`hivelist`, `printkey`, `userassist`) e Auditoria de Credenciais (`hashdump` / `lsadump`)
- [[volatility3-persistencia-servicos-callbacks-ssdt-drivers-windows]] — Volatility 3: Detecção de Rootkits de Kernel Windows, Drivers Maliciosos (*BYOVD*), SSDT, Callbacks e Serviços (`svcscan`, `modules`, `driverscan`, `ssdt`, `callbacks`)
- [[volatility3-forense-linux-rootkits-check-syscall-modules-bash-sockstat]] — Volatility 3: Forense de Memória Linux — Processos, Histórico `bash`, Sockets (`sockstat`) e Detecção de Rootkits LKM (`check_syscall`, `check_modules`, `check_idt`)
- [[volatility3-varredura-yarascan-memoria-virtual-fisica-extracao-dumps]] — Volatility 3: Caça em Memória com Regras YARA (`yarascan.YaraScan` / `windows.vadyarascan.VadYaraScan`) e Extração de Arquivos (`dumpfiles`)

### CAPEv2 Malware Sandbox — Detonação Dinâmica, API/Syscall Hooking, Debugger Programável por YARA e Extração de Configuração

- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — CAPEv2 Sandbox: Arquitetura de Detonação de Malware, *API/Syscall Hooking* (`capemon`) e Debugger Furtivo Programável
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — CAPEv2 Sandbox: Desempacotamento Dinâmico Automático (*Passive* vs *Active Unpacking* `unpacker=2`) e Captura de Injeções
- [[capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox]] — CAPEv2 Sandbox: Programação Dinâmica do Debugger via Assinaturas **YARA** (`meta: cape_options`) para Unpacking e Anti-Sandbox
- [[capev2-extracao-configuracao-malware-cape-parsers-maco-malduck]] — CAPEv2 Sandbox: Extração Estática e Dinâmica de Configuração de Malware (`CAPE-parsers`, `extract_config`, `MaCo` e `MalDuck`)
- [[capev2-captura-amsi-powershell-dotnet-syscall-hooking-nirvana]] — CAPEv2 Sandbox: Captura de Payloads **AMSI** (*Anti-Malware Scan Interface*), `.NET` / PowerShell / WSH e *Syscall Hooking* Anti-Evasão
- [[capev2-assinaturas-comportamentais-rede-suricata-mitre-attack]] — CAPEv2 Sandbox: Classificação Tripla — Assinaturas Comportamentais Python, Inspeção PCAP com **Suricata** e Mapeamento MITRE ATT&CK
- [[capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp]] — CAPEv2 Sandbox: Automação via **REST API v2** (`/apiv2/`, Autenticação por Token DRF, `throttling.py` e Integração com Cortex/MISP)
- [[capev2-anti-vm-hardening-kvm-qemu-acpi-smbios-human-interaction]] — CAPEv2 Sandbox: Hardening Anti-Detecção de VM (*Anti-VM Cloaking* em KVM/QEMU, SMBIOS/ACPI, Artefatos de Usuário e *Interactive Desktop*)
- [[capev2-roteamento-rede-inetsim-tor-vpn-isolamento-pcap]] — CAPEv2 Sandbox: Roteamento Por Tarefa (`route=inetsim`, `route=tor`, `route=vpn`, `route=none`) e Prevenção de Abuso Lateral
- [[capev2-integracao-memoria-volatility3-processamento-dumps-forenses]] — CAPEv2 Sandbox: Geração de Dumps Completos de Memória RAM (`memory=1`) e Pós-Processamento Integrado com **Volatility 3**

### Wireshark, TShark & Dumpcap — Análise Forense de Pacotes (PCAPNG), Filtros BPF vs Display, Decriptação TLS/Kerberos e Extração

- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Wireshark & `dumpcap`: Arquitetura de Separação de Privilégios, Formato Nativo **`pcapng`** e Isolamento da Superfície de Ataque de Dissecadores
- [[wireshark-tshark-filtros-captura-bpf-vs-display-filters-duas-passagens]] — `tshark`: Diferença entre Filtros de Captura **BPF** (`-f`) e **Display Filters** (`-Y` / `-R`), e Análise em Duas Passagens (`-2`)
- [[wireshark-extracao-campos-tshark-json-ek-fields-automacao-dfir]] — `tshark`: Extração Estruturada de Campos (`-T fields -e ...`, `-T json`, `-T ek`) para Triagem Rápida em Linha de Comando
- [[wireshark-estatisticas-forenses-tshark-z-conversations-io-follow]] — `tshark`: Estatísticas Forenses (`-q -z conv,tcp`, `-z io,phs`, `-z endpoints`, `-z dns,tree`, `-z http,tree`) e Reconstrução de Streams (`-z follow`)
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Wireshark & `tshark`: Decriptação Passiva de Tráfego **TLS 1.2/1.3** (`SSLKEYLOGFILE` e `editcap --inject-secrets`) e **Kerberos** (`keytab`)
- [[wireshark-extracao-arquivos-objetos-http-smb-dicom-tshark]] — Wireshark & `tshark`: Extração Forense de Arquivos e Payloads Transferidos via Rede (`--export-objects http,smb,tftp,imf`)
- [[wireshark-analise-ataques-active-directory-kerberos-ldap-smb-dcerpc]] — Wireshark & `tshark`: Filtros de Detecção de Ataques em Active Directory (Kerberos Roasting, `DCSync` `DRSUAPI`, NTLM Relay e `psexec`)
- [[wireshark-manipulacao-pcaps-editcap-mergecap-capinfos-reordercap]] — Utilitários de Manipulação Forense de PCAPs do Wireshark: `capinfos`, `editcap`, `mergecap` e `reordercap`
- [[wireshark-dissecadores-customizados-lua-protocolos-c2-proprietarios]] — Wireshark & `tshark`: Desenvolvimento de Dissecadores Customizados em **Lua** (`Proto`, `ProtoField`, `DissectorTable`) para Protocolos C2 Proprietários
- [[wireshark-captura-remota-sshdump-extcap-perfis-analise-soc]] — Wireshark & `tshark`: Captura Remota Segura via **Extcap (`sshdump` / `ciscodump`)** e Padronização de *Configuration Profiles* (`-C`) para o SOC

### Bettercap — Auditoria de Redes Ethernet IPv4/IPv6, WiFi 802.11, Bluetooth Low Energy (BLE), HID 2.4GHz, CAN-bus e Caplets

- [[bettercap-arquitetura-modulos-interativos-caplets-api-rest-websocket]] — Bettercap: Arquitetura em Go, Sessões Interativas, Automação Reprodutível com **Caplets (`.cap`)** e API REST / WebSocket (`api.rest`)
- [[bettercap-reconhecimento-rede-net-recon-net-probe-syn-scan]] — Bettercap: Reconhecimento de Host em Camada 2/3 (`net.recon`, `net.probe`, `net.show` e `syn.scan` Assíncrono)
- [[bettercap-auditoria-mitm-arp-spoof-ndp-spoof-dhcp6-defesas-l2]] — Bettercap: Auditoria de Resiliência de Camada 2 contra Spoofing (`arp.spoof`, `ndp.spoof`, `dhcp6.spoof`) e Validação de **DAI / RA Guard**
- [[bettercap-auditoria-dns-spoof-proxies-http-https-packet-proxy]] — Bettercap: Simulação de Redirecionamento DNS (`dns.spoof`) e Proxies Transparentes Scriptáveis (`http.proxy`, `https.proxy`, `tcp.proxy` e `packet.proxy`)
- [[bettercap-sniffer-rede-net-sniff-filtros-bpf-expressao-regular]] — Bettercap: Captura Seletiva e Inspeção de Tráfego com `net.sniff` (Filtros BPF, Expressões Regulares e Gravação PCAP)
- [[bettercap-auditoria-wifi-80211-recon-wpa-pmkid-80211w-pmf]] — Bettercap: Auditoria de Redes Sem Fio **WiFi 802.11** (`wifi.recon`, Descoberta de APs/Clientes, Captura EAPOL/PMKID e Validação de **802.11w PMF**)
- [[bettercap-auditoria-bluetooth-low-energy-ble-recon-enum-gatt]] — Bettercap: Auditoria de Dispositivos **Bluetooth Low Energy (BLE)** (`ble.recon`, `ble.show`, `ble.enum` e Inspeção de Características **GATT**)
- [[bettercap-auditoria-hid-24ghz-canbus-automotivo-dbc-industrial]] — Bettercap: Auditoria de Periféricos Sem Fio **2.4GHz HID** (`hid.recon`) e Barramentos Automotivos/Industriais **CAN-bus** (`can.recon` / Arquivos **DBC**)
- [[bettercap-monitoramento-eventos-events-stream-triggers-webhooks]] — Bettercap: Monitoramento de Eventos (`events.stream`), Filtros (`events.ignore`), Gatilhos Reativos (`events.on`) e Sensores de Honeypot L2
- [[bettercap-automacao-caplets-api-rest-tls-seguranca-operacional]] — Bettercap: Desenvolvimento de **Caplets (`.cap`)** Auditáveis, Hardening do Módulo `api.rest` e Governança de Escopo em Pentests

### Responder — Envenenamento LLMNR, NBT-NS, mDNS, DHCPv6 e WPAD, Captura NetNTLMv2/Kerberos, MultiRelay e Hardening Windows

- [[responder-arquitetura-envenenamento-llmnr-nbtns-mdns-analise-passiva]] — Responder: Arquitetura de Resolução de Nomes Multicast/Broadcast (**LLMNR** UDP 5355, **NBT-NS** UDP 137 e **mDNS** UDP 5353) e Modo Passivo (`-A`)
- [[responder-servidores-autenticacao-rogue-smb-http-ldap-mssql-ntlmv2]] — Responder: Servidores de Autenticação *Rogue* Integrados (SMB, HTTP/HTTPS, LDAP, MSSQL, SMTP/IMAP, WinRM, RDP) e Captura **NetNTLMv1/v2**
- [[responder-captura-kerberos-asrep-roasting-force-ntlm-downgrade]] — Responder: Servidor Kerberos Integrado (`KerberosMode = CAPTURE` vs `FORCE_NTLM` via `KDC_ERR_ETYPE_NOSUPP`)
- [[responder-envenenamento-ipv6-dhcpv6-dns-takeover-wpad-mitigacao]] — Responder: Auditoria de **DHCPv6 DNS Takeover** (`--dhcpv6`, `SendRA`) e Descoberta Automática de Proxy **WPAD** (`-w` / `-P`)
- [[responder-escopo-responder-conf-respondto-dontrespondto-autoignore]] — Responder: Controle Estrito de Escopo em `Responder.conf` (`RespondTo`, `DontRespondTo`, `RespondToName`, `DontRespondToTLD` e `AutoIgnoreAfterSuccess`)
- [[responder-fluxo-ntlm-relay-desativar-smb-http-ntlmrelayx-multirelay]] — Responder & `ntlmrelayx.py`: Desativação dos Servidores `SMB` e `HTTP` no `Responder.conf` para **NTLM Relay** em Tempo Real
- [[responder-utilitarios-runfinger-findsqlsrv-icmp-redirect-multirelay]] — Ferramentas Auxiliares da Suíte Responder (`tools/RunFinger.py`, `tools/FindSQLSrv.py` e `tools/MultiRelay.py`)
- [[responder-auditoria-offline-senhas-hashcat-netntlmv2-netntlmv1-regras]] — Auditoria de Força de Senhas sobre Hashes Capturados pelo Responder (`NetNTLMv2` Hashcat `-m 5600` vs `NetNTLMv1` `-m 5500`)
- [[responder-deteccao-blue-team-suricata-zeek-sysmon-canary-queries]] — Detecção de Envenenamento LLMNR/NBT-NS/mDNS/DHCPv6 pelo **Blue Team** (Suricata, Zeek, Windows Event Logs e *Canary Name Queries*)
- [[responder-defesa-hardening-gpo-desativar-llmnr-nbtns-wpad-smb-signing]] — Hardening Definitivo do Windows e Active Directory contra o Responder (Desativar **LLMNR**, **NBT-NS**, **mDNS**, **WPAD** e Exigir **SMB/LDAP Signing**)

### Fortra Impacket — Pilha de Protocolos de Rede Windows (SMB1-3, MSRPC, Kerberos, LDAP, TDS), Exemplos e Defesas de AD

- [[impacket-arquitetura-biblioteca-protocolos-rede-smb-msrpc-kerberos]] — Fortra Impacket: Arquitetura da Biblioteca Python de Protocolos de Rede (`ImpactPacket`, `SMBConnection`, `DCERPC v5`, `Kerberos` e `LDAP`)
- [[impacket-ataques-kerberos-getnpusers-getuserspns-ticketer-silver-golden]] — Impacket: Auditoria de Protocolo Kerberos (`GetNPUsers.py` AS-REP Roasting, `GetUserSPNs.py` Kerberoasting, `getTGT.py`, `getST.py` e `ticketer.py`)
- [[impacket-execucao-remota-psexec-smbexec-wmiexec-atexec-dcomexec-opsec]] — Impacket: Comparação Forense e de OPSEC dos 5 Métodos de Execução Remota (`psexec.py`, `smbexec.py`, `wmiexec.py`, `atexec.py` e `dcomexec.py`)
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Impacket: Auditoria de Extração de Credenciais com `secretsdump.py` (`SAM` / `LSA Secrets` Remotos, Parsing Offline de `NTDS.dit` e **`DCSync`** `DRSUAPI`)
- [[impacket-retransmissao-ntlmrelayx-smb-ldap-adcs-esc8-rbcd-shadow-credentials]] — Impacket: Retransmissão Multiprocolo com `ntlmrelayx.py` (SMB, LDAP/LDAPS, HTTP **AD CS ESC8**, *RBCD*, *Shadow Credentials* e SOCKS Proxy)
- [[impacket-enumeracao-msrpc-rpcdump-samrdump-lookupsid-netview-services]] — Impacket: Enumeração MSRPC e Controle de Serviços (`rpcdump.py`, `samrdump.py`, `lookupsid.py`, `netview.py`, `reg.py` e `services.py`)
- [[impacket-cliente-mssqlclient-xp-cmdshell-linked-servers-trusted-links]] — Impacket: Auditoria de Microsoft SQL Server com `mssqlclient.py` (Autenticação Windows/SQL, `enable_xp_cmdshell`, *Impersonation* `EXECUTE AS` e *Linked Servers*)
- [[impacket-compartilhamentos-smbclient-smbserver-transferencia-segura-smb2]] — Impacket: Inspeção de Compartilhamentos com `smbclient.py` e Servidor SMB Efêmero com `smbserver.py` (`-smb2support` e Autenticação)
- [[impacket-gestao-contas-acl-addcomputer-dacledit-rbcd-laps-dpapi]] — Impacket: Auditoria de Objetos de Diretório e Criptografia (`addcomputer.py`, `dacledit.py`, `rbcd.py`, `GetLAPSPassword.py` e **`dpapi.py`**)
- [[impacket-desenvolvimento-scripts-customizados-dcerpc-smbconnection-pytest]] — Impacket: Desenvolvimento de Scripts de Auditoria em Python com `SMBConnection` e `DCERPCTransportFactory`, e Suíte de Testes `pytest` / `tox`

### NetExec (nxc) — Auditoria Multi-Protocolo de Redes Corporativas e Active Directory (SMB, LDAP, WinRM, WMI, MSSQL, SSH, RDP)

- [[netexec-arquitetura-sucessor-crackmapexec-protocolos-nxcdb-workspaces]] — NetExec (`nxc` & `nxcdb`): Arquitetura do Sucessor Open-Source do CrackMapExec, Protocolos Suportados e Isolamento por *Workspaces*
- [[netexec-protocolo-smb-enumeracao-signing-shares-sessoes-disks]] — NetExec (`nxc smb`): Mapeamento de Sub-Redes SMB, Verificação de `signing:False` / `SMBv1:True`, Compartilhamentos (`--shares`) e Sessões (`--sessions`)
- [[netexec-auditoria-credenciais-password-spraying-pass-the-hash-lockout]] — NetExec: Auditoria de Reutilização de Credenciais Locais (*LAPS Audit*), *Pass-the-Hash* (`-H`) e *Password Spraying* Seguro (`--no-bruteforce` / `--continue-on-success`)
- [[netexec-protocolo-ldap-kerberoasting-asreproast-bloodhound-delegacao]] — NetExec (`nxc ldap`): Auditoria de Active Directory via LDAP/LDAPS (`--kerberoasting`, `--asreproast`, `--trusted-for-delegation`, `--gmsa` e `--bloodhound`)
- [[netexec-autenticacao-kerberos-ccache-aeskey-kdchost-opsec]] — NetExec: Operação 100% Kerberos (`-k`, `--use-kcache`, `--aesKey` e `--kdcHost`) em Redes com NTLM Restrito
- [[netexec-protocolos-winrm-wmi-execucao-remota-powershell-dpapi]] — NetExec (`nxc winrm` & `nxc wmi`): Auditoria de Gerenciamento Remoto Windows (WS-Management Portas `5985`/`5986` e WMI) e Execução (`-x` / `-X`)
- [[netexec-protocolos-mssql-ssh-rdp-ftp-vnc-auditoria-multi-servico]] — NetExec (`nxc mssql`, `ssh`, `rdp`, `ftp`, `vnc`): Auditoria Multiprocolo Híbrida Windows/Linux, Capturas de Tela RDP e Privileged Escalation
- [[netexec-modulos-auditoria-adcs-petitpotam-nopac-zerologon-slinky]] — NetExec: Catálogo de Módulos (`-M` / `--list-modules`) para Auditoria de **AD CS**, **Coerção RPC** (`coerce_plus`), **WebDAV** e **LAPS**
- [[netexec-gerenciamento-banco-nxcdb-credenciais-hosts-exportacao]] — NetExec (`nxcdb`): Consulta Estruturada do Banco de Dados de Auditoria (`hosts`, `creds`, `admin`, `shares`) e Reutilização por ID (`-id`)
- [[netexec-deteccao-blue-team-telemetria-windows-zeek-suricata-hardening]] — Detecção do NetExec pelo **Blue Team** (Correlação de Eventos Windows `4624`/`4625`/`5140`/`5145`/`4697`, Zeek e Hardening de Tiering AD)

## Tranche 7 (IDs 601–700)

### testssl.sh — Auditoria de Criptografia TLS/SSL, Protocolos, Cifras PFS, STARTTLS, Simulação de Clientes e Vulnerabilidades

- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — `testssl.sh`: Arquitetura de Auditoria de Servidores TLS/SSL via Sockets TCP Nativo e Binários OpenSSL Estáticos
- [[testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn]] — `testssl.sh`: Verificação de Versões de Protocolo (`-p` — SSLv2/SSLv3/TLS 1.0/1.1/1.2/1.3, QUIC/HTTP3 e ALPN)
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — `testssl.sh`: Auditoria de Categorias de Cifras (`-s` / `-E`), **Forward Secrecy** (`-f`), Curvas Elípticas e Híbridas Pós-Quânticas (**ML-KEM**)
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — `testssl.sh`: Auditoria de Certificados X.509 (`-S`), Cadeia de Confiança, **OCSP Stapling**, *Certificate Transparency* e Registros **DNS CAA**
- [[testssl-vulnerabilidades-criptograficas-heartbleed-robot-drown-poodle-logjam]] — `testssl.sh`: Varredura de Vulnerabilidades Criptográficas TLS (`-U` — Heartbleed, ROBOT,Ticketbleed, CCS, DROWN, POODLE, Sweet32, FREAK, Logjam e CRIME/BREACH)
- [[testssl-auditoria-starttls-smtp-imap-pop3-ldap-postgres-xmpp]] — `testssl.sh`: Auditoria de Criptografia Oportunista e Obrigatória via **`STARTTLS`** (`-t smtp,imap,pop3,ftp,ldap,postgres,mysql,xmpp`)
- [[testssl-cabecalhos-seguranca-http-hsts-hpkp-cookies-banners]] — `testssl.sh`: Inspeção de Cabeçalhos de Segurança HTTP (`-h` — HSTS, CSP, X-Frame-Options, Cookies `Secure`/`HttpOnly` e Banners de Servidor)
- [[testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl]] — `testssl.sh`: Simulação de Handshake de Clientes (`-c` / `--client-simulation`) e Cálculo de **Rating Qualys SSL Labs** (`--rating`)
- [[testssl-varredura-massa-file-nmap-gnmap-parallel-json-html-csv]] — `testssl.sh`: Varredura em Massa (`--file` / `-iL`, Entrada Nmap `-oG`), Execução Paralela (`--parallel`) e Relatórios Estruturados (`--jsonfile`, `--csvfile`, `--htmlfile`)
- [[testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd]] — `testssl.sh`: Teste de VirtualHosts (`--ip` / `--SNI`), Autenticação Mútua **mTLS** (`--mtls`), Modo Discreto (`--sneaky`) e Gate de CI/CD

### EFF Certbot & Protocolo ACME (RFC 8555) — Emissão/Renovação Automatizada X.509, Desafios HTTP-01/DNS-01, Hooks e ARI

- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — EFF Certbot & Protocolo **ACME (RFC 8555)**: Arquitetura de Conta, Separação entre *Authenticators* e *Installers* e Estrutura `/etc/letsencrypt/`
- [[certbot-validacao-http01-webroot-standalone-nginx-apache-seguranca]] — Certbot: Validação de Domínio **`HTTP-01`** (`--webroot`, `--standalone`, `--nginx`, `--apache`) e Operação sem Interrupção de Serviço
- [[certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns]] — Certbot: Validação **`DNS-01`** para Certificados *Wildcard* e Isolamento de Credenciais DNS com **Delegação `CNAME` (`acme-dns`)**
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Certbot: Automação de Renovação (`certbot renew`), `systemd` Timers e Diferença entre `--pre-hook`, `--post-hook` e **`--deploy-hook`**
- [[certbot-chaves-ecdsa-p256-p384-rsa-ocsp-must-staple-reuse-key]] — Certbot: Criptografia de Chave Pública (**ECDSA `secp256r1` / `secp384r1`** vs RSA), `--reuse-key` e `--must-staple`
- [[certbot-acme-renewal-information-ari-revogacao-comprometimento-chave]] — Certbot: Suporte a **ARI (*ACME Renewal Information*)**, Resposta a Incidentes de Comprometimento de Chave e `certbot revoke`
- [[certbot-integracao-cas-privadas-eab-external-account-binding-server]] — Certbot: Uso com CAs Corporativas e Comerciais via **`--server`** e **EAB (*External Account Binding*)** (`--eab-kid` / `--eab-hmac-key`)
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Governança de Emissão ACME: Registros **DNS CAA (`issue`, `issuewild`, `iodef`, `accounturi`)** (RFC 8659 / RFC 8657) e *Certificate Transparency*
- [[certbot-hardening-nginx-apache-ssl-config-perfis-intermediate-modern]] — Certbot: Perfis de Configuração TLS gerados para Nginx/Apache (`options-ssl-nginx.conf`), *Session Tickets* e **Mozilla SSL Configuration Generator**
- [[certbot-execucao-containers-docker-volumes-permissoes-rootless]] — Certbot: Execução Isolada em Containers Docker (`certbot/certbot`), Volumes Persistentes e Operação *Non-Root* (`--config-dir`, `--work-dir`, `--logs-dir`)

### Hashcat — Auditoria de Resistência de Senhas e Hashes em GPU, Modos de Ataque, Motor de Regras In-Kernel, Máscaras e Hashcat Brain

- [[hashcat-arquitetura-gpu-opencl-cuda-hip-metal-in-kernel-rules]] — Hashcat: Arquitetura de Auditoria de Senhas em GPU (Backends CUDA/HIP/Metal/OpenCL), *In-Kernel Rule Engine* e Perfis de Carga (`-w`)
- [[hashcat-modos-ataque-dicionario-combinator-mask-hybrid-pcfg]] — Hashcat: Os Modos de Ataque (`-a 0` Wordlist, `-a 1` Combinator, `-a 3` Mask/Brute-Force, `-a 6`/`-a 7` Hybrid e `-a 9` Association)
- [[hashcat-motor-regras-in-kernel-funcoes-mutacao-depuracao-regras]] — Hashcat: Linguagem de Regras de Mutação (`-r`, `-j`, `-k`), *Multi-Rules* e Estatísticas de Eficiência (`--debug-mode`)
- [[hashcat-ataques-mascara-charsets-customizados-hcchr-markov-increment]] — Hashcat: Ataques de Máscara (`-a 3`), *Custom Charsets* (`-1` a `-4`), Arquivos `.hcmask` e Ordenação por **Cadeias de Markov**
- [[hashcat-auditoria-active-directory-ntds-kerberoasting-asrep-dcc2]] — Hashcat: Modos de Hash para Auditoria de Active Directory (`-m 1000` NTLM, `-m 3000` LM, `-m 5600` NetNTLMv2, `-m 13100`/`19700` Kerberoast, `-m 18200` AS-REP e `-m 2100` DCC2)
- [[hashcat-hashcat-brain-sessoes-distribuicao-potfile-encrypted-plains]] — Hashcat: Operação Avançada — **Hashcat Brain** (`--brain-server` / `--brain-client`), Sessões (`--session` / `--restore`) e **Encrypted Plains**
- [[hashcat-extensibilidade-assimilation-bridge-plugins-python-rust-c]] — Hashcat v7+: **Assimilation Bridge** para Criação de Novos Modos de Hash em **Python, Rust ou C** sem Escrever Kernels GPU
- [[hashcat-ataques-pcfg-probabilistic-context-free-grammar-slow-candidates]] — Hashcat: Geração Gramatical com **PCFG (*Probabilistic Context-Free Grammar*)** e Modo **`--slow-candidates` (`-S`)**
- [[hashcat-mapeamento-teclado-hex-salt-compressao-arquivos-fde]] — Hashcat: Mapeamento de Layout de Teclado (`--keyboard-layout-mapping`), `--hex-salt` e Leitura Transparente de Wordlists Comprimidas (`.gz`, `.xz`, `.zst`)
- [[hashcat-defesa-engenharia-armazenamento-senhas-argon2id-bcrypt-scrypt-passphrases]] — Defesa Contra Quebra Offline em GPU: Engenharia de Armazenamento de Senhas com **Argon2id (RFC 9106)**, `bcrypt`/`scrypt`, *Pepper* em HSM/KMS e *Passphrases*

### NSA Ghidra — Engenharia Reversa de Software (SRE), Descompilador, SLEIGH/P-Code, analyzeHeadless, PyGhidra e BSim

- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — NSA Ghidra: Arquitetura de Engenharia Reversa de Software (SRE), Linguagem **SLEIGH**, Representação Intermediária **P-Code** e Descompilador
- [[ghidra-representacao-intermediaria-pcode-analise-fluxo-dados-varnodes]] — Ghidra: Análise de Fluxo de Dados (*Data-Flow / Taint Analysis*) sobre **P-Code** (`Varnode`, `PcodeOp`, *HighFunction* e *SSA Form*)
- [[ghidra-automacao-cli-analyzeheadless-importacao-scripts-lote]] — Ghidra: Automação em Linha de Comando e Pipelines CI/DFIR com **`analyzeHeadless`** (`-import`, `-preScript`, `-postScript` e `-readOnly`)
- [[ghidra-scripting-pyghidra-cpython3-flatprogramapi-automacao]] — Ghidra: Desenvolvimento de Scripts em **Python 3 Nativo (`PyGhidra`)** e Uso da **`FlatProgramAPI`**
- [[ghidra-reconstrucao-tipos-structs-classes-cpp-rtti-vtables-pdb-dwarf]] — Ghidra: Reconstrução de Estruturas C (`Data Type Manager`), Classes C++ (`RTTI` / `vtable`), *Parse C Source* e Símbolos **PDB / DWARF**
- [[ghidra-identificacao-funcoes-estaticas-functionid-fidb-bsim]] — Ghidra: Reconhecimento de Bibliotecas Estáticas com **FunctionID (`fidb`)** e Busca Vetorial de Similaridade Comportamental com **BSim**
- [[ghidra-engenharia-reversa-firmware-bare-metal-memory-map-svd]] — Ghidra: Engenharia Reversa de **Firmware Embarcado / Bare-Metal** (Descoberta de *Base Address*, *Memory Map* MMIO e Arquivos CMSIS **SVD**)
- [[ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware]] — Ghidra: Emulação Segura de Código com **`EmulatorHelper`** (Execução de P-Code para Desofuscação de Strings sem Executar o Malware)
- [[ghidra-colaboracao-ghidraserver-version-tracking-patch-diffing]] — Ghidra: Engenharia Reversa Colaborativa com **GhidraServer** e Análise de Patches (*Patch Diffing*) com **Version Tracking (`VT`)**
- [[ghidra-depurador-dinamico-debugger-gdb-lldb-dbgeng-trace-time-travel]] — Ghidra: **Ghidra Debugger** — Depuração Dinâmica Híbrida (`gdb`, `lldb`, Windows `dbgeng`) e *Time-Travel / Trace Recording*

### Radare2 (r2) — Framework de Análise Binária, rabin2, radiff2, rasm2, Grafo de Fluxo de Controle, Emulação ESIL e r2pipe

- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Radare2 (`r2`): Arquitetura Unix-First de Engenharia Reversa, Comandos Hierárquicos, Filtro Interno `~` e Iterador `@`
- [[radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings]] — Radare2 (`rabin2`): Triagem Estática de Executáveis, Auditoria de Mitigações de Compilador (**NX**, **Canary**, **PIE**, **RELRO**) e Extração de Símbolos/Strings
- [[radare2-analise-fluxo-controle-aaa-grafos-cfg-xrefs-decompiler-pdg]] — Radare2 (`r2`): Análise de Código (`aaa`), Grafos de Fluxo de Controle (`agf` / `agfj`), Referências Cruzadas (`axt` / `axf`) e Descompilação (`pdg`)
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Radare2: Emulação Segura com **ESIL (*Evaluable Strings Intermediate Language*)** (`aei`, `aeim`, `aes`, `aeso` e `emu.str=true`)
- [[radare2-comparacao-binarios-patch-diffing-radiff2-assinaturas-zignatures]] — Radare2 (`radiff2` & Zignatures `z`): *Patch Diffing* de Binários (`-g`, `-AC`) e Reconhecimento de Funções com **Zignatures**
- [[radare2-busca-padroes-rafind2-rahash2-entropia-secoes-empacotamento]] — Radare2 (`rafind2` & `rahash2`): Caça de Padrões Binários/ROP Gadgets e Cálculo de **Entropia por Blocos** para Detecção de *Packers* e Chaves
- [[radare2-montador-desmontador-rasm2-rax2-analise-shellcode]] — Radare2 (`rasm2` & `rax2`): Montagem/Desmontagem Multi-Arquitetura de **Shellcodes** e Conversão de Representações Numéricas/Binárias
- [[radare2-automacao-scripting-r2pipe-python-javascript-qjs]] — Radare2 (`r2pipe` & QuickJS `-j`): Automação Programática de Engenharia Reversa em Python e JavaScript Nativo
- [[radare2-depuracao-reversivel-checkpoints-dts-rarun2-gdb-frida]] — Radare2: Depuração Reversível (*Time-Travel Checkpoints* `dts+`/`dtsc`/`dtsr`), Perfis de Execução **`rarun2`** e Integração **`r2frida`**
- [[radare2-integracao-yara-r2yara-r2sarif-projetos-auditoria]] — Radare2: Geração de Regras YARA Baseadas em Opcodes (`r2yara` / `pcy`), Exportação **SARIF** (`r2sarif`) e Gestão de Projetos

### Frida — Instrumentação Dinâmica de Binários e Apps Mobile (Gum, Interceptor, Stalker, Java/ObjC Bridges, Gadget e CModule)

- [[frida-arquitetura-instrumentacao-dinamica-gum-v8-quickjs-modos]] — Frida: Arquitetura de Instrumentação Dinâmica (`frida-core`, `frida-gum`, Runtimes **QuickJS/V8**) e Modos *Injected*, *Embedded (`frida-gadget`)* e *Preloaded*
- [[frida-hooking-nativo-interceptor-attach-replace-nativefunction-nativepointer]] — Frida: Hooking de Funções Nativas C/C++/Rust/Go com **`Interceptor.attach`**, `Interceptor.replace`, `NativePointer` e `NativeFunction`
- [[frida-rastreamento-instrucoes-stalker-code-tracing-coverage-cmodule]] — Frida: Rastreamento Dinâmico de Instruções e Cobertura com **`Stalker`** (*Dynamic Binary Translation*) e Alta Performance com **`CModule`**
- [[frida-instrumentacao-mobile-android-java-perform-ios-objc-ssl-pinning]] — Frida: Auditoria de Segurança Mobile (**OWASP MASVS**) — Pontes **`Java.perform`** (Android ART/Dalvik) e **`ObjC.classes`** (iOS/macOS Objective-C)
- [[frida-inspecao-memoria-memory-scan-memoryaccessmonitor-apiresolver]] — Frida: Varredura de Memória em Tempo Real (`Memory.scan`, `Process.enumerateRanges`), **`MemoryAccessMonitor`** e **`ApiResolver`**
- [[frida-cli-frida-trace-frida-discover-autogenerated-handlers]] — Ferramentas CLI do Frida: Rastreamento Instantâneo com **`frida-trace`** (`-i`, `-I`, `-a`, `-j`, `-m`) e **`frida-discover`**
- [[frida-comunicacao-bidirecional-rpc-exports-send-recv-python-host]] — Frida: Comunicação Bidirecional Host-Agente (`send`/`recv`) e Exposição de Funções Internas como **API RPC (`rpc.exports`)** em Python
- [[frida-empacotamento-frida-gadget-configuracao-sem-root-jailbreak]] — Frida: Instrumentação sem Root/Jailbreak com **`frida-gadget`** e Modos de Operação (`listen`, `connect`, `script`, `script-directory`)
- [[frida-desempacotamento-memoria-malware-dex-pe-elf-dumping]] — Frida: Extração Dinâmica de Payloads Desempacotados em Memória (DEX Android, Módulos PE/ELF e Strings Decifradas)
- [[frida-furtividade-cloak-anti-frida-deteccao-defesa-runtimes]] — Frida: Subsistema **`Cloak`** e Engenharia de Detecção Anti-Instrumentação vs Bypass em Aplicações Críticas

### Fail2ban — Prevenção de Intrusão Baseada em Logs, Jails, Filtros Seguros contra ReDoS, Actions nftables/ipset e Backoff

- [[fail2ban-arquitetura-daemon-precedencia-conf-local-sqlite-client]] — Fail2ban: Arquitetura do Daemon, Ordem Estrita de Precedência (`*.conf` vs `*.local`) e Operação via **`fail2ban-client`**
- [[fail2ban-configuracao-jails-bantime-findtime-maxretry-ignoreip]] — Fail2ban: Anatomia de uma **Jail** (`findtime`, `maxretry`, `bantime`, `ignoreip`, `ignoreself` e `backend = systemd`)
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Fail2ban: Escrita Segura de Filtros (`failregex`, `ignoreregex`, `<HOST>` vs `<ADDR>`) e Prevenção de **ReDoS** e *Log Injection*
- [[fail2ban-testes-performance-fail2ban-regex-benchmark-logs]] — Fail2ban: Validação e Benchmark de Expressões Regulares com **`fail2ban-regex`** antes do Deploy em Produção
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Fail2ban: Escalabilidade de Firewall com Sets **`nftables` / `ipset`**, *Exponential Backoff* (`bantime.increment`) e Jail **`recidive`**
- [[fail2ban-protecao-proxies-reversos-nginx-http-auth-limit-req-xff]] — Fail2ban: Proteção de Proxies Reversos **Nginx / Envoy** (`nginx-http-auth`, `nginx-limit-req`, `nginx-botsearch`) e Cuidados com `X-Forwarded-For`
- [[fail2ban-agrupamento-sessoes-tags-f-mlfid-f-id-no-failure]] — Fail2ban: Correlação Multi-Linha com Tags de Sessão (**`<F-MLFID>`**, **`<F-ID>`**, **`<F-NOFAIL>`**) para Daemons que Logam IP e Falha em Linhas Separadas
- [[fail2ban-acoes-customizadas-webhooks-thehive-abuseipdb-observabilidade]] — Fail2ban: Desenvolvimento de **Actions (`action.d/`)** Customizadas, Integração com Webhooks SOC/TheHive e Métricas Prometheus
- [[fail2ban-operacao-administrativa-ban-unban-manual-dbpurgeage]] — Fail2ban: Operação de Resposta a Incidentes via `fail2ban-client` (`set <jail> banip`, `unbanip`, `unban --all` e Auditoria SQLite)
- [[fail2ban-limites-arquiteturais-defesa-em-profundidade-ssh-mfa-wireguard]] — Fail2ban: Limites Arquiteturais (*Rate Limiting* vs Autenticação Forte), *IPv6 Subnet Banning* e Defesa em Profundidade

### Sudo (sudo & sudo_logsrvd) — Delegação de Privilégios no Linux/Unix, sudoers, SHA-256 Digest Pinning, NOEXEC, sudoedit e I/O Logging

- [[sudo-arquitetura-plugins-sudoers-visudo-menor-privilegio]] — Sudo (`sudo`): Arquitetura Modular de Plugins (`sudo.conf`, `sudoers.so`), Validação Sintática com **`visudo -c`** e Menor Privilégio
- [[sudo-gramatica-regras-sudoers-aliases-ordem-precedencia-ultima-regra]] — Sudoers: Gramática de Especificação de Comandos, Aliases (`User_Alias`, `Runas_Alias`, `Host_Alias`, `Cmnd_Alias`) e a Regra **"Last Match Wins"**
- [[sudo-integridade-binarios-sha256-digest-pinning-scripts-administrativos]] — Sudoers: Pinagem Criptográfica de Binários e Scripts com **SHA-224 / SHA-256 / SHA-384 / SHA-512 Digest** no `/etc/sudoers`
- [[sudo-prevencao-gtfobins-noexec-sudoedit-restricao-argumentos-curingas]] — Sudoers: Prevenção de Escalação de Privilégio (**GTFOBins**) — Uso da Tag **`NOEXEC:`**, **`sudoedit` (`sudo -e`)** e Perigos do Curinga `*`
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Sudoers: Hardening de `Defaults` — **`env_reset`**, **`secure_path`**, **`use_pty`**, `timestamp_type=tty` e `passwd_tries`
- [[sudo-auditoria-io-logging-log-input-log-output-sudoreplay]] — Sudo: Gravação Forense Completa de Sessões de Terminal (**I/O Logging** `log_input`, `log_output`, `log_subcmds`) e Reprodução com **`sudoreplay`**
- [[sudo-centralizacao-logs-sudo-logsrvd-tls-mtls-imutabilidade]] — Sudo (`sudo_logsrvd`): Transmissão Centralizada em Tempo Real de Logs de Eventos e I/O via TLS Mútuo (**mTLS**) contra Adulteração Local
- [[sudo-plugins-python-aprovacao-just-in-time-politicas-customizadas]] — Sudo 1.9+: Extensão de Políticas e Auditoria com **`sudo_python.so`** (Aprovação *Just-In-Time*, Checagem de Chamados no TheHive/Jira e Contexto)
- [[sudo-restricoes-chroot-runchroot-runcwd-selinux-role-type-apparmor]] — Sudoers: Confinamento de Comandos Delegados com SELinux (`ROLE=` / `TYPE=`), AppArmor (`APPARMOR_PROFILE=`) e `RUNCHROOT=` / `RUNCWD=`
- [[sudo-auditoria-superficie-ataque-cve-2021-3156-cve-2023-22809-alternativas]] — Auditoria da Superfície de Ataque do Sudo (Lições de `CVE-2021-3156` *Baron Samedit* e `CVE-2023-22809`), `nosuid` e Alternativas Mínimas

### Bubblewrap (bwrap) — Sandboxing Linux sem Privilégios, User/Mount/PID/Net Namespaces, PR_SET_NO_NEW_PRIVS, TIOCSTI e Seccomp

- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Bubblewrap (`bwrap`): Arquitetura de Sandboxing sem Privilégios no Linux, **User Namespaces (`CLONE_NEWUSER`)** e **`PR_SET_NO_NEW_PRIVS`**
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Bubblewrap (`bwrap`): Construção Zero-Trust do Sistema de Arquivos (`--ro-bind`, `--bind`, `--tmpfs`, `--proc`, `--dev`, `--dir` e `--file`)
- [[bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback]] — Bubblewrap (`bwrap`): Isolamento de Namespaces (`--unshare-all`, `--unshare-net`, `--unshare-pid`), *Reaping* de Zumbis (**PID 1**) e `--disable-userns`
- [[bubblewrap-isolamento-terminal-new-session-tiocsti-die-with-parent]] — Bubblewrap (`bwrap`): Proteção contra Injeção de Comandos no Terminal (**`CVE-2017-5226` / `TIOCSTI`** via **`--new-session`**) e **`--die-with-parent`**
- [[bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop]] — Bubblewrap (`bwrap`): Restrição de Syscalls do Kernel via **`--seccomp FD`** (`--add-seccomp-fd`) e Remoção de Capabilities (`--cap-drop ALL`)
- [[bubblewrap-higienizacao-variaveis-ambiente-clearenv-setenv-unsetenv]] — Bubblewrap (`bwrap`): Higienização de Variáveis de Ambiente (`--clearenv`, `--setenv`, `--unsetenv`), `--chdir` e Controle de `argv[0]`
- [[bubblewrap-prevencao-escape-sockets-dbus-x11-wayland-xdg-dbus-proxy]] — Bubblewrap (`bwrap`): Prevenção de Escape de Sandbox via Sockets do Host (**D-Bus**, **X11**, Docker Socket, `ssh-agent`) e Uso do **`xdg-dbus-proxy`**
- [[bubblewrap-monitoramento-ciclo-vida-info-fd-json-status-fd-block-fd]] — Bubblewrap (`bwrap`): Sincronização e Observabilidade Programática (`--info-fd`, `--json-status-fd`, `--block-fd`, `--sync-fd` e `--args FD`)
- [[bubblewrap-injecao-arquivos-memoria-file-bind-data-ro-bind-data]] — Bubblewrap (`bwrap`): Injeção Efêmera de Configurações e Segredos em Memória via Descritores de Arquivo (`--ro-bind-data FD DEST`, `--bind-data` e `--perms`)
- [[bubblewrap-confinamento-workers-conversao-arquivos-limites-cgroups-systemd]] — Bubblewrap (`bwrap`) + `systemd-run`: Defesa contra Negação de Serviço (Fork Bombs / Exaustão de RAM) com **cgroups v2** e `AppArmor` para `bwrap`

### Project Quay Clair v4 & ClairCore — Análise Estática de Vulnerabilidades em Imagens de Containers OCI/Docker, Indexer, Matcher e Notifier

- [[clair-arquitetura-analise-estatica-containers-claircore-indexer-matcher-notifier]] — Project Quay **Clair v4 & `ClairCore`**: Arquitetura de Análise Estática de Imagens OCI/Docker (`Indexer`, `Matcher` e `Notifier`)
- [[clair-fluxo-indexacao-content-addressable-manifest-layers-indexreport]] — Clair v4 (`Indexer` & `ClairCore`): Indexação Endereçada por Conteúdo de Manifestos OCI, Deduplicação de Camadas e `IndexReport`
- [[clair-scanners-pacotes-os-dpkg-rpm-apk-linguagens-gobin-python-java]] — ClairCore: Matriz de Scanners de Pacotes de Sistema Operacional (`dpkg`, `rpm`, `apk`) e Linguagens (`gobin`, `python`, `java`, `nodejs`, `ruby`, `rust`)
- [[clair-motor-matching-updaters-fontes-ovals-osv-cvss-enrichment]] — Clair v4 (`Matcher`): Atualizadores Contínuos de Feeds de Segurança (OVAL, **OSV**, Red Hat VEX/CSAF, Debian/Ubuntu/Alpine SecDB e NVD CVSS Enrichment)
- [[clair-servico-notificacao-notifier-webhooks-novos-cves-imagens-antigas]] — Clair v4 (`Notifier`): Detecção Proativa de **Novos CVEs** em Imagens Já Implantadas e Entrega Confiável via **Webhooks / AMQP / STOMP**
- [[clair-cli-clairctl-client-submissao-manifestos-exportacao-offline]] — Clair v4 (`clairctl`): Operação via Linha de Comando (`clairctl report`, `export-updaters` / `import-updaters`) para CI/CD e Ambientes *Air-Gapped*
- [[clair-implantacao-combo-vs-microservicos-postgresql-escalabilidade]] — Clair v4: Modos de Implantação (`combo` vs Microsserviços `indexer`/`matcher`/`notifier`), Dimensionamento de PostgreSQL e Coordenação via `clair-lock`
- [[clair-autenticacao-seguranca-api-psk-jwt-tls-introspeccao]] — Clair v4: Hardening da API — Autenticação **JWT com Pre-Shared Key (`auth.psk`)**, TLS Mútuo e Isolamento da Porta de Introspecção
- [[clair-enriquecimento-cvss-severidade-normalizada-priorizacao-remediacao]] — Clair v4: Normalização de Severidade (`Unknown`, `Negligible`, `Low`, `Medium`, `High`, `Critical`), Enriquecimento CVSS e Priorização
- [[clair-integracao-project-quay-harbor-admission-controllers-vex]] — Clair v4: Integração Nativa com **Project Quay**, Políticas de **Kubernetes Admission Control** e Redução de Superfície com Imagens Mínimas

## Tranche 8 (IDs 701–800)

### GNU Privacy Guard (GnuPG / gpg) — OpenPGP (RFC 4880/9580), Subchaves, gpg-agent, scdaemon YubiKey/Smartcards, gpgv e Git Signing

- [[gnupg-arquitetura-openpgp-gpg2-gpg-agent-scdaemon-dirmngr]] — GNU Privacy Guard (**GnuPG 2.x**): Arquitetura Modular (`gpg`, `gpg-agent`, `scdaemon`, `dirmngr` e `keyboxd`) e Padrão **OpenPGP (RFC 4880 / RFC 9580)**
- [[gnupg-hierarquia-chave-mestra-certify-offline-subchaves-sign-encrypt-auth]] — GnuPG: Arquitetura de **Chave Mestra `[C]` Offline** e **Subchaves Operacionais (`[S]` Sign, `[E]` Encrypt, `[A]` Authenticate)** em Curvas **Ed25519 / Cv25519**
- [[gnupg-smartcards-yubikey-openpgp-scdaemon-card-edit-keytocard]] — GnuPG & **`scdaemon`**: Armazenamento de Subchaves em Hardware (**YubiKey / SmartCard OpenPGP v3.4**), `keytocard` e Proteção de PIN/KDF
- [[gnupg-operacao-gpg-agent-pinentry-cache-ttl-ssh-agent-socket]] — GnuPG (`gpg-agent`): Configuração de Cache (`default-cache-ttl`, `max-cache-ttl`), Emulação **`enable-ssh-support`** e *Agent Forwarding* Remoto
- [[gnupg-verificacao-assinaturas-pacotes-gpgv-status-fd-automacao]] — GnuPG (`gpgv` & `--status-fd`): Verificação Determinística de Assinaturas de Releases e Pacotes sem Efeitos Colaterais em Scripts e CI/CD
- [[gnupg-assinatura-commits-tags-git-allowed-signers-verificacao-ci]] — GnuPG: Assinatura Criptográfica de **Commits e Tags Git (`commit.gpgsign`, `tag.gpgSign`)** e Gate de Verificação em Pipelines de CI/CD
- [[gnupg-criptografia-simetrica-hibrida-aead-aes256-s2k-argon2-iteracoes]] — GnuPG: Criptografia Simétrica (`-c`) e Híbrida Assimétrica (`-e -r`), **S2K (`s2k-count` / Argon2)** e Preferências de Cifra (`AES256`, `SHA512`)
- [[gnupg-distribuicao-chaves-wkd-web-key-directory-dane-keyservers-dirmngr]] — GnuPG & `dirmngr`: Descoberta Segura de Chaves Públicas via **WKD (*Web Key Directory*)** e **OPENPGPKEY DANE (RFC 7929)** vs Keyservers HKP
- [[gnupg-certificado-revogacao-ciclo-vida-expiracao-rotacao-subchaves]] — GnuPG: Ciclo de Vida Criptográfico — Certificados de Revogação (`--gen-revoke`), Renovação de Validade (`--quick-set-expire`) e Resposta a Comprometimento
- [[gnupg-modelo-confianca-tofu-trust-on-first-use-wot-tsign]] — GnuPG: Modelos de Validação de Chaves (**`tofu+pgp`**, *Web of Trust* Clássico, `--tofu-policy` e Assinaturas de Confiança `tsign`)

### VeraCrypt — Criptografia de Disco e Volumes Contêiner Multiplataforma, XTS-AES/Cascades, PIM, Keyfiles e Plausible Deniability

- [[veracrypt-arquitetura-criptografia-volumes-xts-pbkdf2-pim-cabecalho]] — VeraCrypt: Arquitetura de Criptografia de Volumes Multiplataforma, Modo **XTS (IEEE P1619)**, **PBKDF2-RIPEMD160/SHA-512/Whirlpool/BLAKE2s** e **PIM**
- [[veracrypt-criacao-montagem-cli-headless-non-interactive-linux]] — VeraCrypt em Servidores Linux Headless (`veracrypt --text --non-interactive`): Criação, Montagem Segura via `stdin` e Desmontagem
- [[veracrypt-cifras-cascata-aes-twofish-serpent-camellia-kuznyechik]] — VeraCrypt: Cifras Individuais vs **Cifras em Cascata (*Cascades*: `AES-Twofish-Serpent`)** em Modo XTS e Impacto de Hardware `AES-NI`
- [[veracrypt-autenticacao-multifator-keyfiles-pim-personal-iterations-multiplier]] — VeraCrypt: Autenticação Multifator de Volumes com **Keyfiles**, Tokens PKCS#11 (YubiKey/SmartCard) e **PIM (*Personal Iterations Multiplier*)**
- [[veracrypt-volumes-ocultos-hidden-volumes-plausible-deniability-protecao]] — VeraCrypt: **Hidden Volumes (*Plausible Deniability*)**, Funcionamento da Proteção de Volume Oculto (`--protect-hidden`) e Limites Forenses
- [[veracrypt-backup-restauracao-cabecalho-volume-emergencia-corrupcao]] — VeraCrypt: Estrutura de **Cabeçalho Primário vs Cabeçalho de Backup Embutido (`--restore-header`)** e Recuperação de Desastres
- [[veracrypt-higiene-memoria-ram-encryption-cold-boot-hibernacao-swap]] — VeraCrypt: Criptografia de Chaves em Memória RAM, Mitigação de *Cold Boot / DMA Attacks*, Hibernação, Swap e `veracrypt -d`
- [[veracrypt-criptografia-sistema-efi-bootloader-dcs-secure-boot-tpm]] — VeraCrypt no Windows: Criptografia da Partição do Sistema Operacional (**VeraCrypt EFI Boot Loader `VeraCrypt-DCS`**) e Coexistência com **Secure Boot**
- [[veracrypt-interoperabilidade-nativa-linux-cryptsetup-tcrypt-open]] — Interoperabilidade Forense e Operacional: Abertura Nativa de Volumes **VeraCrypt** no Kernel Linux via **`cryptsetup open --type tcrypt --veracrypt`**
- [[veracrypt-builds-reprodutiveis-source-date-epoch-verificacao-pgp]] — VeraCrypt: Verificação de Supply Chain — Assinaturas OpenPGP da IDRIX e **Builds Reprodutíveis (`SOURCE_DATE_EPOCH`)** para `.deb` e `.rpm`

### Linux Cryptsetup & LUKS2 — dm-crypt, Keyslots Argon2id, Kernel Keyring, TPM2/FIDO2 systemd-cryptenroll, dm-verity e dm-integrity

- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Linux **`cryptsetup` & LUKS2**: Arquitetura do Subsistema `dm-crypt`, Metadados JSON **LUKS2**, `veritysetup` (`dm-verity`) e `integritysetup` (`dm-integrity`)
- [[cryptsetup-formatacao-luks2-aes-xts-plain64-argon2id-setores-4k]] — Cryptsetup: Formatação Segura **LUKS2 (`luksFormat`)** — `aes-xts-plain64` (512 bits), Parâmetros **Argon2id** e Alinhamento de Setores de **4096 Bytes**
- [[cryptsetup-gerenciamento-keyslots-luksaddkey-lukskillslot-lukschangekey]] — Cryptsetup: Gestão de **Keyslots LUKS2** (`luksAddKey`, `luksChangeKey`, `luksRemoveKey`, `luksKillSlot`) e Conversão de KDF (`luksConvertKey`)
- [[cryptsetup-integracao-kernel-keyring-logon-keys-vk-caching]] — Cryptsetup & **Linux Kernel Keyring**: Proteção da Volume Key com Chaves do Tipo **`logon`** e Tokens `luks2-keyring`
- [[cryptsetup-desbloqueio-hardware-systemd-cryptenroll-tpm2-fido2-pkcs11]] — LUKS2 + **`systemd-cryptenroll`**: Vinculação de Keyslots a Chips **TPM 2.0 (PCRs + PIN)**, Chaves de Segurança **FIDO2 (YubiKey)** e SmartCards **PKCS#11**
- [[cryptsetup-recriptografia-online-cryptsetup-reencrypt-resiliencia]] — Cryptsetup: **Criptografia e Recriptografia Online (`cryptsetup reencrypt`)** de Volumes LUKS2 Montados com *Crash Recovery* em Metadados
- [[cryptsetup-integridade-autenticada-aead-dm-integrity-chacha20-poly1305]] — Cryptsetup & **`integritysetup` (`dm-integrity`)**: Criptografia Autenticada (**AEAD**) de Disco contra Adulteração Offline (*Evil Maid / Bit-Flipping*)
- [[cryptsetup-verificacao-imutavel-veritysetup-dm-verity-roothash-secure-boot]] — Cryptsetup **`veritysetup` (`dm-verity`)**: Verificação Criptográfica por Árvore de Merkle (**Root Hash**) para Sistemas Operacionais e Containers Imutáveis
- [[cryptsetup-backup-restauracao-cabecalho-luksheaderbackup-luksheaderrestore]] — Cryptsetup: Backup e Restauração de Cabeçalho LUKS2 (`luksHeaderBackup` / `luksHeaderRestore`), `--header` Destacado e `discard` (TRIM)
- [[cryptsetup-abertura-volumes-bitlocker-veracrypt-truecrypt-forense]] — Cryptsetup em DFIR: Abertura Nativa de Discos **Windows BitLocker (`--type bitlk`)**, **Apple FileVault2 (`fvault2`)** e **VeraCrypt (`tcrypt`)** no Linux

### Clevis & Tang — Network-Bound Disk Encryption (NBDE), Protocolo McCallum-Relyea (ECMR), Shamir Secret Sharing (sss) e LUKS2

- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Clevis & Tang (**NBDE — *Network-Bound Disk Encryption***): Arquitetura Criptográfica *Stateless* com Troca **McCallum-Relyea (`ECMR`)** sem Key Escrow
- [[clevis-operacao-servidor-tang-rotacao-chaves-jwk-adv-verificacao]] — Tang Server: Operação de `/var/db/tang/`, Thumbprints **JWK (`S256`)** e **Rotação Graciosa de Chaves (`jose jwk gen`)** sem Quebrar o Boot
- [[clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato]] — Clevis: Arquitetura de **Pins (`tang`, `tpm2`, `sss`, `pkcs11`)** e Criptografia de Segredos em Objetos **JWE (`clevis encrypt` / `clevis decrypt`)**
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Clevis Pin **`sss` (*Shamir's Secret Sharing*)**: Políticas de Quórum de Alta Disponibilidade (`t: 2` de 3 Tangs) e Vinculação Híbrida **`TPM2` + `Tang`**
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Clevis + LUKS2 (`clevis luks bind`): Desbloqueio Automatizado da Partição Raiz (`/`) no Boot via **`dracut` / `initramfs-tools`** e Rede Pré-Boot
- [[clevis-auditoria-regeneracao-clevis-luks-list-regen-unbind-edit]] — Clevis: Ciclo de Vida de Vínculos LUKS (`clevis luks list`, `unlock`, `regen`, `edit` e `unbind`) após Rotação de Chaves Tang ou Mudança de PCRs
- [[clevis-pin-tpm2-pcr-banks-sha256-assinatura-politicas-seguranca]] — Clevis Pin **`tpm2`**: Seleção Segura de Bancos e Registradores **PCR (`pcr_bank`, `pcr_ids`)** para Integridade de Boot
- [[clevis-pin-pkcs11-smartcards-yubikey-desbloqueio-discos-luks]] — Clevis Pin **`pkcs11`**: Desbloqueio de Volumes LUKS2 com SmartCards e Tokens de Hardware **PKCS#11** via URI RFC 7512
- [[clevis-seguranca-rede-tang-segmentacao-vlan-ipsec-wireguard-mtls]] — Arquitetura de Segurança de Rede para **Tang (NBDE)**: Segmentação de VLAN de Boot, *802.1X MACsec* e Riscos de Exposição do Endpoint `/rec`
- [[clevis-monitoramento-auditoria-logs-tangd-alertas-desbloqueio-anomalo]] — Observabilidade e Detecção de Intrusão no **Tang / NBDE**: Monitoramento de Requisições `POST /rec/` e Alertas de Desbloqueio Fora de Janela

### mitmproxy (mitmproxy, mitmdump, mitmweb) — Proxy de Interceptação TLS/HTTP1-3/QUIC/WebSockets/DNS, Modos WireGuard/Local e Addons Python

- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — **`mitmproxy`**, **`mitmdump`** e **`mitmweb`**: Arquitetura do Proxy de Interceptação Programável para HTTP/1, HTTP/2, **HTTP/3 (QUIC)**, WebSockets, TCP/UDP e DNS
- [[mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse]] — mitmproxy: Os 9 Modos de Operação (`regular`, **`local` via eBPF/OS**, **`wireguard`** User-Space, `reverse`, `transparent`, `tun`, `upstream`, `socks5` e `dns`)
- [[mitmproxy-autoridade-certificadora-mitm-it-mtls-client-certs-sslkeylogfile]] — mitmproxy: Gestão da CA Dinâmica (`~/.mitmproxy/`, Domínio Mágico **`mitm.it`**), Certificados de Cliente **mTLS** (`--certs` / `--client-certs`) e `SSLKEYLOGFILE`
- [[mitmproxy-expressoes-filtro-flow-filters-interceptacao-seletiva]] — mitmproxy: Linguagem de **Expressões de Filtro de Fluxo (*Flow Filter Expressions*)** para Visualização (`v`), Interceptação (`i`) e Exportação
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — mitmproxy: Desenvolvimento de **Addons em Python (`-s script.py`)** — Hooks de Ciclo de Vida (`request`, `response`, `websocket_message`, `tcp_message`, `dns_request`)
- [[mitmproxy-modificacao-trafego-modify-body-modify-headers-map-local]] — mitmproxy: Reescrita Declarativa sem Código (`--modify-headers`, `--modify-body`, `--map-local` e `--map-remote`)
- [[mitmproxy-replay-cliente-servidor-testes-regressao-idor-bola]] — mitmproxy: **Client-Side Replay (`-C`)** e **Server-Side Replay (`-S`)** para Testes de Regressão de Autorização (**IDOR / BOLA**) e Simulação Offline
- [[mitmproxy-leitura-programatica-arquivos-fluxo-flowreader-har-export]] — mitmproxy (`mitmproxy.io.FlowReader` & `save_har`): Análise Forense Offline de Arquivos `.mitm`, Extração de Segredos e Exportação **HAR / cURL / OpenAPI**
- [[mitmproxy-interceptacao-http3-quic-websockets-grpc-protobuf-dns]] — mitmproxy: Interceptação de Protocolos Modernos — **HTTP/3 (QUIC sobre UDP)**, **gRPC / Protocol Buffers**, **WebSockets** e Servidor **DNS** Scriptável
- [[mitmproxy-proxy-reverso-waf-leve-decepcao-honeypot-upstream-chaining]] — mitmproxy: Uso Defensivo como **Reverse Proxy de Diagnóstico (`--mode reverse`)**, Honeypot de API de Alta Interação e **Upstream Proxy Chaining**

### Gobuster (OJ/gobuster) — Enumeração Concorrente em Go de Diretórios/Arquivos (dir), Subdomínios DNS (dns), Virtual Hosts (vhost), Buckets S3/GCS, TFTP e Fuzzing (fuzz)

- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — **Gobuster (`OJ/gobuster`)**: Arquitetura de Enumeração Concorrente em Go (`dir`, `dns`, `vhost`, `s3`, `gcs`, `tftp` e `fuzz`) e Controle de Threads (`-t`)
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Gobuster Modo **`dir`**: Descoberta de Diretórios e Arquivos Ocultos, Extensões (`-x`), Filtros de Status (`-s` / `-b`) e **`--exclude-length`**
- [[gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros]] — Gobuster Modo **`vhost`**: Descoberta de *Virtual Hosts* Internos em Reverse Proxies, **`--append-domain`** e Diferenciação de Respostas
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Gobuster Modo **`dns`**: Enumeração Ativa de Subdomínios DNS (`--domain`), Resolvers Customizados (`--resolver`), Exibição de IPs/CNAMEs (`-i`, `-c`) e Wildcards
- [[gobuster-enumeracao-cloud-buckets-s3-aws-gcs-google-cloud-storage]] — Gobuster Modos **`s3`** e **`gcs`**: Descoberta de Buckets de Armazenamento em Nuvem (**AWS S3** e **Google Cloud Storage**) e Listagem de Objetos
- [[gobuster-modo-fuzz-marcador-customizado-url-headers-body-parametros]] — Gobuster Modo **`fuzz`**: Fuzzing de Parâmetros Query/REST, Cabeçalhos HTTP e Corpo de Requisição com a Palavra-Chave **`FUZZ`**
- [[gobuster-enumeracao-tftp-equipamentos-rede-voip-firmwares-configs]] — Gobuster Modo **`tftp`**: Auditoria de Servidores **TFTP (Porta 69/UDP)** em Redes Internas, Telefonia VoIP e Provisionamento PXE/Cisco
- [[gobuster-autenticacao-mtls-certificados-p12-pem-cookies-headers-proxies]] — Gobuster: Varredura Autenticada com **Certificados de Cliente mTLS (`--client-cert-p12` / `--client-cert-pem`)**, Cookies, JWT e Proxies (`--proxy`)
- [[gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups]] — Gobuster: Geração de Permutações por **Arquivo de Padrões (`-p` / `--pattern`)** para Descoberta de Backups e Artefatos Corporativos
- [[gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao]] — Gobuster: Controle de Taxa (`--delay`, `-t`), User-Agent (`-a`), TLS (`--tls-min-version`) e **Detecção Defensiva no WAF / SIEM**

### OWASP Amass (owasp-amass/amass) — External Attack Surface Management (EASM), Open Asset Model (OAM), amass intel/enum/db, ASN/BGP e Grafo

- [[amass-arquitetura-easm-owasp-open-asset-model-oam-grafo]] — OWASP **Amass**: Arquitetura de **External Attack Surface Management (EASM)**, Modelo de Grafo e **Open Asset Model (OAM)**
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — OWASP Amass (`amass intel`): Descoberta de **Sementes Horizontais** — Mapeamento de **ASNs (`-asn`)**, Blocos **CIDR (`-cidr`)**, Organizações (`-org`) e *Reverse Whois*
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — OWASP Amass (`amass enum`): Diferença Arquitetural entre os Modos **Passive (`-passive`)**, **Normal (DNS Validated)** e **Active (`-active`)**
- [[amass-configuracao-fontes-datasources-yaml-chaves-api-rate-limit]] — OWASP Amass: Configuração de **`config.yaml` e `datasources.yaml`** — Chaves de API de Threat Intelligence, Rate Limits e `minimum_ttl`
- [[amass-forca-bruta-recursiva-permutacoes-alterations-mascaras-hashcat]] — OWASP Amass: Força Bruta DNS Recursiva (`-brute`, `-min-for-recursive`) e Geração Inteligente de **Permutações (`-alts`, `-awm` Máscaras Hashcat)**
- [[amass-resolvers-dns-confiaveis-dns-qps-protecao-wildcard-poisoning]] — OWASP Amass: Pool de **Resolvedores DNS Confiáveis (`-rf`, `-trf`)**, Limite de Taxa (`-dns-qps`, `-max-dns-queries`) e Detecção de **Wildcards / DNS Poisoning**
- [[amass-banco-dados-grafo-persistencia-consultas-oam-subs-amass-db]] — OWASP Amass & **`oam-tools` (`oam_subs` / `amass db`)**: Persistência em Banco de Grafo (`-dir` / PostgreSQL) e Extração de Relações OAM
- [[amass-monitoramento-continuo-drift-superficie-ataque-oam-track]] — OWASP Amass (`oam_track` / `amass track`): Monitoramento Contínuo de **Drift da Superfície de Ataque** e Alertas de Novos Subdomínios e Mudanças de IP
- [[amass-visualizacao-topologia-rede-oam-viz-d3-maltego-gexf]] — OWASP Amass (`oam_viz` / `amass viz`): Exportação do Grafo de Superfície de Ataque para **D3.js HTML Interativo (`-d3`)**, **Gephi (`-gexf`)**, **Graphviz (`-dot`)** e **Maltego**
- [[amass-engine-scripting-ads-extensibilidade-pipeline-httpx-nuclei]] — OWASP Amass: Integração em Pipelines de Reconhecimento (**Amass -> `oam_subs` -> `httpx` -> `katana` -> `nuclei`**) e Execução Contêinerizada Docker

### Masscan (robertdavidgraham/masscan) — Scanner de Portas TCP/UDP Assíncrono em Escala de Internet, Cifra BlackRock, SYN Cookies, Banner Checking e Excludefile

- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — **Masscan (`robertdavidgraham/masscan`)**: Arquitetura Assíncrona *Stateless*, Pilha TCP/IP em User-Space, **Cifra BlackRock** e *SYN Cookies*
- [[masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables]] — Masscan **`--banners`**: Como Resolver o Conflito de **Pacotes `RST` do Kernel Linux** usando **`--source-ip` Dedicado** ou **`--adapter-port` + `iptables`/`nftables`**
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Masscan: Dimensionamento de Taxa (`--rate`), Exclusão Obrigatória de Sub-redes Críticas (**`--excludefile`**) e Aceleração **`PF_RING` DNA**
- [[masscan-arquivos-configuracao-pausa-retomada-paused-conf-echo]] — Masscan: Arquivos de Configuração (`-c`), Pausa e Retomada Exata (**`paused.conf` / `--resume`**) e Distribuição em Cluster (**`--shards`**)
- [[masscan-formatos-saida-binaria-ob-readscan-conversao-ox-oj-ol-og]] — Masscan: Gravação em Formato Binário Nativo (**`-oB`**) e Conversão Offline Instantânea (**`--readscan`**) para XML Nmap (`-oX`), JSON (`-oJ`), Grepable (`-oG`) e List (`-oL`)
- [[masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados]] — Masscan: Varredura de Portas **UDP (`-pU:53,123,161,500`)**, Uso de **`--nmap-payloads`** e Injeção de Payloads UDP Customizados (`--pcap-payloads`)
- [[masscan-customizacao-http-sni-vhost-payloads-heartbleed-poodle]] — Masscan: Customização de Requisições HTTP (`--http-user-agent`, `--http-header`, `--http-method`), Captura de **Certificados TLS X.509** e Checagens **SMB / VULN**
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Arquitetura de Varredura em **Dois Estágios**: Descoberta Rápida de Portas (`0-65535`) com **Masscan** + Fingerprinting Profundo (`-sV -sC`) com **Nmap**
- [[masscan-ajustes-rede-arp-router-mac-adapter-vlan-bpf-pcap]] — Masscan: Ajustes de Camada de Enlace (**`--interface`**, **`--adapter-ip`**, **`--adapter-mac`**, **`--router-mac`**), Tags **802.1Q VLAN** e Diagnóstico `--packet-trace`
- [[masscan-deteccao-defensiva-syn-cookies-suricata-zeek-conntrack-tuning]] — Defesa e Detecção contra Varreduras **Masscan**: Proteção da Tabela **`nf_conntrack`** em Firewalls e Detecção de Varreduras Espalhadas no **Suricata / Zeek**

### RustScan (bee-san/RustScan) — Scanner de Portas Assíncrono em Rust/Tokio, Handoff Automático para Nmap, Ajuste de Batch/Timeout/Ulimit e Scripting Engine

- [[rustscan-arquitetura-tokio-async-descoberta-portas-handoff-nmap]] — **RustScan (`bee-san/RustScan`)**: Arquitetura Assíncrona em **Rust (`Tokio`)**, Varredura das 65.535 Portas e **Handoff Automático para o Nmap (`--`)**
- [[rustscan-ajuste-performance-batch-size-timeout-ulimit-nofile]] — RustScan: Engenharia de Performance e Confiabilidade — **Batch Size (`-b`)**, **Timeout (`-t`)**, Tries (`--tries`) e Limite de Descritores (**`--ulimit`**)
- [[rustscan-selecao-alvos-enderecos-cidr-hosts-file-ranges-portas]] — RustScan: Especificação de Alvos (**`-a` IPs, Hostnames, Blocos CIDR e Arquivos de Hosts**), Faixas de Portas (`-r` / `-p`) e **`--exclude-ports`**
- [[rustscan-ordem-varredura-scan-order-serial-random-evasao-ids]] — RustScan: Ordem de Sondagem (**`--scan-order serial` vs `--scan-order random`**) e Comportamento Frente a Sistemas de Detecção de Intrusão (IDS)
- [[rustscan-modos-saida-greppable-accessible-automacao-pipelines]] — RustScan: Modo **`--greppable` (`-g`)** para Automação em Shell/Python e Modo **`--accessible`** para Acessibilidade e Logs Limpos
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — RustScan: Padronização de Equipe com o Arquivo de Configuração **`~/.rustscan.toml`** (`--config-path`)
- [[rustscan-motor-scripts-customizados-rustscan-scripts-toml-python-lua]] — RustScan **Scripting Engine (`--scripts custom`)**: Automação Pós-Descoberta em Python, Shell, Lua ou Binários via **`.rustscan_scripts.toml`**
- [[rustscan-execucao-container-docker-ulimit-rede-host-alias]] — RustScan em Containers **Docker (`rustscan/rustscan`)**: Configuração de `--network host`, `ulimit` do Container e Montagem de Volumes para o Nmap
- [[rustscan-comparacao-arquitetural-rustscan-vs-masscan-vs-nmap-vs-zmap]] — Decisão Arquitetural de Scanners de Portas: Quando Usar **RustScan** vs **Masscan** vs **ZMap** vs **Nmap** em Engajamentos Reais
- [[rustscan-varredura-ipv6-dual-stack-resolucao-hickory-dns-timeout]] — RustScan em Redes **IPv6 e Dual-Stack**: Varredura de Endereços IPv6, Resolução Assíncrona (`hickory-resolver`) e Mitigação de Exaustão de *Conntrack* Local

### ZMap & ZGrab 2.0 (zmap/zmap, zmap/zgrab2) — Varredura Stateless em Escala de Internet via Grupos Cíclicos Multiplicativos, Probe/Output Modules e Handshakes L7

- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — **ZMap (`zmap/zmap`)**: Arquitetura de Varredura *Stateless* de Pacote Único via Permutação em **Grupos Cíclicos Multiplicativos ($\mathbb{Z}_p^*$)**
- [[zmap-modulos-sondagem-probe-modules-tcp-synscan-icmp-udp-dns]] — ZMap **Probe Modules (`-M`)**: Sondagem `tcp_synscan` (padrão), `icmp_echoscan`, `udp`, `dns` e `upnp` com **`--probe-args`**
- [[zmap-controle-banda-taxa-bandwidth-rate-cooldown-time-sender-threads]] — ZMap: Controle de Largura de Banda (**`-B 10M` / `--bandwidth`**) vs Taxa de Pacotes (**`-r` / `--rate`**), `--sender-threads` e `--cooldown-time`
- [[zmap-listas-bloqueio-blocklist-allowlist-conformidade-rfc]] — ZMap: Governança de Escopo com **`/etc/zmap/blocklist.conf` (`-b`)**, **Allowlist (`-w`)** e **`--ignore-blocklist-errors`**
- [[zmap-modulos-saida-output-modules-campos-output-filter-json-csv]] — ZMap **Output Modules (`-O`)**, Seleção de Campos (**`-f` / `--output-fields`**) e Expressões Booleanas **`--output-filter`**
- [[zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes]] — Arquitetura **ZMap (L4) + ZGrab 2.0 (L7)**: Pipeline de Sondagem em Escala de Camada de Transporte para Transcrição Completa de Handshakes de Aplicação
- [[zmap-zgrab2-configuracao-multiplos-modulos-multiple-ini-triggers]] — **ZGrab 2.0 (`zgrab2 multiple -c config.ini`)**: Orquestração de Múltiplos Protocolos L7, Formato CSV (`IP, DOMAIN, TAG, PORT`) e **`--trigger`**
- [[zmap-auditoria-protocolos-industriais-ot-ics-scada-zgrab2-modbus-siemens-dnp3]] — ZGrab 2.0 em Auditoria de Redes **OT / ICS / SCADA** e Bancos de Dados: Módulos `modbus`, `siemens` (S7), `dnp3`, `bacnet`, `fox` e `mongodb`/`redis`
- [[zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards]] — ZMap: Boas Práticas de **Varredura Ética (*Ethical Scanning*)**, Reprodutibilidade Científica (**`--seed`**), Distribuição (**`--shards`**) e Metadados (`--notes`)
- [[zmap-deteccao-defensiva-assinatura-ip-id-54321-suricata-zeek]] — Engenharia de Detecção (Blue Team): Identificação da Assinatura Clássica do **ZMap (`IP ID = 54321` / `0xd431`)** no **Suricata**, **Zeek** e **`tcpdump`**

## Tranche 9 (IDs 801–900)

### Checkmarx KICS (Keeping Infrastructure as Code Secure) — Scanner SAST Multi-IaC com OPA/Rego, Queries Customizadas, Bill of Materials (BoM) e CI/CD

- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — **Checkmarx KICS (*Keeping Infrastructure as Code Secure*)**: Arquitetura de SAST para **Infraestrutura como Código (IaC)** Baseada em **Open Policy Agent (Rego)**
- [[kics-desenvolvimento-queries-customizadas-rego-cxpolicy-metadata]] — KICS: Criação de **Consultas Customizadas em `Rego` (`CxPolicy [ result ]`)**, Metadados `metadata.json` e `kics generate-id`
- [[kics-auto-remediacao-kics-remediate-correcao-automatica-iac]] — KICS **`remediate`**: Auto-Remediação Determinística de Misconfigurations em Infraestrutura como Código (`remediation` + `remediationType`)
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — KICS: Governança de Exceções — Comentários Inline (**`# kics-scan ignore`**) e Exclusão por **`similarityID` (`-x` / `--exclude-results`)**
- [[kics-inventario-recursos-iac-bill-of-materials-bom-m]] — KICS: Geração de **Inventário de Recursos de Nuvem Pré-Deploy (*IaC Bill of Materials — BoM*, `-m` / `--bom`)**
- [[kics-analise-terraform-variaveis-tfvars-modulos-plan-json]] — KICS para **Terraform e OpenTofu**: Resolução de Variáveis (`--terraform-vars-path`), Módulos e Auditoria de `terraform show -json`
- [[kics-auditoria-kubernetes-helm-dockerfile-pod-security-containers]] — KICS para **Kubernetes, Helm Charts e Dockerfiles**: Auditoria Integrada da Imagem (`Dockerfile`) até o Manifesto do Pod (`Deployment`)
- [[kics-auditoria-especificacoes-openapi-swagger-grpc-protobuf-apis]] — KICS para **OpenAPI (v2/v3) e gRPC (`.proto`)**: *Shift-Left API Security* desde o Contrato da API (`--enable-openapi-refs`)
- [[kics-deteccao-segredos-embutidos-passwords-keys-regex-rules]] — KICS: Detecção Integrada de **Segredos e Credenciais Hardcoded** em IaC (`passwords_and_secrets`, `--secrets-regexes-path` e `--disable-secrets`)
- [[kics-governanca-severidade-fail-on-ignore-on-exit-sarif-cicd]] — KICS em Pipelines CI/CD: Configuração Declarativa (`kics.config`), Códigos de Saída (**`--fail-on`**, **`--ignore-on-exit`**) e Relatórios **SARIF / SonarQube / GitLab**

### ProjectDiscovery Naabu — Scanner Rápido de Portas SYN/CONNECT/UDP em Go, Descoberta de Hosts (ARP/ICMP/TCP), Shodan InternetDB e Handoff para Nmap/httpx

- [[naabu-arquitetura-varredura-portas-syn-connect-udp-deduplicacao-ip]] — ProjectDiscovery **Naabu**: Arquitetura de Varredura de Portas **SYN / CONNECT / UDP** em Go, Permutação `BlackRock` e **Deduplicação Automática de IP**
- [[naabu-exclusao-cdn-waf-exclude-cdn-port-threshold-protecao]] — Naabu: Exclusão Inteligente de **IPs de CDN / WAF (`-exclude-cdn` / `-ec`)** e Proteção contra Honeypots/Port-Spoofing (**`-port-threshold` / `-pts`**)
- [[naabu-enumeracao-passiva-shodan-internetdb-passive-zero-pacotes]] — Naabu **`-passive`**: Enumeração Passiva Instantânea de Portas Abertas via **Shodan InternetDB** com Zero Pacotes Enviados ao Alvo
- [[naabu-descoberta-hosts-ativos-host-discovery-sn-wn-icmp-arp-tcp]] — Naabu **Host Discovery (`-sn` / `-wn`)**: Sondagem Híbrida de Hosts Vivos via **ICMP (`-pe`, `-pp`, `-pm`)**, **TCP Ping (`-ps`, `-pa`)**, **ARP (`-arp`)** e **IPv6 ND (`-nd`)**
- [[naabu-integracao-nativa-nmap-cli-service-fingerprinting-nse]] — Naabu + **Nmap (`-nmap-cli`)**: Handoff Automático de Portas Descobertas para Detecção de Versão (`-sV`) e Scripts NSE (`-sC`) do Nmap
- [[naabu-selecao-portas-top-ports-full-smart-scan-preditivo-verify]] — Naabu: Seleção de Portas (`-p -`, `-top-ports full|100|1000`), Verificação Dupla TCP (**`-verify`**) e **Smart Scan Preditivo (`-ss` / `-smart-scan`)**
- [[naabu-varredura-atraves-proxies-socks5-connect-payload-ipv6]] — Naabu em Operações Red Team e Pivoting: Varredura `CONNECT` via **Proxy SOCKS5 (`-proxy`, `-proxy-auth`)** e **`-connect-payload` (`-cp`)**
- [[naabu-entrada-asn-cidr-exclusao-escopo-exclude-hosts-file]] — Naabu: Varredura Direta por **ASN (`AS1449`) e CIDR**, Exclusão de Escopo (`-eh` / `-ef`) e Política de Rede (`networkpolicy`)
- [[naabu-configuracao-persistente-resume-cfg-metricas-monitoramento]] — Naabu: Arquivo de Configuração Persistente (`~/.config/naabu/config.yaml`), Retomada de Varredura (**`-resume`**) e Telemetria (`-metrics-port`)
- [[naabu-integracao-pipeline-subfinder-dnsx-naabu-httpx-nuclei]] — Pipeline Unix ProjectDiscovery Completo: **`subfinder` -> `dnsx` -> `naabu` -> `httpx` -> `katana` -> `nuclei`**

### ProjectDiscovery dnsx — Toolkit DNS Multi-Propósito em Go, Filtragem de Wildcard DNS, Reconhecimento de Registros/SPF/DMARC/DNSSEC, CDN/ASN e Força Bruta

- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — ProjectDiscovery **`dnsx`**: Arquitetura do Toolkit DNS Multi-Propósito sobre `retryabledns`, Resolvers **UDP / TCP / DoH / DoT** e Modo **`-recon`**
- [[dnsx-deteccao-asn-cdn-filtragem-wildcards-auto-wildcard-wd]] — `dnsx`: Filtragem Automática de **DNS Wildcards (`-wd` / `-auto-wildcard`, `-wt`)** e Enriquecimento de **ASN (`-asn`) e CDN (`-cdn`)**
- [[dnsx-forca-bruta-subdominios-wordlists-placeholders-fuzz]] — `dnsx`: Força Bruta de Subdomínios (`-d` + `-w`) e **Substituição por Marcador `FUZZ`** em Qualquer Posição do Nome DNS
- [[dnsx-varredura-reversa-ptr-cidr-asn-descoberta-hosts-internos]] — `dnsx` **`-ptr` (`-resp-only`)**: Varredura de **DNS Reverso (`PTR` / `in-addr.arpa`)** a partir de Blocos CIDR e Números de **ASN (`AS...`)**
- [[dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused]] — `dnsx`: Caça a **Subdomain Takeover (`dangling CNAME`)** e Filtragem por Código de Resposta DNS (**`-rcode noerror,nxdomain,servfail,refused`**)
- [[dnsx-auditoria-seguranca-email-spf-dmarc-dkim-caa-txt-mx]] — `dnsx`: Auditoria em Lote de Segurança de E-mail (**SPF / DMARC em `-txt`**, **`-mx`**) e Governança de Certificados (**`-caa`**, **`-soa`**)
- [[dnsx-auditoria-transferencia-zona-axfr-trace-delegacao-dns]] — `dnsx`: Teste em Massa de **Transferência de Zona DNS (`-axfr`)** e Rastreamento da Cadeia de Delegação Autoritativa (**`-trace`**)
- [[dnsx-resolvedores-customizados-doh-dot-rate-limit-retry-timeout]] — `dnsx`: Configuração de **Resolvedores DNS-over-HTTPS (`DoH`) e DNS-over-TLS (`DoT`)**, Controle de Taxa (`-rl`), `-retry` e `-timeout`
- [[dnsx-templates-saida-customizados-ot-json-omit-raw-stream]] — `dnsx`: Formatação Avançada com **Output Templates (`-ot '{{host}} {{a}}'`)**, JSONL Enxuto (`-json -omit-raw`) e Modo **`-stream`**
- [[dnsx-descoberta-servicos-internos-srv-kerberos-ldap-sip-autodiscover]] — `dnsx` **`-srv`**: Enumeração de Registros **`SRV` (RFC 2782)** para Descoberta de Controladores **Active Directory (`_ldap._tcp`, `_kerberos._tcp`)**, SIP e XMPP

### ProjectDiscovery tlsx — Scanner TLS/X.509 Rápido em Go, Múltiplos Motores (crypto/tls, zcrypto, openssl), Extração de SAN/CN, Fingerprinting JA3/JARM e mTLS

- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — ProjectDiscovery **`tlsx`**: Arquitetura do Coletor e Analisador TLS e os 4 Motores de Conexão (**`ctls`**, **`ztls`**, **`openssl`** e **`auto`**)
- [[tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn]] — `tlsx`: Descoberta Ativa de Subdomínios e Ativos via **Campos `SAN` (`-san`) e `CN` (`-cn`)** sobre Blocos **CIDR e ASNs** e Modo **`-pre-handshake` (`-ps`)**
- [[tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked]] — `tlsx`: Auditoria Contínua de **Misconfigurations de Certificados X.509** (`-ex` Expirado, `-ss` Auto-Assinado, `-mm` Mismatched, `-re` Revogado e `-un` Untrusted)
- [[tlsx-fingerprinting-ativo-jarm-ja3-hashes-certificados-shodan]] — `tlsx`: Fingerprinting Criptográfico **`-jarm`**, **`-ja3`**, Serial (`-se`) e Hashes de Certificado (**`-hash md5,sha1,sha256`**) para Threat Hunting
- [[tlsx-enumeracao-versoes-tls-version-enum-cipher-enum-cipher-type]] — `tlsx`: Enumeração de **Versões TLS Suportadas (`-ve` / `-version-enum`)** e Auditoria de **Cifras Fracas/Inseguras (`-ce` / `-cipher-enum`, `-ct`)**
- [[tlsx-customizacao-sni-random-sni-rev-ptr-sni-virtual-hosts]] — `tlsx`: Manipulação Avançada de **TLS SNI (`-sni`, `-random-sni`, `-rev-ptr-sni`)** para Descoberta de *Virtual Hosts* e Bypass de Roteamento
- [[tlsx-exportacao-cadeia-pem-certificate-tls-chain-client-server-hello]] — `tlsx`: Exportação Completa da **Cadeia de Certificados em PEM (`-cert`, `-tls-chain`)** e Transcrição **`-client-hello` / `-server-hello`**
- [[tlsx-auditoria-certificados-wildcard-wc-escopo-blast-radius]] — `tlsx` **`-wc` (`-wildcard-cert`)**: Mapeamento de **Certificados Wildcard (`*.dominio`)** e Redução do *Blast Radius* de Chaves Privadas
- [[tlsx-varredura-multi-porta-starttls-proxies-socks5-concorrencia]] — `tlsx`: Varredura TLS em **Portas Não-Padrão (`-p 443,8443,9443,6443,2379,636`)**, Controle de Concorrência (`-c`, `-delay`) e Proxy **`-proxy`**
- [[tlsx-integracao-pipeline-subfinder-dnsx-naabu-tlsx-httpx-nuclei]] — Pipeline de Descoberta Recursiva por Certificados: **`subfinder` -> `dnsx` -> `naabu` -> `tlsx -dns` -> `httpx` -> `nuclei`**

### WPScan (wpscanteam/wpscan) — Scanner de Segurança WordPress, Enumeração de Plugins/Temas/Usuários/Backups/Timthumbs, Força Bruta XML-RPC MultiCall e API WPVulnDB

- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — **WPScan (`wpscanteam/wpscan`)**: Arquitetura do Scanner de Segurança WordPress em Ruby (`Typhoeus`/`Nokogiri`), Banco Local `~/.cache/wpscan/db` e **API WPVulnDB**
- [[wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed]] — WPScan (`--enumerate` / `-e`): Enumeração de **Plugins (`vp`, `ap`, `p`) e Temas (`vt`, `at`, `t`)** e Modos de Detecção (`passive`, `aggressive`, `mixed`)
- [[wpscan-enumeracao-usuarios-u-author-id-rest-api-oembed-mitigacao]] — WPScan (`-e u1-50`): Vetores de **Enumeração de Usuários WordPress** (`/?author=N`, REST API `/wp-json/wp/v2/users`, `oEmbed`, `wp-sitemap.xml` e RSS) e Hardening
- [[wpscan-auditoria-senhas-forca-bruta-wp-login-xmlrpc-multicall]] — WPScan: Auditoria de Senhas (`-P`) via **`wp-login.php`** vs Amplificação **`xmlrpc.php` (`system.multicall`)** e Como Mitigar no Servidor
- [[wpscan-descoberta-backups-config-exports-db-timthumbs-medias]] — WPScan (`-e cb,dbe,tt,m`): Descoberta de **Backups do `wp-config.php` (`cb`)**, **Dumps de Banco SQL (`dbe`)**, Timthumbs (`tt`) e Mídias (`m`)
- [[wpscan-modo-stealthy-controle-taxa-throttle-random-user-agent-waf]] — WPScan: Modo Furtivo (**`--stealthy`**), Controle de Taxa (**`--throttle`**, **`--max-threads`**), `--random-user-agent` e Bypass/Detecção de WAF
- [[wpscan-varredura-autenticada-cookie-string-basic-auth-vhost-proxy]] — WPScan: Varredura Autenticada (**`--cookie-string`**, **`--cookie-jar`**, `--http-auth`), Cabeçalho **`--vhost`** e Encaminhamento por Proxy (`--proxy`)
- [[wpscan-customizacao-diretorios-wp-content-dir-wp-plugins-dir-escopo]] — WPScan: Instalações WordPress Customizadas (**`--wp-content-dir`**, **`--wp-plugins-dir`**) e Exclusão de Conteúdo (`--exclude-content-based`)
- [[wpscan-arquivos-configuracao-scan-yml-json-relatorios-cicd]] — WPScan: Configuração Segura de Token e Opções em **`~/.config/wpscan/scan.yml`** e Formatos de Saída (**`-f json`, `cli`, `cli-no-color`**)
- [[wpscan-hardening-defensivo-wordpress-wp-cron-xmlrpc-file-edit-headers]] — Hardening Defensivo de **WordPress** Guiado pelos Achados do WPScan (`DISABLE_WP_CRON`, `DISALLOW_FILE_EDIT`, `xmlrpc.php` e `readme.html`)

### Nikto Web Server Scanner (sullo/nikto) — Auditoria de Servidores Web, Cabeçalhos, Arquivos Perigosos/CGIs, Tuning, Mutate, LibWhisker Evasion e Relatórios

- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — **Nikto Web Server Scanner (`sullo/nikto`)**: Arquitetura de Plugins (`program/plugins/`), Bancos de Testes (`db_tests`, `udb_tests`) e `nikto.conf`
- [[nikto-filtragem-categorias-testes-tuning-reverso-x-escopo]] — Nikto **`-Tuning`**: Seleção Cirúrgica de Categorias de Testes (`1`–`9`, `0`, `a`–`e`) e Operador de **Exclusão Reversa (`x`)**
- [[nikto-modos-mutacao-mutate-diretorios-usuarios-apache-cgiwrap]] — Nikto **`-mutate` e `-Cgidirs`**: Descoberta Cruzada de Diretórios/Arquivos (`-mutate 1`), Enumeração Apache `/~user` (`-mutate 3`) e Diretórios CGI
- [[nikto-tecnicas-evasao-ids-waf-libwhisker-evasion-deteccao]] — Nikto **`-evasion`**: As 10 Técnicas de Codificação HTTP **LibWhisker** (`1`–`8`, `A`, `B`) para Teste de Regras de Normalização de **IDS / WAF**
- [[nikto-selecao-plugins-macros-headers-outdated-robots-put-del]] — Nikto **`-Plugins`**: Execução Direta de Plugins Específicos (`headers`, `outdated`, `robots`, `put_del_test`, `ssl`, `apache_expect_xss` e `siebel`)
- [[nikto-varredura-autenticada-headers-cookies-mtls-proxies]] — Nikto: Varredura Autenticada (**`-id` Basic/NTLM**, **`-Add-header`**, `STATIC-COOKIE`), Certificados de Cliente **mTLS (`-RSAcert`, `-key`)** e **`-useproxy`**
- [[nikto-tratamento-soft-404-no404-db-404-strings-falso-positivo]] — Nikto: Calibração contra Páginas **"Soft 404"** (`db_404_strings`, `-no404`) e Prefixo de Diretório **`-root`**
- [[nikto-varredura-multi-host-multi-porta-nmap-gnmap-maxtime-pause]] — Nikto em Lote: Ingestão Direta de Saída **Nmap (`-h scan.gnmap`)**, Múltiplas Portas (`-port 80,443,8080`) e Limites **`-maxtime` / `-Pause`**
- [[nikto-formatos-relatorio-json-xml-html-csv-sqld-defectdojo]] — Nikto: Exportação Multi-Formato (**`-Format json,xml,htm,csv,sqld`**), Ingestão Direta em Banco SQL (**`sqld`**) e **OWASP DefectDojo**
- [[nikto-deteccao-defensiva-assinaturas-waf-user-agent-rate-limiting]] — Engenharia de Detecção (Blue Team): Identificação de Varreduras **Nikto** no **Coraza WAF / OWASP CRS**, **Suricata** e **Fail2ban**

### Wapiti Web Vulnerability Scanner (wapiti-scanner/wapiti) — Scanner DAST Black-Box Assíncrono (httpx/Playwright), Módulos SQLi/XSS/SSRF/XXE/RCE/CSP e OpenAPI

- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — **Wapiti 3 (`wapiti-scanner/wapiti`)**: Arquitetura do Scanner **DAST Black-Box** Assíncrono em Python (`httpx`, `aiosqlite`, `Playwright` e `mitmproxy`)
- [[wapiti-modulos-injecao-sql-timesql-xss-permanentxss-xxe-exec-file]] — Wapiti (`-m` / `--module`): Módulos de Injeção Ativa (`sql`, `timesql`, `ldap`, `xss`, `permanentxss`, `exec`, `file`, `xxe`, `crlf` e `ssrf`)
- [[wapiti-controle-escopo-crawler-scope-depth-exclude-headless-playwright]] — Wapiti: Controle de **Escopo (`--scope`)**, Profundidade (`-d`), Exclusão de Rotas Destrutivas (**`-x` Logout**) e Crawler **Headless (`--headless`)**
- [[wapiti-varredura-autenticada-getcookie-form-script-cookies-ntlm]] — Wapiti: Varredura Autenticada com **`wapiti-getcookie`**, Extração do Navegador (`--cookie`), **`--form-script`** e Autenticação HTTP (`Basic`/`Digest`/`NTLM`)
- [[wapiti-varredura-apis-rest-openapi-swagger-json-payloads]] — Wapiti para **APIs REST (`--swagger`)**: Auditoria Direta de Contratos **OpenAPI / Swagger** e Injeção de Payloads dentro de **Corpos JSON**
- [[wapiti-modulos-postura-csp-http-headers-cookieflags-csrf-ssl]] — Wapiti: Módulos de Postura Defensiva (`csp`, `http_headers`, `cookieflags`, `csrf`, `https_redirect`, `methods` e `ssl`)
- [[wapiti-modulos-cves-cms-wappalyzer-log4shell-spring4shell-takeover]] — Wapiti: Módulos de Reconhecimento e CVEs Críticas (`wapp`, `cms`, `wp_enum`, `nikto`, `backup`, `buster`, `takeover`, `log4shell` e `spring4shell`)
- [[wapiti-deteccao-out-of-band-ssrf-xxe-log4shell-endpoint-customizado]] — Wapiti **Out-of-Band (OAST / `--external-endpoint`)**: Detecção de **Blind SSRF**, **Blind XXE** e **Log4Shell** com Endpoint Externo Próprio
- [[wapiti-performance-tasks-concorrentes-timeouts-persistencia-sqlite]] — Wapiti: Ajuste de Concorrência Assíncrona (**`--tasks`**), Timeouts (`-t`, `--max-scan-time`, `--max-attack-time`) e Sessões SQLite (`--store-session`)
- [[wapiti-relatorios-html-json-xml-md-integracao-proxy-mitmproxy]] — Wapiti: Geração de Relatórios (**`-f html,json,xml,md,csv,txt`**), Encaminhamento via Proxy (**`-p` `mitmproxy` / ZAP**) e Pipelines DevSecOps

### Arjun (s0md3v/Arjun) — Descoberta Heurística de Parâmetros HTTP Ocultos (GET, POST, JSON, XML) via Busca Binária de Anomalias e Extração Passiva

- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — **Arjun (`s0md3v/Arjun`)**: Arquitetura de Descoberta de **Parâmetros HTTP Ocultos** via **Busca Binária em Chunks (`-c`)** e Detecção de Anomalias
- [[arjun-calibracao-fatores-anomalia-define-compare-baseline]] — Arjun (`arjun/core/anomaly.py`): Como Funciona a **Calibração dos 8 Fatores de Anomalia** (`define` & `compare`) para Zero Falsos Positivos
- [[arjun-metodos-http-get-post-json-xml-include-parametros-fixos]] — Arjun (`-m GET|POST|JSON|XML` e `--include`): Descoberta de Atributos Ocultos em **APIs REST JSON (**Mass Assignment / BOPLA**)** e Payloads XML
- [[arjun-coleta-passiva-parametros-passive-wayback-commoncrawl-otx]] — Arjun **`--passive`**: Extração Passiva de Parâmetros Históricos do **Wayback Machine, CommonCrawl e AlienVault OTX** combinada com Validação Ativa
- [[arjun-conversao-estilo-nomenclatura-casing-camel-snake-kebab]] — Arjun **`--casing`**: Adaptação Automática da Wordlist às Convenções de Código do Backend (`snake_case`, `camelCase`, `kebab-case`, `lowercase`)
- [[arjun-importacao-alvos-burpsuite-raw-request-txt-lote]] — Arjun (`-i`): Importação de Múltiplos Alvos a partir de **Arquivos de Texto**, **Itens Exportados do Burp Suite XML** e **Requisições HTTP Brutas (`raw`)**
- [[arjun-controle-taxa-estabilidade-stable-rate-limit-delay-timeout]] — Arjun: Controle de Estabilidade e Evasão de Rate-Limit (**`--stable`**, **`--rate-limit`**, **`-d` Delay**, **`-t` Threads**, **`-T` Timeout** e `--disable-redirects`)
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Arjun (`-oJ`, `-oT`, **`-oB` Proxy Forwarding**): Encaminhamento Automático de Endpoints com Parâmetros Descobertos para **`mitmproxy` / ZAP / Burp**
- [[arjun-heuristicas-extracao-html-js-json-special-payloads]] — Arjun (`arjun/plugins/heuristic.py` e `db/special.json`): Extração Heurística de Parâmetros no Código-Fonte da Resposta e Payloads Especiais
- [[arjun-integracao-pipeline-katana-arjun-dalfox-sqlmap-nuclei]] — Pipeline de Caça a Vulnerabilidades em Parâmetros Ocultos: **`katana` -> `arjun` -> `dalfox` / `sqlmap` / `nuclei -dast`**

### jwt_tool (ticarpi/jwt_tool) & Segurança Criptográfica de JSON Web Tokens (IETF RFC 7515 / RFC 7519 / RFC 8725 BCP) — Auditoria, Tampering e Mitigação

- [[jwttool-arquitetura-auditoria-json-web-tokens-jws-jwe-rfc7519-rfc8725]] — **`jwt_tool` (`ticarpi/jwt_tool`) & Padrão JWT (RFC 7519 / RFC 8725 BCP)**: Anatomia de **JSON Web Tokens (`Header.Payload.Signature`)** e Decodificação
- [[jwttool-ataques-exclusao-assinatura-alg-none-null-blank-psychic-ecdsa]] — `jwt_tool` (`-X a`, `-X n`, `-X b`, `-X p`): Auditoria de Bypass de Assinatura (**`alg: none` CVE-2015-2951**, **Null Signature**, **Blank Password** e **Psychic Signatures CVE-2022-21449**)
- [[jwttool-confusao-algoritmo-assimetrico-simetrico-rs256-hs256-key-confusion]] — `jwt_tool` (**`-X k` — *Key Confusion Attack*, CVE-2016-10555**): Confusão de Algoritmo Assimétrico (**`RS256`**) para Simétrico (**`HS256`**) e Defesa conforme **RFC 8725 §3.1**
- [[jwttool-injecao-cabecalhos-jwk-jku-x5u-kid-path-traversal-sqli]] — `jwt_tool` (`-X i`, `-X s`, `-I -hc kid`): Ataques de **Injeção de Chave no Cabeçalho (`jwk` CVE-2018-0114, `jku`, `x5u`)** e Manipulação de **`kid` (Path Traversal / SQLi)**
- [[jwttool-auditoria-forca-segredos-hmac-dicionario-c-hashcat]] — `jwt_tool` (**`-C -d` Dictionary Attack**) & **Hashcat (`-m 16500`)**: Auditoria de Segredos Simétricos Fracos em **`HS256` / `HS384` / `HS512`**
- [[jwttool-varredura-automatizada-playbook-scan-at-pb-er-canary]] — `jwt_tool` Modos de Varredura Ativa (**`-M pb` Playbook**, **`-M at` All Tests**, **`-M er` Forced Errors** e **`-M cc` Claim Fuzzing**) com **Canary Value (`-cv`)**
- [[jwttool-adulteracao-claims-tampering-injecao-assinatura-customizada]] — `jwt_tool` (`-T`, `-I`, `-S`): Adulteração Interativa e Não-Interativa de **Claims (`-pc` / `-pv`)**, Cabeçalhos (`-hc` / `-hv`) e Re-Assinatura (`hs256` / `rs256` / `es256`)
- [[jwttool-validacao-claims-iss-aud-exp-nbf-typ-cross-jwt-confusion]] — Segurança de Claims JWT conforme **IETF RFC 8725 (§3.8–3.12)**: Prevenção de **Cross-JWT Confusion (`aud`, `iss`, `typ`)** e Validação Temporal (`exp`, `nbf`)
- [[jwttool-verificacao-chaves-publicas-jwks-reconstrucao-rsa-ecdsa]] — `jwt_tool` (`-V -pk` / `-jw`): Verificação de Tokens contra **Chaves Públicas PEM e Arquivos JWKS**, Extração de Chaves e Reconstrução
- [[jwttool-revogacao-ciclo-vida-jti-token-binding-dpop-mtls-defesa]] — Arquitetura Defensiva de Sessões JWT: **Curta Duração (`exp`)**, Revogação via **`jti` Allowlist/Blocklist**, Cookies `HttpOnly` e **Sender-Constrained Tokens (`mTLS` RFC 8705 / `DPoP` RFC 9449)**

### Feroxbuster (epi052/feroxbuster) — Descoberta Recursiva Forçada de Conteúdo Web em Rust, Auto-Tune/Auto-Bail, Filtros de Similaridade, Extração de Links e Estado

- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — **Feroxbuster (`epi052/feroxbuster`)**: Arquitetura de **Descoberta Recursiva de Conteúdo Web (*Forced Browsing*)** em Rust (`tokio`)
- [[feroxbuster-protecao-inteligente-auto-tune-auto-bail-rate-limit]] — Feroxbuster: Adaptação Inteligente de Taxa (**`--auto-tune`**), Aborto Automático de Erros (**`--auto-bail`**) e Limite Explícito (**`--rate-limit`**)
- [[feroxbuster-filtragem-precisa-status-size-words-lines-regex-similar]] — Feroxbuster: Filtros Multi-Dimensionais (`-C`, `-S`, `-W`, `-N`, `-X`) e **Filtro de Similaridade Fuzzy (`--filter-similar-to`)** contra *Soft-404 Dinâmicos*
- [[feroxbuster-coleta-inteligente-palavras-backups-extensoes-links]] — Feroxbuster: Geração Dinâmica de Wordlist a partir do Alvo (**`--collect-words` (`-g`)**, **`--collect-backups` (`-B`)**, **`--collect-extensions` (`-E`)** e `--extract-links`)
- [[feroxbuster-gerenciamento-estado-state-file-resume-from-time-limit]] — Feroxbuster: Persistência de Estado (**`ferox-*.state`**), Retomada Exata (**`--resume-from`**) e Orçamento de Tempo (**`--time-limit`**)
- [[feroxbuster-encaminhamento-seletivo-replay-proxy-replay-codes-burp-mitmproxy]] — Feroxbuster: **`--replay-proxy`** e **`--replay-codes`** — Como Enviar Apenas os Achados Válidos (`200`, `301`, `403`) para o **`mitmproxy` / ZAP / Burp**
- [[feroxbuster-autenticacao-mtls-request-file-headers-cookies-queries]] — Feroxbuster: Auditoria Autenticada via **`--request-file` (Raw HTTP)**, Certificados **mTLS (`--client-cert`, `--client-key`)**, `-H`, `-b` e `-Q`
- [[feroxbuster-configuracao-persistente-ferox-config-toml-escopo]] — Feroxbuster: Padronização Corporativa com **`ferox-config.toml`**, Controle de Fronteira (**`--scope`**) e Bloqueio (**`--dont-scan`**)
- [[feroxbuster-pipelines-stdin-silent-json-encadeamento-httpx-nuclei]] — Feroxbuster em Pipelines Unix: Leitura de Alvos via **`--stdin`**, Modo **`--silent` (`-q`)**, Saída **JSON Lines (`--json`)** e `--parallel`
- [[feroxbuster-comparacao-feroxbuster-vs-ffuf-vs-gobuster-vs-katana]] — Decisão Arquitetural de Descoberta Web: Quando Usar **Feroxbuster** vs **`ffuf`** vs **Gobuster** vs **Katana** em Pentests e EASM

## Tranche 10 (IDs 901–1000)

### Turbot Steampipe & Powerpipe (turbot/steampipe, turbot/powerpipe) — Auditoria de Segurança e Conformidade Multi-Cloud Zero-ETL via SQL (Postgres FDW) e Benchmarks CIS/NIST/SOC2 em HCL

- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — **Turbot Steampipe (`turbot/steampipe`)**: Arquitetura **Zero-ETL** baseada em **PostgreSQL Foreign Data Wrappers (FDW)** para Consulta de APIs Cloud via SQL
- [[steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam]] — Steampipe: **JOINs Relacionais Cross-Cloud e Cross-SaaS** (`aws` + `kubernetes` + `github` + `okta`) para Investigação de Incidentes e IAM
- [[steampipe-agregadores-multi-conta-connections-spc-aws-organizations]] — Steampipe: Conexões Multi-Conta e **Agregadores (`type = "aggregator"`)** em `~/.steampipe/config/*.spc` para Varrer **AWS Organizations / GCP Folders**
- [[steampipe-powerpipe-benchmarks-conformidade-cis-nist-pci-soc2]] — **Powerpipe (`turbot/powerpipe`)**: Execução de +5.000 Controles de Conformidade (**CIS Benchmarks, NIST 800-53, PCI DSS, SOC 2, HIPAA**) sobre o Steampipe
- [[steampipe-autoria-controles-customizados-powerpipe-hcl-policy-as-code]] — Powerpipe HCL: Autoria de **Controles e Benchmarks Customizados (*Policy-as-Code*)** com SQL (`status`, `reason`, `resource` e Dimensões)
- [[steampipe-auditoria-shift-left-iac-plugins-terraform-kubernetes-docker]] — Steampipe **Shift-Left IaC**: Auditoria SQL de Arquivos Locais **Terraform (`.tf`, `.tfstate`)**, Manifestos **Kubernetes YAML** e **`Dockerfile`**
- [[steampipe-auditoria-postura-github-supply-chain-branch-protection-actions]] — Steampipe Plugin **`github`**: Auditoria SQL de **Supply Chain, Repositórios Públicos, Branch Protection, Segredos e GitHub Actions**
- [[steampipe-modo-servico-steampipe-service-cache-ttl-clientes-externos]] — Steampipe **`steampipe service`**: Operação como Daemon PostgreSQL (`:9193`), Controle de **Cache TTL (`--cache-ttl`)** e Conexão via `psql` / Grafana / Metabase
- [[steampipe-snapshots-exportacao-relatorios-html-json-md-cicd]] — Steampipe & Powerpipe em **CI/CD**: Snapshots Históricos (**`.pps`**, `--snapshot`), Exportação (`json`, `html`, `md`, `csv`, `asff`) e Exit Codes
- [[steampipe-comparacao-zero-etl-vs-cloudquery-elt-decisao-cspm]] — Decisão Arquitetural de CSPM: Quando Usar **Steampipe (Zero-ETL Live SQL)** vs **CloudQuery (ELT Data Warehouse)** vs **Prowler**

### CloudQuery (cloudquery/cloudquery) — Framework ELT de Alta Performance em Go/Apache Arrow para Inventário de Ativos e Postura de Segurança Multi-Cloud (CSPM)

- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — **CloudQuery (`cloudquery/cloudquery`)**: Arquitetura **ELT (*Extract-Load-Transform*)** de Alta Performance baseada em **Apache Arrow** e Plugins gRPC
- [[cloudquery-configuracao-fontes-aws-gcp-azure-k8s-selecao-tabelas]] — CloudQuery: Configuração Fina de **Fontes (`tables`, `skip_tables`, `concurrency`)** e Escalonamento Inteligente (`dfs`, `round-robin`, `shuffle`)
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — CloudQuery: Modos de Escrita no Destino (**`overwrite-delete-stale`**, **`overwrite`** e **`append`**) e Migração Automática de Schema (`migrate_mode`)
- [[cloudquery-descoberta-multi-conta-aws-organizations-gcp-folders-azure]] — CloudQuery em Escala Enterprise: Descoberta Automática de Contas via **AWS Organizations (`org`)**, **GCP Folders** e **Azure Subscriptions**
- [[cloudquery-politicas-seguranca-sql-cspm-aws-gcp-azure-k8s]] — CloudQuery **CSPM Policies em SQL**: Execução de Views de Conformidade (**CIS, NIST, PCI DSS**) e Detecção de Exposição Pública sobre o Banco Sincronizado
- [[cloudquery-sincronizacao-incremental-state-backend-cursor-otimizacao]] — CloudQuery: **Sincronização Incremental (`backend_options`)** com Cursor de Estado para Tabelas de Grande Volume
- [[cloudquery-exportacao-datalake-duckdb-parquet-s3-clickhouse-analise]] — CloudQuery com **DuckDB e Parquet (`cloudquery/duckdb`, `cloudquery/file`)**: Auditoria Multi-Cloud Portátil e Serverless em Segundos
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — CloudQuery Forense: **Histórico Temporal (`write_mode: append`)** para Investigação de Incidentes ("O Que Mudou na Conta Antes do Ataque?")
- [[cloudquery-grafo-ativos-seguranca-neo4j-caminhos-ataque-iam-rede]] — CloudQuery + **Neo4j (`cloudquery/neo4j`)**: Construção de **Grafos de Superfície de Ataque Cloud** (Rede -> Computação -> Identidade -> Dados)
- [[cloudquery-execucao-segura-containers-kubernetes-cronjob-telemetria]] — CloudQuery em Produção: Implantação como **Kubernetes CronJob Hardened**, Logs Estruturados e Monitoramento de Métricas OpenTelemetry

### JADX (skylot/jadx) — Decompilador Dex-to-Java e Analisador de Segurança Android (APK, AAB, DEX, ARSC, AndroidManifest.xml), Deobfuscator e Scripting

- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — **JADX (`skylot/jadx`)**: Arquitetura do Decompilador **Dalvik/ART Bytecode (`.dex`) para Java** e Decodificador Nativo de `.apk`, `.aab` e `resources.arsc`
- [[jadx-modos-decompilacao-restructure-simple-fallback-show-bad-code]] — JADX: Modos de Decompilação (**`-m auto | restructure | simple | fallback`**) e **`--show-bad-code`** para Métodos Ofuscados que Falham no AST
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — JADX: Desofuscação Automática (**`--deobf`**, `.jobf`), Importação de Mapas **ProGuard/R8 (`--mappings-path`)** e Metadados **Kotlin (`kotlin.Metadata`)**
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Auditoria de Superfície de Ataque Android no JADX: **`AndroidManifest.xml`**, Componentes Exportados (`exported="true"`), **Intent Filters / Deep Links** e `allowBackup`
- [[jadx-auditoria-segredos-hardcoded-strings-xml-buildconfig-native-libs]] — JADX: Caça a **Segredos Hardcoded, Chaves de API, URLs de Homologação e Credenciais** em `BuildConfig.java`, `res/values/strings.xml` e `assets/`
- [[jadx-auditoria-webview-javascriptinterface-ssl-pinning-criptografia]] — Auditoria de Código no JADX (**OWASP MASVS-CODE & CRYPTO**): **WebViews Inseguras (`addJavascriptInterface`)**, **`X509TrustManager` Vazio** e Criptografia Fraca
- [[jadx-exportacao-grafos-fluxo-controle-cfg-call-graph-dot-json]] — JADX: Exportação de **Control Flow Graphs (`--cfg`, `--raw-cfg`)**, **Grafo de Chamadas (`--call-graph json|dot`)** e Saída Estruturada (`--output-format json`)
- [[jadx-exportacao-projeto-gradle-export-gradle-android-studio-ide]] — JADX **`-e` / `--export-gradle`**: Exportação Direta do APK/AAR como um **Projeto Gradle (`build.gradle`)** para Análise no **Android Studio / IntelliJ IDEA**
- [[jadx-depurador-smali-integrado-jadx-gui-adb-jdwp-breakpoints]] — JADX **`jadx-gui` Smali Debugger**: Depuração Passo a Passo via **JDWP / `adb`**, Inspeção de Registradores (`v0`, `p0`) e *Stack Frames* em Tempo Real
- [[jadx-automacao-scripts-jadx-kts-plugins-transformacao-ast]] — JADX Scripting (**`.jadx.kts` Kotlin Scripts**) & `jadx plugins`: Automação de Desofuscação de Strings e Transformação da AST no Pipeline de Decompilação

### Apktool (iBotPeaches/Apktool) — Engenharia Reversa, Decodificação de Recursos Binários (resources.arsc / Binary XML), Patching Smali e Recompilação de APKs

- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — **Apktool (`iBotPeaches/Apktool`)**: Arquitetura de Decodificação de **Binary XML (`AXML`), `resources.arsc`** e Disassembly **Smali (`baksmali`/`smali`)**
- [[apktool-controles-decodificacao-no-src-no-res-only-main-classes]] — Apktool (`d` / `decode`): Uso Cirúrgico de **`-s` (`--no-src`)**, **`-r` (`--no-res`)** e **`--only-main-classes`** para Evitar Erros de `aapt2` em APKs Complexos
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Apktool na Prática: Habilitando **Interceptação HTTPS de CAs de Usuário (`network_security_config.xml`)** e **`android:debuggable="true"`** em Android 7+
- [[apktool-engenharia-reversa-edicao-bytecode-smali-registradores-patch]] — Apktool & **Bytecode Smali**: Anatomia de Métodos (`.locals`, `v0`/`p0`), Desvios Condicionais (`if-eqz`/`if-nez`) e Patching de *Root Detection* / *SSL Pinning*
- [[apktool-injecao-frida-gadget-so-smali-dispositivos-sem-root]] — Apktool + **`frida-gadget.so`**: Como Embutir o Frida Dentro de um APK via `System.loadLibrary` em Smali para Instrumentação em **Aparelhos Sem Root**
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Apktool (`b` / `build`) + **`zipalign`** + **`apksigner` (v1/v2/v3/v4)**: O Pipeline Completo de Recompilação e Assinatura para Android 11–15+
- [[apktool-gestao-frameworks-if-install-framework-roms-fabricantes]] — Apktool (`if` / `install-framework`): Gestão de **APKs de Framework (`framework-res.apk`)** para Aplicativos de Sistema de Fabricantes (Samsung / Xiaomi / AOSP)
- [[apktool-aplicativos-split-apks-app-bundles-aab-fusao-reconstrucao]] — Auditoria de **Split APKs / Android App Bundles (`.aab`, `.apks`, `.xapk`)** com Apktool: Como Decodificar e Fundir Múltiplos Splits (`base.apk` + `split_config.*.apk`)
- [[apktool-anatomia-apktool-yml-sdkinfo-donotcompress-unkownfiles]] — Apktool: Anatomia do Arquivo de Controle **`apktool.yml`** (`sdkInfo`, `versionInfo`, `doNotCompress` e `unknownFiles`)
- [[apktool-defesas-anti-repackaging-assinatura-play-integrity-auditoria]] — Engenharia Defensiva Mobile (**OWASP MASVS-RESILIENCE**): Detecção de **Repackaging (`Apktool`)**, Verificação de Certificado de Assinatura e **Play Integrity API**

### Pwndbg (pwndbg/pwndbg) — Plug-in de Depuração de Baixo Nível, Engenharia Reversa e Exploração de Binários/Kernel para GDB e LLDB

- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — **Pwndbg (`pwndbg/pwndbg`)**: Arquitetura Multi-Debugger (**GDB 12.1+ & LLDB 19+**) com Desmontagem/Emulação **Capstone + Unicorn** e Painel `context`
- [[pwndbg-auditoria-mitigacoes-binarias-checksec-vmmap-aslr-pie-nx-canary]] — Pwndbg: Auditoria de Mitigações de Compilação (**`checksec`: RELRO, Stack Canary, NX, PIE, Fortify, CFI/CET**) e Mapeamento Virtual (**`vmmap`**, **`canary`**)
- [[pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins]] — Pwndbg para **Heap Exploitation (`glibc ptmalloc2` & `jemalloc`)**: Comandos **`heap`**, **`vis_heap_chunks` (`vis`)**, **`bins`**, **`tcache`**, **`arena`** e **`try_free`**
- [[pwndbg-busca-memoria-search-leakfind-telescope-cyclic-offset]] — Pwndbg: Introspecção de Ponteiros (**`telescope`**, **`search`**, **`leakfind`**, **`probeleak`**) e Cálculo de Offset de Buffer Overflow (**`cyclic`**)
- [[pwndbg-analise-got-plt-got-overwrite-relro-ret2plt-ret2libc]] — Pwndbg: Inspeção da **Global Offset Table (`got`)** e **Procedure Linkage Table (`plt`)**, Resolução Lazy Binding (`_dl_runtime_resolve`) e *ret2libc*
- [[pwndbg-integracao-decompiladores-decomp2dbg-ghidra-ida-binja]] — Pwndbg + **Ghidra / IDA / Binary Ninja (`decomp2dbg`)**: Sincronização em Tempo Real de **Código Decompilado C, Símbolos e Structs** no Terminal
- [[pwndbg-depuracao-kernel-linux-qemu-system-kchecksec-slab-pagewalk]] — Pwndbg para **Linux Kernel Exploitation & Research (`qemu-system`)**: Comandos **`kchecksec`**, **`kversion`**, **`slab` (SLUB)**, **`buddydump`** e **`pagewalk`**
- [[pwndbg-inspecao-estado-processo-procinfo-fds-seccomp-rop-runtime]] — Pwndbg: Inspeção de Estado do Processo (**`procinfo`**: UID/GID, **SELinux**, File Descriptors, Conexões), Filtros **Seccomp** e Busca **`rop` / `ropper`** em Runtime
- [[pwndbg-depuracao-binarios-go-rust-windbg-compatibility-layer]] — Pwndbg: Depuração de Binários **Go (`go-dump`)**, Camada de Compatibilidade **WinDbg (`dd`, `dq`, `dps`, `eb`, `eq`)** e Suporte a **LLDB (`pwndbg-lldb`)**
- [[pwndbg-depuracao-cross-architecture-qemu-user-arm-mips-riscv-iot]] — Pwndbg + **`qemu-user` (`qemu-arm`, `qemu-aarch64`, `qemu-mipsel`, `qemu-riscv64`)**: Depuração de Binários **IoT e Firmware Embarcado** em Estações `x86_64`

### Ropper (sashs/Ropper) — Buscador de Gadgets ROP/JOP/SYS Multi-Arquitetura (Capstone/Keystone/PyVEX/Z3), Busca Semântica, Filtro de Badbytes e Geração de Chains

- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — **Ropper (`sashs/Ropper`)**: Arquitetura Multi-Formato (**ELF, PE, Mach-O, Raw**) e Busca de Gadgets **ROP, JOP e SYS** sobre **Capstone & `filebytes`**
- [[ropper-inspecao-cabecalhos-mitigacoes-sec-nx-aslr-cfg-pe-elf]] — Ropper: Inspeção de Cabeçalhos Binários (**`-i`, `-e`, `--imagebase`, `-s`, `-S`, `--imports`, `--symbols`**) e Filtro **Microsoft Control Flow Guard (`--cfg-only`)**
- [[ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade]] — Ropper: Busca Avançada de Gadgets (**`--search`**, `--quality`, **`--stack-pivot`**, `-p` `pop-pop-ret`, `-j` `jmp reg`) e Filtro de **`--badbytes` (`-b`)**
- [[ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores]] — Ropper **`--semantic` (`PyVEX` + `Z3 Theorem Prover`)**: Busca Semântica de Gadgets por Efeito Matemático e Preservação de Registradores (`!reg`)
- [[ropper-geracao-automatica-rop-chains-execve-mprotect-ret2libc]] — Ropper **`--chain`**: Geração Automática de Cadeias ROP Completas (**`execve`**, **`spawn_shell` (`ret2libc`)**, **`mprotect`** e **`virtualprotect`**)
- [[ropper-montador-desmontador-keystone-capstone-asm-disasm-strings]] — Ropper como Canivete Suíço de Opcodes: Montagem **Keystone (`--asm`)**, Desmontagem **Capstone (`--disasm`)** e Busca de Strings/Hex (`--string`, `--section`)
- [[ropper-gadgets-multi-arquitetura-arm-thumb-arm64-mips-iot]] — ROP Multi-Arquitetura no Ropper: Peculiaridades de Gadgets em **ARM32 / Thumb (`pop {pc}` / `bx lr`)**, **ARM64 (`AArch64` `ldp` / `ret`)** e **MIPS (`jr $ra`)**
- [[ropper-automacao-api-python-ropperservice-integracao-pwntools]] — Automação de Exploits em Python com **`RopperService` (`from ropper import RopperService`)**: Busca Programática de Gadgets e Integração com Scripts
- [[ropper-console-interativo-multi-binarios-cache-raw-firmware]] — Ropper **`--console`** e Arquivos **`--raw` (`-r`)**: Sessão Interativa Multi-Binários e Extração de Gadgets em **Dumps de Memória e Firmware Raw (`binwalk`)**
- [[ropper-defesas-contra-rop-jop-cet-shstk-ibt-pac-bti-cfi]] — Engenharia Defensiva contra **ROP e JOP**: Como Funcionam **Intel CET (`SHSTK` & `IBT`)**, **ARM PAC (`Pointer Authentication`) / BTI** e **LLVM CFI**

### Thoughtworks Talisman (thoughtworks/talisman) — Prevenção de Vazamento de Segredos e Chaves Privadas em Hooks Git (pre-commit/pre-push), Detectores de Entropia/Checksums (.talismanrc) e Scan de Histórico

- [[talisman-arquitetura-prevencao-segredos-git-hooks-pre-commit-pre-push]] — **Thoughtworks Talisman (`thoughtworks/talisman`)**: Arquitetura dos **6 Detectores de Segredos** em Hooks Git (**`pre-commit` vs `pre-push`**)
- [[talisman-governanca-checksum-sha256-talismanrc-ignore-detectors]] — Talisman **`.talismanrc` & Checksum SHA-256 (`--checksum`)**: Por Que o Modelo de **Exceção Vinculada ao Hash** Impede Vazamentos Futuros em Arquivos Ignorados
- [[talisman-configuracao-avancada-scopeconfig-allowed-custom-patterns-severity]] — Talisman `.talismanrc`: Escopos de Linguagem (**`scopeconfig`**), Expressões Permitidas (**`allowed_patterns` Vault**), **`custom_patterns`** e **`threshold`**
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Talisman em Escala de Engenharia: Instalação via **Global Git Hook Template (`init.templateDir`)**, Framework **`pre-commit`** e **Husky**
- [[talisman-modo-interativo-talisman-interactive-cli-developer-experience]] — Talisman Modo Interativo (**`-i` / `TALISMAN_INTERACTIVE=true`**): Fluxo Guiado de Aprovação de Falsos Positivos e Atualização Automática do `.talismanrc`
- [[talisman-varredura-historico-git-scan-reportdirectory-scanwithhtml]] — Talisman em **CI/CD e Auditoria de Repositórios**: Varredura Completa de Histórico Git (**`--scan`**), **`--ignoreHistory`**, **`--pattern`** e Relatórios HTML (`--scanWithHtml`)
- [[talisman-anatomia-detectores-entropia-base64-hex-creditcard-filesize]] — Por Dentro dos Detectores do Talisman: Cálculo de **Entropia de Shannon**, Decodificação Recursiva **Base64/Hex**, Cartões de Crédito e Limite de Tamanho
- [[talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection]] — Governança DevSecOps sobre o `.talismanrc`: Como Impedir que Desenvolvedores Aprovem Vazamentos Reais via **GitHub `CODEOWNERS`** e Auditoria de PR
- [[talisman-resposta-incidente-vazamento-revogacao-git-filter-repo]] — Resposta a Incidentes de Vazamento de Segredo no Git: Por Que um Commit de `git rm` Não Apaga o Segredo e Como Limpar o Histórico com `git filter-repo`
- [[talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog]] — Defesa em Profundidade para Segredos no Git: Comparação Técnica entre **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**

### awslabs git-secrets (awslabs/git-secrets) — Prevenção de Commits de Credenciais AWS, Mensagens de Commit e Merges via Hooks Git e Secret Providers

- [[gitsecrets-arquitetura-prevencao-credenciais-aws-hooks-git-grep]] — **awslabs `git-secrets` (`awslabs/git-secrets`)**: Arquitetura dos **3 Hooks Git (`pre-commit`, `commit-msg`, `prepare-commit-msg`)** e Subcomando Nativo `git secrets`
- [[gitsecrets-registro-padroes-aws-register-aws-bedrock-aws-provider]] — `git-secrets` **`--register-aws` & `--aws-provider`**: Detecção de Prefixos IAM (`AKIA`, `ASIA`, `AROA`), Chaves **Amazon Bedrock (`ABSK`)** e Leitura de `~/.aws/credentials`
- [[gitsecrets-padroes-proibidos-permitidos-gitallowed-provedores-externos]] — `git-secrets`: Adição de Padrões Proibidos (`--add`), Literais (`--literal`), Exceções (`.gitallowed` / `--allowed`) e **Secret Providers (`--add-provider`)**
- [[gitsecrets-instalacao-hooks-locais-templates-globais-init-templatedir]] — `git-secrets` em Escala Corporativa: Configuração de **Templates Globais do Git (`init.templateDir`)** e Injeção Retroativa em Repositórios Existentes
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — `git-secrets` Modos de Varredura: **`--scan`** (`--cached`, `--untracked`, `--no-index`, `-r`, `stdin`) vs **`--scan-history`** em Todo o Histórico Git
- [[gitsecrets-protecao-env-local-secret-provider-dinamico-vazamento]] — Técnica Avançada com `git-secrets`: Usando **`--add-provider`** para Garantir que Nenhum Valor do `.env` Local Seja Copiado para o Código
- [[gitsecrets-diferencas-egrep-gnu-bsd-macos-linux-portabilidade]] — Portabilidade de Expressões Regulares no `git-secrets`: Diferenças entre **GNU `grep -E` (Linux)** e **BSD `grep -E` (macOS)** e Boas Práticas POSIX ERE
- [[gitsecrets-bloqueio-merges-contaminados-prepare-commit-msg-no-ff]] — Como o Hook **`prepare-commit-msg`** do `git-secrets` Impede que um **Merge (`--no-ff`)** Contamine a Branch Principal com Histórico Sujo
- [[gitsecrets-integracao-pipelines-cicd-github-actions-gitlab-pre-receive]] — Implantação de `git-secrets` em **Pipelines CI/CD** e **Hooks Server-Side (`pre-receive`)** para Impedir Bypass com `git commit --no-verify`
- [[gitsecrets-eliminacao-credenciais-estaticas-aws-oidc-sso-iam-roles]] — Além do `git-secrets`: Como Eliminar 100% as Chaves Estáticas `AKIA...` nas Estações e no CI/CD com **AWS IAM Identity Center (SSO)** e **OIDC Federation**

### CDK — Zero-Dependency Container Penetration Toolkit (cdk-team/CDK) — Auditoria de Isolamento de Containers, Linux Capabilities, Cgroups, Docker Socket e Kubernetes

- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — **CDK (`cdk-team/CDK`)**: Arquitetura do Toolkit **Zero-Dependency** em Go para Auditoria de Segurança e Pós-Exploração em Containers Slim/Distroless
- [[cdk-escapes-capabilities-cap-dac-read-search-sys-admin-sys-module-ptrace]] — CDK & **Linux Capabilities Perigosas**: Auditoria e Exploração de **`CAP_DAC_READ_SEARCH`** (`open_by_handle_at`), **`CAP_SYS_MODULE`**, **`CAP_SYS_ADMIN`** e **`CAP_SYS_PTRACE`**
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — CDK: Anatomia de Escapes via **Cgroups v1 `release_agent` (`mount-cgroup`)**, **User Namespaces (`CVE-2022-0492`)**, `rewrite-cgroup-devices`, `mount-procfs` e `lxcfs-rw`
- [[cdk-auditoria-docker-socket-api-runc-containerd-shim-ucurl-dcurl]] — CDK: Comprometimento via **Docker Unix Socket (`docker.sock`, `ucurl`)**, **Docker TCP API (`:2375`, `dcurl`)**, `runc` (`CVE-2019-5736`) e `containerd-shim` (`CVE-2020-15257`)
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — CDK para **Kubernetes**: Clientes Nativos **`cdk kcurl`** (API Server), **`cdk ectl`** (`etcd`), Dump de `Secrets`/`ConfigMaps` e Descoberta de Componentes
- [[cdk-ferramentas-embutidas-net-tools-ps-netstat-ifconfig-probe-nc-vi]] — CDK **Built-in Tool Module**: Como Operar em Containers Distroless usando **`cdk ps`**, **`cdk netstat`**, **`cdk ifconfig`**, **`cdk probe`**, **`cdk nc`** e **`cdk vi`**
- [[cdk-auditoria-cloud-metadata-imds-ak-leakage-istio-route-localnet]] — CDK: Auditoria de **Cloud Metadata API (IMDS)**, Varredura de Chaves (**`ak-leakage`**), Sidecar **Istio (`istio-check`)** e `route_localnet` (`CVE-2020-8558`)
- [[cdk-auditoria-persistencia-kubernetes-daemonset-cronjob-shadow-apiserver]] — Análise de Técnicas de **Persistência em Kubernetes** Mapeadas pelo CDK (`k8s-backdoor-daemonset`, `k8s-cronjob`, `k8s-shadow-apiserver` e `CVE-2020-8554`)
- [[cdk-entrega-binarios-containers-restritos-dev-tcp-thin-builds-deteccao]] — Análise de Entrega *Fileless/In-Band* em Containers (`/dev/tcp`, `thin` builds) e Como **Bloquear na Camada de Runtime (`KubeArmor` / `Tracee`)**
- [[cdk-compilacao-customizada-build-tags-perfis-avaliacao-red-team]] — CDK: Perfis de Avaliação (**`--profile`**), Compilação Seletiva por **Go Build Tags (`thin`)** e Testes de Regressão de Hardening Kubernetes

### Peirates (inguardians/peirates) — Plataforma de Pentest e Pós-Exploração Kubernetes, Gestão de ServiceAccounts/Certificados, Cloud IMDS, Kubelet API e Escapes

- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — **Peirates (`inguardians/peirates`)**: Arquitetura da Plataforma de Pentest Kubernetes, Gestão de **Múltiplos Contextos de `ServiceAccount` (`sa-menu`)** e Modo `-m`
- [[peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac]] — Peirates: Coleta de Tokens (`list-secrets`, **`secret-to-sa`**), Prechecks **`set-auth-can-i`** e Força Bruta de Contextos (**`kubectl-try-all-until-success`**)
- [[peirates-coleta-credenciais-cloud-imds-aws-gcp-kops-s3-gcs]] — Peirates na Nuvem (**AWS EKS / kOps & Google GKE**): Comandos **`aws-get-token`**, **`gcp-get-token`**, **`gcp-attack-kube-env`** e **`aws-attack-kops-1`**
- [[peirates-execucao-remota-pods-exec-via-api-exec-via-kubelet-10250]] — Peirates: Movimentação Lateral e Execução Remota em Pods via **`exec-via-api` (`21`)** e **Kubelet API (`exec-via-kubelet` `22` na Porta `10250`)**
- [[peirates-escapes-containers-docker-socket-hostpath-hostpid-leakyvessels]] — Peirates: Escapes de Container e Comprometimento de Nó (**`attack-pod-hostpath-mount`**, **`leakyvessels` CVE-2024-21626**, **`hostpid-breakout`** e **`docker-socket-breakout`**)
- [[peirates-escapes-avancados-core-pattern-ptrace-hostlog-symlink]] — Peirates: Técnicas Avançadas de Escape (**`hostproc-core-pattern-breakout` `29`**, **`hostpid-ptrace-breakout` `32`** e **`hostlog-symlink-read` `33`**)
- [[peirates-roubo-credenciais-filesystem-no-nodefs-steal-secrets-cert-menu]] — Peirates Pós-Escape: Coleta Automatizada de Credenciais do Nó (**`nodefs-steal-secrets` `30`**) e Contextos de Certificados TLS (**`cert-menu` `9`**)
- [[peirates-descoberta-interna-pods-mounts-tcpscan-enumerate-dns]] — Peirates: Reconhecimento Interno de Cluster com **`dump-pod-info` (`4`)**, **`find-volume-mounts` (`5`)**, **`tcpscan` (`93`)** e **`enumerate-dns` (`94`)**
- [[peirates-execucao-kubectl-embutido-curl-shell-interativo]] — Peirates: Uso da Biblioteca **`kubectl` Embutida (`90`)**, Cliente HTTP **`curl` (`91`)** e Comandos de Sistema de Arquivos (`cd`, `ls`, `cat`, `shell`)
- [[peirates-matriz-defesa-profundidade-kubernetes-pss-rbac-imds-ebpf]] — Matriz de Defesa em Profundidade Kubernetes (Marco **1.000/2.000** do Lote `software-seguranca-2000-0003`): Como Neutralizar **Peirates & CDK** do Código ao Kernel

## Tranche 11 (IDs 1001–1100)

### CNCF Cartography (cartography-cncf/cartography) — Consolidação de Ativos Multi-Cloud, Kubernetes, Identidade (Okta/GitHub/Entra) e Superfície de Ataque em Grafo Neo4j

- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — **CNCF Cartography (`cartography-cncf/cartography`)**: Arquitetura de Consolidação de Ativos de Infraestrutura, Nuvem, Kubernetes e Identidade em **Grafo Neo4j**
- [[cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3]] — Cartography **Data Enrichment (`Analysis Jobs`)**: Como São Calculados os Atributos Derivados **`exposed_internet: true`** e **`anonymous_access: true`**
- [[cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s]] — Threat Hunting e Descoberta de **Caminhos de Ataque (*Attack Paths*)** no Cartography com Consultas **OpenCypher** Multi-Hop
- [[cartography-identidade-federada-okta-entra-aws-github-keycloak]] — Grafo de Identidade Cross-Platform no Cartography: Correlacionando **Okta, Microsoft Entra ID, Keycloak, Google Workspace, GitHub e AWS IAM**
- [[cartography-motor-regras-cartography-rules-auditoria-automatizada]] — Execução Automatizada de Regras de Segurança no Grafo com **`cartography-rules`** (`list`, `run`, `object_storage_public` e Frameworks)
- [[cartography-gestao-vulnerabilidades-cves-epss-kev-crowdstrike-ecr]] — Priorização de Vulnerabilidades Baseada em Contexto no Cartography: Cruzando **CrowdStrike Spotlight, AWS ECR/Inspector, EPSS e CISA KEV**
- [[cartography-topologia-kubernetes-eks-gke-aks-pods-rbac-containers]] — Mapeamento de Clusters **Kubernetes (EKS, GKE, AKS)** no Cartography: Conectando `Pod`, `Container`, `ServiceAccount`, `RBAC`, `Service` e Imagens Cloud
- [[cartography-governanca-ia-agentes-bedrock-vertex-openai-anthropic-aibom]] — Segurança e Governança de **IA em Produção (`AI Security Posture / AIBOM`)** no Cartography: **AWS Bedrock, GCP Vertex AI, OpenAI e Anthropic**
- [[cartography-sincronizacao-multi-conta-update-tag-cleanup-staleness]] — Operação em Produção do Cartography: Sincronização Multi-Conta AWS (`--aws-sync-all-profiles`), **`UPDATE_TAG`** e Limpeza de Nós Obsoletos (**`Cleanup Jobs`**)
- [[cartography-extensibilidade-custom-modules-drift-detection-auditoria]] — Extensibilidade do Cartography: Como Construir **Módulos Customizados (`IntelModule`)** para Ingerir Ativos Internos e CMDBs no Grafo de Segurança

### NCC Group Scout Suite (nccgroup/ScoutSuite) — Auditoria de Postura de Segurança Multi-Cloud (AWS, Azure, GCP, Alibaba, OCI) Offline via Rulesets JSON

- [[scoutsuite-arquitetura-auditoria-multi-cloud-offline-nccgroup]] — **NCC Group Scout Suite (`nccgroup/ScoutSuite`)**: Arquitetura de Auditoria de Postura de Segurança Multi-Cloud Assíncrona e **Inspeção 100% Offline**
- [[scoutsuite-auditoria-aws-iam-s3-ec2-rds-cloudtrail-vpc]] — Scout Suite na **AWS (`scout aws`)**: Escopo de Serviços (`--services`), Regiões (`--regions`), Controle de Taxa (`--max-rate`) e Mínimo Privilégio IAM
- [[scoutsuite-auditoria-azure-rbac-entra-storage-network-keyvault]] — Scout Suite no **Microsoft Azure (`scout azure`)**: Modos de Autenticação (`--cli`, `--msi`, `--service-principal`) e Varredura Multi-Subscription
- [[scoutsuite-auditoria-gcp-projects-folders-organizations-service-account]] — Scout Suite no **Google Cloud Platform (`scout gcp`)**: Auditoria em Escala por **Organization (`--organization-id`), Folder (`--folder-id`) e `--all-projects`**
- [[scoutsuite-customizacao-rulesets-regras-json-conditions-parametrizadas]] — Anatomia do Motor de Regras do Scout Suite (**`Ruleset` & `ProcessingEngine`**): Como Escrever **Regras e Rulesets JSON Customizados (`--ruleset`)**
- [[scoutsuite-reexecucao-offline-fetch-local-update-comparacao-diffs]] — Workflow Avançado do Scout Suite: Reavaliação Instantânea com **`--fetch-local`**, Atualização Parcial (**`--update`**) e Exportação JSON/SQLite (`--result-format`)
- [[scoutsuite-gestao-excecoes-exceptions-json-mapeamento-ip-ranges]] — Redução de Falsos Positivos e Enriquecimento de Rede no Scout Suite: Arquivos de Exceção (**`--exceptions`**) e Mapeamento de CIDRs Conhecidos (**`--ip-ranges`**)
- [[scoutsuite-auditoria-alibaba-oci-digitalocean-kubernetes-multicloud]] — Auditoria de Nuvens Alternativas e Clusters com Scout Suite: **Alibaba Cloud (`aliyun`), Oracle Cloud (`oci`), DigitalOcean (`do`) e Kubernetes (`k8s`)**
- [[scoutsuite-extracao-dados-jq-automacao-cicd-defectdojo-ingestao]] — Automação e Integração do Scout Suite em Pipelines CI/CD: Parsing do Payload JSON (`scoutsuite_results_*.js`) com **`jq`** e Ingestão no **DefectDojo**
- [[scoutsuite-comparacao-cspm-scoutsuite-prowler-steampipe-cartography]] — Arquitetura Comparativa de Ferramentas Open-Source de Segurança Cloud: Quando Usar **Scout Suite vs Prowler vs Steampipe/Powerpipe vs CloudQuery vs Cartography**

### Rhino Security Labs Pacu (RhinoSecurityLabs/pacu) — Framework de Pentest, Escalação de Privilégio IAM, Movimentação Lateral e Red Team em AWS

- [[pacu-arquitetura-framework-pentest-aws-sessoes-sqlite-modulos]] — **Rhino Security Labs Pacu (`RhinoSecurityLabs/pacu`)**: Arquitetura do Framework de Pentest e Red Team para **AWS**, Sessões Isoladas e Banco **SQLite/SQLAlchemy**
- [[pacu-gestao-credenciais-set-keys-import-keys-whoami-bruteforce-permissions]] — Reconhecimento Furtivo de Permissões no Pacu: `set_keys`, `import_keys`, `whoami` e **`iam__bruteforce_permissions` / `iam__enum_permissions`**
- [[pacu-escalacao-privilegio-iam-privesc-scan-21-vetores-ataque]] — Escalação de Privilégio no AWS IAM com Pacu (**`iam__privesc_scan`**): Anatomia dos **21+ Vetores Clássicos de Privesc (`PassRole`, `CreatePolicyVersion`, `AttachUserPolicy`)**
- [[pacu-enumeracao-externa-sem-autenticacao-iam-roles-users-account-id]] — Reconhecimento AWS **Sem Credenciais na Conta Alvo** no Pacu: Enumeração de Roles e Usuários via Validação de `AssumeRolePolicy` e `S3/KMS` Cross-Account
- [[pacu-auditoria-monitoramento-cloudtrail-guardduty-config-deteccao]] — Pacu vs Monitoramento AWS (**CloudTrail, GuardDuty, Config & CloudWatch**): Módulos de Enumeração (`detection__enum_services`) e Controles de Blindagem (SCPs)
- [[pacu-pos-exploracao-ec2-userdata-ssm-ebs-snapshots-exfiltracao]] — Pós-Exploração em **Amazon EC2, SSM e EBS** com Pacu: Extração de Segredos de **`UserData` (`ec2__download_userdata`)**, Snapshots EBS e Execução via **Systems Manager**
- [[pacu-auditoria-lambda-env-vars-codigo-backdoor-api-gateway]] — Auditoria e Pós-Exploração de **AWS Lambda (`lambda__enum`)** no Pacu: Extração de Código-Fonte, Variáveis de Ambiente e Riscos de `UpdateFunctionCode`
- [[pacu-deteccao-honeytokens-canarytokens-aws-iam-detect-honeytokens]] — Detecção de **Honeytokens / Canarytokens AWS** (`iam__detect_honeytokens`) e Como Projetar **Decoys de Credenciais AWS Indetectáveis** para o Blue Team
- [[pacu-persistencia-aws-backdoor-iam-roles-users-lambda-remediacao]] — Análise de Técnicas de **Persistência em AWS IAM** Mapeadas pelo Pacu (`iam__backdoor_*`) e Playbook de **Erradicação e Resposta a Incidentes (DFIR)**
- [[pacu-automacao-purple-team-aws-cloudtrail-sigma-guardduty-validacao]] — Engenharia de Detecção (**Purple Team AWS**) com Pacu: Como Validar Regras **Sigma (`aws_cloudtrail`)** e Alertas do **Amazon GuardDuty**

### MobSF — Mobile Security Framework (MobSF/Mobile-Security-Framework-MobSF & MobSF/mobsfscan) — Plataforma Automatizada de SAST, DAST e Análise de Malware Mobile (Android APK/AAB, iOS IPA e Windows APPX)

- [[mobsf-arquitetura-sast-dast-mobile-apk-aab-ipa-appx]] — **Mobile Security Framework (`MobSF`)**: Arquitetura da Plataforma All-in-One de **SAST, DAST e Análise de Malware Mobile** (`APK`, `AAB`, `XAPK`, `IPA`, `APPX`)
- [[mobsf-analise-estatica-android-manifest-certificados-apkid-niap]] — MobSF **Android Static Analyzer**: Auditoria de Assinaturas (`apksigtool` v1–v4), Detecção de Packers (**`APKiD`**), `AndroidManifest.xml`, **NIAP** e Bibliotecas `.so` (`LIEF`)
- [[mobsf-analise-estatica-ios-ipa-plist-ats-macho-pie-arc-canary]] — MobSF **iOS Static Analyzer**: Auditoria de Pacotes `.ipa`, **`Info.plist` (`App Transport Security / ATS`)**, Entitlements e Binários **Mach-O (`PIE`, `ARC`, `Canary`)**
- [[mobsf-analise-dinamica-android-ios-frida-emulator-corellium-mitm]] — MobSF **Dynamic Analyzer**: Instrumentação Interativa com **Frida**, Emuladores Android (**AVD / Genymotion**) e **Corellium iOS** com Interceptação HTTPS
- [[mobsf-instrumentacao-frida-live-api-monitor-scripts-auxiliares]] — MobSF **Live API Monitor & Frida Code Editor**: Monitoramento de Criptografia/Rede em Tempo Real e Scripts Auxiliares (`SSL Pinning`, `Root Bypass`, `Hook`)
- [[mobsf-mobsfscan-sast-shift-left-codigo-java-kotlin-swift-objc-sarif]] — **`mobsfscan` (`MobSF/mobsfscan`)**: SAST Shift-Left de Código-Fonte Mobile (**Java, Kotlin, Android XML, Swift, Objective-C e `Info.plist`**) com Saída **SARIF e SonarQube**
- [[mobsf-analise-privacidade-trackers-exodus-permissoes-malware-domains]] — Auditoria de **Privacidade (LGPD/GDPR), Rastreadores (`Exodus Privacy`) e Inteligência de Malware** no MobSF: SDKs de Terceiros, Domínios, GeoIP e Quarks/APKiD
- [[mobsf-automacao-api-rest-cicd-pdf-json-scorecard-diff]] — Automação DevSecOps com a **API REST do MobSF (`/api/v1/*`)**: Upload, Scan, Relatório JSON/PDF, **App Security Scorecard** e **Diff/Compare de Versões**
- [[mobsf-auditoria-segredos-entropia-firebase-aws-google-services-json]] — Caça a Credenciais Cloud e **Bancos Firebase Abertos (`google-services.json` / `GoogleService-Info.plist`)** em Aplicativos Mobile com MobSF
- [[mobsf-implantacao-corporativa-autenticacao-saml-sso-postgres-seguranca]] — Implantação Corporativa Segura do MobSF: Autenticação **SAML 2.0 SSO (`python3-saml`)**, Banco **PostgreSQL**, Filas Assíncronas (`django-q2`) e Hardening

### SensePost Objection (sensepost/objection) — Exploração em Runtime Mobile (Android & iOS) movida por Frida sem Root/Jailbreak (patchapk, patchipa, SSL Pinning Bypass, Keystore/Keychain)

- [[objection-arquitetura-runtime-mobile-exploration-frida-repl-usb]] — **SensePost Objection (`sensepost/objection`)**: Arquitetura de Exploração Mobile em Runtime sobre **Frida** para **Android e iOS Sem Root/Jailbreak**
- [[objection-patchapk-patchipa-instrumentacao-sem-root-jailbreak]] — Instrumentação Sem Root/Jailbreak com **`objection patchapk`** e **`objection patchipa`**: Automação do `frida-gadget` e Configurações de Script
- [[objection-bypass-ssl-pinning-android-ios-network-security-trustkit]] — Bypass Universal de **SSL/TLS Certificate Pinning** no `objection`: **`android sslpinning disable`** e **`ios sslpinning disable`** (`OkHttp3`, `Conscrypt`, `TrustKit`, `NSURLSession`)
- [[objection-bypass-root-jailbreak-detection-simulacao-android-ios]] — Auditoria de Detecção de **Root e Jailbreak** no `objection`: Comandos **`disable`** vs **`simulate`** para Testar a Resiliência da Defesa do Aplicativo
- [[objection-inspecao-android-keystore-heap-activities-intents-services]] — Exploração Android no `objection`: Auditoria do **Android Keystore (`android keystore list`)**, Manipulação de **Objetos na Heap (`android heap`)** e Lançamento de **Activities/Intents**
- [[objection-exploracao-ios-keychain-dump-nsuserdefaults-plist-bypasses]] — Exploração iOS no `objection`: Dump do **iOS Keychain (`ios keychain dump`)**, **`ios nsuserdefaults get`**, **`ios plist cat`**, **`ios cookies get`** e Bypass de **`TouchID/FaceID`**
- [[objection-inspecao-memoria-memory-dump-search-write-sqlite-files]] — Auditoria de Memória RAM e Bancos Locais no `objection`: **`memory dump`**, **`memory search`**, **`sqlite connect`** e Proteção de Dados em Repouso (**SQLCipher**)
- [[objection-hooking-dinamico-watch-class-method-argumentos-stacktrace]] — Engenharia Reversa Dinâmica sem Decompilação no `objection`: Rastreamento de Classes, Argumentos, Retornos e **Stack Traces (`--dump-args --dump-return --dump-backtrace`)**
- [[objection-sistema-plugins-customizados-importacao-scripts-frida-api]] — Extensibilidade do `objection`: Sistema de **Plugins (`plugin load`)**, Execução de Scripts Frida (`import`) e API REST (`--api-host` / `--api-port`)
- [[objection-protecao-ui-flag-secure-screenshots-clipboard-backgrounding]] — Auditoria de Proteções de Interface e Vazamento em Background no `objection`: **`android ui FLAG_SECURE`**, Pasteboard/Clipboard e Snapshots de Tela

### angr (angr/angr) — Framework Python de Análise Binária, Execução Simbólica/Concólica (SimulationManager, Claripy/Z3, PyVEX, CLE) e Decompilação

- [[angr-arquitetura-analise-binaria-execucao-simbolica-cle-pyvex-claripy]] — **`angr` (`angr/angr`)**: Arquitetura da Suíte de Análise Binária Multi-Arquitetura (**`CLE`, `archinfo`, `PyVEX`, `Claripy/Z3`, `SimEngine` e `Analyses`**)
- [[angr-carregador-binarios-cle-shared-libraries-firmware-blobs-base-addr]] — O Carregador **`CLE` (*CLE Loads Everything*)** do `angr`: Espaço de Endereçamento, Posição Independente (`PIE`), Bibliotecas Compartilhadas e **Firmware Raw (`Blob`)**
- [[angr-motor-solver-claripy-bitvectors-bvs-bvv-restricoes-z3]] — Álgebra Simbólica no `angr` com **`claripy`**: Bitvectors Simbólicos (**`BVS`** vs **`BVV`**), Árvores AST e Resolução de Restrições com **Z3 (`state.solver`)**
- [[angr-execucao-simbolica-simstate-simulation-manager-explore-find-avoid]] — Execução Simbólica com **`SimState`** e **`SimulationManager` (`simgr.explore`)**: Navegando até Estados Alvo (`find`) e Podando Caminhos Inválidos (`avoid`)
- [[angr-hooks-simprocedures-substituicao-funcoes-anti-debug-crypto]] — Engenharia Reversa com **`@proj.hook`** e **`angr.SimProcedure`**: Neutralizando `ptrace` Anti-Debug, `sleep`, Loops Pesados e Funções Criptográficas
- [[angr-analise-estatica-cfgfast-cfgemulated-decompilador-reaching-definitions]] — Análise Estática e Decompilação no `angr`: **`CFGFast` vs `CFGEmulated`**, Grafo de Dependências (**`DDG` / `ReachingDefinitions`**) e **`Decompiler`**
- [[angr-mitigacao-explosao-estados-veritesting-dfs-length-limiter-symbion]] — Como Mitigar a **Explosão de Estados (*State Explosion*)** no `angr`: Técnicas de Exploração **`Veritesting`**, **`DFS`**, **`LoopSeer`**, **`LengthLimiter`** e **`LAZY_SOLVES`**
- [[angr-execucao-concolica-hibrida-fuzzing-driller-afl-qiling-unicorn]] — Execução Concólica Híbrida e Fuzzing Assistido por Solver (**`Driller`**) & Engine Nativa **Unicorn (`angr.options.UNICORN`)**
- [[angr-auditoria-firmware-iot-firmalice-authentication-bypass-backdoors]] — Auditoria de Firmware IoT com `angr` (**`Firmalice`**): Detecção Automática de **Backdoors e Authentication Bypass** em Binários Embarcados
- [[angr-descoberta-vulnerabilidades-memoria-unconstrained-bof-aeg-rop]] — Caça a Corrupção de Memória e **Exploit Generation (`save_unconstrained=True` & `angrop`)**: Encontrando e Explorando **Stack Buffer Overflows** com `angr`

### Yelp detect-secrets (Yelp/detect-secrets) — Prevenção Corporativa de Vazamento de Segredos Baseada em Baseline Auditável (.secrets.baseline), Plugins e Hooks

- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — **Yelp `detect-secrets` (`Yelp/detect-secrets`)**: Arquitetura de **Separação de Responsabilidades (`Separation of Concerns`)** e Arquivo **`.secrets.baseline`**
- [[detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud]] — Catálogo dos **27+ Plugins Detectores** do `detect-secrets`: `AWSKeyDetector`, `OpenAIDetector`, `GitHubTokenDetector`, `KeywordDetector` e Limiares de Entropia
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Auditoria Interativa e Verificação Ativa com **`detect-secrets audit`**: Rotulação (`is_secret`), Relatório (`--report`) e Comparação (**`--diff`**)
- [[detectsecrets-bloqueio-commits-detect-secrets-hook-pre-commit-cicd]] — Bloqueio em Tempo Real com **`detect-secrets-hook`**: Integração com **Framework `pre-commit`** e Pipelines CI/CD (`git diff --staged` & `git ls-files`)
- [[detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist]] — Arquitetura de **Filtros Heurísticos (`filters_used`)**, Dicionários (**`--word-list`**), Exclusões Regex e **Allowlists Inline (`pragma: allowlist secret`)**
- [[detectsecrets-extensibilidade-api-python-secretscollection-custom-plugins]] — API Python do `detect-secrets` (**`SecretsCollection` & `transient_settings`**): Criando **Plugins e Filtros Customizados (`file://...`)**
- [[detectsecrets-modo-slim-resolucao-conflitos-merge-monorepos-escala]] — Operando `detect-secrets` em **Monorepos de Grande Escala**: Modo **`--slim`**, Execução Paralela Multi-Core e Varredura de Arquivos Não-Rastreados (`--all-files`)
- [[detectsecrets-deteccao-bypasses-auditoria-ci-cd-github-actions-sarif]] — Detecção de Bypass (`git commit --no-verify`) no CI/CD com `detect-secrets`: Como Auditar tanto **Novos Segredos** quanto **Adições Não-Auditadas ao Baseline**
- [[detectsecrets-calibracao-keyworddetector-falsos-positivos-testes-i18n]] — Afundando Falsos Positivos do **`KeywordDetector`** no `detect-secrets`: Como Escrever Código e Testes Sem Disparar Alertas de Variáveis `password` / `secret` / `token`
- [[detectsecrets-estrategia-adocao-corporativa-brownfield-greenfield-git]] — Estratégia de Adoção Corporativa (`Brownfield` vs `Greenfield`): Combinando **Yelp `detect-secrets`**, **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**

### GitHub CodeQL (github/codeql) — Motor de Análise Semântica de Código (Variant Analysis), Bancos de Dados AST/CFG/DFG e Consultas Declarativas QL de Taint Tracking (DataFlow::PathGraph)

- [[codeql-arquitetura-analise-semantica-bancos-dados-ast-cfg-dfg]] — **GitHub CodeQL (`github/codeql`)**: Arquitetura de **Análise Semântica de Código (*Code as Data*)**, Extratores de Linguagem e Bancos Relacionais (`AST`, `CFG`, `DFG`)
- [[codeql-linguagem-ql-predicados-classes-logica-declarativa-datalog]] — Fundamentos da Linguagem **QL (`.ql`)** no CodeQL: Estrutura **`from ... where ... select`**, Predicados Lógicos, Classes de AST e Recursão Transitiva (`+` e `*`)
- [[codeql-analise-fluxo-dados-taint-tracking-sources-sinks-sanitizers]] — Análise Interprocedural de **Fluxo de Dados e *Taint Tracking*** no CodeQL (`DataFlow::ConfigSig` / `TaintTracking::Global`): **`isSource`**, **`isSink`** e **`isBarrier`**
- [[codeql-suites-consultas-default-security-extended-security-and-quality]] — Suítes Oficiais de Consultas do CodeQL (**`.qls`**): Diferenças entre **`default`**, **`security-extended`** e **`security-and-quality`** e Filtros de Query Suite
- [[codeql-variant-analysis-pesquisa-vulnerabilidades-zero-day-escala]] — **Variant Analysis** com CodeQL e **Multi-Repository Variant Analysis (MRVA)**: Encontrando Todas as Variantes de um *Zero-Day / Bug* em Milhares de Repositórios
- [[codeql-model-packs-data-extensions-frameworks-internos-yaml]] — Extensão Semântica sem Escrever Código QL: **CodeQL Model Packs & Data Extensions (`models-as-data` em YAML)** para Mapear Bibliotecas Internas
- [[codeql-modos-build-compiled-languages-none-autobuild-manual]] — Criando Bancos CodeQL para Linguagens Compiladas (**C/C++, Java, Kotlin, C#, Go, Rust, Swift**): Modos **`build-mode: none`**, **`autobuild`** e **`manual`**
- [[codeql-auditoria-workflows-github-actions-injection-pwn-requests]] — Auditoria de Segurança de Pipelines CI/CD (**GitHub Actions**) com CodeQL (`--language=actions`): Detectando **Expression Injection** e **`pull_request_target` (*Pwn Requests*)**
- [[codeql-testes-unitarios-qlpacks-codeql-test-run-expected]] — Engenharia de Qualidade em Regras SAST: Pacotes **`qlpack.yml`** e Testes Unitários Automatizados de Consultas `.ql` com **`codeql test run`** (`.expected`)
- [[codeql-otimizacao-performance-ram-threads-cache-ci-cd]] — Otimização de Performance e Recursos do CodeQL em Grande Escala: Calibração de **`--threads`**, **`--ram`**, Compilation Cache e Exclusão de Caminhos (`paths-ignore`)

### SigmaHQ (SigmaHQ/sigma & SigmaHQ/sigma-specification) — Formato Aberto Universal de Assinaturas de Detecção para SIEM/EDR (sigma-cli, pySigma, Logsources, Modificadores, Correlações e Filtros)

- [[sigma-arquitetura-formato-universal-regras-deteccao-siem-yaml]] — **SigmaHQ (`SigmaHQ/sigma`)**: Arquitetura do Padrão Aberto Universal de **Regras de Detecção para Logs e SIEMs** (*Detection-as-Code* em YAML)
- [[sigma-anatomia-logsource-taxonomy-process-creation-sysmon-cloud]] — Anatomia do Bloco **`logsource`** e **`taxonomy`** na Especificação Sigma v2.1: Abstraindo **Windows Event Logs, Sysmon, Linux `auditd` e CloudTrail**
- [[sigma-logica-detection-modificadores-valores-base64offset-windash-re]] — Modificadores de Valor (**`Value Modifiers`**) no Sigma: **`contains`**, **`all`**, **`base64offset`**, **`utf16le`**, **`windash`**, **`cidr`** e **`fieldref`**
- [[sigma-expressoes-condition-operadores-1-of-all-of-not-agregacoes]] — Construindo a Cláusula **`condition`** no Sigma: Operadores Booleanos (`and`, `or`, `not`), Seletores Wildcard (**`1 of selection_*`**, **`all of them`**) e Valores Especiais (`null`)
- [[sigma-regras-correlacao-v2-event-count-value-count-temporal-ordered]] — **Sigma Correlation Rules (Especificação v2.0 / v2.1)**: Correlação Multi-Evento **`event_count`**, **`value_count`**, **`temporal`** e **`temporal_ordered`** (`timespan` & `group-by`)
- [[sigma-filtros-sigma-filters-reducao-falsos-positivos-sem-fork]] — **Sigma Filters (`filter` em Especificação v2.1)**: Como Suprimir Falsos Positivos do Ambiente Local **Sem Modificar as Regras Oficiais do SigmaHQ**
- [[sigma-conversao-queries-sigma-cli-pysigma-backends-pipelines-siem]] — Compilação de Regras com **`sigma-cli` e `pySigma`**: Backends (**Splunk SPL, Elastic EQL/Lucene, Sentinel KQL, QRadar, Loki**) e Pipelines de Transformação
- [[sigma-placeholders-expansao-listas-variaveis-ambiente-corporativo]] — Uso de **Placeholders (`%variavel%` eModificador `|expand`)** no Sigma para Parametrizar Domínios VIP, Sub-redes de Servidores e Contas de Administração
- [[sigma-mapeamento-mitre-attack-cobertura-lacunas-navigator-tags]] — Governança de Cobertura de Detecção com Sigma: Mapeamento de **Tags MITRE ATT&CK (`attack.tXXXX`)**, CVEs (`cve.YYYY.NNNN`) e **ATT&CK Navigator**
- [[sigma-pipeline-detection-as-code-cicd-validacao-schema-testes]] — Implantando **Detection-as-Code (DaC)** com Sigma em CI/CD: Validação de JSON Schema (`sigma check`), Linting, Conversão Automatizada e Deploy no SIEM

### Yamato Security Hayabusa (Yamato-Security/hayabusa) — Motor de Threat Hunting e Timeline Forense Ultrarrápido em Rust para Windows Event Logs (.evtx) baseado em Regras Sigma

- [[hayabusa-arquitetura-threat-hunting-timeline-forense-evtx-sigma-rust]] — **Yamato Security Hayabusa (`Yamato-Security/hayabusa`)**: Arquitetura em **Rust** para Threat Hunting e Geração Ultrarrápida de **Timelines Forenses Windows (`.evtx`)** com **Sigma v2**
- [[hayabusa-geracao-timelines-csv-json-jsonl-perfis-saida-timesketch]] — Geração de Timelines no Hayabusa (`csv-timeline`, `json-timeline`, `dfir-timeline`): **Perfis de Saída (`list-profiles`)** e Integração Direta com **Timesketch & Elastic**
- [[hayabusa-comandos-analise-metricas-logon-summary-critical-systems]] — Triagem Rápida de Incidentes com Hayabusa: **`logon-summary`**, **`computer-metrics`**, **`eid-metrics`**, **`log-metrics`** e **`config-critical-systems`**
- [[hayabusa-extracao-base64-pivot-keywords-busca-regex-evtx]] — Caça a Payloads Ocultos nos Logs `.evtx` com Hayabusa: **`extract-base64`**, **`pivot-keywords-list`** e **`search` (Keywords / Regex)**
- [[hayabusa-calibracao-regras-level-tuning-expand-list-custom-rules]] — Calibração de Severidade e Regras no Hayabusa: **`level-tuning`**, **`expand-list`**, Perfis de Status (`--status`) e Regras Sigma Customizadas (`--rules`)
- [[hayabusa-coleta-remota-escala-velociraptor-kape-live-analysis]] — Caça a Ameaças em Escala Corporativa: Integrando **Hayabusa** com **Rapid7 Velociraptor** e **KAPE** + Execução **`--live-analysis`**
- [[hayabusa-canais-evtx-essenciais-sysmon-powershell-rdp-defender-wmi]] — Os **10 Canais de Log Windows (`.evtx`) Mais Valiosos** Analisados pelo Hayabusa: Muito Além de `Security.evtx`, `System.evtx` e `Application.evtx`
- [[hayabusa-enriquecimento-geoip-maxmind-mmdb-conexoes-externas-rdp]] — Enriquecimento Automático de **GeoIP (`MaxMind GeoLite2 .mmdb`)** no Hayabusa: Identificando Logons RDP, SMB e Conexões de Rede de Países Incomuns
- [[hayabusa-deteccao-ataques-active-directory-dcsync-kerberoasting-golden-ticket]] — Caçando Ataques contra **Active Directory** nos Logs `.evtx` com Hayabusa: **DCSync (`4662`), Kerberoasting (`4769`), AS-REP Roasting (`4768`), Pass-the-Hash e NTLM Relay**
- [[hayabusa-visualizacao-relatorios-html-metrics-timeline-explorer-workflow]] — Workflow Completo de DFIR com Hayabusa (Marco **1.100/2.000** do Lote `software-seguranca-2000-0003`): Relatório Executivo HTML (`-H`), Timeline Explorer e `jq`

## Tranche 12 (IDs 1101–1200)

### WithSecure Chainsaw (WithSecureLabs/chainsaw) — Triagem Forense Multi-Artefatos Windows (.evtx, $MFT, Registry Hives, Shimcache e SRUM) em Rust e Motor Lógico TAU

- [[chainsaw-arquitetura-forense-windows-evtx-mft-registry-srum-rust]] — Arquitetura do **Chainsaw (`WithSecureLabs/chainsaw`)**: Triagem Forense Multi-Artefatos Windows (`.evtx`, `$MFT`, Registry Hives, Shimcache e SRUM) em Rust
- [[chainsaw-hunting-regras-sigma-tau-engine-mappings-evtx]] — Threat Hunting com **`chainsaw hunt`**: Motor **TAU Engine**, Mapeamentos **`sigma-event-logs-all.yml`** e Regras Nativas do Chainsaw
- [[chainsaw-busca-forense-search-regex-expressoes-tau-filtros-temporais]] — Busca Forense de Alta Precisão com **`chainsaw search`**: Expressões **TAU (`-t`)**, Regex (`-e`), Janelas Temporais e Extração JSON
- [[chainsaw-analise-shimcache-amcache-timeline-execucao-binarios]] — Reconstrução de Linha do Tempo de Execução com **`chainsaw analyse shimcache`**: Correlação entre **`SYSTEM` (`AppCompatCache`)** e **`Amcache.hve`**
- [[chainsaw-analise-srum-srudb-dat-telemetria-rede-processos-exfiltracao]] — Forense de Exfiltração de Dados e Consumo de Rede por Processo com **`chainsaw analyse srum`** (**`SRUDB.dat`** + Hive **`SOFTWARE`**)
- [[chainsaw-dump-artefatos-mft-registry-esedb-json-analise-forense]] — Extração Bruta e Conversão de Artefatos (**`$MFT`**, Hives de Registro e Bancos ESE) para JSON com **`chainsaw dump`**
- [[chainsaw-regras-nativas-av-alerts-defender-sophos-kaspersky-evtx]] — Triagem de Alertas de Antivírus/EDR (**Windows Defender, Sophos, F-Secure e Kaspersky**) e Limpeza de Logs com as Regras Nativas do Chainsaw
- [[chainsaw-autoria-regras-customizadas-tau-filter-document-fields]] — Autoria de **Regras Nativas do Chainsaw** e Mapeamentos Customizados no Formato **TAU Engine** (`filter`, `group`, `fields`)
- [[chainsaw-deteccao-movimentacao-lateral-logins-brute-force-contas]] — Investigação de **Movimentação Lateral, Brute-Force e Escalação de Privilégio** (`lateral_movement` e `security`) com o Chainsaw
- [[chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir]] — Playbook Integrado **Chainsaw + Hayabusa** em DFIR: Como Combinar o Melhor dos Dois Motores Rust na Triagem Forense Windows

### Red Canary Atomic Red Team (redcanaryco/atomic-red-team & invoke-atomicredteam) — Biblioteca Aberta de Testes Determinísticos Mapeados ao MITRE ATT&CK e Execução Automatizada

- [[atomicredteam-arquitetura-biblioteca-testes-mitre-attack-yaml]] — Arquitetura do **Atomic Red Team (`redcanaryco/atomic-red-team`)**: Biblioteca Aberta de Testes Determinísticos Mapeados ao **MITRE ATT&CK**
- [[atomicredteam-anatomia-especificacao-yaml-input-arguments-executors-cleanup]] — Anatomia da Especificação YAML de um Teste Atômico: **`auto_generated_guid`**, **`input_arguments`**, **`dependencies`**, **`executor`** e **`cleanup_command`**
- [[atomicredteam-execucao-invoke-atomicredteam-powershell-showdetails-checkprereqs]] — Motor de Execução **`Invoke-AtomicRedTeam`** (PowerShell Core Multiplataforma): `-ShowDetails`, `-CheckPrereqs`, `-GetPrereqs` e `-Cleanup`
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Emulação de Adversários em **Linux, macOS e Containers** com Atomic Red Team: Persistência (`systemd`/`cron`), Credenciais e Escape de Container
- [[atomicredteam-testes-cloud-aws-azure-ad-gcp-m365-identidade]] — Testes Atômicos de **Nuvem e Identidade** (`iaas:aws`, `iaas:azure`, `iaas:gcp`, `azure-ad`, `office-365`, `google-workspace`)
- [[atomicredteam-logging-estruturado-executionlog-correlacao-siem-edr]] — Logging Estruturado de Execuções (`-ExecutionLogPath`), Módulos de Log Customizados (**Syslog, JSON, CSV, Attire**) e Correlação com o SIEM
- [[atomicredteam-engenharia-deteccao-ciclo-validacao-sigma-hayabusa-chainsaw]] — Ciclo Completo de **Engenharia de Detecção (*Detection Engineering*)**: Executando Atomic Red Team e Validando com **Sigma, Hayabusa e Chainsaw**
- [[atomicredteam-desenvolvimento-novos-atomics-validacao-ci-pre-commit]] — Desenvolvimento e Validação de **Novos Testes Atômicos Corporativos**: Schema Validation, `pre-commit` e Boas Práticas de Autoria
- [[atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator]] — Integração do **Atomic Red Team** com **MITRE Caldera**, **VECTR** e Camadas do **MITRE ATT&CK Navigator**
- [[atomicredteam-limites-testes-atomicos-variacoes-procedimento-evasao]] — Limites dos Testes Atômicos: **Ancoragem em Procedimentos (*Procedure-Level Anchoring*)** e Como Evitar Regras Frágeis de Linha de Comando

### MITRE Caldera (mitre/caldera) — Plataforma Automatizada de Emulação de Adversários, Agentes C2 (Sandcat/Manx), Planejamento Orientado a Fatos e Operações Purple Team

- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Arquitetura do **MITRE Caldera (`mitre/caldera`)**: Plataforma Automatizada de Emulação de Adversários, C2 Assíncrono e Ecossistema de Plugins
- [[caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw]] — Agentes do Caldera (**`Sandcat`**, **`Manx`** e **`Ragdoll`**): Identificadores **`paw`**, Canais de Contato C2 (**HTTP, TCP, DNS, Gist**) e Grupos Red/Blue
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Motor de Decisão Autônoma do Caldera: **Abilities**, **Adversary Profiles**, **Planners (`atomic`, `batch`, `buckets`)**, **Facts** e **Parsers**
- [[caldera-plugins-stockpile-emu-atomic-planos-ctid]] — Bibliotecas de Ameaças do Caldera: Plugins **`stockpile`**, **`atomic`** e **`emu`** (Planos Oficiais do **MITRE CTID** — FIN6, APT29, Sandworm, LockBit)
- [[caldera-furtividade-ofuscadores-jitter-builder-evasao-edr]] — Controles de Furtividade (*Stealth*) em Operações do Caldera: **Obfuscators** (`plain-text`, `base64`, `caesar`, `steganography`), **Jitter** e **Autonomous Mode**
- [[caldera-operacoes-blue-team-response-gameboard-purple-team]] — Caldera para o **Blue Team e Purple Team**: Plugins **`response`**, **`gameboard`** e **`compass`** para Defesa Automatizada e Visualização Conjunta
- [[caldera-relatorios-debrief-api-rest-automacao-cicd]] — Automação via **API REST v2 (`/api/v2/operations`)** e Relatórios Executivos/Técnicos com o Plugin **`debrief`** do Caldera
- [[caldera-movimentacao-lateral-descoberta-fatos-credenciais-smb-ssh]] — Emulação Automática de **Movimentação Lateral** no Caldera: Encadeando Descoberta de Sub-rede, Extração de Credenciais e Pivô SMB/SSH/WinRM
- [[caldera-hardening-seguranca-implantacao-ssl-local-yml-autenticacao]] — Hardening e Segurança Operacional de uma Implantação do **MITRE Caldera**: `conf/local.yml`, Plugin **`ssl`**, **`saml`** e Isolamento de Rede
- [[caldera-desenvolvimento-plugins-customizados-skeleton-abilities-parsers]] — Extensibilidade do Caldera: Criando **Plugins Customizados (`mitre/skeleton`)**, Novos **Parsers de Fatos** e **Planners** Sob Medida

### Certipy (ly4k/Certipy — certipy-ad) — Auditoria, Enumeração e Testes de Segurança em Active Directory Certificate Services (AD CS ESC1–ESC17, Shadow Credentials e Golden Certificates)

- [[certipy-arquitetura-auditoria-active-directory-certificate-services-adcs]] — Arquitetura do **Certipy (`ly4k/Certipy`)**: Auditoria, Enumeração e Testes de Segurança em **Active Directory Certificate Services (AD CS)**
- [[certipy-enumeracao-find-vulnerable-bloodhound-templates-cas-ldap]] — Enumeração e Diagnóstico de AD CS com **`certipy find`**: Flag **`-vulnerable`**, Saída JSON/Stdout e Integração com **BloodHound**
- [[certipy-vulnerabilidades-templates-esc1-esc2-esc3-san-eku-enrollment]] — Anatomia e Mitigação de **`ESC1`, `ESC2` e `ESC3`**: Abuso de **`ENROLLEE_SUPPLIES_SUBJECT` (SAN)**, **Any Purpose EKU** e **Enrollment Agent**
- [[certipy-permissoes-acls-esc4-esc5-esc7-writeproperty-manageca]] — Controle de Acesso no AD CS (**`ESC4`, `ESC5` e `ESC7`**): ACLs Perigosas em Templates (`certipy template`) e na Autoridade Certificadora (`ManageCA` / `ManageCertificates`)
- [[certipy-ataques-configuracao-ca-relay-esc6-esc8-esc11-epa-https]] — Configurações Inseguras da CA e **NTLM Relay para AD CS (`ESC6`, `ESC8` e `ESC11`)**: Flag `EDITF_ATTRIBUTESUBJECTALTNAME2`, Web Enrollment HTTP e RPC
- [[certipy-mapeamento-certificados-esc9-esc10-esc13-esc14-esc15-kb5014754]] — Mapeamento Fraco de Certificados e Novas Classes (**`ESC9`, `ESC10`, `ESC13`, `ESC14`, `ESC15`/`EKUwu`, `ESC16` e `ESC17`**) e o Patch **`KB5014754`**
- [[certipy-shadow-credentials-msds-keycredentiallink-whfb-pkinit]] — Auditoria e Abuso de **Shadow Credentials (`msDS-KeyCredentialLink`)** com **`certipy shadow`**: Como Funciona o **Windows Hello for Business (WHfB)** no AD
- [[certipy-autenticacao-pkinit-schannel-certipy-auth-unpac-the-hash]] — Autenticação via Certificado com **`certipy auth`**: **Kerberos PKINIT (`EventID 4768`)**, **UnPAC-the-Hash (`PAC_CREDENTIAL_INFO`)** e **LDAPS Schannel**
- [[certipy-persistencia-golden-certificates-roubo-chave-privada-ca-dpapi]] — Persistência de Domínio com **Golden Certificates (`certipy ca -backup` / `certipy forge`)** e Como Proteger a Chave Privada da CA com **HSM**
- [[certipy-hardening-monitoramento-adcs-event-ids-4886-4887-sigma]] — Guia Definitivo de **Hardening e Monitoramento de AD CS (Blue Team)**: Ativando Auditoria da CA (**Event IDs `4886`, `4887`, `4888`, `4898`, `4899`**) e Regras Sigma

### AIDE — Advanced Intrusion Detection Environment (aide/aide) — Monitoramento Criptográfico de Integridade de Arquivos (FIM), Atributos Estendidos (ACL/SELinux/xattrs/e2fsattrs) e Detecção de Rootkits em Linux

- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Arquitetura do **AIDE (`aide/aide` — Advanced Intrusion Detection Environment)**: Monitoramento de Integridade de Arquivos (**FIM**) e Detecção de Rootkits em Linux/Unix
- [[aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf]] — Anatomia de Regras e Atributos no **`aide.conf`**: Combinando **`sha256+sha512`**, **`acl`**, **`xattrs`**, **`selinux`** e **`e2fsattrs`**
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Regras de Seleção e Expressões Regulares PCRE2 no **`aide.conf`**: Seleções Regulares (`/caminho`), Restritas (`=/caminho`), Negativas (`!/caminho`) e Macros
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Ciclo Operacional do AIDE: **`--init`**, **`--check`**, **`--update`**, **`--compare`** e Interpretação dos **Códigos de Retorno (`1` a `7`)** em Scripts
- [[aide-monitoramento-logs-crescentes-growing-size-rotacao-logrotate]] — Monitoramento de Integridade de **Arquivos de Log (`S` / `ANF` / `ARF`)** no AIDE: Como Detectar Truncamento de Logs sem Falsos Positivos no `logrotate`
- [[aide-protecao-banco-dados-assinatura-gpg-armazenamento-remoto-ssh]] — Blindagem Anti-Tampering do Próprio AIDE: Verificação Remota via **SSH/SFTP**, Mídia Read-Only e Assinatura Criptográfica **GnuPG**
- [[aide-configuracao-modular-debian-ubuntu-aide-conf-d-update-aide-conf]] — Arquitetura Modular no Debian/Ubuntu (**`/etc/aide/aide.conf.d/`**): **`update-aide.conf`**, **`aideinit`** e Integração com Pacotes `.deb`
- [[aide-integracao-siem-syslog-json-auditoria-pci-dss-cis-benchmark]] — Integração do AIDE com **SIEM e Conformidade (`PCI-DSS 11.5` / `CIS Benchmarks`)**: Parseando Relatórios de Alteração e Alertando sobre Drift
- [[aide-otimizacao-performance-workers-multithread-limites-io-producao]] — Otimização de Performance e Controle de Impacto de I/O do AIDE em Produção: **Multithreading (`num_workers`)**, `ionice` e `nice`
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Caça a Backdoors e Persistência Linux com o AIDE: Detectando Adulteração em **`/etc/ld.so.preload`**, Módulos **PAM (`/lib/security/`)**, `sshd` e `systemd`

### Cowrie (cowrie/cowrie) — Honeypot SSH e Telnet de Média e Alta Interação (Modos Shell, Proxy QEMU Pool e LLM), Captura de Malware e Replay de Sessões TTY (playlog)

- [[cowrie-arquitetura-honeypot-ssh-telnet-shell-proxy-llm]] — Arquitetura do **Cowrie (`cowrie/cowrie`)**: Honeypot SSH e Telnet de Média e Alta Interação (`backend = shell`, `proxy` e `llm`)
- [[cowrie-sistema-arquivos-falso-fs-pickle-fsctl-createfs-honeyfs]] — Customização do Sistema de Arquivos Falso do Cowrie: **`fs.pickle`**, **`createfs`**, **`fsctl`**, **`honeyfs` (`contents_path`)** e **`txtcmds`**
- [[cowrie-politicas-autenticacao-userdb-authrandom-ssh-keys-honeytokens]] — Estratégias de Autenticação no Cowrie: **`UserDB` (`etc/userdb.txt`)** vs. **`AuthRandom`** e Captura de Credenciais de Força Bruta
- [[cowrie-captura-malware-downloads-ttylog-playlog-asciinema]] — Coleta Automática de Malware (**`var/lib/cowrie/downloads/`**) e Replay Visual de Sessões TTY com **`playlog`** e **`asciinema`**
- [[cowrie-modo-proxy-alta-interacao-backend-pool-qemu-libvirt]] — Cowrie em **Modo Proxy de Alta Interação (`backend = proxy`)**: Orquestrando um Pool de VMs **QEMU/Libvirt (`backend_pool`)** Transparentemente
- [[cowrie-telemetria-json-siem-splunk-elastic-misp-threat-intel]] — Telemetria Estruturada do Cowrie (**`var/log/cowrie/cowrie.json`**): Eventos `eventid`, Fingerprints **HASSH** e Integração com SIEM e **MISP**
- [[cowrie-isolamento-seguranca-redirecionamento-portas-nftables-docker]] — Implantação Segura do Cowrie em Produção: Redirecionamento da Porta **`22` -> `2222`** via **`nftables`**, Gerenciamento do SSH Real e Hardening Docker
- [[cowrie-anti-fingerprinting-disfarce-honeypot-banners-uptime-rede]] — Técnicas de **Anti-Fingerprinting** no Cowrie: Como Evitar que Atacantes e Scanners Identifiquem que o Servidor é um Honeypot
- [[cowrie-modo-llm-inteligencia-artificial-emulacao-dinamica-comandos]] — Emulação Dinâmica de Comandos com **IA Generativa (`backend = llm`)** no Cowrie: Como Responder a Qualquer Comando Inédito do Atacante
- [[cowrie-deception-engineering-intranet-deteccao-movimentacao-lateral-ssh]] — Engenharia de Deception na **Rede Interna (Intranet)** com Cowrie: Transformando Tentativas de Movimentação Lateral SSH em Alertas de Alta Fidelidade

### Thinkst OpenCanary (thinkst/opencanary) — Honeypot Multiprotocolo de Baixa Interação para Detecção de Intrusão em Redes Internas, Módulos de Protocolo e Breadcrumbs

- [[opencanary-arquitetura-honeypot-multiprotocolo-rede-interna-thinkst]] — Arquitetura do **OpenCanary (`thinkst/opencanary`)**: Honeypot Multiprotocolo de Baixa Interação para Detecção de Intrusão em Redes Internas
- [[opencanary-modulos-protocolos-http-https-naslogin-smb-samba-audit]] — Emulação de **Servidores de Arquivos (SMB/Samba)** e **Painéis Web de Storage (`http.skin = nasLogin`)** no OpenCanary
- [[opencanary-modulos-bancos-dados-mysql-mssql-redis-git-ssh-rdp]] — Armadilhas para **Bancos de Dados (`MySQL`, `MSSQL`, `Redis`)**, **Repositórios `Git` (`9418`)** e **Acesso Remoto (`RDP`, `VNC`, `SSH`, `Telnet`)** no OpenCanary
- [[opencanary-deteccao-varredura-rede-portscan-snmp-llmnr-ntp-tftp]] — Detecção Precoce de Reconhecimento de Rede com OpenCanary: Módulos **`portscan`**, **`snmp` (`161/UDP`)**, **`llmnr` (`5355/UDP`)**, **`tftp`** e **`ntp`**
- [[opencanary-customizacao-banners-perfis-servicos-perfis-industriais]] — Módulo **`tcpbanner`** do OpenCanary: Emulando Protocolos Proprietários, Serviços Legados e Controladores Industriais (**ICS/OT**)
- [[opencanary-alertas-logger-syslog-webhook-slack-correlator-siem]] — Arquitetura de Alertas e **`PyLogger`** do OpenCanary: **Syslog RFC, Webhooks (Slack/Teams), SMTP, HPFeeds** e **`opencanary-correlator`**
- [[opencanary-implantacao-docker-host-network-ansible-frota-sensores]] — Implantação de Frota de Sensores OpenCanary com **Docker (`--network host`)** e **Ansible**: Preservando o IP Real de Origem (`src_host`)
- [[opencanary-integracao-canarytokens-breadcrumbs-active-directory-dns]] — Estratégia de **Breadcrumbs (Iscas)** para Atrair Atacantes ao OpenCanary: Registros **DNS Internos**, **SPNs no Active Directory** e Arquivos `.env`
- [[opencanary-mapeamento-logtypes-regras-sigma-siem-automacao-soar]] — Tabela de **`logtype`** do OpenCanary e Automação de Resposta (**SOAR / Active Response**) no SIEM
- [[opencanary-arquitetura-combinada-opencanary-cowrie-defesa-profundidade]] — Arquitetura de Deception em Camadas: Combinando **OpenCanary** (Detecção Multiprotocolo Rápida) e **Cowrie** (Análise Comportamental Pós-Login)

### WireGuard — VPN Criptográfica Moderna no Kernel Linux, Protocolo Noise_IKpsk2 (ChaCha20-Poly1305, Curve25519, BLAKE2s), Cryptokey Routing (AllowedIPs) e Resistência Pós-Quântica

- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Arquitetura do **WireGuard**: VPN Criptográfica no Kernel Linux, Handshake **`Noise_IKpsk2`** e Primitivas Fixas (**ChaCha20-Poly1305, Curve25519, BLAKE2s**)
- [[wireguard-cryptokey-routing-allowedips-tabela-roteamento-peers]] — O Conceito Central do WireGuard — **Cryptokey Routing (`AllowedIPs`)**: Unificando Tabela de Roteamento IP e Lista de Controle de Acesso Criptográfica
- [[wireguard-handshake-1rtt-pfs-rekeying-timers-presharedkey-pos-quantico]] — Handshake **1-RTT (`Noise_IKpsk2`)**, **Perfect Forward Secrecy (PFS)**, Rotação Automática de Chaves a Cada 2 Minutos e **`PresharedKey` Pós-Quântica**
- [[wireguard-furtividade-silencio-udp-cookie-reply-mitigacao-dos]] — Furtividade de Rede (*Stealth*) e Mitigação de **DoS (`mac1`, `mac2` e `Cookie Reply`)** no WireGuard: Por Que o WireGuard é Invisível ao Nmap
- [[wireguard-operacao-cli-wg-wg-quick-iproute2-fwmark-roteamento]] — Operação e Automação com **`wg(8)`**, **`wg-quick(8)`**, **`iproute2`** e Roteamento Baseado em Políticas (**`FwMark`** para Full-Tunnel sem Loop)
- [[wireguard-integracao-firewall-nftables-postup-postdown-killswitch]] — Segurança de Tráfego no WireGuard com **`nftables`**: Hooks **`PreUp`/`PostUp`/`PreDown`/`PostDown`**, Isolamento entre Peers e **Kill-Switch**
- [[wireguard-isolamento-network-namespaces-linux-containerizacao-roteamento]] — Arquitetura Avançada no Linux — **Isolamento por Network Namespaces (`ip netns`)** com WireGuard: Roteamento Físico Separado do Túnel
- [[wireguard-otimizacao-mtu-mss-clamping-fragmentacao-performance-kernel]] — Diagnóstico de Rede e Otimização de **MTU (`1420` Bytes) e TCP MSS Clamping** em Túneis WireGuard IPv4/IPv6
- [[wireguard-monitoramento-auditoria-healthcheck-rotacao-chaves-gerencia]] — Monitoramento Operacional, **Dynamic Debugging** no Kernel e Gestão de Ciclo de Vida de Chaves WireGuard em Ambientes Corporativos
- [[wireguard-governanca-zero-trust-automacao-malha-headscale-tailscale]] — WireGuard em Escala Corporativa (**Zero Trust Mesh VPN**): Plano de Dados do Kernel + Planos de Controle Automatizados (**SSO/OIDC, Rotação Efêmera e NAT Traversal**)

### Linux nftables (Netfilter Project) — Subsistema Moderno de Classificação de Pacotes e Firewall Stateful no Kernel Linux, Família Dual-Stack inet, Sets/Verdict Maps em O(1) e Flowtables

- [[nftables-arquitetura-firewall-kernel-linux-netfilter-tabelas-inet]] — Arquitetura do **`nftables` (`Netfilter Project`)**: Máquina Virtual de Bytecode no Kernel Linux, Família Dual-Stack **`inet`** e Substituição do `iptables`
- [[nftables-chains-hooks-prioridades-conntrack-stateful-firewall]] — Anatomia de **Chains, Hooks (`prerouting`, `input`, `forward`, `output`, `postrouting`, `ingress`), Prioridades** e **Connection Tracking (`ct state`)** no `nftables`
- [[nftables-conjuntos-sets-anonimos-nomeados-intervalos-timeouts-dinamicos]] — Conjuntos de Alta Performance (**Sets Anônimos e Nomeados**) no `nftables`: Intervalos CIDR (`flags interval`), `auto-merge`, `timeout` e Blocklists em $O(1)$
- [[nftables-mapas-vereditos-vmap-concatenacoes-arquitetura-escalavel]] — Mapas de Veredito (**`vmap`**) e **Concatenações de Seletores (`.` Tuplas)** no `nftables`: Substituindo Centenas de Regras Lineares por Uma Única Busca em Hash
- [[nftables-rate-limiting-meters-dynamic-sets-anti-bruteforce-ssh]] — Proteção Anti-Brute-Force e **Rate Limiting Dinâmico por IP (`flags dynamic, timeout` / `ct count`)** Nativamente no `nftables`
- [[nftables-nat-masquerade-dnat-snat-redirecionamento-portas]] — Configuração de **NAT (`snat`, `masquerade`, `dnat` e `redirect`)** no `nftables` para Gateways VPN, Containers e Honeypots
- [[nftables-protecao-ddos-familia-netdev-ingress-synproxy-raw-notrack]] — Mitigação de **DDoS em Linha de Velocidade** com `nftables`: Família **`netdev` (`hook ingress`)**, Bypass de Conntrack (**`notrack`**) e **`synproxy`**
- [[nftables-aceleracao-hardware-software-flowtables-fastpath-roteadores]] — Aceleração de Fluxos de Rede com **`flowtables` (Fastpath Software e Hardware Offload)** no `nftables` para Gateways de Alta Vazão (10GbE / 40GbE)
- [[nftables-logging-estruturado-ulogd2-nflog-rastreamento-nftrace-debug]] — Depuração em Tempo Real (**`meta nftrace set 1` / `nft monitor trace`**) e Logging Estruturado JSON (**`nflog` + `ulogd2`**) no `nftables`
- [[nftables-transacoes-atomicas-rollback-seguro-automacao-ansible-json]] — Operação Segura sem Lockout: **Transações Atômicas (`nft -f`)**, Saída JSON (`nft -j`), Migração `iptables-translate` e Rollback Automático

### OpenSSH (openssh/openssh-portable 10.x) — Arquitetura de Separação de Privilégios (sshd-session / seccomp), Troca de Chaves Híbrida Pós-Quântica (mlkem768x25519-sha256), Chaves FIDO2 (ed25519-sk) e Certificados SSH CA

- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Arquitetura de Segurança do **OpenSSH (`openssh-portable`)**: Separação de Processos (`sshd`, `sshd-session`, `sshd-auth`) e Sandbox `seccomp` no Kernel
- [[openssh-criptografia-pos-quantica-kex-mlkem768-sntrup761-chacha20]] — Criptografia **Pós-Quântica Híbrida** no OpenSSH: Key Exchange **`mlkem768x25519-sha256`** e **`sntrup761x25519-sha512`**, Cifras AEAD e MACs `etm`
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Hardening Completo do **`/etc/ssh/sshd_config`**: Desabilitando Senhas, `PermitRootLogin no`, `AuthenticationMethods`, `MaxAuthTries` e `LoginGraceTime`
- [[openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch]] — Autenticação Resistente a Phishing e Infostealers com **Chaves de Hardware FIDO2/U2F (`ed25519-sk` e `ecdsa-sk`)** no OpenSSH
- [[openssh-certificados-ssh-ca-user-host-certificates-principals-ttl]] — Eliminando `authorized_keys` Estáticos e Alertas TOFU (`known_hosts`) com **Autoridade Certificadora SSH (`ssh-keygen -s` User & Host Certificates)**
- [[openssh-seguranca-ssh-agent-destination-constraints-session-bind]] — Segurança do **`ssh-agent`**: O Perigo do **`ForwardAgent yes`**, Restrições de Destino (**`ssh-add -h` + `session-bind@openssh.com`**) e Isolamento
- [[openssh-tunelamento-seguro-proxyjump-bastion-restricao-forwarding]] — Arquitetura de **Bastion Host (Jump Host)** com **`ProxyJump` (`-J`)** e Blindagem do Bastion com `AllowTcpForwarding local`, `PermitOpen` e `ForceCommand`
- [[openssh-restricoes-authorized-keys-restrict-command-sftp-chroot]] — Confinamento Granular em **`authorized_keys` (`restrict`, `command=`, `from=`)** e **SFTP Chroot Jail (`internal-sftp` + `ChrootDirectory`)**
- [[openssh-auditoria-forense-loglevel-verbose-fingerprints-pam-tty]] — Auditoria e Forense de Acessos SSH: **`LogLevel VERBOSE`**, Rastreamento de **Fingerprints `SHA256` de Chaves e Certificados** e Timers de Inatividade (`ChannelTimeout`)
- [[openssh-auditoria-automatizada-ssh-audit-testes-conformidade-cicd]] — Auditoria Automatizada de Servidores e Clientes OpenSSH: Inspecionando Banners, Algoritmos KEX/Ciphers/MACs e Prevenindo Regressões

## Tranche 13 (IDs 1201–1300)

### KeePassXC (keepassxreboot/keepassxc) — Gerenciamento de Cofres de Credenciais Offline KDBX 4 (Argon2id/ChaCha20), YubiKey HMAC-SHA1, ssh-agent, keepassxc-cli e Passkeys

- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Arquitetura Criptográfica do **KeePassXC (`keepassxreboot/keepassxc`)**: Formato **KDBX 4**, Derivação **Argon2id** e Cifras **ChaCha20 / AES-256 / Twofish**
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Chave Composta do KeePassXC: Combinando **Senha Mestra + Key File + Hardware Challenge-Response (`YubiKey` / `OnlyKey` HMAC-SHA1)**
- [[keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock]] — Integração Nativa com **`ssh-agent`** no KeePassXC: Carregamento Automático de Chaves SSH ao Destravar o Cofre e Remoção Automática no Lock
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Automação de Segredos no Terminal com **`keepassxc-cli`**: Injetando Credenciais e TOTPs em Variáveis de Ambiente sem Expor no `.bash_history`
- [[keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing]] — Integração Segura com Navegadores (**`keepassxc-proxy`**) e Suporte a **Passkeys (WebAuthn / FIDO2)** no KeePassXC: Prevenção contra Phishing de Domínio
- [[keepassxc-autotype-sequencias-customizadas-protecao-window-title]] — Segurança do **Auto-Type (`Ctrl+Shift+V`)** no KeePassXC: Sequências Customizadas (`{USERNAME}{TAB}{PASSWORD}{TOTP}`), Delay e Validação de Título de Janela
- [[keepassxc-freedesktop-secret-service-substituicao-gnome-keyring-linux]] — KeePassXC como Provedor **`org.freedesktop.secrets` (Secret Service D-Bus)** no Linux: Substituindo o `gnome-keyring` / `KWallet` com Criptografia Forte
- [[keepassxc-compartilhamento-equipes-keeshare-assinatura-merge-git]] — Compartilhamento Seguro de Cofres em Equipe com **KeeShare** (Contêineres Assinados) e Resolução de Conflitos com **`keepassxc-cli merge`**
- [[keepassxc-auditoria-saude-senhas-hibp-k-anonymity-relatorios]] — Auditoria de Saúde Criptográfica do Cofre (**Database Reports**): Verificação Privada **HaveIBeenPwned (`k-Anonymity`)**, Reuso e Entropia
- [[keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866]] — Segurança de Memória em Gerenciadores de Senhas Desktop: Lições do **`keepass-password-dumper` (`CVE-2023-35866`)**, `prctl(PR_SET_DUMPABLE)` e Isolamento

### Plaso / log2timeline (log2timeline/plaso) — Motor Forense de Super Timelines e Targeted Timelines Multi-Artefatos (log2timeline.py, psort.py, pinfo.py, psteal.py) e Integração Timesketch

- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Arquitetura do **Plaso (`log2timeline/plaso`)**: Motor de **Super Timeline Forense** Multi-Artefatos para Windows, Linux, macOS e Android
- [[plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker]] — Extração Forense com **`log2timeline.py`**: Processando Imagens **E01/RAW**, Partições Múltiplas (`--partitions`), **Volume Shadow Copies (`--vss_stores`)** e **BitLocker**
- [[plaso-presets-parsers-customizados-win7-linux-macos-targeted-timelines]] — Timelines Direcionadas (**Targeted Timelines**) no Plaso: Controlando **`--parsers`** (`win7`, `linux`, `macosx`, `webhist`) e **`-f` Filter Files**
- [[plaso-inspecao-diagnostico-pinfo-compare-auditoria-extracao]] — Auditoria e Diagnóstico de Arquivos `.plaso` com **`pinfo.py`**: Metadados de Pré-Processamento, Contagem por Parser e **`--compare`**
- [[plaso-filtragem-exportacao-psort-time-slice-dynamic-output-l2tcsv]] — Pós-Processamento, Recorte Temporal (**`--slice`**) e Linguagem de Filtro no **`psort.py`**: Exportando `l2tcsv`, `dynamic` e `json_line`
- [[plaso-tagging-eventos-analysis-plugins-viper-virustotal-nsrl]] — Rotulagem Automática (**Event Tagging**) e **Analysis Plugins** no Plaso: Destacando Execução, Persistência, Logins e Indicadores Maliciosos
- [[plaso-integracao-timesketch-opensearch-psteal-investigacao-colaborativa]] — Pipeline Direto **`psteal.py`** e Integração Nativa **Plaso + Google Timesketch (`opensearch_ts`)**: Investigação Forense Colaborativa em Escala
- [[plaso-forense-linux-macos-containers-syslog-auditd-plist-unified-logs]] — Forense de Servidores **Linux, macOS e Containers** com o Plaso: Parsers `syslog`, `systemd_journal`, `utmp`/`wtmp`, `bash_history`, `fsext` e `plist`
- [[plaso-forense-navegadores-webhist-chrome-firefox-edge-downloads-cookies]] — Reconstrução de **Atividade de Navegadores e Downloads de Malware (`webhist`)** no Plaso: Chrome/Edge (Chromium), Firefox, Safari e Extensões
- [[plaso-otimizacao-performance-workers-memoria-hashes-sha256-escala]] — Otimização de Performance e Extração de **Hashes `SHA-256` (`--hashers`)** no `log2timeline.py`: Gerenciando Workers, Memória e Arquivos Grandes

### Mandiant capa (mandiant/capa) — Detecção Automatizada de Capacidades em Binários (PE, ELF, .NET, Shellcode) e Relatórios de Sandbox Mapeadas ao MITRE ATT&CK e MBC

- [[capa-arquitetura-deteccao-capacidades-binarios-mitre-attack-mbc-mandiant]] — Arquitetura do **Mandiant `capa` (`mandiant/capa`)**: Detecção Automatizada de Capacidades em Binários (**PE, ELF, .NET, Shellcode**) Mapeadas ao **MITRE ATT&CK** e **MBC**
- [[capa-modos-saida-verbose-vv-enderecos-funcoes-json-automacao]] — Triagem Rápida vs. Engenharia Reversa Profunda no `capa`: Modos Padrão, Verboso (**`-v`**), Muito Verboso (**`-vv`**) e Exportação **`-j` JSON**
- [[capa-anatomia-regras-yaml-escopos-file-function-basic-block-instruction]] — Anatomia das Regras YAML do **`capa-rules`**: Escopos Estáticos (**`file`, `function`, `basic block`, `instruction`**) e Operadores Lógicos (`and`, `or`, `count`, `optional`)
- [[capa-filtros-restricao-escopo-tags-functions-processes-otimizacao]] — Acelerando o `capa` em Binários Complexos: Filtros por Tag/Namespace (**`-t`**), Restrição por Endereço de Função (**`--restrict-to-functions`**) e Cache **`.viv`**
- [[capa-analise-multi-formato-pe-elf-dotnet-shellcode-assinaturas-flirt]] — Análise Multi-Formato no `capa`: Executáveis **Windows PE**, **Linux ELF**, Assemblies **.NET (CIL)**, **Shellcode Bruto (`-f sc32`/`sc64`)** e Assinaturas **FLIRT (`-s`)**
- [[capa-analise-dinamica-relatorios-sandbox-cape-drakvuf-vmray-processos]] — Análise Dinâmica com o `capa`: Extraindo Capacidades de Relatórios de **Sandboxes (`CAPE`, `DRAKVUF`, `VMRay`)** e Filtrando por **PID (`--restrict-to-processes`)**
- [[capa-integracao-ida-pro-ghidra-binary-ninja-capa-explorer-web]] — Integração do `capa` com **Ghidra, IDA Pro, Binary Ninja** e **`capa Explorer Web`**: Navegação Interativa e Renomeação de Funções na Engenharia Reversa
- [[capa-mapeamento-mitre-attack-malware-behavior-catalog-mbc-diferencas]] — Por que o `capa` Mapeia Simultaneamente para o **MITRE ATT&CK** e para o **Malware Behavior Catalog (`MBC`)**? Entendendo a Diferença Técnica
- [[capa-uso-biblioteca-python-automacao-pipelines-triagem-malware-soc]] — Usando o `capa` como **Biblioteca Python (`capa.main`, `capa.rules`, `capa.engine`)**: Construindo Pipelines Automatizados de Triagem de Malware e Validação de Builds
- [[capa-workflow-combinado-floss-yara-velociraptor-engenharia-reversa]] — Workflow Integrado de Análise de Malware e DFIR: Combinando **Mandiant `FLOSS` + `capa` + `YARA` + `Velociraptor` / `Plaso`**

### Mandiant FLOSS (mandiant/flare-floss) — Extração e Desofuscação de Strings em Malware (Static, Stack Strings, Tight Strings, Decoded Strings via Emulação e Go/Rust)

- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Arquitetura do **Mandiant FLOSS (`mandiant/flare-floss`)**: Superando o `strings` Tradicional com Extração de **Stack Strings, Tight Strings, Decoded Strings e Go/Rust**
- [[floss-desofuscacao-stack-strings-tight-strings-construcao-pilha-x86]] — Como o FLOSS Reconstrói **Stack Strings** e **Tight Strings**: Desfazendo a Ofuscação de Strings Montadas Caractere por Caractere na Pilha da CPU
- [[floss-emulacao-funcoes-decoded-strings-vivisect-xor-rc4-custom]] — Extração de **Decoded Strings** no FLOSS: Identificando Heurísticas de Funções de Decodificação e Emulando a CPU com **`vivisect`**
- [[floss-extracao-strings-go-rust-utf8-estruturas-slice-sem-null-byte]] — Análise de Binários Modernos em **Go (`Golang`)** e **Rust** com o FLOSS: Extraindo Strings de Estruturas `StringHeader` / Slices sem Terminador `\x00`
- [[floss-layout-aware-static-strings-section-structure-semantic-tags]] — Strings Estáticas Conscientes de Layout (**Layout-Aware Static Strings**) e **Tags Semânticas (`--tag`, `--interesting`)** no FLOSS
- [[floss-busca-filtragem-query-regex-json-html-web-viewer]] — Busca com Expressões Regulares (**`--query`**), Exportação **`-j` JSON** e Relatório Visual Interativo (**`--html`**) no FLOSS
- [[floss-integracao-ida-pro-ghidra-binary-ninja-relatorio-html]] — Anotando Automaticamente Desmontadores (**IDA Pro, Ghidra, Binary Ninja e x64dbg**) com os Scripts Gerados pelo FLOSS
- [[floss-analise-shellcode-arquivos-grandes-limites-tuning-performance]] — Analisando **Shellcodes (`-f sc32`/`sc64`)** e Binários Gigantes (**`-L` / `--large-file`**, `--max-strings`, `--max-address-space`) no FLOSS
- [[floss-criacao-regras-yara-ioc-hunting-a-partir-strings-desofuscadas]] — Armadilha Clássica em **Regras YARA**: Por que Usar *Decoded Strings* do FLOSS em Regras YARA de Disco Falha (e Como Usar para Caça em Memória!)
- [[floss-automacao-python-batch-triage-comparacao-builds-supply-chain]] — Automação em Lote com o **FLOSS** (`FLOSS_CACHE_DIR`, API JSON) para Triagem de Malware em Escala e Auditoria de Binários de Terceiros

### Gophish (gophish/gophish) — Framework Open-Source de Simulação de Phishing, Treinamento de Conscientização (Security Awareness), Operações Red Team e Automação via API/Webhooks

- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Arquitetura do **Gophish (`gophish/gophish`)**: Plataforma Open-Source de Simulação de Phishing, Red Team e Treinamento de Conscientização em Segurança
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Configuração de **Sending Profiles (Perfis SMTP)** e Cabeçalhos Customizados (`X-Phish-Test`) no Gophish: Entregabilidade, SPF/DKIM/DMARC e Autorização
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Engenharia de **Email Templates** no Gophish: Variáveis de Template (`{{.FirstName}}`, `{{.URL}}`, `{{.Tracker}}`), Importação de E-mail Original (`RFC 5322`) e Anexos
- [[gophish-landing-pages-captura-credenciais-redirecionamento-educativo]] — Criação de **Landing Pages** Éticas no Gophish: Clonagem de Site, **`Capture Submitted Data`**, Privacidade de Senhas e Redirecionamento Educativo (*Teachable Moment*)
- [[gophish-grupos-usuarios-importacao-csv-segmentacao-departamentos]] — Gerenciamento de **Users & Groups** no Gophish: Importação em Lote via CSV e Segmentação de Campanhas por Perfil de Risco (`Position`)
- [[gophish-execucao-campanhas-agendamento-send-by-date-throttling]] — Orquestração de **Campaigns** no Gophish: Cadência de Disparo (**`Send Emails By`**), Prevenção de *Rate-Limiting* SMTP e Escalonamento Temporal
- [[gophish-relatorios-eventos-email-reportado-rid-metricas-soc]] — Métricas de Sucesso e **Email Reporting (`/report?rid=...`)** no Gophish: Medindo Não Apenas Cliques, Mas a **Taxa de Reporte ao SOC (`Email Reported`)**
- [[gophish-webhooks-integracao-soar-slack-automacao-api-rest]] — Automação em Tempo Real com **Webhooks Autenticados (`HMAC-SHA256`)** e **API REST** no Gophish: Integrando Simulações ao SOAR e Treinamento
- [[gophish-imap-monitoramento-caixa-entrada-respostas-automaticas]] — Monitoramento **IMAP** de Caixa de Entrada no Gophish: Detectando Respostas Diretas dos Usuários e Auto-Replies (*Out-of-Office*)
- [[gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado]] — OPSEC e Hardening de Infraestrutura **Gophish** para Red Teams: Customizando o Parâmetro `rid`, Cabeçalhos `X-Gophish` e Proteção com Proxy Reverso

### OWASP ModSecurity v3 (libmodsecurity) — Motor de Web Application Firewall (WAF) em C++17, Linguagem SecRule, Detecção Léxica libinjection (@detectSQLi/@detectXSS) e OWASP CRS

- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Arquitetura do **OWASP ModSecurity v3 (`libmodsecurity`)**: Motor WAF Standalone em C++17 e Conectores para **Nginx, Apache e Envoy**
- [[modsecurity-modos-operacao-secruleengine-detectiononly-on-tuning]] — Implantação Segura do ModSecurity em Produção: **`SecRuleEngine DetectionOnly` vs. `On`** e Inspeção dos Corpos de Requisição e Resposta
- [[modsecurity-anatomia-secrule-variaveis-operadores-transformacoes-acoes]] — Anatomia da Linguagem **`SecRule`** e as **5 Fases de Processamento HTTP** no ModSecurity: `VARIABLES`, `@OPERATOR`, `t:transform` e `ACTIONS`
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Inspeção Nativa de **APIs JSON e XML (`ctl:requestBodyProcessor`)** e Proteção contra **ReDoS / JSON Bomb** no ModSecurity v3
- [[modsecurity-deteccao-sqli-xss-libinjection-detectsqli-detectxss]] — Detecção Léxica de **SQL Injection (`@detectSQLi`)** e **XSS (`@detectXSS`)** com **`libinjection`** no ModSecurity v3: Além das Expressões Regulares
- [[modsecurity-integracao-owasp-crs-anomaly-scoring-paranoia-level]] — Integração do ModSecurity com o **OWASP Core Rule Set (`CRS`)**: Modelo de **Pontuação de Anomalia (*Anomaly Scoring*)** e **Paranoia Levels (`PL1`–`PL4`)**
- [[modsecurity-tuning-falsos-positivos-exclusoes-ctl-ruleremovetargetbyid]] — Engenharia de Tuning e Eliminação Cirúrgica de Falsos Positivos no ModSecurity: **`ctl:ruleRemoveTargetById`** vs. `SecRuleRemoveById`
- [[modsecurity-auditoria-logs-json-secauditlogparts-ingestao-siem-wazuh]] — Logs de Auditoria Estruturados em **JSON (`SecAuditLogFormat JSON`)** e Anatomia de **`SecAuditLogParts` (`ABIJDEFHZ`)** para Ingestão em SIEM / Wazuh
- [[modsecurity-virtual-patching-cve-zero-day-mitigacao-imediata-borda]] — Aplicando **Virtual Patching** no ModSecurity v3: Mitigando **Zero-Days e CVEs Críticas** na Borda em Minutos Enquanto o Código da Aplicação é Corrigido
- [[modsecurity-inspecao-uploads-arquivos-files-tmpnames-antivirus-yara]] — Proteção contra **Upload de Webshells e Malware** no ModSecurity: Inspecionando `FILES`, `FILES_TMPNAMES` e Integrando **`@inspectFile`** com **YARA / ClamAV**

### strongSwan (strongswan/strongswan) — VPN IPsec/IKEv2 no Linux, Daemon charon, Interface vici/swanctl.conf, Interfaces Virtuais XFRM (Route-Based), TPM 2.0/PKCS#11 e IKEv2 Pós-Quântico (RFC 9370 ML-KEM)

- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Arquitetura Moderna do **strongSwan (`strongswan/strongswan`)**: Daemon **`charon`**, Protocolo **`vici`** e Configuração Declarativa **`swanctl.conf`**
- [[strongswan-estrutura-swanctl-conf-connections-children-secrets-pools]] — Anatomia do **`/etc/swanctl/swanctl.conf`**: As 4 Seções Principais (**`connections`, `children`, `secrets`, `pools`**) e Diretórios `/etc/swanctl/x509*`
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — VPN **Site-to-Site IKEv2** com strongSwan: Geração de PKI com **`pki`**, Autenticação Mútua X.509 (`auth = pubkey`) e Sob Demanda (**`start_action = trap`**)
- [[strongswan-roadwarrior-virtual-ip-pools-eap-tls-eap-mschapv2]] — VPN de Acesso Remoto (**Roadwarrior**) com strongSwan: **Virtual IP `pools`**, `local_ts = 0.0.0.0/0` e Clientes Nativos (**Windows, macOS, iOS, Android**)
- [[strongswan-suites-criptograficas-proposals-aes-gcm-chacha20-pfs-dh]] — Engenharia Criptográfica no strongSwan: Configurando **`proposals`** e **`esp_proposals`** com AEAD (**`aes256gcm16`**, **`chacha20poly1305`**) e **PFS (`ecp384`, `curve25519`)**
- [[strongswan-criptografia-pos-quantica-pqc-ikev2-rfc9370-ml-kem-hibrido]] — VPNs **Pós-Quânticas Híbridas (PQC)** no strongSwan: Implementando **RFC 9370 (*Multiple Key Exchanges in IKEv2*)** com **ML-KEM (`ke1_mlkem768` / `mlkem1024`)**
- [[strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf]] — VPN Baseada em Rota (**Route-Based VPN**) no strongSwan: Interfaces Virtuais do Kernel Linux (**XFRM Interfaces `xfrmi`** com **`if_id_in` / `if_id_out`**) e BGP/OSPF
- [[strongswan-validacao-revogacao-certificados-crl-ocsp-authorities]] — Autoridades Certificadoras (**`authorities`**), Validação **OCSP / CRL** e Políticas Estritas de Revogação (`revocation = strict`) no strongSwan
- [[strongswan-integracao-hardware-tpm2-pkcs11-hsm-protecao-chaves]] — Proteção de Chaves Privadas de VPN em Hardware com o strongSwan: Integração Nativa com **TPM 2.0 (`handle`)**, **Smartcards / YubiKey (`PKCS#11`)** e HSMs
- [[strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump]] — Diagnóstico e Troubleshooting Avançado de Túneis IPsec no Linux: **`swanctl --list-sas`**, **`swanctl --log`**, **`ip -s xfrm state/policy`** e NAT-Traversal (`UDP 4500`)

### Firejail (netblue30/firejail) — Sandboxing de Aplicações Linux com Kernel Namespaces, Filtros seccomp-bpf, Linux Capabilities, AppArmor, Isolamento X11/D-Bus e Perfis .profile

- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Arquitetura do **Firejail (`netblue30/firejail`)**: Isolamento de Aplicações Linux com **Kernel Namespaces, `seccomp-bpf`, Linux Capabilities e AppArmor**
- [[firejail-anatomia-perfis-profile-blacklist-whitelist-read-only-include]] — Anatomia dos Perfis **`.profile`** e Customizações **`.local`** no Firejail: `blacklist`, `whitelist`, `read-only`, `noexec` e Herança `include`
- [[firejail-isolamento-filesystem-private-private-dev-private-etc-bin]] — Isolamento Efêmero de Sistema de Arquivos no Firejail: **`--private`**, **`--private-dev`**, **`--private-etc`**, **`--private-bin`** e **`--private-tmp`**
- [[firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs]] — Redução de Superfície de Ataque do Kernel no Firejail: **`--seccomp`**, **`--caps.drop=all`**, **`--nonewprivs`** e **`--noroot` (User Namespace)**
- [[firejail-isolamento-rede-net-none-veth-netfilter-dns-sandboxing]] — Isolamento de Rede no Firejail: **`--net=none`**, Interfaces Virtuais **`veth` (`--net=eth0` / `br0`)**, Firewall Interno **`--netfilter`** e **`--protocol`**
- [[firejail-isolamento-grafico-x11-xephyr-xvfb-xpra-wayland-dbus]] — Protegendo o Servidor Gráfico e o Barramento IPC no Firejail: Isolamento de **X11 (`--x11=xephyr`/`xpra`)**, **Wayland** e Filtragem de **D-Bus (`--dbus-user`)**
- [[firejail-integracao-apparmor-cgroups-rlimits-controle-recursos]] — Defesa em Profundidade no Firejail: Integração com **AppArmor (`--apparmor`)**, Limites de Recursos (**`rlimits`**) e **Control Groups (`--cgroup`)**
- [[firejail-construcao-perfis-customizados-build-auditoria-sandbox]] — Geração Automática de Perfis de Segurança sob Medida com **`firejail --build`** e Auditoria de Sandboxes em Execução (**`--join`**, **`--ls`**, **`--get`**)
- [[firejail-hardening-global-firejail-config-suid-firejail-users-grupos]] — Hardening Global do Próprio Firejail (**`/etc/firejail/firejail.config`** e **`firejail.users`**): Mitigando Riscos de Binários SUID no Linux
- [[firejail-sandboxing-navegadores-leitores-pdf-analise-artefatos-dfir]] — Sandboxing Prático de **Navegadores Web, Clientes de E-mail e Triagem de Artefatos Suspeitos (DFIR)** no Desktop Linux com Firejail

### Linux-PAM (linux-pam/linux-pam) — Arquitetura de Módulos de Autenticação Plugáveis (auth, account, password, session), Bloqueio pam_faillock, Qualidade pam_pwquality, MFA FIDO2/TOTP e Auditoria auid

- [[pam-arquitetura-pluggable-authentication-modules-grupos-auth-account]] — Arquitetura do **Linux-PAM (`linux-pam/linux-pam`)**: Os 4 Grupos de Gerenciamento (**`auth`, `account`, `password`, `session`**) e Arquivos `/etc/pam.d/`
- [[pam-flags-controle-required-requisite-sufficient-optional-substack]] — Semântica das **Control Flags** do Linux-PAM (**`required`, `requisite`, `sufficient`, `optional`**) e Sintaxe Avançada `[success=done default=ignore]`
- [[pam-protecao-forca-bruta-pam-faillock-faillock-conf-bloqueio-contas]] — Bloqueio contra Força Bruta no Linux com **`pam_faillock.so`** e **`/etc/security/faillock.conf`**: `deny`, `fail_interval`, `unlock_time` e `even_deny_root`
- [[pam-qualidade-senhas-pam-pwquality-entropia-dicionario-historico]] — Políticas de Complexidade de Senhas (`pam_pwquality.so` / `/etc/security/pwquality.conf`) e Histórico Anti-Reuso (`pam_pwhistory.so`) no Linux-PAM
- [[pam-controle-acesso-pam-access-access-conf-pam-time-pam-wheel]] — Controle de Acesso Granular por Origem e Horário no PAM: **`pam_access.so` (`/etc/security/access.conf`)**, **`pam_time.so`** e Restrição de `su` com **`pam_wheel.so`**
- [[pam-limites-recursos-sessao-pam-limits-limits-conf-fork-bomb-core]] — Blindagem de Sessão com **`pam_limits.so` (`/etc/security/limits.conf`)** e **`pam_umask.so`**: Prevenindo **Fork Bombs (`nproc`)**, Core Dumps (`core 0`) e Permissões Frouxas
- [[pam-auditoria-rastreabilidade-pam-loginuid-auditd-pam-tty-audit]] — Rastreabilidade Imutável de Identidade no Linux: Como o **`pam_loginuid.so`** Preserva o **`auid` (*Audit UID*)** Original Mesmo Após `sudo su -`!
- [[pam-autenticacao-multifator-mfa-pam-u2f-fido2-google-authenticator-sshd]] — Autenticação Multifator (**MFA**) no Linux-PAM para **`sshd`** e **`sudo`**: Integrando Chaves de Hardware **FIDO2 (`pam_u2f.so`)** e **TOTP (`pam_google_authenticator.so`)**
- [[pam-isolamento-namespaces-pam-namespace-polimorfico-tmp-var-tmp]] — Diretórios Polimórficos por Usuário com **`pam_namespace.so` (`/etc/security/namespace.conf`)**: Isolando `/tmp` e `/var/tmp` em Servidores Multiusuário
- [[pam-auditoria-integridade-pam-d-prevencao-backdoors-pam-permit]] — Caça a **Backdoors PAM** em Resposta a Incidentes (DFIR): Detectando `pam_permit.so`, `pam_exec.so` Malicioso e Modificações de Binários em `/lib/security/`

### OpenSSL 3.x (openssl/openssl) — Arquitetura de Providers (default, fips, legacy, base), Conformidade FIPS 140-3, Operações EVP (genpkey, x509, s_client, dgst, mac, kdf, cms, pkcs12) e Políticas @SECLEVEL

- [[openssl-arquitetura-providers-openssl3-default-fips-legacy-cnf]] — Arquitetura do **OpenSSL 3.x (`openssl/openssl`)**: `libssl`, `libcrypto` e o Novo Modelo de **Providers (`default`, `fips`, `legacy`, `base`, `null`)**
- [[openssl-conformidade-fips-140-3-fipsmodule-cnf-fipsinstall-validacao]] — Conformidade **FIPS 140-3** no OpenSSL 3.x: Ativando o **`fips` Provider (`fips.so`)**, Auto-Testes **`openssl fipsinstall`** e `default_properties = fips=yes`
- [[openssl-geracao-chaves-genpkey-ed25519-ecdsa-rsa-pss-protecao-pkcs8]] — Geração Moderna de Chaves Assimétricas com **`openssl genpkey`**: Preferindo **`Ed25519` / `X25519` / `ECDSA P-384`** e Proteção **PKCS#8 (`-aes-256-cbc`)**
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Operações de **PKI e Certificados X.509** no OpenSSL 3.x: Gerando **CSRs e Certificados com `SAN` (`-addext subjectAltName`)** em Uma Única Linha!
- [[openssl-diagnostico-tls-s-client-certificados-ciphers-alpn-ocsp]] — Diagnóstico Profundo de **TLS 1.3 / 1.2 e mTLS** com **`openssl s_client`**: Inspecionando Cadeia de Certificados, **SNI**, **ALPN**, **OCSP Stapling** e Cipher Suites
- [[openssl-hashes-hmac-kdf-dgst-mac-kdf-hkdf-pbkdf2-scrypt-argon2]] — Integridade Criptográfica, **HMAC** e Derivação de Chaves (**KDF**) no OpenSSL 3.x: **`openssl dgst`**, **`openssl mac`** e **`openssl kdf` (`HKDF`, `PBKDF2`, `Scrypt`, `Argon2id`)**
- [[openssl-criptografia-simetrica-enc-pbkdf2-iter-limitacoes-cms-age]] — Criptografia de Arquivos com **`openssl enc`** vs. **`openssl cms`**: A Importância Obrigatória de **`-pbkdf2 -iter 600000`** e Limites de Cifras Sem MAC
- [[openssl-formatos-certificados-chaves-pem-der-pkcs12-conversao-segura]] — Conversão Segura entre Formatos de Certificados e Chaves (**`PEM`, `DER`, `PKCS#12 / .pfx`, `PKCS#7`**) no OpenSSL 3.x: Criptografia Forte no **`openssl pkcs12`**
- [[openssl-politicas-seguranca-openssl-cnf-cipherstring-seclevel-minprotocol]] — Hardening Sistêmico via **`/etc/ssl/openssl.cnf`**: Impondo **`MinProtocol = TLSv1.2`** e **`CipherString = DEFAULT@SECLEVEL=2`** para Todas as Aplicações do Servidor!
- [[openssl-benchmarking-criptografico-speed-evp-aes-ni-avx512-pqc-ml-kem]] — Benchmarking Criptográfico e Aceleração de Hardware com **`openssl speed -evp`**: Medindo **AES-NI / VAES**, **ChaCha20-Poly1305**, **Ed25519** e **ML-KEM / ML-DSA**

## Tranche 14 (IDs 1301–1400)

### authentik (goauthentik/authentik) — Plataforma Open-Source de Identidade e SSO (OIDC, SAML 2.0, Outposts Proxy/LDAP/RADIUS/RAC, Flows/Stages, Expression Policies Python, SCIM e Blueprints IaC)

- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Arquitetura do **authentik (`goauthentik/authentik`)**: Core Server, **Embedded Outpost** em Go, **Worker** Assíncrono e **PostgreSQL**
- [[authentik-motor-flows-stages-bindings-autenticacao-contextual]] — O Motor de **Flows, Stages e Stage Bindings** no authentik: Construindo Jornadas de Autenticação, MFA Adaptativo, Enrollment e Recovery sem Código Fixo
- [[authentik-politicas-reputacao-ip-expressoes-python-rbac-abac]] — Motor de Políticas (**Policy Engine**) do authentik: **Expression Policies** em Python, **Reputation Policy** Anti-Brute-Force, GeoIP e HIBP
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Provedores **OAuth2 / OIDC**, **SAML 2.0** e **SCIM 2.0** no authentik: Assinatura de JWTs, Property Mappings (Scopes) e Provisionamento Automático de Ciclo de Vida
- [[authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida]] — Arquitetura de **Outposts** no authentik: Protegendo Aplicações Sem SSO via **Proxy / ForwardAuth (Traefik, Nginx, Envoy)** e Gateways **LDAP / RADIUS**
- [[authentik-blueprints-infraestrutura-como-codigo-gitops-automacao]] — Identidade como Código (**Identity-as-Code**) no authentik com **Blueprints YAML**: Versionando Fluxos, Políticas, Provedores e RBAC via GitOps
- [[authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio]] — Autenticação Resistente a Phishing no authentik: **WebAuthn / Passkeys (FIDO2)**, Restrição de **MDS Attestation (`AAUID`)**, TOTP e Códigos de Recuperação
- [[authentik-diretorio-ldap-active-directory-sync-federacao-fontes]] — Sincronização de Diretório (**LDAP Source / Active Directory**) e Federação OAuth/SAML no authentik: Coexistência e Migração Gradual de Legados
- [[authentik-auditoria-eventos-notificacoes-webhooks-siem-rbac]] — Auditoria de Eventos de Segurança, **Notification Rules / Webhooks** e **RBAC Granular por Objeto** no authentik: Monitorando o IdP no SIEM
- [[authentik-hardening-producao-secret-key-reverse-proxy-tls-backups]] — Hardening de Produção do **authentik**: Proteção da **`AUTHENTIK_SECRET_KEY`**, Configuração de `trusted_proxies`, Isolamento de Outposts e Backups

### Kanidm (kanidm/kanidm) — Gerenciamento de Identidade (IdM) Memory-Safe em Rust, Passkeys FIDO2 WebAuthn Attested, OAuth2/OIDC com PKCE, LDAPS Read-Only e Autenticação POSIX SSH/PAM (`kanidm-unixd`)

- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Arquitetura do **Kanidm (`kanidm/kanidm`)**: Plataforma Completa de Gerenciamento de Identidade (IDM) em **Rust** com Banco Transacional Próprio e Padrões Estritos
- [[kanidm-configuracao-server-toml-domain-origin-zfs-backups-online]] — Configuração Segura do **`server.toml`** no Kanidm: Consistência Estrita **`domain` / `origin` (WebAuthn)**, `http_client_address_info` (`proxy-v2`) e `[online_backup]`
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Autenticação Criptográfica no Kanidm: **Passkeys (WebAuthn)**, **Attested Passkeys (Verificação de Fabricante FIDO)** e Políticas de Credenciais por Grupo
- [[kanidm-modelo-privilegios-separacao-admin-idm-admin-reauth-sudo]] — Modelo de Privilégio Mínimo e **Reautenticação (`re-auth` Estilo `sudo`)** no Kanidm: Por que `admin` e `idm_admin` São Estritamente Separados?
- [[kanidm-provedor-oauth2-oidc-pkce-strict-scope-maps-claims-custom]] — Provedor **OAuth2 / OpenID Connect (OIDC)** no Kanidm: Obrigatoriedade de **PKCE (`S256`)**, **Scope Maps** Baseados em Grupos e **Claim Maps**
- [[kanidm-integracao-linux-pam-nss-kanidm-unixd-ssh-keys-tpm]] — Autenticação Linux/Unix e Distribuição de Chaves SSH no Kanidm: Daemon **`kanidm_unixd`**, PAM/NSS, **Cache Offline Protegido por TPM 2.0** e **`kanidm_ssh_authorizedkeys`**
- [[kanidm-gateway-ldaps-read-only-service-accounts-api-tokens]] — Gateway **LDAPS Somente-Leitura (`:636`)** e **Service Accounts** no Kanidm: Integrando Sistemas Legados sem Expor o Diretório a Escritas LDAP
- [[kanidm-ciclo-vida-identidades-valid-from-expire-recycle-bin-tombstones]] — Governança de Ciclo de Vida de Contas no Kanidm: Janelas Temporais Automáticas (**`--valid-from` / `--expire`**), **Recycle Bin** e **Tombstones**
- [[kanidm-replicacao-alta-disponibilidade-mtls-multi-node-consistencia]] — Alta Disponibilidade e **Replicação Multi-Nó (`[replication]`)** no Kanidm: Sincronização via **mTLS** e Resolução de Conflitos por **CSN (*Change Sequence Number*)**
- [[kanidm-operacao-cli-kanidmd-certificados-backups-migracoes-json]] — Operação, Recuperação de Desastres e **Migrações Declarativas (`/etc/kanidm/migrations.d/`)** no Kanidm: `kanidmd database backup/restore` e `SIGHUP`

### Vaultwarden (dani-garcia/vaultwarden) — Servidor Bitwarden Client API em Rust, Criptografia Zero-Knowledge Client-Side, Organizations & Collections, FIDO2 WebAuthn 2FA, Bitwarden Send e Event Logs

- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Arquitetura do **Vaultwarden (`dani-garcia/vaultwarden`)**: Servidor Alternativo **Bitwarden** em **Rust**, Criptografia **Zero-Knowledge Client-Side** e Bancos SQLite/PostgreSQL
- [[vaultwarden-blindagem-painel-admin-token-argon2-phc-signups-allowed]] — Hardening Crítico do **Vaultwarden**: Desabilitando Cadastros Abertos (**`SIGNUPS_ALLOWED=false`**), Convites e Protegendo o **`ADMIN_TOKEN` com Argon2id PHC**
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Compartilhamento Corporativo no Vaultwarden: **Organizations**, **Collections**, Papéis RBAC (`Owner`, `Admin`, `Manager`, `User`), **Groups** e **Organization Policies**
- [[vaultwarden-autenticacao-2fa-webauthn-fido2-yubikey-totp-duo-email]] — Autenticação Multifator (**2FA**) e Derivação de Chave (**Argon2id Client-Side**) no Vaultwarden: **FIDO2 WebAuthn**, **YubiKey OTP**, **TOTP** e **Duo**
- [[vaultwarden-compartilhamento-efemero-send-acesso-emergencia-anexos]] — Compartilhamento Efêmero (**Bitwarden Send**) e **Emergency Access** no Vaultwarden: Eliminando Senhas no Slack/E-mail com Expiração e Contagem de Visualizações
- [[vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting]] — Arquitetura de Proxy Reverso, **WebSockets** e **`IP_HEADER`** no Vaultwarden: Sincronização Instantânea, Prevenção de IP Spoofing e **Fail2ban / CrowdSec**
- [[vaultwarden-auditoria-event-logs-retencao-monitoramento-siem-soc]] — Logs de Auditoria Organizacional (**Event Logs**) e Retenção (`EVENTS_DAYS_RETAIN`) no Vaultwarden: Rastreando Acessos, Exportações de Cofre e Mudanças de Permissão
- [[vaultwarden-automacao-cli-bw-api-keys-ssh-agent-pipelines-devops]] — Automação com **Bitwarden CLI (`bw`)**, **Personal API Keys (`client_id` / `client_secret`)** e **SSH Agent** Conectados ao Vaultwarden
- [[vaultwarden-backups-consistentes-sqlite3-online-backup-rsa-keys-anexos]] — Estratégia de **Backup e Disaster Recovery** do Vaultwarden: Backup Online Atômico do **SQLite (`sqlite3 .backup`)**, Chaves **`rsa_key*`**, `attachments` e Criptografia **`age` / `GPG`**
- [[vaultwarden-sso-directory-connector-ldap-scim-emergencia-enterprise]] — Provisionamento Corporativo no Vaultwarden: **Bitwarden Directory Connector (LDAP / Active Directory / Entra ID / Okta)**, Notificações Push e Hardening de Container

### Rustls (rustls/rustls) — Biblioteca Moderna de TLS 1.3 e TLS 1.2 Memory-Safe em Rust, Arquitetura CryptoProvider (`aws-lc-rs` / `ring`), Troca de Chaves Pós-Quântica (`X25519MLKEM768`), FIPS 140-3, mTLS e ECH

- [[rustls-arquitetura-tls-memory-safe-rust-cryptoprovider-aws-lc-ring]] — Arquitetura do **Rustls (`rustls/rustls`)**: Biblioteca Moderna de **TLS 1.3 e TLS 1.2 Memory-Safe em Rust** e Modelo de **`CryptoProvider` (`aws-lc-rs` e `ring`)**
- [[rustls-decisoes-seguranca-non-features-tls12-tls13-pfs-aead-obrigatorio]] — Filosofia **"Secure by Default" e Non-Features Deliberadas** no Rustls: Por que o Rustls Proíbe Cifras Sem PFS, Modos CBC (`MAC-then-Encrypt`), Renegociação e TLS < 1.2?
- [[rustls-troca-chaves-pos-quantica-hibrida-x25519mlkem768-fips]] — Criptografia **Pós-Quântica Híbrida (`X25519MLKEM768`)** e Conformidade **FIPS 140-3** no Rustls com `aws-lc-rs`: Protegendo o Tráfego TLS Hoje
- [[rustls-validacao-certificados-webpki-root-store-pinning-crl]] — Verificação Estrita de Certificados X.509 no Rustls com **` rustls-webpki`**: `RootCertStore`, `rustls-native-certs`, `webpki-roots` e Revogação **CRL / OCSP**
- [[rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust]] — Autenticação Mútua (**mTLS Zero-Trust**) e Seleção Dinâmica de Certificados via **SNI (`ResolvesServerCert`)** em Servidores Rustls
- [[rustls-privacidade-encrypted-client-hello-ech-rfc9849-sni-alpn]] — Privacidade no Handshake TLS 1.3 com **Encrypted Client Hello (`ECH` — `RFC 9849`)**, Compressão de Certificados (**`RFC 8879`**) e **Raw Public Keys (`RFC 7250`)** no Rustls
- [[rustls-retomada-sessao-tickets-0rtt-anti-replay-seguranca]] — Retomada de Sessão (**Session Resumption**), Rotação de **Session Tickets** e Riscos de **Replay em Dados `0-RTT` (`EarlyData`)** no Rustls
- [[rustls-otimizacao-performance-vectored-io-fragment-size-tokio-rustls]] — Performance de Alta Vazão no Rustls: **Vectored I/O (`write_vectored`)**, **`max_fragment_size`**, Zero-Copy Unbuffering e Integração **`tokio-rustls`**
- [[rustls-depuracao-segura-sslkeylogfile-keylog-wireshark-auditoria]] — Depuração Controlada de Tráfego TLS 1.3 com **`KeyLogFile` (`SSLKEYLOGFILE`)** e **Session Exporters (`RFC 5705` / `RFC 8446`)** no Rustls
- [[rustls-integracao-c-ffi-rustls-ffi-curl-apache-mod-tls-migracao]] — Levando Segurança de Memória para Aplicações em C/C++ com **`rustls-ffi` (`crustls`)**: Integrando o Rustls no **`curl`**, **Apache `mod_tls`** e Daemons Legados

### Cisco Snort 3 (snort3/snort3 — Snort++) — Motor NIDS/NIPS Multithreaded em C++17, Configuração LuaJIT (`snort.lua`), Detecção Portless (`wizard` + `binder`), Sticky Buffers, OpenAppID, Hyperscan e Modo Inline `libdaq`

- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Arquitetura do **Cisco Snort 3 (`snort3/snort3` — Snort++)**: Motor NIDS/NIPS **Multithreaded em C++17**, Configuração **LuaJIT (`snort.lua`)** e **Hyperscan**
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Configuração de **`snort.lua`** e Detecção de Protocolos Independente de Porta (**Portless Inspection**): Como o **`wizard`** e o **`binder`** Derrotam Evasões de Porta!
- [[snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics]] — Inspetores Profundos de Protocolo (**Service Inspectors**) no Snort 3: **`http_inspect` / `http2_inspect`**, **`js_norm`**, **`dce_smb`** e Protocolos Industriais **OT/ICS (`modbus`, `dnp3`, `s7commplus`, `iec104`)**
- [[snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data]] — A Nova Sintaxe de Regras do **Snort 3**: **Sticky Buffers (`http_uri`, `http_header`, `http_client_body`, `file_data`)**, Cabeçalhos de Serviço (`alert http`) e `snort2lua`
- [[snort-appid-openappid-visibilidade-camada-7-shadow-it-rna]] — Descoberta de Aplicações Camada 7 (**OpenAppID / `appid`**) e Descoberta Passiva de Rede (**`rna` — *Real-time Network Awareness***) no Snort 3
- [[snort-modos-operacao-libdaq-afpacket-nfq-inline-ips-drop-reject]] — Operação Inline (**IPS Ativo: `drop`, `sdrop`, `reject`**) vs. Passivo (**IDS / TAP**) no Snort 3 com **`libdaq` (`afpacket`, `nfq`, `pcap`, `dpdk`)**
- [[snort-reputacao-ip-suppress-event-filter-rate-filter-anti-dos]] — Controle de Ruído, **IP Reputation (`reputation`)**, **`suppress`**, **`event_filter`** e **`rate_filter`** no Snort 3: Prevenindo Alert Fatigue e Floods
- [[snort-saidas-logs-alert-json-unified2-integracao-siem-opensearch]] — Saídas Estruturadas de Eventos no Snort 3: Configurando **`alert_json`** para Ingestão Direta em **SIEM (Wazuh, OpenSearch, ELK, Splunk)** e Captura de Pacotes
- [[snort-profiling-performance-profiler-latency-tuning-regras-lentas]] — Engenharia de Performance e Detecção de Gargalos no Snort 3: **`profiler` (CPU/Memória por Regra e Módulo)**, **`latency`** e **`perf_monitor`**
- [[snort-gerenciamento-regras-pulledpork3-talos-policies-connectivity-security]] — Gerenciamento de Regras **Cisco Talos** e Políticas Baseadas em Metadados (**`connectivity`, `balanced`, `security`, `max-detect`**) no Snort 3 com **PulledPork 3**

### Arkime (arkime/arkime, ex-Moloch) — Full Packet Capture (FPC) e Indexação de Metadados SPI em Escala Multi-Gigabit (`capture`, `viewer`, `wiseService`, `Parliament`, `Cont3xt` e Correlação `communityId`)

- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Arquitetura do **Arkime (`arkime/arkime`, ex-Moloch)**: Sistema de **Full Packet Capture (FPC)** e Indexação de Metadados **SPI** em Escala Multi-Gigabit
- [[arkime-configuracao-config-ini-tiered-pcapdir-freespaceg-rotacao]] — Configuração Hierárquica (**`/opt/arkime/etc/config.ini`**), Retenção Automática de Disco (**`freeSpaceG`**) e Timeouts de Fluxo no Arkime
- [[arkime-otimizacao-captura-alta-velocidade-tpacketv3-snf-dpdk-threads]] — Captura Sem Perda de Pacotes em Links de **10 Gbps a 100 Gbps** no Arkime: `packetThreads`, **`tpacketv3` (`AF_PACKET`)**, **`pcapWriteMethod=simple-nodirect`** e **Criptografia de PCAP em Repouso**
- [[arkime-linguagem-busca-expressoes-sessions-spiview-spigraph-hunting]] — Caça a Ameaças (**Threat Hunting**) no Arkime: Linguagem de Expressões de Busca, **Sessions**, **SPI View**, **SPI Graph** e **Connections Graph**
- [[arkime-enriquecimento-wiseservice-threat-intel-regras-yara-tagger]] — Enriquecimento em Tempo Real com **`wiseService` (*With Intelligence See Everything*)**, **YARA** em Fluxo (`yara.ini`) e **`arkime.rules`**
- [[arkime-ecossistema-parliament-cont3xt-esproxy-federacao-multi-cluster]] — O Ecossistema Completo do Arkime: **`Parliament`** (Multi-Cluster Dashboard), **`Cont3xt`** (Agregador de CTI/OSINT) e **`esProxy`**
- [[arkime-seguranca-viewer-tls-reverse-proxy-headers-passwordsecret]] — Segurança e Autenticação do **Arkime Viewer**: `passwordSecret`, `serverSecret`, TLS Mútuo entre Sensores e Integração **SSO (`authMode=header-jwt` / OIDC)**
- [[arkime-ingestao-pcap-offline-dfir-capture-r-analise-forense]] — Uso do Arkime em **Laboratórios de DFIR Offline (`capture -r`)**: Importando Diretórios de Arquivos `.pcap` de Incidentes para Investigação Visual e Grafo
- [[arkime-automacao-api-rest-cron-queries-alertas-exportacao-pcap]] — Automação no Arkime: **Periodic Queries (*Cron Queries*)**, **Hunt Jobs (Busca de Bytes/Regex nos PCAPs Brutos)** e Extração de PCAP via **API REST**
- [[arkime-integracao-zeek-suricata-snort-malcolm-correlacao-community-id]] — Tríade da Visibilidade de Rede (**NSM**): Correlacionando **Arkime (FPC) + Zeek (Logs de Transação) + Suricata / Snort 3 (Alertas IDS)** via **`communityId`**

### RITA (activecm/rita — Real Intelligence Threat Analytics) — Caça a Ameaças em Logs Zeek para Detecção Matemática de C2 Beaconing (IP/SNI/Strobe), Long Connections, DNS Tunneling e Modificadores de Prevalência

- [[rita-arquitetura-caca-ameacas-logs-zeek-beaconing-dns-tunneling]] — Arquitetura do **RITA (`activecm/rita` — *Real Intelligence Threat Analytics*)**: Caça a Ameaças (**Threat Hunting**) em Logs **Zeek** para Detecção de **C2 Beaconing**
- [[rita-matematica-deteccao-beacons-intervalos-jitter-tamanho-score]] — A Matemática da Detecção de **Beaconing C2 (Com e Sem *Jitter*)** no RITA: Desvio de Intervalos (`Delta Times`), Simetria de Bytes, dispersão MADM e Score
- [[rita-beaconing-sni-tls-domain-fronting-cdn-cloudflare-hunting]] — Detecção de **SNI / FQDN Beaconing** no RITA: Caçando Implants C2 que Rotacionam IPs atrás de **CDNs (Cloudflare, CloudFront, Fastly, Azure Front Door)**
- [[rita-deteccao-long-connections-conexoes-persistentes-ssh-rdp-c2]] — Caça a **Long Connections** (Conexões Persistentes) no RITA: Detectando Shells Reversos Interativos, Túneis SSH/Ngrok e Exfiltração Contínua
- [[rita-deteccao-dns-tunneling-subdominios-unicos-iodine-dnscat2]] — Detecção de **C2 e Exfiltração por DNS Tunneling (`iodine`, `dnscat2`, `sliver dns`, `cobalt strike dns`)** no RITA
- [[rita-modificadores-score-prevalencia-raridade-first-seen-missing-host]] — Modificadores Inteligentes de Score (**`modifiers`**) no RITA: **Prevalência na Rede (`prevalence`)**, **`first_seen`** e **`missing_host_count` (Conexões Diretas a IP Sem DNS)**
- [[rita-filtros-rede-interna-whitelist-safelist-config-hjson-tuning]] — Configuração de Sub-redes Internas (**`internal_subnets`**) e Listas de Exclusão (**`never_included_ips` / `never_included_domains`**) no `/etc/rita/config.hjson`
- [[rita-threat-intel-feeds-customizados-online-ip-fqdn-correlacao]] — Integração de Feeds de **Threat Intelligence (`threat_intel`)** no RITA: Cruzando Conexões Zeek com Listas de IoCs (`online_feeds` e Feeds Customizados)
- [[rita-operacao-continua-rolling-datasets-zeek-cron-automacao-soc]] — Operação Contínua no SOC com **Rolling Datasets (`--rolling` vs. `--rebuild`)**, Exportação CSV (`--stdout`) e Integração de Alertas RITA no SIEM
- [[rita-fluxo-investigacao-caca-ameacas-rita-zeek-arkime-wireshark]] — Playbook Completo de **Threat Hunting de Rede**: Do Score de Beacon no **RITA** ao Pivotamento no **Zeek (`uid` / `community_id`)** e Captura Bruta no **Arkime**

### Gravitational Teleport (gravitational/teleport) — Plataforma de Acesso Zero-Trust Baseada em Certificados Efêmeros para SSH (Gravação eBPF), Kubernetes, Databases, Web Apps, Windows RDP, Machine ID (`tbot`) e JIT Access Requests

- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Arquitetura do **Gravitational Teleport (`gravitational/teleport`)**: Acesso **Zero-Trust Baseado em Identidade** e **Certificados de Curta Duração** (Sem Chaves Estáticas!)
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Acesso SSH com **Gravação Completa de Sessão Interativa** e **Auditoria Enriquecida por eBPF (`enhanced_recording`)** no Teleport
- [[teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas]] — Acesso Zero-Trust a **Clusters Kubernetes (`tsh kube login`)** e **Bancos de Dados (`tsh db connect` — PostgreSQL, MySQL, MongoDB, Redis)** sem Senhas Compartilhadas
- [[teleport-acesso-web-apps-jwt-headers-windows-desktop-rdp-mcp]] — Acesso Seguro a **Aplicações Web Internas (`Application Service` + JWT)**, **Windows Desktops (`RDP` Sem Senha via Smartcard Virtual)** e **Servidores MCP (IA)** no Teleport
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Controle de Acesso **RBAC + ABAC (`labels`)**, **Per-Session MFA (FIDO2 WebAuthn)** e Restrição de IP/Dispositivo em Roles do Teleport
- [[teleport-fluxos-just-in-time-access-requests-chatops-slack-jira]] — Privilégio Zero Permanente (**Zero Standing Privilege — ZSP**) com **Just-In-Time (JIT) Access Requests** no Teleport: Aprovação via Slack, Mattermost, PagerDuty ou Jira
- [[teleport-identidade-maquina-machine-id-tbot-cicd-renovacao-automatica]] — Identidade de Máquina e Automação CI/CD com **Teleport Machine ID (`tbot`)**: Aposentando Segredos de Longa Duração no GitHub Actions, GitLab CI e Ansible
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Ingresso Seguro de Agentes (**Node Joining**) no Teleport: Eliminando Tokens Estáticos com **Cloud Auto-Joining (AWS IAM, GCP, Azure, Kubernetes)** e **TPM Joining**
- [[teleport-auditoria-eventos-gravacao-s3-dynamodb-integracao-siem]] — Arquitetura de Alta Disponibilidade, **Armazenamento de Auditoria e Gravações (S3 / GCS / MinIO)** e Exportação de Eventos para **SIEM (`event-handler`)** no Teleport
- [[teleport-federacao-trusted-clusters-leaf-root-isolamento-multi-tenant]] — Federação Multi-Cluster e Multi-Cloud com **Trusted Clusters (`Root Cluster` e `Leaf Clusters`)** no Teleport

### FreeIPA (freeipa/freeipa — Red Hat IdM) — Identidade, Política e Auditoria Integrada para Frotas Linux (389-ds LDAP, MIT Kerberos KDC, Dogtag PKI + `certmonger`, BIND DNS, HBAC, Sudo Centralizado, 2FA/Passkeys e Cross-Forest AD Trust)

- [[freeipa-arquitetura-identidade-linux-389ds-kerberos-dogtag-pki-dns]] — Arquitetura do **FreeIPA (`freeipa/freeipa` / Red Hat Identity Management)**: Identidade, Política e Auditoria Integrada para Linux (**389-ds LDAP, MIT Kerberos KDC, Dogtag PKI e BIND DNS**)
- [[freeipa-controle-acesso-hbac-host-based-access-control-regras-pam]] — Controle de Acesso Baseado em Host (**HBAC — *Host-Based Access Control***) e **`hbactest`** no FreeIPA: Restringindo *Quem* Acessa *Qual Servidor* por *Qual Serviço PAM*
- [[freeipa-governanca-sudo-centralizado-sudorule-sudocmd-auditoria]] — Governança Centralizada de **`sudo` (`sudorule`, `sudocmd`, `sudocmdgroup`)** no FreeIPA: Aposentando arquivos `/etc/sudoers` Locais Espalhados
- [[freeipa-pki-dogtag-certmonger-auto-renovacao-mtls-subca]] — PKI Corporativa Integrada (**Dogtag CA & KRA**) e Renovação Automática de Certificados em Hosts Linux com **`certmonger` (`ipa-getcert`)** no FreeIPA
- [[freeipa-autenticacao-2fa-otp-totp-hotp-passkeys-radius-pkinit]] — Autenticação Multifator (**2FA / MFA**) e **Passwordless** no FreeIPA: Tokens **TOTP/HOTP (`otptoken`)**, **Passkeys FIDO2**, **Smartcards (`PKINIT`)** e **RADIUS Proxy**
- [[freeipa-ssh-chaves-publicas-ldap-hostkeys-known-hosts-sssd]] — Segurança de **SSH Centralizada** no FreeIPA: Chaves Públicas de Usuário no LDAP (`ipaSshPubKey`), Verificação Automática de **Host Keys (`known_hosts`)** e **Kerberos GSSAPI**
- [[freeipa-automember-grupos-dinamicos-hosts-usuarios-escalabilidade]] — Automação Zero-Touch em Escala com **`automember` (Regras de Auto-Associação)** no FreeIPA: Classificando Servidores e Usuários Automaticamente no Ingresso
- [[freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba]] — Integração Corporativa **FreeIPA + Microsoft Active Directory (`Cross-Forest Kerberos Trust`)**: Identidade Unificada Windows e Linux sem Duplicar Contas!
- [[freeipa-replicacao-multi-master-topologia-hidden-replicas-backups]] — Alta Disponibilidade (**Multi-Master Topology**), **`Hidden Replicas`** e Backup/Restore (`ipa-backup` / `ipa-restore`) no FreeIPA
- [[freeipa-rbac-delegacao-privilegios-selinux-usermap-subids-containers]] — Delegação Administrativa (**RBAC: `role`, `privilege`, `permission`**), **SELinux User Mapping (`selinuxusermap`)** e **Subordinate IDs (`subid`)** no FreeIPA

### TPM 2.0 Software Stack & Tools (`tpm2-software/tpm2-tss` & `tpm2-tools`) — Raiz de Confiança em Hardware, Registradores PCR e Measured Boot, Selagem LUKS2 (`tpm2_unseal`), Enhanced Authorization, Atestação Remota (`tpm2_quote`), `tpm2-pkcs11` e `swtpm`

- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Arquitetura do **TPM 2.0 (`tpm2-tss` & `tpm2-tools`)**: Raiz de Confiança em Hardware, Camadas da Stack TCG (`FAPI`, `ESYS`, `TCTI`) e **As 4 Hierarquias (`Owner`, `Endorsement`, `Platform`, `Null`)**
- [[tpm2-registradores-pcr-measured-boot-extend-sha256-uefi-eventlog]] — Funcionamento dos **PCRs (*Platform Configuration Registers*)** e **Measured Boot** no TPM 2.0: A Operação Unidirecional **`PCR_Extend`** e os Bancos **`sha256`**
- [[tpm2-hierarquia-chaves-createprimary-create-load-persist-evictcontrol]] — Gerenciamento de Chaves no TPM 2.0: **`tpm2_createprimary`**, **`tpm2_create`**, **`tpm2_load`** e Persistência em NVRAM com **`tpm2_evictcontrol`**
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Selagem de Segredos (**Sealing / Unsealing** Vinculado a **PCRs**) com `tpm2_createpolicy`, `tpm2_unseal` e Desbloqueio **LUKS2 (`systemd-cryptenroll`)**
- [[tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin]] — Políticas Avançadas de Autorização (**Enhanced Authorization — EA**) no TPM 2.0: **`tpm2_policyauthorize` (Políticas Assinadas)**, **`tpm2_policyor`** e **`tpm2_policysecret`**
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Atestação Remota de Hardware e Boot (**Remote Attestation**) no TPM 2.0: **Endorsement Key (`EK`)**, **Attestation Key (`AK`)**, **`tpm2_quote`** e **`tpm2_checkquote`**
- [[tpm2-pkcs11-ssh-tls-nginx-openvpn-chaves-hardware-nao-exportaveis]] — Uso de Chaves TPM 2.0 Não-Exportáveis em **OpenSSH, Nginx, OpenVPN, StrongSwan e Rust/Go** com **`tpm2-pkcs11`** e **`tpm2-openssl` Provider**
- [[tpm2-nvram-armazenamento-seguro-contadores-monotonicos-anti-rollback]] — Memória Não-Volátil (**NVRAM**: `tpm2_nvdefine`, `tpm2_nvwrite`, `tpm2_nvread`) e **Contadores Monotônicos Anti-Rollback (`tpm2_nvincrement`)** no TPM 2.0
- [[tpm2-protecao-forca-bruta-dictionary-attack-lockout-clear-seguranca]] — Proteção Contra Força Bruta em Hardware (**Dictionary Attack Lockout**: `tpm2_dictionarylockout`), Senhas de Hierarquia (`tpm2_changeauth`) e **TRNG (`tpm2_getrandom`)**
- [[tpm2-simulacao-testes-ci-cd-swtpm-tcti-qemu-vtpm-containers]] — Testes Automatizados em CI/CD e Virtualização (**`vTPM`**) com **`swtpm` (`libtpms`)** e Seleção de **`TCTI` (`TPM2TOOLS_TCTI`)** no `tpm2-tss`

## Tranche 15 (IDs 1401–1500)

### SSSD (SSSD/sssd — System Security Services Daemon) — Identidade Centralizada e Autenticação Offline em Frotas Linux (Domínios IPA/AD/LDAP, Cache LDB, Mapeamento SID->UID, GPOs, SSH AuthorizedKeysCommand e Smart Cards PKCS#11)

- [[sssd-arquitetura-system-security-services-daemon-responders-providers-ldb]] — Arquitetura do **SSSD (`SSSD/sssd` — *System Security Services Daemon*)**: Responders (`nss`, `pam`, `ssh`, `sudo`, `autofs`), Backends Plugáveis e Cache Offline **`ldb`**
- [[sssd-configuracao-dominios-ipa-ad-ldap-krb5-enumeracao-performance]] — Configuração de Domínios no **`/etc/sssd/sssd.conf`**: Provedores `id_provider` / `auth_provider` (`ipa`, `ad`, `ldap`, `krb5`) e Por Que Manter **`enumerate = false`**!
- [[sssd-integracao-active-directory-realmd-id-mapping-gpo-access-control]] — Integração Nativa **Linux + Active Directory (`id_provider = ad`)** no SSSD: Ingresso com `realm join`, **Mapeamento Determinístico SID-para-UID (`ldap_id_mapping`)** e **GPOs no Linux**
- [[sssd-cache-offline-credenciais-sss-cache-invalidacao-troubleshooting]] — Funcionamento do **Cache em Duas Camadas (`Memory Cache` + `LDB`)**, Autenticação Offline (`cache_credentials`) e Invalidação Cirúrgica com **`sss_cache`** no SSSD
- [[sssd-controle-acesso-pam-access-provider-simple-ldap-hbac-gpo]] — Provedores de Autorização (**`access_provider`**) no SSSD: Filtrando Quem Pode Fazer Login via **`simple` (`simple_allow_groups`)**, **`ldap` (`ldap_access_filter`)**, **`ipa` (HBAC)** e **`ad` (GPO)**
- [[sssd-autenticacao-smartcards-pkcs11-certmap-fido2-passkeys]] — Autenticação **Passwordless** no Linux com SSSD: **Smartcards X.509 (`pam_cert_auth = True` / PKCS#11 `p11_child`)**, Regras de **`certmap`** e **Passkeys FIDO2 WebAuthn (`passkey_child`)**
- [[sssd-idp-externo-oauth2-oidc-device-flow-entra-id-keycloak-authentik]] — Autenticação Direta de Desktops e Servidores Linux em **Provedores Cloud OAuth2 / OIDC (`id_provider = idp` — Entra ID, Keycloak, Okta, Authentik, Kanidm)** com SSSD
- [[sssd-isolamento-privilegios-rootless-socket-activation-infopipe-dbus]] — Hardening do Próprio SSSD: Execução **Sem Privilégios (`user = sssd`)**, **Systemd Socket Activation**, **Application Domains** e Interface D-Bus **`InfoPipe` (`sssd_ifp`)**
- [[sssd-otimizacao-performance-ignore-group-members-dyndns-krb5-fast]] — Tuning de Performance e Segurança de Rede no SSSD: **`ignore_group_members`**, Atualização Dinâmica de DNS Segura (**`dyndns_update` via GSS-TSIG**) e **Kerberos FAST**
- [[sssd-diagnostico-sssctl-user-checks-logs-debug-level-auditoria]] — Diagnóstico Avançado e Forense de Autenticação no SSSD com **`sssctl` (`user-checks`, `analyze`, `debug-level`)** e Logs `/var/log/sssd/*.log`

### Keylime (keylime/keylime & rust-keylime) — Atestação Remota Contínua Baseada em Hardware TPM 2.0 (Registrar, Verifier, Tenant, Rust Agent, IMA Runtime File Integrity, Measured Boot UEFA e Revogação Criptográfica)

- [[keylime-arquitetura-atestacao-remota-tpm2-verifier-registrar-rust-agent]] — Arquitetura do **CNCF Keylime (`keylime/keylime` & `rust-keylime`)**: Atestação Remota Contínua Baseada em **TPM 2.0**, `Verifier`, `Registrar`, `Tenant` e Agente Oficial em **Rust**
- [[keylime-fluxo-registro-ek-ak-makecredential-activatecredential-ekcert]] — Bootstrapping de Confiança no Keylime: Validação da **Endorsement Key (`EKCert`)**, Desafio **`MakeCredential` / `ActivateCredential`** e Registro da **`AK`** no `Registrar`
- [[keylime-provisionamento-payload-criptografado-bootstrap-chaves-mtls]] — Entrega Segura de Segredos (**Encrypted Payload Provisioning**) no Keylime: Derivação Tripartida da Chave **`U` + `V` = `K`** só Após Aprovação na Atestação!
- [[keylime-monitoramento-integridade-runtime-linux-ima-allowlists-polices]] — Monitoramento de Integridade em Tempo de Execução (**Runtime Integrity Monitoring**) no Keylime com **Linux IMA (`Integrity Measurement Architecture` — `PCR 10`)**
- [[keylime-criacao-politicas-keylime-create-policy-assinatura-ima-evm]] — Geração de Políticas de Runtime (**`keylime_create_policy`**), Verificação de Assinaturas Digitais **`ima-sig`** e Repositórios de Pacotes Confiáveis no Keylime
- [[keylime-atestacao-measured-boot-uefi-eventlog-elchecking-politicas]] — Atestação de **Measured Boot UEFI (`binary_bios_measurements`)** e Políticas de Firmware/Secure Boot (`--mb_refstate`) no Keylime
- [[keylime-revogacao-automatica-webhooks-local-action-isolamento-zero-trust]] — Resposta Automática a Incidentes (**Revocation Framework**) no Keylime: Isolando Nós Comprometidos em Segundos via **Webhooks**, **ZeroMQ** e Scripts **`local_action_*`**
- [[keylime-configuracao-segura-mtls-verifier-registrar-banco-postgresql-ha]] — Hardening e Escalabilidade em Produção do Keylime: **mTLS Obrigatório (`trusted_client_ca`)**, Banco **PostgreSQL HA** e Configuração do **`rust-keylime` (`/etc/keylime/agent.conf`)**
- [[keylime-modelo-push-attestation-edge-nat-firewalls-escalabilidade]] — Atestação em Bordas Restritas e Atrás de NAT/Firewalls: **Push Mode Attestation (`keylime-push-model-agent`)** vs. Modelo Pull Clássico no Keylime
- [[keylime-atestacao-containers-kubernetes-spire-confidential-computing]] — Integração do Keylime com **Kubernetes, SPIFFE/SPIRE (`node-attestor`) e Confidential Computing (AMD SEV-SNP / Intel TDX vTPM)**: Zero-Trust Ancorado no Silício

### OpenSCAP & ComplianceAsCode (OpenSCAP/openscap & ComplianceAsCode/content) — Auditoria Automatizada e Remediação de Conformidade SCAP 1.3 (XCCDF, OVAL, CPE, CVE, Perfis CIS/STIG/PCI-DSS/ANSSI, `oscap-ssh` e Ansible/Bash)

- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Arquitetura do **OpenSCAP (`OpenSCAP/openscap`)** e **ComplianceAsCode (`scap-security-guide`)**: Padrões NIST SCAP (`XCCDF`, `OVAL`, `CPE`, `ARF`) e CLI **`oscap`**
- [[openscap-auditoria-xccdf-eval-profiles-cis-stig-pci-arf-relatorio-html]] — Executando Auditorias de Conformidade com **`oscap xccdf eval`**: Perfis **CIS Level 1/2, DISA STIG, PCI-DSS e OSPP**, Resultados **`--results-arf`** e Relatórios HTML
- [[openscap-remediacao-automatizada-online-remediate-ansible-bash-playbooks]] — Remediação Automatizada de Hardening no OpenSCAP: Exportando **Playbooks Ansible (`--fix-type ansible`)**, Scripts **Bash (`--fix-type bash`)** vs. `--remediate`
- [[openscap-customizacao-perfis-tailoring-files-variaveis-excecoes-xccdf]] — Customização de Benchmarks Corporativos no OpenSCAP com **Tailoring Files (`--tailoring-file`)**: Ajustando Variáveis XCCDF e Desabilitando Regras Incompatíveis
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Varredura de Vulnerabilidades de Pacotes (**CVE Scanning**) com **`oscap oval eval`**: Avaliando Feeds OVAL Oficiais (Red Hat, Ubuntu, Debian, SUSE, AlmaLinux)
- [[openscap-auditoria-containers-imagens-vms-oscap-podman-oscap-docker]] — Auditoria Offline de **Containers (`oscap-podman` / `oscap-docker`)**, Sistemas de Arquivos Montados (**`oscap-chroot`**) e Imagens de VM (**`oscap-vm` `qcow2`**)
- [[openscap-auditoria-remota-oscap-ssh-automacao-agentless-bastion]] — Varredura Remota Agentless via SSH com **`oscap-ssh`**: Auditando e Remediando Frotas de Servidores Linux sem Instalar Agentes Permanentes
- [[openscap-engenharia-regras-complianceascode-yaml-jinja2-templating]] — Como Escrever Regras Customizadas no **`ComplianceAsCode/content`**: `rule.yml`, Templates Parametrizados Jinja2 e Compilação Multi-Formato (`XCCDF`, `OVAL`, `Ansible`, `Bash`, `CEL`)
- [[openscap-kubernetes-compliance-operator-cel-scansettingbinding]] — Conformidade de Clusters **Kubernetes e OpenShift** com **ComplianceAsCode (`CEL Content`)** e **Compliance Operator (`ScanSettingBinding`)**
- [[openscap-integracao-ci-cd-oscap-arf-to-json-autotailor-governanca]] — Pipeline de **Continuous Compliance (Conformidade Contínua)** em CI/CD com OpenSCAP: Validando Golden Images, Parseando `ARF XML` e Prevenindo Drift

### fapolicyd (linux-application-whitelisting/fapolicyd) — Application Whitelisting no Linux via Kernel `fanotify` (`FAN_OPEN_EXEC_PERM`), Trust Database LMDB (`rpmdb` + `file`), Verificação SHA-256/IMA e Proteção Contra Execução via Interpretadores

- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Arquitetura do **fapolicyd (`linux-application-whitelisting/fapolicyd` — *File Access Policy Daemon*)**: **Application Whitelisting** no Linux via Kernel **`fanotify`** e Banco **`LMDB`**
- [[fapolicyd-politicas-known-libs-restrictive-fagenrules-rules-d]] — Políticas Modulares em **`/etc/fapolicyd/rules.d/`**, Compilador **`fagenrules`** e Diferença entre os Perfis **`known-libs`** e **`restrictive`** no fapolicyd
- [[fapolicyd-sintaxe-regras-decision-perm-subject-object-customizacao]] — A Receita de Escrita de Regras no fapolicyd: **`decision perm subject : object`**, Tipos MIME (`ftype`), `trust=1` e `deny_audit`
- [[fapolicyd-gerenciamento-trust-database-fapolicyd-cli-file-add-trust-d]] — Gerenciando o **Banco de Confiança (`trust.d/`)** com **`fapolicyd-cli`**: Autorizando Binários Customizados, Agentes de Terceiros e Aplicações em `/opt`
- [[fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering]] — Modos de Verificação de Integridade (**`integrity = none | size | ima | sha256`**) no `/etc/fapolicyd/fapolicyd.conf`: Impedindo Substituição de Binários Confiáveis!
- [[fapolicyd-modo-permissivo-debug-deny-testes-seguros-producao]] — Testando Políticas sem Risco de Lockout no fapolicyd: Modo **`--permissive`**, Diagnóstico **`--debug-deny`** e Interpretação dos Eventos de Negação
- [[fapolicyd-bloqueio-interpretadores-python-shell-ld-so-evasao]] — Blindando Interpretadores (**Python, Perl, Ruby, PHP, Lua, Node.js e Bash**) e Bloqueando Evasões `ld.so` / `/dev/shm` no fapolicyd
- [[fapolicyd-tuning-performance-watch-fs-q-size-caches-containers]] — Tuning de Performance do **`/etc/fapolicyd/fapolicyd.conf`**: Sistemas de Arquivos Monitorados (`watch_fs`), `ignore_mounts`, Tamanho de Fila `q_size` e Cache Hit Ratio
- [[fapolicyd-auditoria-auditd-fanotify-syslog-format-correlacao-siem]] — Correlação de Bloqueios do fapolicyd com **`auditd` (`FANOTIFY`)** e Customização do **`syslog_format`** para Detecção Imediata no SIEM
- [[fapolicyd-automacao-ansible-systemd-hardening-ciclo-vida-pacotes]] — Operação em Escala do fapolicyd com **Ansible (`rhel-system-roles.fapolicyd`)**, Integração **`dnf` / `rpm`** e Proteção do Daemon contra Parada Indevida

### YubiKey & Hardware Security Tokens (`Yubico/yubikey-manager` `ykman` & `Yubico/pam-u2f`) — FIDO2/WebAuthn Passkeys Residentes, Autenticação Linux PAM U2F (`pamu2fcfg`), PIV Smart Card X.509, OpenPGP Hardware Card e OATH/Yubico OTP

- [[yubikey-arquitetura-ykman-aplicacoes-fido2-piv-openpgp-oath-otp]] — Arquitetura da **YubiKey** e CLI Oficial **`ykman` (`Yubico/yubikey-manager`)**: Os 5 Applets Isolados em Hardware (`FIDO2`, `PIV`, `OpenPGP`, `OATH`, `OTP`) e Interfaces USB/NFC
- [[yubikey-gerenciamento-fido2-passkeys-resident-keys-pin-credenciais]] — Gerenciamento de **FIDO2 / WebAuthn e Passkeys (`Discoverable / Resident Credentials`)** na YubiKey com **`ykman fido`**
- [[yubikey-chaves-ssh-hardware-ed25519-sk-resident-verify-required]] — Chaves SSH Presas ao Hardware da YubiKey (**`ed25519-sk` e `ecdsa-sk`**): `resident`, `verify-required`, `no-touch-required` e Portabilidade com `ssh-keygen -K`
- [[yubikey-autenticacao-linux-pam-u2f-pamu2fcfg-sudo-login-ssh]] — Autenticação Linux Local e 2FA com **`pam-u2f` (`pam_u2f.so` e `pamu2fcfg`)**: Protegendo `sudo`, `gdm`/`sddm`, `polkit` e `sshd` com YubiKey FIDO2
- [[yubikey-gerenciamento-piv-smartcard-x509-slots-9a-9c-9d-9e-pkcs11]] — Smartcard X.509 (**PIV — *Personal Identity Verification* `FIPS 201`**) na YubiKey com **`ykman piv`**: Os Slots `9a`, `9c`, `9d`, `9e` e Hardening de PIN/PUK/Management Key
- [[yubikey-applet-openpgp-gpg-touch-policy-kdf-assinatura-git]] — Blindando o Applet **OpenPGP** da YubiKey com **`ykman openpgp`**: Ativando **KDF On-Card**, Touch Policy (`on` / `fixed`) para **`sig` / `enc` / `aut`** e Contadores de Tentativas
- [[yubikey-applet-oath-totp-hotp-ykman-oath-touch-password-cli]] — Gerador de Códigos **OATH-TOTP e HOTP** em Hardware com **`ykman oath`**: Aposentando Apps de Celular Vulneráveis com Proteção por Senha e Toque (`--touch`)
- [[yubikey-applet-otp-slots-challenge-response-hmac-sha1-luks-keepassxc]] — Configurando os **Slots 1 e 2 do Applet `OTP` (`ykman otp`)**: **HMAC-SHA1 Challenge-Response** para **KeePassXC e LUKS2**, Senha Estática e Yubico OTP
- [[yubikey-bloqueio-interfaces-config-lock-code-usb-nfc-enterprise]] — Hardening Corporativo da YubiKey com **`ykman config`**: Desabilitando Interfaces USB/NFC e Travando Configurações com **`--lock-code` (`Configuration Lock`)**
- [[yubikey-auditoria-atestado-fido-piv-attestation-verificacao-autenticidade]] — Verificação Criptográfica de Autenticidade e Origem de Hardware (**PIV Attestation & FIDO Attestation**) na YubiKey: Provando que uma Chave Foi Gerada *On-Chip*!

### John the Ripper Jumbo (`openwall/john`) — Auditoria de Senhas de Sistema, Utilitários `unshadow`/`*2john`, Modos `Single Crack`, `Wordlist`/Regras de Mangling, `Incremental` Markov, Expressões `PRINCE`/`Mask`, Aceleração OpenCL e `john.pot`

- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Arquitetura do **John the Ripper Jumbo (`openwall/john`)**: Autodetecção de Centenas de Hashes, CPU SIMD (`AVX2`/`AVX512`) / OpenMP / OpenCL, `john.pot` e `--restore`
- [[john-unshadow-auditoria-senhas-unix-linux-etc-passwd-shadow-crypt]] — Auditoria de Senhas Linux/UNIX com **`unshadow`** e `john`: Entendendo Hashes **`yescrypt` (`$y$`)**, **`sha512crypt` (`$6$`)**, **`bcrypt` (`$2b$`)** e Uso dos Campos GECOS
- [[john-modo-single-crack-gecos-username-sementes-mangling-rapido]] — O Poder do Modo **`"Single crack"` (`--single`)** e **`--single-seed`** no John the Ripper: Quebrando Senhas Corporativas Contextualizadas em Segundos
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Modo **`Wordlist` (`--wordlist`)** e Motor de **Regras de Mutação (`--rules` / `doc/RULES`)** no John the Ripper: `best64`, `KoreLogic`, `Jumbo` e Sintaxe de Regras
- [[john-extratores-2john-ssh2john-zip2john-keepass2john-office-pdf]] — A Suíte de Extratores **`*2john`** do John Jumbo: Auditando Chaves Privadas SSH (`ssh2john`), Cofres (`keepass2john`), Arquivos `.zip`/`.7z`/`.rar` e Documentos Office/PDF
- [[john-modos-incremental-markov-mask-subsets-entropia-baixa]] — Modos Avançados Sem Dicionário no John the Ripper: **`Incremental` (Frequência de Trigramas `.chr`)**, **`Markov`**, **`Mask` (`?u?l?l?l?d?d?d?s`)** e **`Subsets`**
- [[john-auditoria-kerberos-active-directory-krb5tgs-asrep-ntds-dit]] — Auditoria de Hashes de **Active Directory e Kerberos** no John Jumbo: **`NT` (`ntds.dit`)**, **Kerberoasting (`krb5tgs`)**, **AS-REP Roasting (`krb5asrep`)** e **`DCC2` (`mscash2`)**
- [[john-modos-externos-compilador-c-embutido-external-filter-custom]] — O Compilador C Embutido do John the Ripper (**`External Mode` — `doc/EXTERNAL`**): Escrevendo Geradores e Filtros de Candidatos (`--external`) em Subconjunto de C
- [[john-execucao-distribuida-fork-node-mpi-opencl-gpu-aceleracao]] — Escalando o John the Ripper em Múltiplos Núcleos, GPUs e Clusters: **`--fork=N`**, **`--node=MIN-MAX/TOTAL`**, OpenMP e Formatos **`-opencl`**
- [[john-expressao-dinamica-dynamic-formats-auditoria-estatisticas-relatorio]] — Formatos Dinâmicos Customizados (**`--format=dynamic=...`**) e Análise Estatística de Senhas Quebradas no John the Ripper

### Aircrack-ng Suite (`aircrack-ng/aircrack-ng`) — Auditoria de Segurança de Redes Sem Fio 802.11 (`airmon-ng`, `airodump-ng`, `aireplay-ng`, Captura de 4-Way Handshake EAPOL/PMKID, `aircrack-ng` SIMD/PBKDF2, `airdecap-ng` e WPA3-SAE)

- [[aircrack-arquitetura-suite-auditoria-wifi-80211-monitor-injection]] — Arquitetura da Suíte **Aircrack-ng (`aircrack-ng/aircrack-ng`)**: Os 4 Pilares da Auditoria de Redes Sem Fio **IEEE 802.11** (Monitoramento, Injeção, Testes de Driver e Cracking SIMD)
- [[aircrack-modo-monitor-airmon-ng-check-kill-mac80211-canais-5ghz-6ghz]] — Gerenciamento de Modo Monitor (**Monitor Mode / `rfmon`**) com **`airmon-ng`**: `check kill`, Pilha Linux `mac80211` (`nl80211`) e Canais 2.4 GHz / 5 GHz
- [[aircrack-captura-airodump-ng-bssid-essid-eapol-handshake-gpsd]] — Reconhecimento e Captura Seletiva 802.11 com **`airodump-ng`**: Bandas (`--band abg`), Filtros `--bssid` / `--essid-regex`, Quadros `PWR`/`Beacons` e `EAPOL`
- [[aircrack-injecao-pacotes-aireplay-ng-teste-driver-deauth-80211w-pmf]] — Injeção de Quadros e Teste de Resiliência **IEEE 802.11w (`PMF` — *Protected Management Frames*)** com **`aireplay-ng`**: `--test` (`-9`) e `--deauth` (`-0`)
- [[aircrack-auditoria-wpa2-psk-four-way-handshake-eapol-pbkdf2-dicionario]] — Anatomia do **4-Way Handshake EAPOL** no WPA/WPA2-PSK e Auditoria com **`aircrack-ng -w`**: `PMK`, `PTK`, `ANonce`, `SNonce`, `MIC` e Pares de Mensagens (`2+3` ou `3+4`)
- [[aircrack-precomputacao-pmk-airolib-ng-sqlite-rainbow-tables-essid]] — Pré-Computação de **Pairwise Master Keys (`PMK`)** com **`airolib-ng`** e `aircrack-ng -r`: Acelerando Auditorias em `1.000x` sobre SSIDs Padronizados
- [[aircrack-descriptografia-trafego-pcap-airdecap-ng-wpa2-wep-wireshark]] — Descriptografia de Capturas 802.11 (`.cap` / `.pcap`) com **`airdecap-ng`**: Removendo Cabeçalhos 802.11 e Decifrando Tráfego WPA/WPA2 (`CCMP`/`TKIP`) para Análise Forense
- [[aircrack-analise-grafos-airgraph-ng-relacoes-capr-cpg-clientes-probes]] — Mapeamento Visual de Relações Sem Fio com **`airgraph-ng`**: Grafos **`CAPR` (*Client to AP Relationship*)** e **`CPG` (*Common Probe Graph*)** a partir do CSV do `airodump-ng`
- [[aircrack-simulacao-rogue-ap-airbase-ng-evil-twin-karmetasploit-defesa]] — Simulação de **Rogue Access Point / Evil Twin** com **`airbase-ng`** e Detecção de Ataques de Associação Automática em Auditorias Red Team
- [[aircrack-evolucao-wpa3-sae-dragonfly-wpa2-enterprise-8021x-mitigacao]] — Do WEP (`PTW`/`KoreK`) e WPA2-PSK ao **WPA3-SAE (*Simultaneous Authentication of Equals* / Dragonfly)** e **OWE**: Por que o WPA3 Elimina o Cracking Offline de Handshakes?

### Kismet Wireless (`kismetwireless/kismet`) — Detecção de Intrusão Sem Fio (WIDS) 100% Passiva e Monitoramento RF Multi-Espectro (Wi-Fi 802.11a/b/g/n/ac/ax/be, BLE, Zigbee, RTL-SDR, Sensores Remotos, Alertas Rogue AP e `kismetdb`)

- [[kismet-arquitetura-wids-sniffer-passivo-rf-wifi-ble-sdr-datasources]] — Arquitetura do **Kismet (`kismetwireless/kismet`)**: Sistema de **Detecção de Intrusão Sem Fio (WIDS)** e Sniffer RF Passivo Multi-Protocolo (**Wi-Fi, Bluetooth/BLE, Zigbee e SDR**)
- [[kismet-configuracao-kismet-site-conf-channel-hopping-multi-radio]] — Configuração Resiliente com **`/etc/kismet/kismet_site.conf`** e Estratégia de **Channel Hopping Distribuído Multi-Rádio** no Kismet
- [[kismet-deteccao-intrusao-wids-alertas-deauth-flood-evil-twin-rogue-ap]] — Motor de **Detecção de Intrusão Sem Fio (WIDS)** do Kismet: Configurando Alertas **`apspoof` (Evil Twin / Rogue AP)**, **`DEAUTHFLOOD`**, **`CHANCONFLICT`** e **`CRYPTODROP`**
- [[kismet-sensores-remotos-kismet-cap-arquitetura-distribuida-tls]] — Arquitetura Distribuída de **Sensores Remotos (`kismet_cap_*`)** no Kismet: Monitorando Filiais, Andares e Datacenters a partir de um Único Servidor Central
- [[kismet-monitoramento-bluetooth-ble-zigbee-sdr-iot-seguranca-fisica]] — Além do Wi-Fi: Monitoramento de **Bluetooth / BLE (`kismet_cap_linux_bluetooth`)**, **Zigbee (`802.15.4`)** e **Rádio Definido por Software (`RTL-SDR`)** no Kismet
- [[kismet-formato-banco-kismetdb-sqlite3-kismetdb-to-pcap-kml-json]] — O Formato Unificado **`kismetdb` (`.kismet` SQLite3)** e os Utilitários de Extração Forense (`kismetdb_to_pcap`, `kismetdb_to_kml`, `kismetdb_dump_devices`)
- [[kismet-automacao-api-rest-websockets-alertas-tempo-real-siem-soar]] — Automação e Integração com SIEM/SOAR via **API REST e WebSockets (`.ekjson` / `.itjson`)** do Kismet: Consumindo Alertas WIDS e Handshakes em Tempo Real
- [[kismet-filtros-pacotes-privacidade-pcapng-mascaramento-compliance]] — Filtros de Captura e Conformidade de Privacidade (**LGPD / GDPR / PCI-DSS**) em WIDS com Kismet: Gravando Apenas Quadros de Gerenciamento (Sem Dados de Usuários!)
- [[kismet-seguranca-execucao-suid-grupo-kismet-privsep-api-keys]] — Arquitetura de **Privilege Separation (`privsep`)** do Kismet: Por Que o Servidor `kismet` Roda Sem Privilégios de `root` Usando Helpers SUID Restritos ao Grupo `kismet`?
- [[kismet-auditoria-pci-dss-varredura-rogue-ap-trimestral-mapeamento-gps]] — Conformidade **PCI-DSS Requisito 11.2 (Auditoria Trimestral de Rogue Wireless)** e Mapeamento de Cobertura Física (`GPS` / `KML`) com Kismet

### Scapy (`secdev/scapy`) — Construção, Dissecação, Fuzzing e Automação de Protocolos de Rede em Python (Operador de Camadas `/`, `send`/`sr1`/`srp`, Produto Cartesiano `PacketList`, `sniff`/`PcapReader`, `fuzz()`, `Automaton` e Dissecadores Customizados)

- [[scapy-arquitetura-manipulacao-pacotes-python-operador-composicao-camadas]] — Arquitetura do **Scapy (`secdev/scapy`)**: Construção e Dissecação de Pacotes de Rede em **Python**, Operador de Composição **`/`** e Sobrecarga Inteligente de Campos
- [[scapy-envio-recebimento-send-sendp-sr-sr1-srp-matching-respostas]] — A Família de Funções de Envio e Recebimento no Scapy: **`send()` vs. `sendp()`** e Pareamento Estímulo-Resposta com **`sr()`, `sr1()` e `srp()`**
- [[scapy-geracao-conjuntos-pacotes-produto-cartesiano-packetlist]] — Geração Declarativa de Conjuntos de Pacotes (**Produto Cartesiano de Campos**) e Manipulação de **`PacketList`** no Scapy
- [[scapy-captura-sniff-filtros-bpf-lfilter-prn-offline-rdpcap-wrpcap]] — Captura Programática (**`sniff()`** com `filter` BPF, `lfilter` Python e Callback `prn`) e Processamento de PCAPs em Streaming (**`PcapReader` vs. `rdpcap`**) no Scapy
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Fuzzing Inteligente de Protocolos de Rede com **`fuzz()`** e `VolatileValue` no Scapy: Testando a Robustez de Parsers, Firewalls e Regras IDS/IPS
- [[scapy-auditoria-camada-2-arp-vlan-8021q-dhcp-dai-port-security]] — Testes de Segurança de **Camada 2 (Data Link)** com Scapy: Auditoria de **Dynamic ARP Inspection (DAI)**, **802.1Q VLAN Hopping (Double Tagging)** e **DHCP Snooping**
- [[scapy-teste-evasao-fragmentacao-ip-overlap-idps-snort-suricata]] — Testando Motores de Reassemblagem de **NIDS/NIPS (Snort 3 / Suricata / Firewalls)** com **`fragment()`** e Fragmentação IP/TCP Customizada no Scapy
- [[scapy-camadas-avancadas-tls-http2-80211-dot11-iot-scada-modbus]] — Submódulos Avançados do Scapy (`load_layer` / `load_contrib`): Dissecando **TLS 1.3 (`scapy.layers.tls`)**, **HTTP/2**, **Wi-Fi `Dot11`/`RadioTap`** e **Protocolos Industriais (`modbus`, `s7comm`)**
- [[scapy-automaton-maquinas-estado-protocolos-customizados-pipes]] — Máquinas de Estado de Protocolo (**`Automaton` — `@ATMT.state`, `@ATMT.receive_condition`**) e **`Pipetool`** no Scapy: Implementando Clientes, Servidores e Honeypots
- [[scapy-definicao-protocolos-customizados-packet-fieldsdesc-dissector]] — Criando Dissecadores de **Protocolos Proprietários ou Binários Customizados** em 10 Linhas no Scapy: Subclasse **`Packet`**, **`fields_desc`** e **`bind_layers()`**

### `tcpdump` & `libpcap` (`the-tcpdump-group/tcpdump`) — Captura e Análise Forense de Pacotes com Filtragem BPF no Kernel, Aritmética de Bytes/Flags TCP, Ring Buffer de Rotação (`-C`/`-W`/`-G`), Linux `SLL2` (`-i any`), `nsenter` e Segurança (`-Z`/`-nn`)

- [[tcpdump-arquitetura-libpcap-bpf-kernel-zero-copy-af-packet]] — Arquitetura do **`tcpdump` e `libpcap` (`the-tcpdump-group/tcpdump`)**: Filtragem **BPF (*Berkeley Packet Filter*) no Kernel**, `AF_PACKET` e Flags Essenciais (`-nn`, `-i`, `-s0`, `-v`)
- [[tcpdump-primitivas-filtros-bpf-host-net-port-portrange-proto-logica]] — Dominando as Primitivas de Filtro **BPF (`pcap-filter(7)`)** no `tcpdump`: Qualificadores de Tipo (`host`, `net`, `port`, `portrange`), Direção (`src`, `dst`) e Protocolo (`tcp`, `udp`, `icmp`, `ether`)
- [[tcpdump-aritmetica-bytes-cabecalhos-tcpflags-offsets-filtros-cirurgicos]] — Filtros BPF Cirúrgicos por **Offset de Bytes (`proto[expr:size]`)** e **Flags TCP (`tcp[tcpflags]`)** no `tcpdump`: Caçando `SYN` Puros, `RST`, Scans `Xmas`/`Null` e `HTTP GET/POST`
- [[tcpdump-gravacao-rotacao-ring-buffer-pcap-c-g-w-z-pos-processamento]] — Gravação Contínua de Pacotes em Disco (**Ring Buffer de Rotação**: `-w`, `-C`, `-G`, `-W`, `-z`) e Flush Imediato (`-U` / `SIGUSR2`) no `tcpdump`
- [[tcpdump-inspecao-payload-ascii-hex-a-x-xx-linhas-buffered-l-pipes]] — Inspeção de Payload em Tempo Real (**`-A` ASCII**, **`-X` / `-XX` Hex+ASCII**) e Streaming Line-Buffered (**`-l` / `--immediate-mode`**) para Pipes Unix no `tcpdump`
- [[tcpdump-diagnostico-redes-modernas-any-vlan-vxlan-geneve-icmp-mtu]] — Diagnóstico de Redes Cloud e Containers com `tcpdump`: Interface **`-i any` (`SLL2`)**, Tags **VLAN (`vlan`)**, Túneis Overlay (**`vxlan` / `geneve`**) e Problemas de **MTU (`icmp[0] == 3 and icmp[1] == 4`)**
- [[tcpdump-captura-remota-ssh-pipes-wireshark-containers-netns-nsenter]] — Captura Remota em Tempo Real via **SSH Pipe para o Wireshark** e Inspeção de **Network Namespaces de Containers (`nsenter -t <PID> -n tcpdump`)**
- [[tcpdump-otimizacao-alta-velocidade-snaplen-s-buffer-b-timestamps-nano]] — Otimização de Captura em Alta Velocidade e Precisão de Tempo no `tcpdump`: **`snaplen` (`-s`)**, Buffer do Kernel (**`-B`**), Precisão **Nanossegundos (`--nano`)** e Bytecode **`-d`**
- [[tcpdump-seguranca-privilegios-drop-root-z-chroot-apparmor-capabilities]] — Segurança Operacional do Próprio `tcpdump`: Abandono de Privilégios (**`-Z user`**), Linux Capabilities (**`cap_net_raw,cap_net_admin`**), Perfis **AppArmor** e Flag **`-n` ao Ler PCAPs**
- [[tcpdump-descriptografia-ipsec-esp-assinatura-tcp-md5-forense-tcpslice]] — Recursos Forenses Avançados do `tcpdump`: Descriptografia de **IPsec ESP (`-E spi@ip algo:secret`)**, Verificação **TCP-MD5 (`-M`)**, Lista de Arquivos (**`-V`**) e **`tcpslice`**

## Tranche 16 (IDs 1501–1600)

### Greenbone Vulnerability Management & OpenVAS (`greenbone/openvas-scanner` & `gvmd`) — Arquitetura GMP/OSP, Feeds NVT/SCAP/CERT, Varreduras Autenticadas (`notus-scanner`), NASL, QoD e Sensores Distribuídos `openvasd`

- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Arquitetura do **Greenbone Vulnerability Management (GVM / OpenVAS)**: **`gvmd` (`GMP`)**, **`ospd-openvas` (`OSP`)**, **`openvas-scanner`**, **`notus-scanner`** e PostgreSQL/Redis
- [[openvas-sincronizacao-feeds-greenbone-nvt-scap-cert-gvmd-data]] — Sincronização dos Feeds de Inteligência do Greenbone (**`greenbone-feed-sync`**): **NVTs (NASL)**, **SCAP (`CVE` / `CPE`)**, **CERT (`DFN-CERT`)** e **`GVMD_DATA`**
- [[openvas-configuracao-alvos-targets-port-lists-alive-test-credenciais]] — Configuração de **Targets, Port Lists e `Alive Test`** no Greenbone/OpenVAS: Evitando Falsos Negativos em Hosts com Firewall que Bloqueia `ICMP Echo`
- [[openvas-varredura-autenticada-ssh-smb-esxi-snmp-notus-scanner]] — Varreduras Autenticadas (**Authenticated Scans — SSH, SMB/WMI, ESXi e SNMP**) e o Motor **`notus-scanner`** no Greenbone/OpenVAS
- [[openvas-perfis-varredura-full-and-fast-cve-scan-matching-version]] — Perfis de Varredura (**`Full and fast`**, **`Host Discovery`**, **`System Discovery`**) e o **`CVE Scan` (`cve_scan_matching_version`)** no `gvmd`
- [[openvas-protocolos-gmp-osp-automacao-gvm-cli-python-gvm-cicd]] — Automação do Greenbone com **`gvm-cli`**, **`python-gvm`** e Protocolo **GMP (`Greenbone Management Protocol`)** sobre Unix Socket / TLS
- [[openvas-linguagem-nasl-scripts-nvt-openvas-nasl-execucao-isolada]] — Anatomia dos Testes de Vulnerabilidade **NASL (*Network Attack Scripting Language*)** e Execução Isolada de Debug com **`openvas-nasl`**
- [[openvas-gestao-resultados-qod-quality-of-detection-overrides-false-positives]] — Triagem de Resultados no Greenbone: **QoD (*Quality of Detection* — `70%` Default)**, **Notes**, **Overrides** e Filtragem de Falsos Positivos
- [[openvas-tuning-performance-max-checks-max-hosts-redis-memoria-redes]] — Tuning de Performance e Concorrência no OpenVAS (**`max_hosts`**, **`max_checks`**, **`time_between_request`**) para Não Derrubar Redes ou Alvos Frágeis
- [[openvas-arquitetura-distribuida-scanners-remotos-osp-rust-openvasd]] — Arquitetura Distribuída com **Scanners Remotos (`OSP` sobre mTLS)** e o Novo Motor em Rust (**`openvasd`**) em Containers (`ghcr.io/greenbone`)

### OWASP Dependency-Check (`dependency-check/DependencyCheck`) — Software Composition Analysis (SCA), Coleta de Evidências (`vendor`/`product`/`version`), Índice Lucene CPE, API NVD v2, Supressões XML e Sonatype Guide

- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Arquitetura do **OWASP Dependency-Check (`dependency-check`)**: Coleta de Evidências (`vendor`, `product`, `version`), Índice **Lucene CPE** e Níveis de Confiança
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Integração com a **API v2 do NIST NVD (`--nvdApiKey`)**, Cache de Banco **H2** e Estratégia de Espelhamento em CI/CD no OWASP Dependency-Check
- [[depcheck-analisadores-ecossistemas-jar-dotnet-npm-golang-python-experimental]] — Analisadores Multi-Linguagem do OWASP Dependency-Check: **Java (`JarAnalyzer` / Maven / Gradle)**, **.NET 8**, **Go (`go.mod`)**, **Node.js (`npm audit`)**, **Ruby (`bundle-audit`)** e **Elixir (`mix_audit`)**
- [[depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline]] — Plugins Nativos **Maven (`dependency-check-maven`)** e **Gradle (`org.owasp.dependencycheck`)**: Goal **`aggregate`** e Quality Gate **`failBuildOnCVSS`**
- [[depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl]] — Triagem e Supressão Auditável de Falsos Positivos no OWASP Dependency-Check: Arquivo **`suppressions.xml` (`--suppression`)**, `packageUrl`, `cpe`, `cve` e `until`
- [[depcheck-integracao-sonatype-oss-index-sonatype-guide-autenticacao]] — Enriquecimento de Análise com **Sonatype OSS Index / Sonatype Guide** e **CISA Known Exploited Vulnerabilities (`KEV`)** no OWASP Dependency-Check
- [[depcheck-analise-javascript-retirejs-npm-audit-yarn-pnpm-lockfiles]] — Auditoria de Dependências Frontend e Node.js no OWASP Dependency-Check: **`RetireJS Analyzer`**, `package-lock.json`, `pnpm-lock.yaml` e `yarn.lock`
- [[depcheck-execucao-offline-air-gapped-espaco-corporativo-central-db]] — Operando o OWASP Dependency-Check em Ambientes **Air-Gapped (Redes Isoladas)** ou com **Banco de Dados Central PostgreSQL / MySQL / MS SQL**
- [[depcheck-formatos-relatorio-sarif-junit-json-gitlab-defectdojo-github]] — Integração de Relatórios do OWASP Dependency-Check (`SARIF`, `JUnit`, `JSON`, `HTML`, `CSV`, `XML`) com **GitHub Code Scanning, GitLab e OWASP DefectDojo**
- [[depcheck-comparativo-dependency-check-vs-dependency-track-osv-scanner-sbom]] — Arquitetura Comparada de SCA: Quando Usar **OWASP Dependency-Check** vs. **OWASP Dependency-Track (SBOM CycloneDX)** vs. **OSV-Scanner / `pip-audit` / `govulncheck`**

### AFL++ (`AFLplusplus/AFLplusplus` — American Fuzzy Lop Plus Plus) — Coverage-Guided Fuzzing, Instrumentação `afl-clang-lto`, `CMPLOG` Redqueen, Persistent Mode (`LLVMFuzzerTestOneInput`), Sanitizers (`ASAN`/`UBSAN`) e `FRIDA`/`QEMU` Mode

- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Arquitetura do **AFL++ (`AFLplusplus/AFLplusplus`)**: Fuzzing Guiado por Cobertura (*Coverage-Guided Greybox Fuzzing*), Compilador **`afl-cc`** e Modos **`LTO` (`afl-clang-lto`)**, **`LLVM`** e **`GCC_PLUGIN`**
- [[aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva]] — Superando Magic Bytes e Checksums no AFL++: **`AFL_LLVM_CMPLOG=1` (*Redqueen / Input-to-State*)**, **`AFL_LLVM_LAF_ALL=1`** e Instrumentação Seletiva (**`AFL_LLVM_ALLOWLIST`**)
- [[aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver]] — Multiplicando a Velocidade em 20x no AFL++: **Persistent Mode (`__AFL_LOOP` / `LLVMFuzzerTestOneInput`)**, Memória Compartilhada (**`__AFL_INIT`**) e **Deferred Forkserver**
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Potencializando a Detecção de Bugs Silenciosos no AFL++ com Sanitizers: **`AFL_USE_ASAN=1` (AddressSanitizer)**, **`AFL_USE_UBSAN=1`**, **`AFL_USE_CFISAN=1`** e **`AFL_USE_MSAN=1`**
- [[aflplusplus-engenharia-corpus-sementes-afl-cmin-afl-tmin-dicionarios]] — Engenharia e Minimização de Corpus no AFL++: Destilação de Conjunto (**`afl-cmin`**), Minimização de Arquivo (**`afl-tmin`**) e Dicionários de Tokens (**`-x`** / **`AUTODICT`**)
- [[aflplusplus-campanhas-paralelas-multicore-master-secondary-sync]] — Escalando Campanhas Multicore no AFL++ (`-M` Principal e `-S` Secundários): Diversificando Estratégias (**`MOpt` `-L 0`**, **Power Schedules `-p`**, **`CMPLOG`** e **`ASAN`**)
- [[aflplusplus-fuzzing-binarios-fechados-frida-mode-qemu-unicorn-nyx]] — Fuzzing de Binários Sem Código-Fonte (**Binary-Only Targets**) no AFL++: **FRIDA Mode (`-O`)**, **QEMU Mode (`-Q`)**, **Unicorn Mode (`-U`)** e **Nyx Full-System (`-X`)**
- [[aflplusplus-custom-mutators-python-c-libprotobuf-mutator-structure-aware]] — Fuzzing Consciente de Estrutura (**Structure-Aware / Grammar Fuzzing**) no AFL++: **Custom Mutators em C e Python (`AFL_CUSTOM_MUTATOR_LIBRARY` / `PYTHONPATH`)**
- [[aflplusplus-fuzzing-servicos-rede-desocketing-preeny-afl-network-proxy]] — Como Fazer Fuzzing de **Servidores de Rede (TCP/UDP Sockets)** no AFL++: *Desocketing* com `LD_PRELOAD` (`libdesock`), Persistent Harness e Isolamento de Estado
- [[aflplusplus-triagem-crashes-reproducao-gdb-pwndbg-cov-analysis-lcov]] — Triagem de Crashes (`out/default/crashes/`), Análise de Cobertura de Código (**`AFLplusplus/cov-analysis` / `llvm-cov`**) e Reprodução no **GDB / Pwndbg**

### Valgrind (`valgrind.org` — `Memcheck`, `Helgrind`, `DRD`, `Massif`, `DHAT`) — Instrumentação Binária Dinâmica via VEX IR, Bits `V`/`A` de Memória Sombra, Detecção de Memory Leaks, `vgdb`, Client Requests e Data Races

- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Arquitetura do **Valgrind (`valgrind 3.27+`)** e do Motor **Memcheck**: Instrumentação Dinâmica via **VEX IR** e Máquina de Sombra de Bits **`V` (*Valid-Value*)** e **`A` (*Valid-Address*)**
- [[valgrind-erros-memcheck-invalid-read-write-uninitialised-track-origins]] — Interpretando Erros Críticos do **Memcheck**: `Invalid read/write`, `Use of uninitialised value` (**`--track-origins=yes`**), `Syscall param` e `Invalid free()` / `Mismatched free()`
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Taxonomia de Vazamentos de Memória (**Memory Leaks**) no Valgrind Memcheck: **`definitely lost`**, **`indirectly lost`**, **`possibly lost`** e **`still reachable`**
- [[valgrind-arquivos-supressao-gen-suppressions-ci-cd-bibliotecas-terceiros]] — Gerenciando Falsos Positivos de Bibliotecas de Terceiros no Valgrind com **Suppression Files (`--gen-suppressions=all` e `--suppressions=arquivo.supp`)**
- [[valgrind-inspecao-interativa-vgdb-gdbserver-monitor-commands-leak-check]] — Inspeção de Vazamentos e Memória **Em Tempo Real (Sem Parar o Daemon)** no Valgrind via **`vgdb`** e **GDB Remote Monitor (`--vgdb=yes`)**
- [[valgrind-client-requests-custom-allocators-mempool-valgrind-h-redzones]] — Auditando **Alocadores Customizados de Memória (Memory Pools / Arenas)** com as Macros **Client Request (`<valgrind/memcheck.h>`)** do Valgrind
- [[valgrind-concorrencia-data-races-deadlocks-helgrind-drd-pthreads]] — Caçando **Race Conditions (*Data Races*)** e **Deadlocks** em Programas Multithreaded C/C++ com **`--tool=helgrind`** e **`--tool=drd`** no Valgrind
- [[valgrind-deteccao-overflow-stack-globais-exp-sgcheck-limites]] — Limitações Arquiteturais do Memcheck em **Arrays de Stack/Globais** e Como Auditar Overflows de Stack com **`exp-sgcheck` / AddressSanitizer**
- [[valgrind-perfilamento-heap-massif-dhat-otimizacao-memoria-dos]] — Investigando **Negação de Serviço por Exaustão de Memória (Memory DoS)** e Uso de Heap com **`--tool=massif` (`ms_print`)** e **`--tool=dhat`** no Valgrind
- [[valgrind-auditoria-daemons-fork-trace-children-file-descriptors-fds]] — Auditando Daemons Complexos no Valgrind: Seguindo Processos Filhos (**`--trace-children=yes`**), Vazamento de **File Descriptors (`--track-fds=yes`)** e Logs XML para CI

### Sliver C2 (`BishopFox/sliver`) — Framework Open-Source de Emulação de Adversários e Red Team em Go, Canais C2 (`mTLS`, `WireGuard`, `HTTP(S)`, `DNS`), Modos `Beacon` vs. `Session`, BOF/COFF In-Memory, Pivoting e Detecção Blue Team

- [[sliver-arquitetura-c2-emulacao-adversarios-mtls-wireguard-http-dns]] — Arquitetura do **Sliver C2 (`BishopFox/sliver`)**: Emulação de Adversários Multi-Plataforma em Go, Chaves Assimétricas por Binário e Protocolos **mTLS, WireGuard, HTTP(S) e DNS**
- [[sliver-modos-operacao-beacon-assincrono-jitter-vs-session-interativa]] — Implantes Sliver: **Beacon Mode (Assíncrono com Intervalo + Jitter)** vs. **Session Mode (Tempo Real)** e Promoção On-Demand com **`interactive`**
- [[sliver-protocolos-transporte-mtls-wireguard-https-dns-traffic-encoders]] — Engenharia dos 4 Canais de Transporte C2 do Sliver (**`mtls`**, **`wg` WireGuard**, **`https` C2 Profiles** e **`dns` Canário**) e **Traffic Encoders (Wasm)**
- [[sliver-modo-multiplayer-operadores-grpc-mtls-rbac-auditoria-logs]] — Operação em Equipe (**Multiplayer Mode** sobre gRPC mTLS), Gerenciamento de Operadores (**`new-operator`**) e **Audit Log JSON** Completo para Purple Team no Sliver
- [[sliver-execucao-em-memoria-bof-coff-execute-assembly-sideload-spawndll]] — Pós-Exploração *In-Memory* no Sliver: **BOF / COFF Loader (`Armory`)**, **`execute-assembly` (.NET CLR)**, **`sideload`** e **`spawndll`** sem Tocar o Disco
- [[sliver-pivoting-portfwd-socks5-pivots-named-pipes-tcp-interno]] — Pivoting e Movimentação Lateral no Sliver: **`socks5` In-Memory**, **`portfwd`**, **`rportfwd`** e **Internal Peer-to-Peer Pivots (`pivots named-pipe` / `tcp`)**
- [[sliver-compilacao-ofuscacao-garble-stagers-shellcode-external-builders]] — Compilação Avançada de Implantes no Sliver: Ofuscação de Símbolos (**`garble`**), Formatos (`executable`, `shared-lib`, `service`, `shellcode`), **Stagers** e **External Builders**
- [[sliver-monitoramento-credenciais-loot-watchtower-canary-domains]] — Gestão de Credenciais (**`loot`**), Monitoramento Contínuo de Vazamento de Implantes (**`Watchtower` — VirusTotal / XForce**) e **Canary Domains** no Sliver
- [[sliver-extensao-cursed-chrome-electron-debug-port-post-exploitation]] — Pós-Exploração de Navegadores e Apps **Electron (`Slack`, `VS Code`, `Teams`, `Discord`)** com o Subsistema **`cursed`** do Sliver
- [[sliver-deteccao-defesa-blue-team-ja3-jarm-rita-yara-memory-scanning]] — Engenharia de Detecção (**Blue Team / SOC / NSM**) Contra Implantes **Sliver C2**: Assinaturas **JARM/JA4 TLS**, Caça a Beacons no **RITA/Zeek** e **YARA em Memória**

### Chisel (`jpillora/chisel`) — Tunelamento Rápido TCP/UDP sobre HTTP/WebSockets Criptografado via SSH (`crypto/ssh`), Pinning `--fingerprint`, Controle `--authfile`, Reverse Port Forwarding (`R:socks`), `--backend` e Detecção NIDS

- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Arquitetura do **Chisel (`jpillora/chisel`)**: Tunelamento Rápido **TCP e UDP** Encapsulado sobre **HTTP / WebSockets** e Criptografado via **SSH (`crypto/ssh`)**
- [[chisel-autenticacao-seguranca-keygen-keyfile-fingerprint-authfile-regex]] — Blindando o Chisel Contra MITM e Acesso Não Autorizado: **`--keygen` / `--keyfile`**, Pinning de **`--fingerprint`** e Controle de Acesso **`--authfile` (`users.json`)**
- [[chisel-encaminhamento-portas-forward-reverse-r-socks5-udp]] — Sintaxe Completa de `<remote>` no Chisel: Tunelamento **Local (Forward)**, **Reverso (`R:`)**, **Proxy Dinâmico `SOCKS5` (`--socks5` / `R:socks`)** e **Túneis `UDP` (`/udp`)**
- [[chisel-camuflagem-reverse-proxy-backend-tls-letsencrypt-headers]] — Camuflagem HTTP (**`--backend` Reverse Proxy**), TLS Nativo (**`--tls-domain` Let's Encrypt / `--tls-cert`**) e Customização de **`--header` / `Host`** no Chisel
- [[chisel-atravessando-proxies-corporativos-socks-http-connect-stdio-ssh]] — Atravessando Proxies de Saída Corporativos (**`--proxy` HTTP CONNECT / SOCKS5**) e **SSH sobre HTTP (`stdio:` + `ssh -o ProxyCommand`)** com o Chisel
- [[chisel-operacao-sinais-unix-sigusr2-sighup-sigint-tuning-keepalive]] — Operação e Diagnóstico em Tempo de Execução no Chisel: Sinais Unix (**`SIGUSR2` Stats**, **`SIGHUP` Reconnect**, **`SIGINT`/`SIGTERM`**) e Tuning de Backoff
- [[chisel-encadeamento-multi-hop-double-pivoting-proxychains-ng-nmap]] — Double Pivoting (Encadeamento Multi-Hop de Túneis Chisel) e Integração com **`proxychains4` (`proxychains-ng`)** para Segmentos Isolados
- [[chisel-uso-defensivo-acesso-remoto-zero-trust-containers-k8s-dev]] — Uso Legítimo de Engenharia e DevSecOps do Chisel: Túneis Seguros de Diagnóstico em **Containers (`ghcr.io/jpillora/chisel`)** e Ambientes Cloud
- [[chisel-tunelamento-udp-dns-snmp-wireguard-over-chisel-tcp]] — Tunelamento de Protocolos **UDP (`<remote>/udp`)** no Chisel: Encapsulando Consultas **DNS (`53/udp`)**, **SNMP (`161/udp`)** ou **WireGuard** sobre HTTP/WebSockets
- [[chisel-deteccao-forense-blue-team-websocket-ssh-banner-rita-suricata]] — Engenharia de Detecção (**Blue Team / SOC / NIDS**) Contra Túneis **Chisel**: Handshake **WebSocket (`Sec-WebSocket-Protocol: chisel-v3`)**, Banner SSH Interno e **Long Connections**

### Ligolo-ng (`nicocha30/ligolo-ng`) — Pivoting e Tunelamento Avançado de Camada 3 via Interface `TUN` e Pilha Userland Google `gVisor`, Roteamento Automático (`autoroute`), IP Mágico `240.0.0.1`, Listeners Reversos e Multi-Hop

- [[ligolo-arquitetura-tunelamento-camada-3-tun-gvisor-sem-socks]] — Arquitetura do **Ligolo-ng (`nicocha30/ligolo-ng`)**: Tunelamento de **Camada 3 (VPN-like)** com Interface **`TUN`** no Proxy e Pilha TCP/IP Userland (**Google `gVisor`**) no Agente
- [[ligolo-configuracao-tls-autocert-selfcert-fingerprint-pinning]] — Segurança Criptográfica do Túnel Ligolo-ng: **Let's Encrypt (`-autocert`)**, Certificados Próprios (`-certfile`) e Pinning de **SHA-256 Fingerprint (`-selfcert` + `-accept-fingerprint`)**
- [[ligolo-operacao-sessoes-ifconfig-autoroute-interface-create-tun]] — Fluxo Operacional Completo no Console do Ligolo-ng (`v0.6+` / `v0.8+`): **`session`**, **`ifconfig`**, **`interface_create`**, **`interface_add_route`** e **`tunnel_start`**
- [[ligolo-acesso-ip-local-agente-magic-cidr-240-0-0-1-loopback]] — Acessando Serviços em **`127.0.0.1` (`localhost`)** da Própria Máquina do Agente via Ligolo-ng: O Endereço Mágico **`240.0.0.1`**
- [[ligolo-port-forwarding-reverso-listeners-agent-bind-transferencia]] — Listeners e Port Forwarding Reverso no Ligolo-ng (**`listener_add`**, **`listener_list`**): Recebendo Conexões e Implantes da Rede Interna Isolada
- [[ligolo-boas-praticas-nmap-unprivileged-pe-traducao-syn-connect-gvisor]] — Por Que Usar **`nmap --unprivileged`** (ou `-sT -Pn`) Através do Ligolo-ng? Entendendo a Tradução de Pacotes `SYN` e `ICMP` no `gVisor` do Agente
- [[ligolo-transporte-websocket-socks-proxy-saida-corporativo-bind-mode]] — Atravessando Proxies Corporativos e Firewalls no Ligolo-ng: **Suporte a WebSockets (`ws://` / `wss://`)**, Proxy de Saída (**`--socks`**) e **Modo Bind**
- [[ligolo-multiplos-tuneis-simultaneos-segmentacao-interfaces-tun-paralelas]] — Operando **Múltiplos Túneis Simultâneos** para Diferentes Sub-Redes no Ligolo-ng: Uma Interface **`TUN`** Dedicada por Agente
- [[ligolo-auditoria-active-directory-impacket-netexec-certipy-bloodhound-tun]] — Executando Ferramentas de Auditoria **Active Directory (`NetExec`, `Impacket`, `Certipy`, `BloodHound CE`, `Responder`)** Nativamente sobre a Interface `TUN` do Ligolo-ng
- [[ligolo-deteccao-defesa-blue-team-certificado-padrao-yamux-gvisor-edr]] — Engenharia de Detecção (**Blue Team / SOC / NSM / EDR**) Contra o **Ligolo-ng**: Certificado TLS Default (`ligolo`), Multiplexador **`hashicorp/yamux`** e Telemetria de Processo

### THC-Hydra (`vanhauser-thc/thc-hydra`) — Auditoria Paralelizada de Autenticação de Rede em 50+ Protocolos, Password Spraying (`-u`), Verificações `-e nsr`, Formulários Web (`http-post-form`), `pw-inspector` e Validação de `Fail2ban`/`pam_faillock`

- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Arquitetura do **THC-Hydra (`vanhauser-thc/thc-hydra`)**: Auditoria Paralelizada de Autenticação de Rede em Mais de 50 Protocolos (`SSH`, `RDP`, `SMB`, `HTTP-Form`, `LDAP`, `PostgreSQL`, `MySQL`, `SNMP`)
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Modos de Credenciais no THC-Hydra: **Password Spraying (`-u` Loop Around Users)**, Pares `login:pass` (**`-C`**), Verificações Extras (**`-e nsr`**) e Parada Imediata (**`-f` / `-F`**)
- [[thc-hydra-auditoria-formularios-web-http-post-form-get-form-cookies]] — Auditando Formulários de Login Web e APIs com **`http-post-form` / `https-post-form`** no THC-Hydra: Sintaxe `"caminho:corpo:condicao"`, `F=` vs. `S=` e Headers `H=`
- [[thc-hydra-controle-concorrencia-tasks-t-timeouts-w-restore-sessao-r]] — Controle de Concorrência (**`-t` vs. `-T`**), Pausa Entre Tentativas (**`-W` / `-c`**), Retomada de Sessão (**`-R` `hydra.restore`**) e Saída JSON (**`-b json -o`**) no THC-Hydra
- [[thc-hydra-auditoria-bancos-dados-postgres-mysql-mssql-redis-mongodb]] — Auditando Autenticação de Bancos de Dados (**PostgreSQL, MySQL/MariaDB, MS-SQL, Redis, MongoDB e Oracle**) com o THC-Hydra
- [[thc-hydra-auditoria-protocolos-infraestrutura-ssh-sshkey-rdp-smb-snmp]] — Auditando Protocolos de Infraestrutura e Gerência no THC-Hydra: **`ssh` / `sshkey`**, **`rdp`**, **`smb`**, **`snmp` (Community Strings v1/v2c/v3)** e **`cisco-enable`**
- [[thc-hydra-geracao-bruteforce-x-charset-pw-inspector-filtragem-wordlists]] — Geração On-the-Fly (**`-x min:max:charset`**) e Filtragem de Wordlists por Política de Senha com o Utilitário **`pw-inspector`** do THC-Hydra
- [[thc-hydra-auditoria-email-diretorio-smtp-enum-imap-pop3-ldap-tls]] — Auditando Serviços de E-mail e Diretório no THC-Hydra: Enumeração de Contas **`smtp-enum` (`VRFY`/`EXPN`/`RCPT TO`)**, **`smtp`**, **`imap`/`pop3`** e **`ldap3` (`-S` LDAPS)**
- [[thc-hydra-validacao-controles-defensivos-fail2ban-crowdsec-waf-pam]] — Usando o THC-Hydra em **Purple Team e Engenharia de Confiabilidade de Segurança** para Validar Regras do **Fail2ban, CrowdSec, WAF (Coraza/ModSecurity) e `pam_faillock`**
- [[thc-hydra-deteccao-forense-redes-user-agent-padrao-conexoes-suricata-zeek]] — Engenharia de Detecção (**Blue Team / SOC / NIDS / SIEM**) Contra Ataques do **THC-Hydra**: `User-Agent` Default (`Mozilla/4.0 (Hydra)`), Padrões de Conexão e Correlação

### `pip-audit` & PyPA Advisory Database (`pypa/pip-audit` & `pypa/advisory-database`) — Auditoria Oficial de Vulnerabilidades Python, Serviços PyPI/OSV, Modo `--require-hashes`/`--disable-pip`, `--fix`, SBOM CycloneDX e `ecosystem_specific.imports`

- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Arquitetura do **`pip-audit` (`pypa/pip-audit`)** e **Python Packaging Advisory Database (`pypa/advisory-database`)**: Serviços **`pypi`** vs. **`osv`** e Reuso do Cache do `pip`
- [[pip-audit-modos-varredura-requirements-pyproject-locked-local-venv]] — Auditando Ambientes Virtuais (`-l`), Arquivos `requirements.txt` (`-r`) e Lockfiles de Projetos (`pyproject.toml` / `pylock.*.toml` `--locked`) no `pip-audit`
- [[pip-audit-remediacao-automatica-fix-dry-run-require-hashes-no-deps]] — Correção Automática de Dependências Vulneráveis (**`--fix`** e **`--fix --dry-run`**) e Auditoria Reprodutível com Hashes (**`--require-hashes` / `--no-deps` / `--disable-pip`**) no `pip-audit`
- [[pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo]] — O Modelo de Segurança do `pip-audit` (**Security Model**): Por Que Auditar `requirements.txt` Não-Pinados Pode Executar `setup.py` e Como Prevenir com `--require-hashes`
- [[pip-audit-geracao-sbom-cyclonedx-json-xml-formatos-markdown-sarif]] — Geração Nativa de **SBOM CycloneDX (`-f cyclonedx-json` / `cyclonedx-xml`)**, Relatórios **Markdown (`-f markdown`)** e **JSON** no `pip-audit`
- [[pip-audit-excecoes-ignore-vuln-governanca-supressao-exit-codes]] — Governança de Exceções no `pip-audit`: Ignorando Vulnerabilidades Específicas (**`--ignore-vuln PYSEC-...`**) e Tratamento de Exit Codes em CI/CD
- [[pip-audit-indices-privados-index-url-extra-index-url-cache-offline]] — Usando o `pip-audit` com **Repositórios PyPI Privados (`--index-url` / `--extra-index-url`)**, Autenticação `keyring` e Cache HTTP (`--cache-dir`)
- [[pip-audit-integracao-pre-commit-github-actions-gh-action-pip-audit]] — Automação Shift-Left do `pip-audit`: Hook Oficial **`pre-commit`** e GitHub Action Oficial (**`pypa/gh-action-pip-audit`**)
- [[pip-audit-anatomia-pypa-advisory-database-osv-schema-imports]] — Anatomia da Base **`pypa/advisory-database`**: Formato **OpenSSF OSV YAML (`PYSEC-*`)**, Validação `check-jsonschema` e **`ecosystem_specific.imports`**
- [[pip-audit-auditoria-containers-python-multistage-path-site-packages]] — Auditando **Containers Python Distroless e Multi-Stage Builds** com `pip-audit`: Usando a Flag **`--path` (`site-packages`)** sem Instalar o `pip-audit` na Imagem Final

### Go Vulnerability Management (`golang/vuln` — `govulncheck` & `vuln.go.dev`) — Análise Estática de Alcançabilidade por Grafo de Chamadas (Call Graph Reachability), Auditoria de Binários (`-mode binary`/`extract`), `OpenVEX`/`SARIF` e API `vuln/scan`

- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Arquitetura do **`govulncheck` (`golang.org/x/vuln/cmd/govulncheck`)**: Análise Estática de Alcançabilidade (**Call Graph Reachability**) e Base **`vuln.go.dev`**
- [[govulncheck-interpretacao-relatorio-call-stacks-show-traces-verbose]] — Interpretando Pilhas de Chamadas (**Call Stacks**) no `govulncheck`: Vulnerabilidades **Chamadas (`Called`) vs. Apenas Importadas**, **`-show traces`** e **`-show verbose`**
- [[govulncheck-auditoria-binarios-compilados-mode-binary-mode-extract]] — Auditando **Binários Go Compilados (`-mode binary`)** e Extração de Blobs Leves (**`-mode extract`**) para Containers e Imagens em Produção com o `govulncheck`
- [[govulncheck-formatos-integracao-sarif-openvex-json-streaming-ci-cd]] — Exportando **`SARIF` (`-format sarif`)**, **`OpenVEX` (`-format openvex`)** e **Streaming `JSON` (`-format json`)** no `govulncheck` e o Comportamento de Exit Codes
- [[govulncheck-banco-dados-customizado-db-espelho-local-air-gapped-privacy]] — Operando o `govulncheck` Offline (**Air-Gapped**) ou com Mirror Corporativo via Flag **`-db`**: Arquitetura do Go Vulnerability Database (`vuln.go.dev`)
- [[govulncheck-limitacoes-analise-estatica-reflect-unsafe-stripped-binaries]] — Limitações Conhecidas da Análise Estática do `govulncheck`: Ponteiros de Função/Interfaces, Pacotes **`reflect`** e **`unsafe`**, Go < 1.18 e Binários *Stripped*
- [[govulncheck-api-programatica-golang-org-x-vuln-scan-automacao-customizada]] — Usando o `govulncheck` como Biblioteca em Go (**`golang.org/x/vuln/scan`**): Construindo Ferramentas Internas de Segurança e Scanners de Plataforma
- [[govulncheck-remediacao-go-get-upgrade-go-mod-tidy-stdlib-toolchain]] — Fluxo de Remediação de Vulnerabilidades Detectadas pelo `govulncheck`: Atualizando Módulos (**`go get pac@vX.Y.Z`**), **`go mod tidy`** e Toolchain **`go` (`stdlib`)**
- [[govulncheck-triagem-json-jq-distincao-modulo-pacote-simbolo-ci-gate]] — Filtrando e Automatizando Quality Gates com `govulncheck -format json` e `jq`: Distinguindo Achados de **Nível de Símbolo (`function`)** vs. **Nível de Módulo**
- [[govulncheck-pipeline-devsecops-go-completo-gosec-govulncheck-syft-cosign]] — Arquitetura de Referência DevSecOps para **Go (`golang`)**: Combinando **`gosec` (SAST)**, **`govulncheck` (Reachable SCA)**, **`Syft` (SBOM)** e **`Cosign` (Assinatura Sigstore)**

## Tranche 17 (IDs 1601–1700)

### RustSec `cargo-audit` — consulta do `Cargo.lock` à base de advisories, auditoria de binários, exceções e uso seguro em CI

- [[cargo-audit-fluxo-cargo-lock-rustsec-advisory-db]] — `cargo-audit`: fluxo entre `Cargo.lock`, RustSec Advisory Database e achados por versão
- [[cargo-audit-identificadores-rustsec-faixas-versoes-triagem]] — Triagem de achados `RUSTSEC-*`: identificador, faixa afetada e versão de correção
- [[cargo-audit-lockfile-ausente-risco-cargo-update-projeto-nao-confiavel]] — `cargo-audit` e projeto sem `Cargo.lock`: por que evitar comandos Cargo em código não confiável
- [[cargo-audit-opcao-file-lockfile-externo-reproducibilidade]] — `cargo audit --file`: auditar um `Cargo.lock` externo sem entrar no workspace
- [[cargo-audit-ignorar-advisory-justificativa-expiracao]] — Ignorar um advisory em `cargo-audit`: exceção rastreável, justificativa e reavaliação
- [[cargo-audit-config-audittoml-controle-versao-excecoes]] — `audit.toml` versionado: governança das exceções locais do `cargo-audit`
- [[cargo-audit-bin-inventario-dependencias-binario-rust]] — `cargo audit bin`: leitura de dependências em binários Rust distribuídos
- [[cargo-auditable-metadados-embed-binario-limites]] — `cargo auditable`: metadados embutidos e limites da auditoria de binários Rust
- [[cargo-audit-fix-dry-run-remediacao-experimental]] — `cargo audit fix --dry-run`: avaliar remediação antes de alterar dependências
- [[cargo-audit-ci-audit-check-agendamento-falha]] — `cargo-audit` em CI: política de falha, atualização da base e trilha do relatório

### `cargo-deny` — checks de advisories, licenças SPDX, dependências banidas, versões duplicadas e fontes de crates

- [[cargo-deny-checks-grafo-dependencias-rust-configuracao]] — `cargo-deny`: checks declarativos sobre o grafo de dependências Cargo
- [[cargo-deny-advisory-db-rustsec-atualizacao-offline]] — `cargo-deny check advisories`: fonte RustSec, cache local e atualidade dos dados
- [[cargo-deny-ignores-advisory-expiry-reason-escopo]] — Exceções em `[advisories]`: ID, motivo, escopo e expiração
- [[cargo-deny-yanked-unmaintained-unsound-advisories]] — Separar vulnerabilidade, crate `yanked`, descontinuidade e advisory de soundness
- [[cargo-deny-licencas-spdx-allowlist-exceptions]] — Política de licenças em `cargo-deny`: expressões SPDX e exceções explícitas
- [[cargo-deny-license-clarifications-hash-confidence]] — Clarificações de licença no `cargo-deny`: expressão, arquivo e hash
- [[cargo-deny-bans-versoes-duplicadas-dependencias-proibidas]] — `[bans]` no `cargo-deny`: dependências proibidas e versões múltiplas
- [[cargo-deny-sources-registries-git-allowlist]] — `[sources]` no `cargo-deny`: limitar registries e dependências Git
- [[cargo-deny-target-features-grafo-resolucao-reprodutivel]] — Alvos e features na policy do `cargo-deny`: auditar o grafo que realmente será compilado
- [[cargo-deny-github-action-ci-review-policy]] — Executar `cargo-deny` em CI: configuração como código e feedback de pull request

### Mozilla `cargo-vet` — auditoria humana diferencial de crates, critérios de segurança, imports confiáveis e exemptions

- [[cargo-vet-modelo-auditoria-terceiros-criterios-rust]] — `cargo-vet`: registrar auditorias de código Rust de terceiros junto ao projeto
- [[cargo-vet-init-supply-chain-exemptions-iniciais]] — `cargo vet init`: inicializar supply chain sem confundir exemptions com auditorias
- [[cargo-vet-check-novas-dependencias-gate-ci]] — `cargo vet check`: detectar código de terceiro novo no grafo de build
- [[cargo-vet-criteria-safe-to-run-safe-to-deploy]] — Critérios do `cargo-vet`: definir o que uma auditoria precisa demonstrar
- [[cargo-vet-differential-audit-diff-versao-crate]] — Auditoria diferencial no `cargo-vet`: revisar a diferença entre versões de uma crate
- [[cargo-vet-imports-organizacoes-trust-explicito]] — Imports de auditorias no `cargo-vet`: confiar em organizações de forma explícita
- [[cargo-vet-suggest-priorizar-backlog-auditoria]] — `cargo vet suggest`: priorizar backlog de auditorias com mudanças menores
- [[cargo-vet-certify-record-audit-trilha-versao]] — `cargo vet certify`: registrar uma auditoria ligada à versão revisada
- [[cargo-vet-record-violation-integridade-audits]] — `cargo vet record-violation`: registrar que uma versão contradiz uma auditoria
- [[cargo-vet-exemptions-backlog-diferencial-seguranca]] — Exemptions no `cargo-vet`: backlog explícito, não selo de segurança

### `cargo-geiger` — estatística de blocos `unsafe` no crate e nas dependências Rust, interpretação e limites de cobertura

- [[cargo-geiger-proposito-estatisticas-unsafe-rust]] — `cargo-geiger`: medir presença de `unsafe` sem converter contagem em nota de segurança
- [[cargo-geiger-execucao-workspace-grafo-dependencias]] — Executar `cargo geiger` na raiz do workspace e delimitar o grafo analisado
- [[cargo-geiger-blocos-unsafe-review-invariantes]] — Transformar os pontos `unsafe` do `cargo-geiger` em uma fila de revisão de invariantes
- [[cargo-geiger-uso-unsafe-necessario-encapsulamento]] — Interpretar `unsafe` no contexto: FFI, abstrações de baixo nível e encapsulamento seguro
- [[cargo-geiger-baseline-historico-delta-unsafe]] — Usar baseline de `cargo-geiger` para acompanhar mudanças sem premiar dívida antiga
- [[cargo-geiger-install-locked-openssl-vendored]] — Instalar `cargo-geiger` com Cargo lockado e escolher a biblioteca OpenSSL
- [[cargo-geiger-comparacao-crates-normalizada-toolchain]] — Comparar relatórios `cargo-geiger` com toolchain, features e grafo fixos
- [[cargo-geiger-relatorio-dados-entrada-auditoria-humana]] — Arquivar saída do `cargo-geiger` como evidência de revisão, não como certificado
- [[cargo-geiger-complementar-cargo-audit-clippy-miri]] — Combinar `cargo-geiger` com auditoria de advisories e testes de comportamento inseguro
- [[cargo-geiger-politica-nao-bloquear-por-contagem-bruta]] — Evitar gate binário por contagem bruta de `unsafe` sem contexto de risco

### npm CLI `npm audit` — Bulk Advisory API, remediação sem quebra, relatórios JSON e verificação de assinatura/proveniência

- [[npm-audit-descricao-dependencias-registry-privacidade]] — `npm audit`: envio da descrição de dependências ao registry configurado
- [[npm-audit-lockfile-reprodutibilidade-package-lock]] — `package-lock.json` como entrada do `npm audit`: consistência e reprodutibilidade
- [[npm-audit-bulk-advisory-endpoint-pacotes-versoes]] — Bulk Advisory Endpoint do npm: enviar nomes e versões resolvidas
- [[npm-audit-audit-level-limiar-nao-filtro-relatorio]] — `--audit-level` no npm: limiar do exit code, não filtro dos achados
- [[npm-audit-fix-semver-force-risco-major]] — `npm audit fix` e `--force`: diferenciar atualização compatível de mudança major
- [[npm-audit-omit-producao-devdependencies-escopo]] — Separar dependências de produção e desenvolvimento no `npm audit`
- [[npm-audit-json-sarif-automacao-relatorio]] — `npm audit --json`: preservar dados estruturados para triagem automatizada
- [[npm-audit-metavulnerabilidades-cadeia-transitiva]] — Metavulnerabilidades no npm: quando uma dependência pai só resolve para versão vulnerável
- [[npm-audit-signatures-provenance-attestations-distincao]] — `npm audit signatures`: verificação separada de assinatura e proveniência do registry
- [[npm-audit-exit-code-ci-severidade-politica]] — Códigos de saída do `npm audit`: transformar achados em política CI explícita

### pnpm `audit` — advisories GHSA, escopo por ambiente, correções por overrides, idade mínima e assinaturas de registry

- [[pnpm-audit-bulk-advisory-ghsa-pnpm-v11]] — `pnpm audit` v11+: Bulk Advisory e uso de IDs GHSA
- [[pnpm-audit-prod-dev-optional-dependencies-escopo]] — Delimitar `pnpm audit` por produção, desenvolvimento e dependências opcionais
- [[pnpm-audit-json-patched-versions-null]] — `pnpm audit --json`: diferenciar advisories corrigíveis de sem versão corrigida
- [[pnpm-audit-fix-overrides-workspace-yaml]] — `pnpm audit --fix`: remediar com `overrides` no arquivo de workspace
- [[pnpm-audit-fix-update-lockfile-interativo]] — `pnpm audit --fix=update` e modo interativo: escolher a forma da remediação
- [[pnpm-audit-ignore-ghsa-governanca-prune]] — `audit.ignore` no pnpm: allowlist GHSA com justificativa e limpeza de entradas antigas
- [[pnpm-audit-level-impressao-severidade-policy]] — `--audit-level` no pnpm: controlar severidade exibida sem perder dados brutos
- [[pnpm-audit-registry-errors-nao-mascarar-falha]] — `--ignore-registry-errors`: não confundir indisponibilidade do serviço com resultado limpo
- [[pnpm-audit-signatures-registry-ecdsa-chaves]] — `pnpm audit signatures`: verificar assinaturas ECDSA do registry instalado
- [[pnpm-audit-minimum-release-age-correcoes-seguranca]] — `minimumReleaseAge` e correções no pnpm: equilibrar atraso contra janela de ataque

### Yarn Berry `yarn npm audit` — escopo por workspace, dependências transitivas, saída NDJSON e exclusões explicáveis

- [[yarn-npm-audit-escopo-direto-workspace-default]] — `yarn npm audit`: escopo padrão limitado ao workspace ativo
- [[yarn-npm-audit-all-workspaces-monorepo]] — `yarn npm audit --all`: ampliar a auditoria aos workspaces do monorepo
- [[yarn-npm-audit-recursive-transitivas-cadeia]] — `yarn npm audit --recursive`: incluir dependências transitivas no relatório
- [[yarn-npm-audit-environment-production-devdeps]] — `--environment production`: focar dependências de runtime sem apagar contexto de build
- [[yarn-npm-audit-severity-filtro-relatorio-exit]] — `--severity` no Yarn: filtrar severidades exibidas e interpretar exit status
- [[yarn-npm-audit-json-ndjson-registry-payload]] — Saída JSON/NDJSON no `yarn npm audit`: automação sem perder o relatório bruto
- [[yarn-npm-audit-exclude-packages-false-positive-policy]] — `--exclude` no Yarn: reduzir ruído com escopo de pacote documentado
- [[yarn-npm-audit-ignore-advisory-id-governanca]] — `--ignore` no Yarn: suprimir advisory específico com revisão recorrente
- [[yarn-why-triagem-pacote-transitivo-origem]] — `yarn why` depois do audit: localizar quem introduziu uma dependência transitiva
- [[yarn-audit-registry-relevancia-caminhos-execucao]] — Relevância de advisories no Yarn: cruzar registry, versão e caminho de execução

### Gradle dependency verification — checksums, assinaturas, `verification-metadata.xml`, bootstrap e compatibilidade com locking

- [[gradle-dependency-verification-integridade-nao-vulnerabilidade]] — Gradle Dependency Verification: verificar integridade de artefatos, não ausência de vulnerabilidades
- [[gradle-verification-metadata-bootstrap-review-manual]] — `verification-metadata.xml`: geração inicial é bootstrap, não estabelecimento automático de confiança
- [[gradle-checksum-versus-pgp-signature-verification]] — Checksums e assinaturas PGP no Gradle: propriedades diferentes de verificação
- [[gradle-verification-metadata-unknown-artifact-fail-closed]] — Tratar artefato sem entrada de verificação como mudança que exige revisão
- [[gradle-verification-metadata-trust-keys-export-review]] — Importar e confiar em chaves para verificação de assinaturas Gradle
- [[gradle-verification-metadata-shared-project-scope]] — Centralizar `verification-metadata.xml` no repositório para builds reproduzíveis
- [[gradle-verification-metadata-plugins-build-dependencies]] — Cobertura do Gradle Dependency Verification para plugins e configurações resolvidas
- [[gradle-dependency-locking-version-selection-diferenca-integridade]] — Dependency Locking e Dependency Verification no Gradle: versão fixa versus bytes verificados
- [[gradle-verification-refresh-upgrade-artefactos]] — Atualizar metadata de verificação em upgrades sem aceitar mudanças em massa
- [[gradle-verification-complemento-scanners-sbom]] — Incluir Dependency Verification em uma cadeia de controles de supply chain Gradle

### Apache Maven Enforcer Plugin — execução de regras no build, convergência, versões dinâmicas, dependências proibidas e escopo

- [[maven-enforcer-enforce-pipeline-rules-build]] — `maven-enforcer-plugin`: aplicar requisitos de build com regras declaradas
- [[maven-enforcer-fail-default-true-policy]] — `fail` no Maven Enforcer: falhar por padrão e tratar warn-only com intenção
- [[maven-enforcer-dependency-convergence-transitive-conflicts]] — `dependencyConvergence`: detectar versões transitivas divergentes no grafo Maven
- [[maven-enforcer-ban-dynamic-versions-reproducibilidade]] — Banir versões Maven dinâmicas para builds reprodutíveis
- [[maven-enforcer-banned-dependencies-exclusions]] — `bannedDependencies`: recusar coordenadas Maven com escopo e exceções explícitos
- [[maven-enforcer-require-java-maven-version-build-environment]] — Exigir versões de Java e Maven compatíveis com o build
- [[maven-enforcer-require-property-dependency-management]] — Exigir propriedades e campos de versão no Maven POM
- [[maven-enforcer-configuracao-em-parent-versus-modulos]] — Centralizar regras Enforcer em parent POM sem perder escopo por módulo
- [[maven-enforcer-version-rule-plugin-pin-maintenance]] — Fixar a versão do Maven Enforcer Plugin e revisar mudanças de regras
- [[maven-enforcer-policy-gate-nao-substitui-scanner-advisory]] — Maven Enforcer e scanners de CVE: policy de build não equivale a análise de advisories

### Renovate `vulnerabilityAlerts` — triagem de alertas GitHub, Dependency Graph, configuração de PRs e limites de OSV experimental

- [[renovate-vulnerabilityalerts-github-dependabot-prerequisites]] — `vulnerabilityAlerts` do Renovate depende do Dependency Graph e Dependabot alerts no GitHub
- [[renovate-vulnerabilityalerts-config-pr-settings]] — Personalizar pull requests de correção de vulnerabilidade no Renovate
- [[renovate-vulnerabilityalerts-nao-substitui-dependency-updates]] — Separar alertas de vulnerabilidade e fluxo regular de atualização do Renovate
- [[renovate-osv-vulnerability-alerts-experimental-escopo]] — `osvVulnerabilityAlerts` no Renovate: recurso marcado experimental e sujeito a validação
- [[renovate-security-presets-inherit-config-review]] — Aplicar presets de segurança Renovate com configuração herdada revisável
- [[renovate-vulnerabilityalerts-github-permissions-self-hosted]] — Permissões e execução self-hosted para alertas de vulnerabilidade Renovate
- [[renovate-alertas-dependabot-sla-triage-evidencia]] — Tratar alertas como fila de triagem: owner, prazo, versão corrigida e evidência de merge
- [[renovate-config-validation-preview-dry-run]] — Validar configuração Renovate antes de ativar regras de segurança
- [[renovate-alerta-ghsa-osv-identificadores-mapeamento]] — Correlacionar alertas Renovate com identificadores GHSA/CVE e advisory original
- [[renovate-vulnerabilityalerts-limitacoes-alertas-sem-patch]] — PR de vulnerabilidade sem patch disponível: registrar mitigação em vez de assumir correção
