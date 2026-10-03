# Lote `software-seguranca-2000-0003` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM

Manifesto auditável do terceiro lote de escala (`software-seguranca-2000-0003`), focado em segurança de aplicações (AppSec), segurança da cadeia de suprimentos de software (SBOM/VEX/SCA/SLSA/Scorecard), varredura de segredos, DAST e motores de autorização fina (ReBAC/ABAC/PBAC).

## Resumo do estado atual

- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)
- Meta do lote: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **100 / 2.000 (5,00%)**
- Gate automatizado: **100/100 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 1)
- Revisão factual humana: **0/100**
- Revisão factual por IA: **100/100**
- Contabilizadas como válidas: **100/100**
- Revisor das 100 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranche 1 (100 notas, IDs 1–100) foi conferida factualmente por IA e aprovada sob o protocolo atualizado
- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)
- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-seguranca-2000-0003-tranche-01.md`](../reports/batch-reconciliation-software-seguranca-2000-0003-tranche-01.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-seguranca-2000-0003-tranche-01.md)

Existem 100 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.900 restantes.

## Tranche 1 — Gitleaks, TruffleHog, Google OSV-Scanner V2, OWASP Dependency-Track, OWASP ZAP, ProjectDiscovery Nuclei, OpenFGA, AuthZed SpiceDB, Cerbos e OpenSSF Scorecard (100 notas; revisão factual por IA registrada)

### Gitleaks (varredura determinística de segredos em repositórios Git, diretórios e streams, hierarquia `gitleaks.toml`, `[extend]`, `[allowlist]`, `.gitleaksignore` e `--baseline-path`)

1. [Gitleaks: arquitetura de detecção rápida de segredos em repositórios `git`, diretórios `dir` e `stdin`](../../domains/software-0009/software/seguranca/gitleaks-arquitetura-deteccao-segredos-git-dir-stdin.md)
2. [Gitleaks `gitleaks.toml`: ordem de precedência da configuração e anatomia de tabelas `rules` (`regex`, `keywords`, `entropy`)](../../domains/software-0009/software/seguranca/gitleaks-configuracao-toml-precedencia-rules-keywords-entropy.md)
3. [Gitleaks com `pre-commit`: bloqueio preventivo de segredos na máquina do desenvolvedor antes do `git commit`](../../domains/software-0009/software/seguranca/gitleaks-pre-commit-hook-prevencao-commits-locais-skip.md)
4. [Gitleaks Controle de Falsos Positivos: `[allowlist]`, comentários `gitleaks:allow` e arquivo `.gitleaksignore` por `Fingerprint`](../../domains/software-0009/software/seguranca/gitleaks-allowlists-gitleaksignore-fingerprints-comentarios-allow.md)
5. [Gitleaks Baseline Scanning (`--baseline-path`): adoção incremental em repositórios legados sem bloquear o CI com dívida antiga](../../domains/software-0009/software/seguranca/gitleaks-baseline-scanning-adocao-repositorios-legados-baseline-path.md)
6. [Gitleaks Inspeção Profunda: decodificação recursiva (`--max-decode-depth`) e varredura de arquivos compactados (`--max-archive-depth`)](../../domains/software-0009/software/seguranca/gitleaks-decodificacao-recursiva-arquivos-compactados-max-decode-archive-depth.md)
7. [Gitleaks Relatórios e Integração DevSecOps: geração de saídas `sarif`, `junit`, `json`, `csv` e templates Go (`--report-template`)](../../domains/software-0009/software/seguranca/gitleaks-formatos-relatorio-sarif-junit-json-csv-template.md)
8. [Gitleaks Anatomia da `[allowlist]` Global: exclusão de lockfiles (`go.sum`, `package-lock.json`), binários e `stopwords`](../../domains/software-0009/software/seguranca/gitleaks-allowlist-global-paths-regexes-stopwords-padroes.md)
9. [Gitleaks no CI/CD (`gitleaks git` + opções `git log`): varredura rápida apenas dos commits de um Pull Request](../../domains/software-0009/software/seguranca/gitleaks-varredura-commits-especificos-git-log-options-ci-pr.md)
10. [Gitleaks Diagnóstico de Performance (`--diagnostics`) e Governança: profiling `cpu`/`mem`/`trace`/`http` e evolução para `Betterleaks`](../../domains/software-0009/software/seguranca/gitleaks-diagnostico-performance-pprof-cpu-mem-trace-betterleaks.md)

### TruffleHog (descoberta, classificação, validação ativa em tempo real de mais de 800 tipos de credenciais, `trufflehog analyze`, filtros `--results=verified,unknown` e detectores customizados)

11. [TruffleHog: arquitetura dos 4 pilares (`Discovery`, `Classification`, `Validation` e `Analysis`) para credenciais vazadas](../../domains/software-0009/software/seguranca/trufflehog-arquitetura-discovery-classification-validation-analysis.md)
12. [TruffleHog Fontes de Varredura: inspeção nativa de `git`, `github`, `gitlab`, `s3`, `gcs`, `docker` (camadas OCI) e `filesystem`](../../domains/software-0009/software/seguranca/trufflehog-fontes-varredura-git-github-gitlab-s3-gcs-docker-filesystem.md)
13. [TruffleHog Políticas de Verificação: controle de `--results=verified,unknown,unverified` e modo offline `--no-verification`](../../domains/software-0009/software/seguranca/trufflehog-verificacao-ativa-credenciais-results-verified-unverified-no-verification.md)
14. [TruffleHog Credential Analysis (`trufflehog analyze`): mapeamento de identidade, recursos acessíveis e permissões de chaves vazadas](../../domains/software-0009/software/seguranca/trufflehog-analise-profunda-credenciais-analyze-iam-permissions.md)
15. [TruffleHog em Pipelines CI/CD: varredura diferencial com `--since-commit`, `--branch` e código de saída `--fail` (`183`)](../../domains/software-0009/software/seguranca/trufflehog-ci-cd-github-actions-gitlab-ci-since-commit-branch-fail.md)
16. [TruffleHog Supply Chain Security: verificação criptográfica de binários e `checksums.txt` com Sigstore `cosign verify-blob`](../../domains/software-0009/software/seguranca/trufflehog-verificacao-assinatura-cosign-checksums-supply-chain.md)
17. [TruffleHog Custom Detectors (`--config`): criação de detectores Regex customizados com verificação via servidor Webhook](../../domains/software-0009/software/seguranca/trufflehog-custom-regex-detectors-webhook-verification-config.md)
18. [TruffleHog Arquitetura Interna de Concorrência: pipeline de `Sources`, `Chunks`, `Decoders`, `Aho-Corasick` e `Detectors`](../../domains/software-0009/software/seguranca/trufflehog-arquitetura-concorrencia-process-flow-chunks-decoders-detectors.md)
19. [TruffleHog Filtragem de Escopo e Limites de Arquivos: `--include-paths`, `--exclude-paths` e controle de archives](../../domains/software-0009/software/seguranca/trufflehog-filtros-exclusao-include-paths-exclude-paths-archive-limits.md)
20. [TruffleHog Além do Git: varredura de `Postman`, `Jenkins`, `Elasticsearch`, `Syslog` e ecossistema colaborativo](../../domains/software-0009/software/seguranca/trufflehog-varredura-postman-jenkins-elasticsearch-jira-slack-enterprise.md)

### Google OSV-Scanner V2 (análise de composição de software sobre `OSV.dev` e `OSV-Scalibr`, varredura de containers, análise de alcançabilidade *Call Analysis* e remediação guiada `osv-scanner fix`)

21. [OSV-Scanner V2: arquitetura em duas fases (*Package Extraction* via `OSV-Scalibr` e *Vulnerability Matching* via `OSV.dev`)](../../domains/software-0009/software/seguranca/osvscanner-arquitetura-osv-dev-osv-scalibr-extracao-matching.md)
22. [OSV-Scanner `scan source`: varredura de 19+ lockfiles, manifestos SBOM (`CycloneDX`/`SPDX`) e hashes de commits Git (`C/C++`)](../../domains/software-0009/software/seguranca/osvscanner-scan-source-lockfiles-sbom-cyclonedx-spdx-git-commits.md)
23. [OSV-Scanner `scan image`: varredura *layer-aware* de imagens de container (pacotes Alpine/Debian/Ubuntu e artefatos Go/Java/Node/Python)](../../domains/software-0009/software/seguranca/osvscanner-scan-image-containers-layer-aware-distros-artifacts.md)
24. [OSV-Scanner Call Analysis (*Reachability*): análise de grafo de chamadas para verificar se a função vulnerável é realmente invocada](../../domains/software-0009/software/seguranca/osvscanner-call-analysis-reachability-go-rust-reducao-falsos-positivos.md)
25. [OSV-Scanner Guided Remediation (`osv-scanner fix`): estratégias `in-place`, `relax` e `override` para atualização segura de dependências](../../domains/software-0009/software/seguranca/osvscanner-guided-remediation-fix-in-place-relax-override-pom-npm.md)
26. [OSV-Scanner License Scanning (`--licenses`): auditoria de licenças de software livre via `deps.dev` e validação contra allowlist SPDX](../../domains/software-0009/software/seguranca/osvscanner-license-scanning-deps-dev-spdx-allowlist-compliance.md)
27. [OSV-Scanner Modo Offline (`--offline-vulnerabilities` e `--download-offline-databases`): operação em redes isoladas e *air-gapped*](../../domains/software-0009/software/seguranca/osvscanner-offline-scanning-download-offline-databases-air-gapped.md)
28. [OSV-Scanner `osv-scanner.toml`: supressão auditável (`IgnoredVulns` com `ignoreUntil`) e sobrescrita (`PackageOverrides`)](../../domains/software-0009/software/seguranca/osvscanner-configuracao-osv-scanner-toml-ignoredvulns-packageoverrides.md)
29. [OSV-Scanner Formatos de Saída (`--format`) e Integração `pre-commit` / GitHub Actions (`sarif`, `cyclonedx-1-5`, `gh-annotations`)](../../domains/software-0009/software/seguranca/osvscanner-formatos-saida-sarif-cyclonedx-html-gh-annotations-pre-commit.md)
30. [OSV-Scanner e `OSV-Scalibr`: arquitetura modular de extratores e detectores na versão V2](../../domains/software-0009/software/seguranca/osvscanner-extensibilidade-osv-scalibr-plugins-arquitetura-v2.md)

### OWASP Dependency-Track (plataforma contínua API-first de análise de SBOM CycloneDX, correlação de vulnerabilidades com pontuação EPSS, triagem VEX e Policy Engine)

31. [OWASP Dependency-Track: arquitetura da plataforma contínua de análise de risco de cadeia de suprimentos baseada em SBOM `CycloneDX`](../../domains/software-0009/software/seguranca/deptrack-arquitetura-owasp-dependency-track-sbom-cyclonedx-api-first.md)
32. [OWASP Dependency-Track Ingestão de SBOM em CI/CD: endpoint `/api/v1/bom`, autenticação `X-Api-Key` e criação automática de projetos](../../domains/software-0009/software/seguranca/deptrack-ingestao-sbom-api-rest-bom-upload-ci-cd-auto-create.md)
33. [OWASP Dependency-Track e `CycloneDX VEX`: consumo e exportação de *Vulnerability Exploitability Exchange* para triagem auditável](../../domains/software-0009/software/seguranca/deptrack-vex-vulnerability-exploitability-exchange-cyclonedx-triagem.md)
34. [OWASP Dependency-Track Inteligência de Vulnerabilidades e `EPSS`: correlação multi-fonte e priorização preditiva de exploração](../../domains/software-0009/software/seguranca/deptrack-fontes-inteligencia-vulnerabilidades-nvd-osv-github-epss.md)
35. [OWASP Dependency-Track Policy Engine: políticas globais e por projeto para risco de segurança, conformidade de licenças e risco operacional](../../domains/software-0009/software/seguranca/deptrack-policy-engine-seguranca-licencas-risco-operacional.md)
36. [OWASP Dependency-Track Portfolio Impact Analysis: resposta imediata a incidentes (*"O que está afetado, e onde?"*) via PURL e CPE](../../domains/software-0009/software/seguranca/deptrack-impact-analysis-portfolio-busca-componentes-afetados-log4shell.md)
37. [OWASP Dependency-Track Inventário de Serviços e APIs: rastreamento de provedores externos, classificação de dados e *Trust Boundaries*](../../domains/software-0009/software/seguranca/deptrack-monitoramento-servicos-externos-apis-trust-boundary-cyclonedx.md)
38. [OWASP Dependency-Track Notificações e Integrações: alertas em tempo real (`Slack`, `Teams`, `Jira`, `Webhooks`) e sincronização com `DefectDojo`](../../domains/software-0009/software/seguranca/deptrack-notificacoes-webhooks-slack-jira-defectdojo-integracoes.md)
39. [OWASP Dependency-Track Autenticação e RBAC (`OIDC`, `LDAP`, `API Keys` e *Portfolio Access Control*): governança multi-equipe](../../domains/software-0009/software/seguranca/deptrack-autenticacao-oidc-oauth2-ldap-teams-rbac-permissions.md)
40. [OWASP Dependency-Track Risco de Desatualização, Banco Privado de Vulnerabilidades e Evolução Arquitetural (`v4` -> `v5`)](../../domains/software-0009/software/seguranca/deptrack-repositorio-outdated-components-private-vuln-db-operacao-v5.md)

### OWASP ZAP / Zed Attack Proxy (DAST declarativo com Automation Framework YAML, `spider`/`spiderAjax`, importação `openapi`/`graphql`, `passiveScan-wait`, `activeScan`, `alertFilter` e `exitStatus`)

41. [OWASP ZAP (Zed Attack Proxy): arquitetura de proxy interceptador, `Passive Scanner` e `Active Scanner` para DAST](../../domains/software-0009/software/seguranca/zaproxy-arquitetura-zed-attack-proxy-dast-passive-active-scanner.md)
42. [ZAP Automation Framework (`zap.sh -cmd -autorun`): controle declarativo em arquivo YAML único para CI/CD](../../domains/software-0009/software/seguranca/zaproxy-automation-framework-yaml-env-jobs-substituicao-packaged-scans.md)
43. [ZAP Crawling e Descoberta (`spider`, `spiderAjax` e `spiderClient`): mapeamento de aplicações tradicionais e SPAs modernas](../../domains/software-0009/software/seguranca/zaproxy-descoberta-superficie-spider-spiderajax-spiderclient-spas.md)
44. [ZAP Segurança de APIs (`openapi`, `graphql`, `soap` e `postman`): importação de contratos para DAST de APIs REST e GraphQL](../../domains/software-0009/software/seguranca/zaproxy-importacao-schemas-apis-openapi-graphql-soap-postman.md)
45. [ZAP Autenticação no Automation Framework: `browser` auth, `autodetect` de sessão e injeção de tokens com o job `replacer`](../../domains/software-0009/software/seguranca/zaproxy-autenticacao-browser-auth-autodetect-replacer-bearer-tokens.md)
46. [ZAP `passiveScan-config` e `passiveScan-wait`: ajuste de regras passivas e sincronização obrigatória da fila de análise](../../domains/software-0009/software/seguranca/zaproxy-passive-scan-config-passive-scan-wait-fila-assincrona.md)
47. [ZAP `activeScan`, `activeScan-policy` e `activeScan-config`: sintonia de *Attack Strength*, *Alert Threshold* e tecnologias do alvo](../../domains/software-0009/software/seguranca/zaproxy-active-scan-policy-strength-threshold-technologies-tuning.md)
48. [ZAP `alertFilter`: supressão e reklasificação declarativa de falsos positivos por `ruleId`, `url` e `parameter`](../../domains/software-0009/software/seguranca/zaproxy-alert-filter-triagem-falsos-positivos-rebaixamento-risco.md)
49. [ZAP Quality Gates em CI/CD: *Job Tests* (`alert`, `stats`, `url`), geração de relatórios (`report`) e `exitStatus`](../../domains/software-0009/software/seguranca/zaproxy-job-tests-assertions-exitstatus-report-sarif-quality-gates.md)
50. [ZAP Fluxos Multi-Step e Customizados: jobs `requestor`, `sequence-import` (arquivos HAR), `sequence-activeScan` e `prune`](../../domains/software-0009/software/seguranca/zaproxy-requestor-sequence-har-import-prune-fluxos-multi-step.md)

### ProjectDiscovery Nuclei (scanner de vulnerabilidades de alta performance baseado em templates YAML multi-protocolo, workflows condicionais, detecção OAST via Interactsh e exportação SARIF)

51. [ProjectDiscovery Nuclei: arquitetura do scanner de vulnerabilidades de alta performance baseado em templates YAML](../../domains/software-0009/software/seguranca/nuclei-arquitetura-scanner-vulnerabilidades-templates-yaml-zero-false-positives.md)
52. [Nuclei Anatomia de um Template YAML: metadados `info` (`severity`, `classification`, `tags`), `matchers` e `extractors`](../../domains/software-0009/software/seguranca/nuclei-anatomia-template-yaml-info-http-matchers-extractors.md)
53. [Nuclei Seleção e Filtragem de Templates: `-tags`, `-etags`, `-severity` (`critical,high`), `-tc` (Template Condition) e `-as` (Automatic Scan)](../../domains/software-0009/software/seguranca/nuclei-filtragem-templates-tags-severity-author-template-condition.md)
54. [Nuclei Além do HTTP: templates multi-protocolo para auditoria de `DNS`, `SSL/TLS`, `TCP`, `WHOIS` e serviços de rede](../../domains/software-0009/software/seguranca/nuclei-multi-protocolo-dns-ssl-tcp-websocket-whois-network-scans.md)
55. [Nuclei Workflows e `flow:` Engine: orquestração condicional multi-step e encadeamento de variáveis entre requisições](../../domains/software-0009/software/seguranca/nuclei-workflows-multi-step-flow-engine-variaveis-dinamicas.md)
56. [Nuclei OAST com `Interactsh` (`{{interactsh-url}}`): detecção *Out-of-Band* sem falsos positivos para Blind SSRF, XXE e RCE](../../domains/software-0009/software/seguranca/nuclei-interactsh-oast-out-of-band-blind-ssrf-rce-log4shell.md)
57. [Nuclei Varreduras Autenticadas (`-H`, `-var` e arquivo de `secrets` com `pre-condition`): autenticação dinâmica em APIs e aplicações](../../domains/software-0009/software/seguranca/nuclei-authenticated-scans-secrets-file-headers-variables-ci-cd.md)
58. [Nuclei Performance, *Request Clustering* e Rate Limiting (`-rl`, `-c`, `-bs`): proteção do alvo e otimização de tráfego](../../domains/software-0009/software/seguranca/nuclei-controle-taxa-concorrencia-rate-limit-bulk-size-request-clustering.md)
59. [Nuclei Modo Headless (`-headless`), Fuzzing DAST (`-dast`) e Assinatura Criptográfica de Templates `code:`](../../domains/software-0009/software/seguranca/nuclei-headless-browser-dast-fuzzing-code-templates-assinatura.md)
60. [Nuclei Exportação e Integração CI/CD (`-sarif-export`, `-jsonl`, `-markdown-export` e `-rc` Report Config para Jira/GitHub/Splunk)](../../domains/software-0009/software/seguranca/nuclei-relatorios-exportacao-sarif-jsonl-markdown-integracao-jira-github.md)

### OpenFGA (motor de autorização CNCF Incubating inspirado no Google Zanzibar para ReBAC/ABAC, DSL `schema 1.1`/`1.2`, Conditions CEL, APIs `Check`/`ListObjects`, `fga model test` e PostgreSQL)

61. [OpenFGA: arquitetura CNCF Incubating do motor de autorização ReBAC/ABAC de alta performance inspirado no Google Zanzibar](../../domains/software-0009/software/seguranca/openfga-arquitetura-cncf-google-zanzibar-rebac-abac-engine.md)
62. [OpenFGA Conceitos Fundamentais: `Store`, `Type`, `Object`, `User` (`userset` e wildcard `*`), `Relation` e `Relationship Tuple`](../../domains/software-0009/software/seguranca/openfga-conceitos-fundamentais-store-type-object-user-relation-tuple.md)
63. [OpenFGA Configuration Language (DSL `schema 1.1`): relações diretas, herança hierárquica (`from`) e operadores `or`, `and` e `but not`](../../domains/software-0009/software/seguranca/openfga-configuration-language-dsl-schema-1-1-operadores-or-and-but-not-from.md)
64. [OpenFGA ABAC Híbrido: combinação de grafos ReBAC com `Conditions` (Google CEL) e `Contextual Tuples`](../../domains/software-0009/software/seguranca/openfga-abac-conditions-cel-contextual-tuples-atributos-tempo-execucao.md)
65. [OpenFGA APIs de Consulta: diferenças e casos de uso entre `Check`, `BatchCheck`, `ListObjects`, `ListUsers` e `Expand`](../../domains/software-0009/software/seguranca/openfga-queries-check-batchcheck-listobjects-listusers-expand.md)
66. [OpenFGA Testes Automatizados de Modelos (`fga model test`): validação declarativa de `.fga.yaml` em pipelines de CI/CD](../../domains/software-0009/software/seguranca/openfga-testes-unitarios-modelos-fga-model-test-ci-cd.md)
67. [OpenFGA Modular Models (`fga.mod`): divisão de modelos de autorização complexos em módulos por equipe e domínio](../../domains/software-0009/software/seguranca/openfga-modular-models-fga-mod-divisao-dominios-equipes.md)
68. [OpenFGA em Produção (`openfga migrate` e Storage Engines): operação com PostgreSQL/MySQL, conexões e Unix Domain Socket](../../domains/software-0009/software/seguranca/openfga-armazenamento-producao-postgres-mysql-migrations-read-replicas.md)
69. [OpenFGA Consistência e Cache (`ConsistencyPreference`): equilíbrio entre `MINIMIZE_LATENCY` e `HIGHER_CONSISTENCY` (*Zookie* / Problema do Novo Inimigo)](../../domains/software-0009/software/seguranca/openfga-performance-caching-consistency-higher-consistency-minimize-latency.md)
70. [OpenFGA Ecossistema e Automação: Terraform Provider (`openfga/openfga`), SDKs oficiais e uso embarcado como biblioteca Go](../../domains/software-0009/software/seguranca/openfga-automacao-terraform-provider-sdks-embedded-go-library.md)

### AuthZed SpiceDB (banco de dados de permissões distribuído inspirado no Google Zanzibar, linguagem de schema `.zed`, Caveats CEL, consistência `ZedToken`, `zed validate` e cluster dispatch)

71. [SpiceDB: arquitetura do banco de dados de permissões distribuído inspirado no Google Zanzibar (`spicedb` e CLI `zed`)](../../domains/software-0009/software/seguranca/spicedb-arquitetura-authzed-google-zanzibar-permissions-database.md)
72. [SpiceDB Schema Language (`.zed`): separação estrita entre `definition`, `relation` (substantivos) e `permission` (verbos computados)](../../domains/software-0009/software/seguranca/spicedb-schema-language-zed-definitions-relations-permissions.md)
73. [SpiceDB Operações de Permissão (`+`, `&`, `-` e `->`): travessia de hierarquias com Arrows e a armadilha de precedência do `+`](../../domains/software-0009/software/seguranca/spicedb-operadores-permissao-union-intersection-exclusion-arrows-precedencia.md)
74. [SpiceDB `Caveats`: combinando ReBAC e ABAC com relacionamentos condicionais avaliados em tempo de execução](../../domains/software-0009/software/seguranca/spicedb-caveats-abac-relacoes-condicionais-cel-contexto.md)
75. [SpiceDB Consistência Global e `ZedToken`: prevenção do *New Enemy Problem* com `at_least_as_fresh`, `minimize_latency` e `fully_consistent`](../../domains/software-0009/software/seguranca/spicedb-consistencia-zedtoken-zookies-at-least-as-fresh-new-enemy.md)
76. [SpiceDB Índices Reversos (`LookupResources` e `LookupSubjects`): listagem eficiente de recursos acessíveis e auditoria de sujeitos](../../domains/software-0009/software/seguranca/spicedb-reverse-indexes-lookupresources-lookupsubjects-paginacao.md)
77. [SpiceDB Validação e Testes em CI/CD (`zed validate`): arquivos YAML de schema, relacionamentos de teste, `assertions` e `expected_relations`](../../domains/software-0009/software/seguranca/spicedb-validacao-testes-schema-zed-validate-assertions-ci.md)
78. [SpiceDB Datastores de Produção e `spicedb migrate`: escolha entre `postgres`, `cockroachdb`, `spanner` e `mysql`](../../domains/software-0009/software/seguranca/spicedb-datastores-postgres-cockroachdb-spanner-mysql-migrate.md)
79. [SpiceDB Dispatching Distribuído em Cluster Kubernetes: roteamento por *Consistent Hashing* entre réplicas para maximizar Cache Hit](../../domains/software-0009/software/seguranca/spicedb-dispatch-cluster-consistent-hashing-kubernetes-caching.md)
80. [SpiceDB `Watch` API e Operações em Massa (`zed backup` / `zed restore` / `zed import`): streaming de mudanças e migração de dados](../../domains/software-0009/software/seguranca/spicedb-watch-api-bulk-import-export-backup-auditoria-eventos.md)

### Cerbos PDP (Policy Decision Point stateless para autorização PBAC/ABAC/RBAC, os 6 tipos de política YAML, `Derived Roles`, APIs `CheckResources` e `PlanResources` AST, `cerbos compile` e JWKS)

81. [Cerbos: arquitetura do Policy Decision Point (`PDP`) stateless para autorização PBAC/ABAC/RBAC declarativa em YAML](../../domains/software-0009/software/seguranca/cerbos-arquitetura-stateless-pdp-pbac-abac-rbac-cloud-native.md)
82. [Cerbos Taxonomia das 6 Políticas: `Resource Policies`, `Derived Roles`, `Principal Policies`, `Role Policies`, `Exported Variables` e `Constants`](../../domains/software-0009/software/seguranca/cerbos-seis-tipos-politicas-resource-derived-roles-principal-role-export.md)
83. [Cerbos `Derived Roles`: evolução limpa de RBAC estático para ABAC contextual usando expressões CEL](../../domains/software-0009/software/seguranca/cerbos-derived-roles-evolucao-rbac-para-abac-condicoes-cel.md)
84. [Cerbos API `CheckResources`: avaliação em lote de múltiplos recursos e múltiplas ações em uma única requisição](../../domains/software-0009/software/seguranca/cerbos-api-checkresources-batch-avaliacao-multiplos-recursos-acoes.md)
85. [Cerbos API `PlanResources` (*Query Plan*): geração de AST de filtros (`CONDITIONAL`) para consultas diretas no banco de dados (Prisma/SQLAlchemy/GORM)](../../domains/software-0009/software/seguranca/cerbos-api-planresources-query-plan-ast-filtros-banco-orm.md)
86. [Cerbos Scoped Policies: herança hierárquica de políticas para SaaS multi-tenant (`acme.corp.uk`) sem duplicar regras](../../domains/software-0009/software/seguranca/cerbos-scoped-policies-hierarquia-multi-tenant-heranca-escopos.md)
87. [Cerbos `cerbos compile` e Validação de Schemas: testes unitários de políticas e checagem de tipos de atributos (`schemas`)](../../domains/software-0009/software/seguranca/cerbos-compilacao-testes-unitarios-cerbos-compile-schemas-json.md)
88. [Cerbos `auxData` e Verificação Nativa de JWT: uso de claims autenticadas do token diretamente nas expressões de política](../../domains/software-0009/software/seguranca/cerbos-auxdata-jwt-verificacao-claims-contexto-criptografico.md)
89. [Cerbos Decision Audit Logs e Policy Outputs: trilha de auditoria de decisões e retorno de obrigações/máscaras para a aplicação](../../domains/software-0009/software/seguranca/cerbos-audit-logs-decision-logs-outputs-mascaramento-campos-sensiveis.md)
90. [Cerbos Topologias de Deploy e Storage Drivers: `sidecar` vs `service` no Kubernetes e sincronização via `git`, `blob` ou `disk`](../../domains/software-0009/software/seguranca/cerbos-implantacao-kubernetes-sidecar-vs-service-storage-git-blob-disk.md)

### OpenSSF Scorecard (avaliação automatizada de postura de segurança em repositórios open-source e supply chain, `Branch-Protection` em 5 Tiers, `Pinned-Dependencies`, `Token-Permissions` e Probes V5)

91. [OpenSSF Scorecard: arquitetura de avaliação automatizada de postura de segurança em repositórios open-source e supply chain](../../domains/software-0009/software/seguranca/scorecard-arquitetura-openssf-avaliacao-seguranca-open-source-supply-chain.md)
92. [OpenSSF Scorecard `Branch-Protection` e `Code-Review`: pontuação em 5 Tiers contra injeção maliciosa na branch principal](../../domains/software-0009/software/seguranca/scorecard-check-branch-protection-tiers-1-a-5-code-review.md)
93. [OpenSSF Scorecard `Binary-Artifacts`: detecção de executáveis e binários não revisáveis commitados no repositório de código-fonte](../../domains/software-0009/software/seguranca/scorecard-check-binary-artifacts-reproducible-builds-supply-chain.md)
94. [OpenSSF Scorecard `Token-Permissions` e `Dangerous-Workflows`: prevenção de escalação de privilégio e injeção em GitHub Actions](../../domains/software-0009/software/seguranca/scorecard-checks-token-permissions-dangerous-workflows-github-actions.md)
95. [OpenSSF Scorecard `Pinned-Dependencies`: fixação de GitHub Actions, imagens Docker e downloads por hash criptográfico SHA](../../domains/software-0009/software/seguranca/scorecard-check-pinned-dependencies-hash-sha-imutavel-containers-actions.md)
96. [OpenSSF Scorecard `Signed-Releases` e `Packaging`: assinatura de artefatos, atestados de proveniência SLSA e pacotes oficiais](../../domains/software-0009/software/seguranca/scorecard-checks-signed-releases-packaging-slsa-provenance-cosign.md)
97. [OpenSSF Scorecard Código Seguro: checks `SAST`, `Fuzzing`, `Vulnerabilities` (OSV) e `Dependency-Update-Tool`](../../domains/software-0009/software/seguranca/scorecard-checks-sast-fuzzing-vulnerabilities-dependency-update-tool.md)
98. [OpenSSF Scorecard Governança e Saúde do Projeto: `Maintained`, `Security-Policy` (`SECURITY.md`), `License` e `CII-Best-Practices`](../../domains/software-0009/software/seguranca/scorecard-checks-maintained-cii-best-practices-security-policy-license.md)
99. [OpenSSF Scorecard GitHub Action (`ossf/scorecard-action`): publicação de alertas SARIF no GitHub Code Scanning e Badge oficial](../../domains/software-0009/software/seguranca/scorecard-github-action-sarif-code-scanning-badge-monitoramento-continuo.md)
100. [OpenSSF Scorecard em Escala: *Probes* estruturadas (V5), API REST (`api.scorecard.dev`) e dataset público no BigQuery](../../domains/software-0009/software/seguranca/scorecard-probes-structured-results-bigquery-api-rest-avaliacao-escala.md)

## Critérios e próximo passo

As 100 notas 1–100 da tranche 1 têm revisão factual por IA registrada no relatório vinculado. O lote continua incompleto: são 100/2.000 notas válidas, restando 1.900 notas materiais.
