# Lote `software-seguranca-2000-0003` — Engenharia de Segurança de Software, AppSec, DevSecOps e IAM

Manifesto auditável do terceiro lote de escala (`software-seguranca-2000-0003`), focado em segurança de aplicações (AppSec), WAF/NSM, criptografia moderna, postura multi-cloud (CSPM/ASPM), segurança da cadeia de suprimentos de software (SBOM/VEX/SCA/SLSA/Scorecard), varredura de segredos, DAST e identidade/autorização (OAuth2/OIDC/ReBAC/ABAC/PBAC).

## Resumo do estado atual

- Domínio / subdomínio: `software` / `seguranca` (`knowledge-federation/domains/software-0009/software/seguranca/`)
- Meta do lote: **2.000 notas substantivas**
- Notas efetivamente redigidas até agora: **200 / 2.000 (10,00%)**
- Gate automatizado: **200/200 aprovadas** (conteúdo mínimo, seções, fontes específicas e wikilinks; reexecutado após a tranche 2)
- Revisão factual humana: **0/200**
- Revisão factual por IA: **200/200**
- Contabilizadas como válidas: **200/200**
- Revisor das 200 notas aprovadas por IA: `Arena.ai Agent Mode`, com relatórios específicos; não são aprovações humanas
- Status do lote maior: `in_progress`; tranches 1–2 (200 notas, IDs 1–200) foram conferidas factualmente por IA e aprovadas sob o protocolo atualizado
- MOC do lote: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)
- Relatório de qualidade do lote: [`note-quality-software-seguranca-2000-0003.md`](../reports/note-quality-software-seguranca-2000-0003.md)
- Reconciliação estrutural mais recente do manifesto/fila: [`batch-reconciliation-software-seguranca-2000-0003-tranche-02.md`](../reports/batch-reconciliation-software-seguranca-2000-0003-tranche-02.md)
- Relatórios factuais por IA: [`tranche 1`](../reports/ai-review-software-seguranca-2000-0003-tranche-01.md), [`tranche 2`](../reports/ai-review-software-seguranca-2000-0003-tranche-02.md)

Existem 200 notas materiais listadas abaixo; não há IDs reservados, placeholders ou registros virtuais para as 1.800 restantes.

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

## Tranche 2 — OWASP Coraza WAF, OWASP Core Rule Set (CRS v4), Ory Hydra, Ory Kratos, Authelia, FiloSottile `age`, OWASP DefectDojo, Prowler, osquery e OISF Suricata (100 notas; revisão factual por IA registrada)

### OWASP Coraza WAF (motor de Web Application Firewall em Go, 5 fases de transação HTTP, linguagem SecLang, `SecRuleEngine`, `SecRequestBodyAccess`, `SecAuditLogFormat JSON` e proxy-wasm)

101. [OWASP Coraza WAF: arquitetura do Web Application Firewall em Go compatível com `SecLang` e OWASP CRS v4](../../domains/software-0009/software/seguranca/coraza-arquitetura-owasp-waf-go-seclang-compatibilidade-crs-v4.md)
102. [Coraza Ciclo de Vida de Transação (`tx`): as 5 fases de avaliação (`Request Headers`, `Request Body`, `Response Headers`, `Response Body`, `Logging`)](../../domains/software-0009/software/seguranca/coraza-ciclo-vida-transacao-cinco-fases-processamento-http.md)
103. [Coraza Diretivas Essenciais `SecLang`: `SecRuleEngine`, `SecRequestBodyAccess`, `SecResponseBodyAccess` e limites de memória](../../domains/software-0009/software/seguranca/coraza-diretivas-seclang-secruleengine-request-response-body-access.md)
104. [Coraza Audit Logging (`SecAuditEngine`, `SecAuditLogParts` e `SecAuditLogFormat`): saída estruturada em `JSON`, `OCSF` e `Native`](../../domains/software-0009/software/seguranca/coraza-audit-logging-secauditengine-parts-abcfhz-formatos-json-ocsf.md)
105. [Coraza em Proxies Cloud-Native: `coraza-proxy-wasm` (Envoy / Istio), `coraza-caddy`, Traefik e HAProxy SPOA](../../domains/software-0009/software/seguranca/coraza-integracoes-cloud-native-proxy-wasm-envoy-istio-caddy-traefik.md)
106. [Coraza Otimização de Performance e Build Tags: memoização de regex/Aho-Corasick, `WAF.Close()`, `SecRxPreFilter` e `no_regex_multiline`](../../domains/software-0009/software/seguranca/coraza-build-tags-otimizacao-memoization-multiphase-rx-prefilter.md)
107. [Coraza em Modo `FIPS 140-3` (`GODEBUG=fips140=on`): detecção em tempo de execução e restrição automática de `t:md5` e `t:sha1`](../../domains/software-0009/software/seguranca/coraza-modo-fips-140-3-restricao-transformacoes-md5-sha1.md)
108. [Coraza Body Processors (`JSON`, `XML`, `URLENCODED`, `MULTIPART`): parsing estruturado de payloads de APIs modernas na Fase 1 e Fase 2](../../domains/software-0009/software/seguranca/coraza-body-processors-json-xml-urlencoded-multipart-inspecao.md)
109. [Coraza SDK de Extensibilidade (`plugins`): registro de Operadores (`RegisterOperator`), Ações, Transformações e Audit Loggers customizados em Go](../../domains/software-0009/software/seguranca/coraza-extensibilidade-plugins-operators-actions-audit-loggers-go.md)
110. [Coraza Testes de Regressão de WAF (`go-ftw` e Coraza Playground): validação automatizada de regras SecLang em CI/CD](../../domains/software-0009/software/seguranca/coraza-testes-regressao-regras-ftw-go-ftw-playground-ci-cd.md)

### OWASP Core Rule Set — CRS v4 (conjunto de regras genéricas de detecção para WAFs, *Anomaly Scoring*, `blocking_paranoia_level` vs `detection_paranoia_level`, exclusões e `crs-toolchain`)

111. [OWASP CRS (Core Rule Set v4): arquitetura do conjunto de regras de detecção genérica para ModSecurity e Coraza](../../domains/software-0009/software/seguranca/owaspcrs-arquitetura-core-rule-set-v4-protecao-owasp-top-ten.md)
112. [OWASP CRS Anomaly Scoring Mode: detecção colaborativa (`setvar`) e bloqueio adiado em `949` (Inbound) e `959` (Outbound)](../../domains/software-0009/software/seguranca/owaspcrs-anomaly-scoring-mode-collaborative-detection-delayed-blocking.md)
113. [OWASP CRS Limiares de Anomalia e Severidades (`CRITICAL=5`, `ERROR=4`, `WARNING=3`, `NOTICE=2`): por que a meta de produção é Threshold `5`](../../domains/software-0009/software/seguranca/owaspcrs-thresholds-severidades-critical-error-warning-notice-calibragem.md)
114. [OWASP CRS Níveis de Paranoia (`PL1` a `PL4`): uso combinado de `tx.blocking_paranoia_level` e `tx.detection_paranoia_level`](../../domains/software-0009/software/seguranca/owaspcrs-paranoia-levels-pl1-a-pl4-blocking-vs-detection-paranoia-level.md)
115. [OWASP CRS Taxonomia Numerada de Regras (`901–999`): organização modular de `REQUEST-911..949` e `RESPONSE-950..959`](../../domains/software-0009/software/seguranca/owaspcrs-taxonomia-arquivos-regras-request-911-a-949-response-950-a-959.md)
116. [OWASP CRS Tuning de Falsos Positivos: `ctl:ruleRemoveTargetById` em tempo de execução (`BEFORE-CRS`) vs `SecRuleUpdateTargetById` (`AFTER-CRS`)](../../domains/software-0009/software/seguranca/owaspcrs-tratamento-falsos-positivos-ctl-ruleremovetargetbyid-before-after.md)
117. [OWASP CRS Rule Exclusion Packages e CRS v4 Plugins: perfis oficiais de exclusão para WordPress, Nextcloud, Drupal e cPanel](../../domains/software-0009/software/seguranca/owaspcrs-exclusion-packages-pre-construidos-wordpress-nextcloud-dokuwiki.md)
118. [OWASP CRS Políticas de Protocolo HTTP (`900200–900250` e `REQUEST-911`/`920`): restrição de métodos HTTP, `Content-Type` e versões TLS/HTTP](../../domains/software-0009/software/seguranca/owaspcrs-validacao-protocolo-http-911-920-metodos-content-type-charset.md)
119. [OWASP CRS Inspeção de Resposta Outbound (`RESPONSE-950` a `959`): bloqueio de vazamento de erros SQL, stack traces e web shells](../../domains/software-0009/software/seguranca/owaspcrs-inspecao-outbound-response-950-a-959-prevencao-vazamento-dados.md)
120. [OWASP CRS Sampling Mode (`tx.sampling_percentage`, Regra `900400`) e `coreruleset-cli`: rollout gradual por amostragem de tráfego](../../domains/software-0009/software/seguranca/owaspcrs-sampling-percentage-rollout-gradual-crs-setup-900400.md)

### Ory Hydra (servidor OAuth 2.0 e OpenID Connect Certified headless em Go, arquitetura *Login & Consent Flow* em 6 passos, `prompt=none`, revogação/introspecção RFC 7662 e rotação JWKS)

121. [Ory Hydra: arquitetura do servidor OAuth 2.0 e OpenID Connect Certificado (*OpenID Certified*) desacoplado de banco de usuários](../../domains/software-0009/software/seguranca/oryhydra-arquitetura-oauth2-openid-connect-certified-headless-server.md)
122. [Ory Hydra Login & Consent Flow: orquestração via `login_challenge`, `consent_challenge` e `skip` com sua própria UI](../../domains/software-0009/software/seguranca/oryhydra-fluxo-login-consent-challenge-verifier-delegacao-ui.md)
123. [Ory Hydra Gerenciamento de OAuth 2.0 Clients: `token_endpoint_auth_method`, obrigatoriedade de `PKCE` e escopos granulares](../../domains/software-0009/software/seguranca/oryhydra-gerenciamento-oauth2-clients-pkce-auth-methods-scopes.md)
124. [Ory Hydra Estratégias de Access Token (`opaque` vs `jwt`) e Token Introspection (`RFC 7662`)](../../domains/software-0009/software/seguranca/oryhydra-estrategias-access-token-opaque-vs-jwt-token-introspection-rfc7662.md)
125. [Ory Hydra Autenticação Machine-to-Machine (`M2M`): `client_credentials` (`RFC 6749`) e `jwt-bearer` (`RFC 7523`)](../../domains/software-0009/software/seguranca/oryhydra-client-credentials-rfc6749-rfc7523-jwt-bearer-m2m.md)
126. [Ory Hydra Gerenciamento e Rotação de Chaves Criptográficas (`JWKS`): conjuntos `hydra.openid.id-token` e `hydra.jwt.access-token`](../../domains/software-0009/software/seguranca/oryhydra-jwks-gerenciamento-chaves-assimetricas-rotacao-zero-downtime.md)
127. [Ory Hydra Logout Federado OpenID Connect: `RP-Initiated`, `Front-Channel Logout 1.0` e `Back-Channel Logout 1.0`](../../domains/software-0009/software/seguranca/oryhydra-oidc-frontchannel-backchannel-logout-revogacao-sessao.md)
128. [Ory Hydra Segurança de `Refresh Tokens`: rotação automática a cada uso e invalidação de toda a família em caso de *Replay*](../../domains/software-0009/software/seguranca/oryhydra-deteccao-reuso-refresh-token-rotacao-mitigacao-roubo.md)
129. [Ory Hydra em Produção: `hydra migrate sql`, limpeza de tokens expirados com `hydra janitor` e escalabilidade stateless](../../domains/software-0009/software/seguranca/oryhydra-operacao-producao-postgres-cockroachdb-migrate-janitor.md)
130. [Ory Hydra + Ory Kratos: arquitetura combinada de Identidade (`Kratos`) e Provedor OAuth2/OIDC (`Hydra`) como substituto de Auth0/Okta](../../domains/software-0009/software/seguranca/oryhydra-integracao-ory-kratos-arquitetura-idp-completo-drop-in.md)

### Ory Kratos (sistema cloud-native e headless de gerenciamento de identidades e usuários, JSON Schemas de `traits`, Self-Service Flows `Browser`/`API`, Passkeys/WebAuthn, MFA e Webhooks)

131. [Ory Kratos: arquitetura API-first de gerenciamento de identidades, credenciais e fluxos de autoatendimento (*Self-Service*)](../../domains/software-0009/software/seguranca/orykratos-arquitetura-api-first-identity-user-management-cloud-native.md)
132. [Ory Kratos Modelo de Identidade e `JSON Schema`: validação de `traits`, `credentials`, `metadata_public` e `metadata_admin`](../../domains/software-0009/software/seguranca/orykratos-modelo-identidade-json-schema-traits-metadata-public-admin.md)
133. [Ory Kratos Self-Service Flows (`login`, `registration`, `recovery`, `verification`, `settings`): arquitetura *Headless UI Nodes* para Browser e API](../../domains/software-0009/software/seguranca/orykratos-fluxos-self-service-browser-vs-api-ui-nodes-csrf.md)
134. [Ory Kratos Gerenciamento de Sessões (`/sessions/whoami`): validação por Cookie (`ory_kratos_session`), `X-Session-Token` e conversão para JWT](../../domains/software-0009/software/seguranca/orykratos-sessoes-whoami-cookies-session-token-caching-tokenizer.md)
135. [Ory Kratos Multi-Factor Authentication (`AAL1` vs `AAL2`): `Passkeys`, `WebAuthn` (FIDO2), `TOTP` e `lookup_secret` (códigos de backup)](../../domains/software-0009/software/seguranca/orykratos-mfa-aal1-aal2-webauthn-passkeys-totp-lookup-secrets.md)
136. [Ory Kratos Segurança de Credenciais `password`: hashing `Argon2id` (ou `bcrypt`), política de similaridade e checagem *Have I Been Pwned* (`k-Anonymity`)](../../domains/software-0009/software/seguranca/orykratos-seguranca-senhas-argon2id-haveibeenpwned-k-anonymity.md)
137. [Ory Kratos Fluxos de `Recovery` e `Verification`: códigos OTP (`code`) vs `link`, `courier` SMTP/HTTP e prevenção de enumeração de contas](../../domains/software-0009/software/seguranca/orykratos-recovery-verification-one-time-codes-link-anti-enumeration.md)
138. [Ory Kratos Actions & Webhooks (`before` / `after` hooks): interceptação e enriquecimento de fluxos com templates `Jsonnet`](../../domains/software-0009/software/seguranca/orykratos-webhooks-actions-before-after-hooks-jsonnet-sincronizacao.md)
139. [Ory Kratos Social Sign-In e Federação OIDC: mapeamento de claims de provedores externos (`Google`, `GitHub`, `Microsoft`, `GitLab`) via `Jsonnet`](../../domains/software-0009/software/seguranca/orykratos-social-sign-in-oidc-federation-jsonnet-data-mapping.md)
140. [Ory Kratos Migração de Identidades sem Reset de Senha (`POST /admin/identities`): importação de hashes `bcrypt`, `argon2`, `pbkdf2` e `scrypt`](../../domains/software-0009/software/seguranca/orykratos-importacao-migracao-identidades-hashes-bcrypt-argon2-pbkdf2.md)

### Authelia (portal open-source de Single Sign-On e 2FA/WebAuthn acoplado a Reverse Proxies, motor de Access Control em 7 dimensões de especificidade, `bypass`/`one_factor`/`two_factor` e OIDC)

141. [Authelia: arquitetura do servidor open-source de autenticação, 2FA, controle de acesso (`ForwardAuth`) e provedor OpenID Connect 1.0](../../domains/software-0009/software/seguranca/authelia-arquitetura-portal-autenticacao-autorizacao-forwardauth-oidc.md)
142. [Authelia `access_control`: políticas `deny`, `bypass`, `one_factor` e `two_factor` e avaliação sequencial *first-match*](../../domains/software-0009/software/seguranca/authelia-access-control-policies-deny-bypass-one-factor-two-factor.md)
143. [Authelia Critérios Granulares de Regra: `domain`, `domain_regex`, `resources`, `subject` (`AND`/`OR`), `methods` e `query`](../../domains/software-0009/software/seguranca/authelia-criterios-regras-domain-regex-resources-subject-methods-query.md)
144. [Authelia `authelia access-control check-policy`: validação determinística de regras de autorização na linha de comando e CI/CD](../../domains/software-0009/software/seguranca/authelia-teste-politicas-cli-access-control-check-policy-ci.md)
145. [Authelia Backends de Autenticação (`authentication_backend`): integração com `LDAP` (Active Directory / OpenLDAP / FreeIPA) e `file` (`Argon2id`)](../../domains/software-0009/software/seguranca/authelia-backends-autenticacao-ldap-active-directory-file-argon2id.md)
146. [Authelia Segundo Fator (`2FA`): configuração de `WebAuthn` (FIDO2 / YubiKey / Passkeys), `TOTP` e notificações `Duo Push`](../../domains/software-0009/software/seguranca/authelia-mfa-webauthn-passkeys-totp-duo-push-configuracao.md)
147. [Authelia Sessões e Persistência de Produção: `session.redis` (HA Sentinel/Cluster) e `storage.postgres` com `encryption_key`](../../domains/software-0009/software/seguranca/authelia-session-redis-sentinel-cluster-storage-postgres-encryption-key.md)
148. [Authelia `regulation`: proteção integrada contra ataques de força bruta com `max_retries`, `find_time` e `ban_time`](../../domains/software-0009/software/seguranca/authelia-regulation-protecao-forca-bruta-max-retries-find-time-ban-time.md)
149. [Authelia como Provedor OpenID Connect 1.0 (`identity_providers.oidc`): proteção de aplicações nativas OIDC (Grafana, Argo CD, GitLab)](../../domains/software-0009/software/seguranca/authelia-openid-connect-provider-clients-authorization-policies-pkce.md)
150. [Authelia Gestão Segura de Segredos (`_FILE` e Templates): injeção de credenciais via arquivos Kubernetes Secrets sem expor texto claro](../../domains/software-0009/software/seguranca/authelia-gestao-segredos-variaveis-ambiente-file-filters-templates-k8s.md)

### FiloSottile `age` (ferramenta, formato `age-encryption.org/v1` e biblioteca Go `filippo.io/age` para criptografia moderna de arquivos com `X25519`, `ChaCha20-Poly1305` `STREAM`, chaves SSH, `scrypt` e plugins)

151. [FiloSottile `age`: arquitetura da ferramenta e formato moderno de criptografia de arquivos (`X25519`, `ChaCha20-Poly1305` e `STREAM`)](../../domains/software-0009/software/seguranca/agecrypt-arquitetura-filosottile-age-criptografia-arquivos-x25519-chacha20.md)
152. [`age` Gerenciamento de Chaves (`age-keygen`) e Múltiplos Destinatários (`-r` e `-R recipients.txt`)](../../domains/software-0009/software/seguranca/agecrypt-chaves-nativas-age-keygen-bech32-multiplos-destinatarios-recipients-file.md)
153. [`age` Criptografia para Chaves SSH Existentes (`ssh-ed25519` e `ssh-rsa`): envio seguro usando `~/.ssh/id_ed25519.pub` ou `github.com/<user>.keys`](../../domains/software-0009/software/seguranca/agecrypt-criptografia-chaves-ssh-ed25519-rsa-github-keys.md)
154. [`age` Criptografia por Passphrase (`-p` / `--passphrase` com `scrypt`) e Identidades Protegidas por Senha](../../domains/software-0009/software/seguranca/agecrypt-passphrase-scrypt-protecao-chaves-identidade-em-repouso.md)
155. [`age` ASCII Armor (`-a` / `--armor`): codificação PEM canônica estrita (`AGE ENCRYPTED FILE`) e proteção de TTY](../../domains/software-0009/software/seguranca/agecrypt-ascii-armor-pem-strict-base64-protecao-tty.md)
156. [`age` Criptografia Simétrica para Arquivo de Identidade (`age --encrypt -i key.txt`): backups sem gerenciar chave pública separada](../../domains/software-0009/software/seguranca/agecrypt-criptografia-simetrica-com-arquivo-identidade-encrypt-i.md)
157. [`age` Sistema de Plugins (`age-plugin-*` e `-j`): chaves em hardware com `age-plugin-yubikey`, Secure Enclave e TPM](../../domains/software-0009/software/seguranca/agecrypt-plugins-hardware-yubikey-fido2-kms-arquitetura-extensivel.md)
158. [`age` Criptografia Pós-Quântica Híbrida e Verificação de Binários com `Sigsum`: proteção contra *Harvest Now, Decrypt Later*](../../domains/software-0009/software/seguranca/agecrypt-suporte-pos-quantico-pq-ml-kem-x25519-especificacao-c2sp.md)
159. [`age` como Biblioteca Nativa em Go (`filippo.io/age`): `age.Encrypt`, `age.Decrypt` e `armor` em aplicações sem processos externos](../../domains/software-0009/software/seguranca/agecrypt-biblioteca-go-filippo-io-age-encrypt-decrypt-streams.md)
160. [`age` em Pipelines GitOps e Dotfiles: integração com `SOPS` (`SOPS_AGE_KEY_FILE`), `Flux CD`, `Argo CD`, `passage` e `chezmoi`](../../domains/software-0009/software/seguranca/agecrypt-integracao-gitops-sops-flux-argocd-chezmoi-pass.md)

### OWASP DefectDojo (plataforma open-source de ASPM e gestão unificada de vulnerabilidades com 500+ parsers, hierarquia `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding`, `reimport-scan` e deduplicação)

161. [OWASP DefectDojo: arquitetura da plataforma open-source de ASPM e gestão unificada de vulnerabilidades com 500+ parsers](../../domains/software-0009/software/seguranca/defectdojo-arquitetura-owasp-aspm-vulnerability-management-500-parsers.md)
162. [DefectDojo Modelo de Dados Hierárquico: `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding` e `Endpoint`](../../domains/software-0009/software/seguranca/defectdojo-modelo-hierarquico-product-type-product-engagement-test-finding.md)
163. [DefectDojo `import-scan` vs `reimport-scan`: automação de pipelines CI/CD com fechamento automático de vulnerabilidades corrigidas](../../domains/software-0009/software/seguranca/defectdojo-api-v2-import-scan-vs-reimport-scan-ciclo-vida-ci-cd.md)
164. [DefectDojo Algoritmos de Deduplicação (`HASH_CODE`, `UNIQUE_ID_FROM_TOOL`, `LEGACY`): eliminação de duplicatas intra-scanner e cross-scanner](../../domains/software-0009/software/seguranca/defectdojo-deduplicacao-algoritmos-hash-code-unique-id-from-tool.md)
165. [DefectDojo Fluxo de Triagem e `Risk Acceptance`: estados `Active`, `Verified`, `False Positive`, `Out of Scope` e Aceite Formal de Risco](../../domains/software-0009/software/seguranca/defectdojo-triagem-findings-verified-false-positive-out-of-scope-risk-acceptance.md)
166. [DefectDojo SLA Engine (`SLA Configuration`): prazos de remediação por severidade (`Critical`, `High`, `Medium`, `Low`) e alertas de violação](../../domains/software-0009/software/seguranca/defectdojo-sla-configuration-enforcement-severidade-notificacoes-atraso.md)
167. [DefectDojo Integração Bidirecional com Jira: criação automática de Issues, sincronização de comentários e fechamento por resolução](../../domains/software-0009/software/seguranca/defectdojo-integracao-bidirecional-jira-sincronizacao-status-comentarios.md)
168. [DefectDojo Arquitetura de Produção: papéis dos componentes `nginx`, `uwsgi` (Django), `celeryworker`, `celerybeat`, `postgres` e `redis`/`valkey`](../../domains/software-0009/software/seguranca/defectdojo-arquitetura-servicos-nginx-uwsgi-celery-beat-worker-postgres-redis.md)
169. [DefectDojo Ingestão Universal: uso nativo de relatórios `SARIF` e criação de parsers customizados para ferramentas internas](../../domains/software-0009/software/seguranca/defectdojo-universal-parser-sarif-conectores-customizados-ingestao.md)
170. [DefectDojo Governança de Acesso (`RBAC`, `Product Type Members` e `SSO` OIDC/SAML/LDAP): isolamento de visibilidade por equipe](../../domains/software-0009/software/seguranca/defectdojo-rbac-product-members-groups-sso-oidc-saml-governanca.md)

### Prowler (plataforma open-source de Cloud Security Posture Management — CSPM multi-cloud para AWS, Azure, GCP, Kubernetes, M365 e GitHub, *Attack Paths* com Cartography/Neo4j, `Mutelist` e saída OCSF)

171. [Prowler: arquitetura da plataforma open-source de segurança e conformidade multi-cloud (`AWS`, `Azure`, `GCP`, `Kubernetes`, `M365`, `GitHub`)](../../domains/software-0009/software/seguranca/prowler-arquitetura-open-cloud-security-platform-cspm-multi-cloud.md)
172. [Prowler Frameworks de Conformidade (`--compliance`) e `Prowler ThreatScore`: auditoria automatizada `CIS`, `NIST`, `PCI-DSS`, `SOC2`, `ISO 27001` e `MITRE ATT&CK`](../../domains/software-0009/software/seguranca/prowler-compliance-frameworks-cis-nist-pci-dss-soc2-iso27001-nis2-ens.md)
173. [Prowler `Attack Paths`: análise de caminhos de ataque combinando inventário `Cartography` com achados do Prowler em `Neo4j` ou `Amazon Neptune`](../../domains/software-0009/software/seguranca/prowler-attack-paths-cartography-neo4j-amazon-neptune-grafos.md)
174. [Prowler Filtragem Granular de Execução: `--checks`, `--services`, `--severity`, `--category` e `--region` / `--excluded-checks`](../../domains/software-0009/software/seguranca/prowler-selecao-granular-checks-services-severities-categories-regions.md)
175. [Prowler `Mutelist` (`-w` / `--mutelist-file`): gerenciamento declarativo de exceções por conta, região, check, recurso e tags](../../domains/software-0009/software/seguranca/prowler-mutelist-yaml-supressao-excecoes-accounts-regions-resources-tags.md)
176. [Prowler para Kubernetes (`prowler kubernetes`): auditoria CIS Kubernetes Benchmark, RBAC, Pod Security e NetworkPolicies](../../domains/software-0009/software/seguranca/prowler-auditoria-kubernetes-clusters-kubeconfig-in-cluster-rbac-pss.md)
177. [Prowler SaaS, IaC e Containers (`github`, `m365`, `googleworkspace`, `okta`, `iac`, `image`): postura unificada além da IaaS](../../domains/software-0009/software/seguranca/prowler-saas-github-m365-googleworkspace-okta-iac-containers.md)
178. [Prowler Formatos de Saída (`json-ocsf`, `json-asff`, `html`, `csv`) e Integração Nativa com `AWS Security Hub` e `S3`](../../domains/software-0009/software/seguranca/prowler-formatos-saida-ocsf-asff-security-hub-s3-defectdojo.md)
179. [Prowler Varreduras Multi-Conta em Escala: `AWS AssumeRole` (`-R`), `AWS Organizations` (`-O`), Subscrições Azure e Projetos GCP](../../domains/software-0009/software/seguranca/prowler-multi-account-aws-organizations-assume-role-azure-subscriptions-gcp.md)
180. [Prowler Extensibilidade: criação de Checks Customizados (`--checks-folder`), `Check Metadata Guidelines` e servidor `Prowler MCP`](../../domains/software-0009/software/seguranca/prowler-custom-checks-python-metadata-guidelines-prowler-mcp-ai.md)

### osquery (instrumentação e monitoramento de sistema operacional orientado a SQL para Linux, macOS e Windows, `osqueryi` vs `osqueryd`, logs diferenciais via RocksDB, `Query Packs`, `FIM` e `Watchdog`)

181. [osquery: arquitetura do framework que expõe o sistema operacional (`Linux`, `macOS`, `Windows`) como um banco relacional SQL](../../domains/software-0009/software/seguranca/osquery-arquitetura-sistema-operacional-banco-relacional-sql-sqlite.md)
182. [osquery `osqueryi` vs `osqueryd`: exploração interativa ad-hoc versus monitoramento contínuo agendado por daemon](../../domains/software-0009/software/seguranca/osquery-osqueryi-vs-osqueryd-shell-interativo-daemon-agendamento.md)
183. [osquery Logs Diferenciais (`added` / `removed` via RocksDB) vs `snapshot: true`: como o `osqueryd` detecta mudanças de estado sem inundar o SIEM](../../domains/software-0009/software/seguranca/osquery-differential-logs-added-removed-vs-snapshot-queries-rocksdb.md)
184. [osquery `Query Packs`: agrupamento modular de queries de detecção com filtros `platform`, `version`, `shard` e `discovery`](../../domains/software-0009/software/seguranca/osquery-query-packs-organizacao-modular-discovery-queries-platform-version.md)
185. [osquery Evented Tables e File Integrity Monitoring (`FIM`): captura em tempo real via `auditd`/`ebpf`/`inotify`/`EndpointSecurity`](../../domains/software-0009/software/seguranca/osquery-evented-tables-file-integrity-monitoring-fim-process-socket-events.md)
186. [osquery Resource Watchdog e Auto-Denylist: garantia de que o agente nunca degrade a CPU ou a memória do host de produção](../../domains/software-0009/software/seguranca/osquery-watchdog-protecao-recursos-cpu-memoria-denylist-queries.md)
187. [osquery para Segurança de Containers e Servidores Linux: tabelas `docker_containers`, `docker_images`, `process_namespaces` e `iptables`](../../domains/software-0009/software/seguranca/osquery-auditoria-containers-docker-namespaces-systemd-linux-secops.md)
188. [osquery Gerenciamento Centralizado de Frota (`TLS Enrollment`, `Fleet`, `osctrl` e `Zentral`): distribuição remota de configuração e Live Queries](../../domains/software-0009/software/seguranca/osquery-gerenciamento-frota-tls-enrollment-fleet-osctrl-zentral.md)
189. [osquery + `YARA` (`yara` e `yara_events`): busca de assinaturas de malware sob demanda e acoplada ao File Integrity Monitoring](../../domains/software-0009/software/seguranca/osquery-integracao-yara-tabelas-yara-yara-events-varredura-memoria-arquivos.md)
190. [osquery Extensions (`Thrift` API) e Logger Plugins (`filesystem`, `syslog`, `aws_kinesis`, `aws_firehose`, `kafka_producer`)](../../domains/software-0009/software/seguranca/osquery-extensoes-thrift-sdk-go-python-logger-plugins-aws-kinesis-kafka.md)

### OISF Suricata (motor multi-threaded de alta performance para `IDS`, `IPS` inline e `Network Security Monitoring — NSM`, telemetria unificada `eve.json`, `suricata-update`, *Sticky Buffers*, `JA3`/`JA4` e `file-store`)

191. [OISF Suricata: arquitetura multi-thread de alta performance para `IDS`, `IPS` e `Network Security Monitoring (NSM)`](../../domains/software-0009/software/seguranca/suricata-arquitetura-oisf-network-ids-ips-nsm-multithreaded.md)
192. [Suricata `EVE JSON` (`eve.json`): telemetria unificada de alertas, fluxos (`flow`), `dns`, `http`, `tls`, `ssh`, `smb` e `fileinfo`](../../domains/software-0009/software/seguranca/suricata-eve-json-log-unificado-alert-flow-dns-http-tls-fileinfo.md)
193. [Suricata Gerenciamento de Regras (`suricata-update`): atualização automatizada do *Emerging Threats Open (ET Open)* e tuning via `enable.conf`/`disable.conf`/`modify.conf`](../../domains/software-0009/software/seguranca/suricata-gerenciamento-regras-suricata-update-et-open-fontes.md)
194. [Suricata Linguagem de Regras e *Sticky Buffers*: escrita de assinaturas de camada 7 (`http.uri`, `http.user_agent`, `dns.query`, `tls.sni`)](../../domains/software-0009/software/seguranca/suricata-anatomia-regras-assinaturas-sticky-buffers-http-dns-tls.md)
195. [Suricata Inspeção de Tráfego Criptografado TLS: fingerprinting de clientes/servidores (`JA3`, `JA3S`, `JA4`), `tls.sni` e certificados X.509](../../domains/software-0009/software/seguranca/suricata-inspecao-tls-fingerprinting-ja3-ja4-sni-certificados-c2.md)
196. [Suricata em Modo IPS Inline (`AF_PACKET` Layer 2 Bridge e `NFQUEUE`): bloqueio ativo de ataques com ações `drop` e `reject`](../../domains/software-0009/software/seguranca/suricata-modo-ips-inline-af-packet-nfqueue-acao-drop-reject.md)
197. [Suricata File Extraction e Hashing (`file-store` v2 e `fileinfo`): cálculo de SHA-256 em tempo real e captura forense de arquivos trafegados](../../domains/software-0009/software/seguranca/suricata-file-extraction-file-store-sha256-deteccao-malware-rede.md)
198. [Suricata Performance Multi-Gigabit (`runmode: workers`, `AF_PACKET`, `eBPF` Bypass e `Hyperscan`): eliminação de perda de pacotes (`kernel_drops`)](../../domains/software-0009/software/seguranca/suricata-tuning-performance-runmodes-workers-af-packet-ebpf-hyperscan.md)
199. [Suricata Análise Forense de `PCAP` (`-r`) e Automação via Unix Socket (`suricatasc`): processamento em lote de capturas de tráfego](../../domains/software-0009/software/seguranca/suricata-analise-offline-pcap-replay-regressao-ci-unix-socket.md)
200. [Suricata `Datasets`, `Thresholds`, `Suppress` e `Flowbits`: correlação de estado entre pacotes, listas dinâmicas e controle de ruído](../../domains/software-0009/software/seguranca/suricata-datasets-thresholding-suppress-rate-filter-correlacao-ioc.md)

## Critérios e próximo passo

As 200 notas 1–200 das tranches 1–2 têm revisão factual por IA registrada nos relatórios vinculados. O lote continua incompleto: são 200/2.000 notas válidas, restando 1.800 notas materiais.
