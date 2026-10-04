# Reconciliação Estrutural — `software-seguranca-2000-0003` (Tranche 01: Notas 1–100)

Data: `2026-10-03`
Lote: `software-seguranca-2000-0003` (`knowledge-federation/domains/software-0009/software/seguranca/`)
Status do lote: `in_progress` (**100 / 2.000** notas substantivas qualificadas — **5,00%**)

## 1. Escopo reconciliado nesta tranche

Abertura do **3º lote de escala (`software-seguranca-2000-0003`)** com a materialização e revisão factual por IA das **100 primeiras notas (IDs 1–100)** em `knowledge-federation/domains/software-0009/software/seguranca/`, cobrindo 10 famílias de ferramentas de Engenharia de Segurança, AppSec, Supply Chain Security e IAM/Autorização:

1. **Gitleaks** (IDs `1–10`): modos `git`/`dir`/`stdin`, precedência de configuração em 4 níveis, `[extend]`, `[allowlist]`, fingerprints `.gitleaksignore`, `--baseline-path`, `--max-decode-depth`/`--max-archive-depth`, `--diagnostics` e nota de transição Betterleaks.
2. **TruffleHog** (IDs `11–20`): 4 pilares (Discovery, Classification, Validation, Analysis), verificação ativa de credenciais vivas (`--results=verified,unknown`), `trufflehog analyze`, escopo Git (`--since-commit`, `--fail` exit code `183`), múltiplos alvos, verificação criptográfica Sigstore Cosign, detectores customizados Regex + Webhook e pipeline Aho-Corasick.
3. **Google OSV-Scanner V2** (IDs `21–30`): motor `OSV-Scalibr` + banco `OSV.dev`, varredura de código-fonte/lockfiles, imagens de container (`--archive` / `--serve`), *Call Analysis* (alcançabilidade em Go e Rust), remediação guiada (`osv-scanner fix` com estratégias `in-place`, `relax` e `override`), auditoria de licenças SPDX, banco offline e configuração `osv-scanner.toml`.
4. **OWASP Dependency-Track** (IDs `31–40`): plataforma contínua API-first de análise de SBOM CycloneDX, upload `/api/v1/bom` (`autoCreate=true`), inteligência multi-fonte (NVD, OSV, GitHub Advisories) + probabilidade de exploração **EPSS**, triagem e exportação **VEX**, **Policy Engine** (segurança, licenças e operacional), análise de impacto em portfólio e RBAC/OIDC.
5. **OWASP ZAP (Zed Attack Proxy)** (IDs `41–50`): arquitetura Passive/Active Scanner, **Automation Framework** declarativo em arquivo YAML único (`env` + `jobs`), descoberta (`spider`, `spiderAjax`, `spiderClient`), importação de contratos de API (`openapi`, `graphql`, `soap`, `postman`), autenticação (`browser`, `autodetect`, `replacer`), sincronização `passiveScan-wait`, ajuste de `activeScan-policy`, `alertFilter`, *Job Tests*, `report` SARIF e `exitStatus`.
6. **ProjectDiscovery Nuclei** (IDs `51–60`): motor de templates YAML com zero falsos positivos, anatomia de `info`/`matchers`/`extractors`, filtragem (`-tags`, `-etags`, `-severity`, `-as`), varredura multi-protocolo (`dns`, `ssl`, `tcp`, `whois`), Workflows e `flow:`, detecção Out-of-Band (OAST) com `Interactsh` (`{{interactsh-url}}`), scans autenticados (`-sf`), *Request Clustering* e exportação SARIF/Markdown/Jira.
7. **OpenFGA** (IDs `61–70`): motor de autorização CNCF Incubating inspirado no Google Zanzibar, conceitos (`Store`, `Type`, `Object`, `User`/`userset`, `Relation`, `Relationship Tuple`), DSL `schema 1.1` (`or`, `and`, `but not`, `from`), Conditions CEL e Contextual Tuples (ABAC híbrido), APIs `Check`/`BatchCheck`/`ListObjects`/`ListUsers`/`Expand`, testes `fga model test`, Modular Models (`fga.mod`), `openfga migrate` (PostgreSQL/MySQL) e `ConsistencyPreference`.
8. **AuthZed SpiceDB** (IDs `71–80`): banco de dados de permissões distribuído inspirado no Google Zanzibar, linguagem de schema `.zed` (`definition`, `relation` substantivo vs `permission` verbo computado), operadores `+`, `&`, `-`, `->` (e precedência histórica do `+`), `caveat` CEL, consistência com `ZedToken` (`minimize_latency`, `at_least_as_fresh`, `fully_consistent`), `LookupResources`/`LookupSubjects`, `zed validate`, datastores (`postgres`, `cockroachdb`, `spanner`, `mysql`), *Consistent Hashing Dispatch* no Kubernetes e `Watch` API.
9. **Cerbos PDP** (IDs `81–90`): Policy Decision Point stateless para PBAC/ABAC/RBAC, os 6 tipos de política YAML (`resourcePolicy`, `derivedRoles`, `principalPolicy`, `rolePolicy`, `exportVariables`, `exportConstants`), evolução RBAC -> ABAC via `derivedRoles`, API em lote `CheckResources`, API de *Query Plan* `PlanResources` (AST de filtros para Prisma/SQLAlchemy/GORM), *Scoped Policies* multi-tenant, `cerbos compile`, verificação nativa de JWT/JWKS em `auxData` e Audit Decision Logs.
10. **OpenSSF Scorecard** (IDs `91–100`): avaliação automatizada de segurança em supply chain open-source, `Branch-Protection` em 5 Tiers e `Code-Review`, `Binary-Artifacts`, `Token-Permissions` e `Dangerous-Workflows` em GitHub Actions, `Pinned-Dependencies` por hash SHA, `Signed-Releases` e `Packaging` (SLSA Provenance), `SAST`/`Fuzzing`/`Vulnerabilities`/`Dependency-Update-Tool`, `Maintained`/`Security-Policy`/`License`/`CII-Best-Practices`, `ossf/scorecard-action` SARIF e *Structured Results (Probes V5)* / API REST / BigQuery.

## 2. Verificação de integridade e reconciliação de contagens

| Indicador | Antes da Tranche 01 | Após a Tranche 01 |
|---|---:|---:|
| Lotes completos (`2.000/2.000`) | `2 / 500` (`software-testes-2000-0001` e `software-devops-2000-0002`) | `2 / 500` (`software-testes-2000-0001` e `software-devops-2000-0002`) |
| Notas válidas em `software-seguranca-2000-0003` | `0 / 2.000 (0,00%)` | `100 / 2.000 (5,00%)` (`in_progress`) |
| Aprovações humanas históricas globais | `49` | `49` (inalteradas) |
| Revisões factuais por IA globais | `3991` | `4091` (`+100`) |
| Total global de notas válidas (`gate + revisão`) | `4040 / 1.000.000 (0,4040%)` | `4140 / 1.000.000 (0,4140%)` |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | `4140` | `4240` (`4140` válidas + `100` legadas pendentes) |

## 3. Artefatos sincronizados

- Manifesto do lote 3: [`software-seguranca-2000-0003.md`](../batches/software-seguranca-2000-0003.md)
- MOC do lote 3: [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)
- Relatório factual por IA da Tranche 01: [`ai-review-software-seguranca-2000-0003-tranche-01.md`](ai-review-software-seguranca-2000-0003-tranche-01.md)
- Auditoria de qualidade do lote 3: [`note-quality-software-seguranca-2000-0003.md`](note-quality-software-seguranca-2000-0003.md)
- Fila global de revisões: [`human-review-queue.md`](human-review-queue.md) (linhas `4041–4140` registradas como `APROVADA POR IA`)
