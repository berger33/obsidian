---
id: software.seguranca.tranche16.001513
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

# Analisadores Multi-Linguagem do OWASP Dependency-Check: **Java (`JarAnalyzer` / Maven / Gradle)**, **.NET 8**, **Go (`go.mod`)**, **Node.js (`npm audit`)**, **Ruby (`bundle-audit`)** e **Elixir (`mix_audit`)**

## Em uma frase
Quais ferramentas de build e runtimes precisam estar presentes no runner de CI/CD para que o **OWASP Dependency-Check** consiga analisar com precisão projetos **.NET, Go, Node.js (`npm`/`pnpm`/`yarn`), Ruby e Elixir**, além de pacotes Java?

## Por que importa
A seção *Requirements -> Build Tools* do `README.md` oficial detalha os requisitos exatos de cada analisador: **(1) `.NET Assemblies`**: o runtime ou SDK do **`.NET 8`** deve estar instalado na máquina que executa o scan (mesmo para analisar assemblies compilados para outras versões do .NET!); **(2) `GoLang`**: o binário **`go`** deve estar instalado para inspecionar `go.mod` e metadados de build.

## Como funciona
**(3) `Node.js` (`npm`, `pnpm`, `yarn`)**: o respectivo gerenciador de pacotes deve estar instalado porque o analisador invoca a API de `audit` nativa dele; **(4) `Ruby`**: requer o **`bundle-audit`** instalado; e **(5) `Elixir`**: requer o **`mix_audit`** instalado (ativando `--enableExperimental` quando aplicável)!

## Exemplo
```bash
# Executar o Dependency-Check habilitando analisadores experimentais (--enableExperimental) e excluindo pastas de testes/mocks (--exclude)
dependency-check.sh \
  --project "Monorepo-Poliglota" \
  --scan . \
  --exclude "**/test/**" \
  --exclude "**/node_modules/.cache/**" \
  --enableExperimental \
  --out ./relatorio-poliglota
```

## Limites e trade-offs
Por que usar **`--exclude "**/test/**"`** (ou configurar o escopo `skipTestScope=true` no plugin Maven/Gradle) é altamente recomendado? Porque bibliotecas usadas exclusivamente em testes unitários locais (que nunca são empacotadas no artefato `.jar` / container de produção!) frequentemente geram alertas que desviam o foco das vulnerabilidades reais que vão para produção!

## Como verificar
Se você estiver escaneando apenas um projeto Java/Kotlin puro e quiser acelerar a execução, você pode desativar analisadores desnecessários com flags como `--disableNodeJS`, `--disableAssembly` ou `--disableRetireJS`.

## Conexões
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Veja também: Integração com a **API v2 do NIST NVD (`--nvdApiKey`)**, Cache de Banco **H2** e Estratégia de Espelhamento em CI/CD no OWASP Dependency-Check.
- [[depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline]] — Veja também: Plugins Nativos **Maven (`dependency-check-maven`)** e **Gradle (`org.owasp.dependencycheck`)**: Goal **`aggregate`** e Quality Gate **`failBuildOnCVSS`**.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
