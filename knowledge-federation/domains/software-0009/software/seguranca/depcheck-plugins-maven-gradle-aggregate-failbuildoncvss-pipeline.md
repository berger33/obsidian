---
id: software.seguranca.tranche16.001514
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md", "https://dependency-check.github.io/DependencyCheck/general/internals.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Plugins Nativos **Maven (`dependency-check-maven`)** e **Gradle (`org.owasp.dependencycheck`)**: Goal **`aggregate`** e Quality Gate **`failBuildOnCVSS`**

## Em uma frase
Por que, em projetos **Java / Kotlin / Scala** construídos com **Maven** ou **Gradle**, é muito melhor executar o **OWASP Dependency-Check como um Plugin de Build (`mvn dependency-check:aggregate` / `./gradlew dependencyCheckAggregate`)** do que rodar o script CLI `dependency-check.sh` sobre uma pasta de arquivos `.jar` soltos?

## Por que importa
Porque dentro do Maven ou Gradle, o plugin tem acesso direto à **Árvore de Resolução de Dependências Completa (`GroupId : ArtifactId : Version` — `GAV` e `Package URL / PURL`)**, sabendo exatamente quais dependências são de escopo `compile`/`runtime` vs. `test`/`provided` e evitando adivinhações heurísticas sobre arquivos `.jar`!

## Como funciona
Além disso, em projetos **Multi-Módulo (Monorepos Maven/Gradle)**, o goal **`aggregate` (`dependencyCheckAggregate`)** analisa todos os submódulos de uma só vez e consolida um único relatório unificado, enquanto o parâmetro **`failBuildOnCVSS`** (ex.: `failBuildOnCVSS=7.0`) quebra automaticamente a pipeline se surgir qualquer CVE de severidade **Alta ou Crítica (`CVSS >= 7.0`)**!

## Exemplo
```bash
# Executar o plugin Maven do OWASP Dependency-Check em modo aggregate quebrando o build se houver vulnerabilidade com CVSS >= 7.0
mvn org.owasp:dependency-check-maven:check \
  -DfailBuildOnCVSS=7.0 \
  -DskipTestScope=true \
  -Dformats=HTML,JSON,SARIF
```

## Limites e trade-offs
Atenção ao aviso importante do `README.md` oficial sobre ambientes **Gradle (`9.0.0+`)**: se outros plugins antigos do seu `build.gradle` puxarem versões obsoletas transitivas do `jackson-bom`, `commons-lang3` ou `commons-text`, o Gradle pode lançar `NoSuchMethodError`. A solução documentada no `README.md` é fixar as versões mínimas em `/buildSrc/build.gradle` via `dependencies { constraints { ... } }`!

## Como verificar
Use sempre `-DskipTestScope=true` (que já é o padrão no plugin Maven) para focar o *Quality Gate* `failBuildOnCVSS` nas dependências que realmente embarcam no artefato de produção.

## Conexões
- [[depcheck-analisadores-ecossistemas-jar-dotnet-npm-golang-python-experimental]] — Veja também: Analisadores Multi-Linguagem do OWASP Dependency-Check: **Java (`JarAnalyzer` / Maven / Gradle)**, **.NET 8**, **Go (`go.mod`)**, **Node.js (`npm audit`)**, **Ruby (`bundle-audit`)** e **Elixir (`mix_audit`)**.
- [[depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl]] — Veja também: Triagem e Supressão Auditável de Falsos Positivos no OWASP Dependency-Check: Arquivo **`suppressions.xml` (`--suppression`)**, `packageUrl`, `cpe`, `cve` e `until`.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Referência cruzada direta com depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
