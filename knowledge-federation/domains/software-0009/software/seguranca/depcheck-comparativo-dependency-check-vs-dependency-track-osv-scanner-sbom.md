---
id: software.seguranca.tranche16.001520
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

# Arquitetura Comparada de SCA: Quando Usar **OWASP Dependency-Check** vs. **OWASP Dependency-Track (SBOM CycloneDX)** vs. **OSV-Scanner / `pip-audit` / `govulncheck`**

## Em uma frase
Uma dúvida clássica de arquitetos de AppSec: a própria fundação OWASP mantém dois projetos com nomes parecidos — o **OWASP Dependency-Check** e o **OWASP Dependency-Track** — além de existirem scanners modernos como **OSV-Scanner**, **`pip-audit`** e **`govulncheck`**. Qual é a diferença exata entre eles e como eles se complementam?

## Por que importa
Veja a distinção arquitetural clara: **(1) OWASP Dependency-Check** é um **Scanner de Linha de Comando / Plugin de Build (Point-in-Time)** que brilha especialmente ao **inspecionar diretórios de artefatos binários legados (`.jar`, `.war`, `.ear`, `.dll`, `.js` soltos)** extraindo evidências para achar CPEs mesmo quando não existe um SBOM ou lockfile limpo!

## Como funciona
Já **(2) OWASP Dependency-Track** é uma **Plataforma Contínua de Monitoramento de Portfólio (Servidor Web + API)** que ingere **SBOMs (`CycloneDX`)** e monitora 24x7 todas as versões em produção contra novas CVEs; enquanto **(3) `govulncheck` / `pip-audit` / `OSV-Scanner`** usam bancos de dados nativos de ecossistema (`OSV` / `PyPA` / `vuln.go.dev`) e análise de grafo de chamadas (*Reachability Analysis*)!

## Exemplo
```bash
# Exemplo de estrategia combinada no CI: escanear binarios/empacotamento com Dependency-Check e verificar o JSON gerado com jq
dependency-check.sh --noupdate --project "App-Legado-EAR" --scan ./dist/app.ear --format JSON --out ./out
jq '.dependencies[] | select(.vulnerabilities != null) | {fileName, vulnerabilities: [.vulnerabilities[].name]}' ./out/dependency-check-report.json
```

## Limites e trade-offs
Portanto, a recomendação de arquitetura para organizações maduras é: **(A)** Nos repositórios modernos com lockfiles, gere o **SBOM CycloneDX** no build, envie para o **OWASP Dependency-Track** e rode scanners com análise de alcançabilidade (como **`govulncheck`** em Go e **`pip-audit`** em Python); e **(B)** Use o **OWASP Dependency-Check** para auditar pacotes binários (`EAR`/`WAR`/`JAR`/`.NET Assemblies`/assets JS estáticos) e entregas de fornecedores!

## Como verificar
Com isso fechamos o módulo do **OWASP Dependency-Check** na Tranche 16!

## Conexões
- [[depcheck-formatos-relatorio-sarif-junit-json-gitlab-defectdojo-github]] — Veja também: Integração de Relatórios do OWASP Dependency-Check (`SARIF`, `JUnit`, `JSON`, `HTML`, `CSV`, `XML`) com **GitHub Code Scanning, GitLab e OWASP DefectDojo**.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev]] — Referência cruzada direta com govulncheck-arquitetura-analise-alcancabilidade-call-graph-vuln-go-dev.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
