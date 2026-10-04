---
id: software.seguranca.tranche16.001519
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

# Integração de Relatórios do OWASP Dependency-Check (`SARIF`, `JUnit`, `JSON`, `HTML`, `CSV`, `XML`) com **GitHub Code Scanning, GitLab e OWASP DefectDojo**

## Em uma frase
Como fazer com que as vulnerabilidades encontradas pelo **OWASP Dependency-Check** apareçam diretamente: **(1) Como anotações de segurança na aba *Security -> Code Scanning* do GitHub**, **(2) Como falhas de teste na aba *Tests* do Jenkins/GitLab CI** e **(3) No painel central de gestão de vulnerabilidades OWASP DefectDojo**?

## Por que importa
Passando múltiplos argumentos **`--format`** (ou `--format ALL`) em uma única execução! O Dependency-Check suporta nativamente os formatos **`HTML`**, **`XML`**, **`CSV`**, **`JSON`**, **`JUNIT`**, **`SARIF`**, **`JENKINS`** e **`GITLAB`**!

## Como funciona
Quando você gera **`--format SARIF`** (`dependency-check-report.sarif`), a action `github/codeql-action/upload-sarif` exibe o alerta diretamente no Pull Request; quando gera **`--format JUNIT`** (`--junitFailOnCVSS 7.0`), qualquer plataforma de CI exibe cada CVE acima do limiar como um caso de teste reprovado; e os formatos **`XML` / `JSON`** são importados nativamente pelo conector *"Dependency Check Scan"* do **OWASP DefectDojo**!

## Exemplo
```bash
# Gerar relatorios SARIF (para GitHub Security), JUNIT (com gate em CVSS 7.0) e XML (para ingestao no OWASP DefectDojo) em uma unica passada
dependency-check.sh \
  --noupdate \
  --project "API-Pagamentos" \
  --scan ./target \
  --format SARIF --format JUNIT --format XML --format HTML \
  --junitFailOnCVSS 7.0 \
  --out ./reports
```

## Limites e trade-offs
Repare na diferença sutil e muito útil entre **`--failOnCVSS 7.0`** e **`--junitFailOnCVSS 7.0`**: enquanto `--failOnCVSS 7.0` faz o próprio processo `dependency-check.sh` retornar exit code diferente de zero imediatamente, `--junitFailOnCVSS 7.0` marca apenas os `<testcase>` com CVSS >= 7.0 como `<failure>` dentro do arquivo `dependency-check-junit.xml`, permitindo que o pipeline continue rodando os estágios seguintes e deixe o coletor JUnit do CI marcar o build como *Unstable/Failed*!

## Como verificar
Combine também com `--prettyPrint` durante depurações locais para que os arquivos `.json`, `.sarif` e `.xml` sejam salvos indentados e fáceis de ler com `less` ou `jq`.

## Conexões
- [[depcheck-execucao-offline-air-gapped-espaco-corporativo-central-db]] — Veja também: Operando o OWASP Dependency-Check em Ambientes **Air-Gapped (Redes Isoladas)** ou com **Banco de Dados Central PostgreSQL / MySQL / MS SQL**.
- [[depcheck-comparativo-dependency-check-vs-dependency-track-osv-scanner-sbom]] — Veja também: Arquitetura Comparada de SCA: Quando Usar **OWASP Dependency-Check** vs. **OWASP Dependency-Track (SBOM CycloneDX)** vs. **OSV-Scanner / `pip-audit` / `govulncheck`**.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline]] — Referência cruzada direta com depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
