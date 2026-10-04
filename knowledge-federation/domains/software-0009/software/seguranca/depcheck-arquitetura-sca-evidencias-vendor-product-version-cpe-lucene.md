---
id: software.seguranca.tranche16.001511
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

# Arquitetura do **OWASP Dependency-Check (`dependency-check`)**: Coleta de Evidências (`vendor`, `product`, `version`), Índice **Lucene CPE** e Níveis de Confiança

## Em uma frase
Como o **OWASP Dependency-Check** — uma das ferramentas de **SCA (*Software Composition Analysis*)** mais tradicionais da OWASP — consegue identificar vulnerabilidades públicas (`CVEs`) em arquivos binários compilados como `.jar`, `.war`, `.ear`, `.dll`, `.exe` e `.nupkg` mesmo quando o projeto não possui um arquivo de manifesto moderno?

## Por que importa
Conforme explicado na documentação arquitetural oficial (`general/internals.html`), o Dependency-Check funciona em 4 etapas: **(1) Analyzers** inspecionam os arquivos escaneados (ex.: o `JarAnalyzer` lê `META-INF/MANIFEST.MF`, `pom.xml` embutido e nomes de pacotes Java dentro do `.jar`) e extraem **Evidências (*Evidence*)** divididas em três cestos: **`vendor`**, **`product`** e **`version`**; **(2) Cada evidência recebe um Nível de Confiança (`low`, `medium`, `high`, `highest`)**.

## Como funciona
**(3) O `CPEAnalyzer` consulta um índice local Apache Lucene** contendo os identificadores **CPE (`cpe:2.3:a:vendor:product:version:...`)** do NVD; e **(4) A confiança final do CPE atribuído é igual ao MENOR nível de confiança entre as evidências usadas na sua identificação**, vinculando em seguida todas as entradas `CVE` associadas no banco H2 local!

## Exemplo
```bash
# Executar o OWASP Dependency-Check CLI sobre os artefatos de uma aplicacao gerando relatorios HTML, JSON e SARIF simultaneamente
dependency-check.sh --version
dependency-check.sh \
  --project "API-Pagamentos" \
  --scan ./target \
  --format HTML --format JSON --format SARIF \
  --out ./relatorios-odc
```

## Limites e trade-offs
Por que o `internals.html` destaca que o Dependency-Check tradicionalmente usa **Correspondência Baseada em Evidências (`CPE Matching`)** em vez de depender exclusivamente do hash SHA-1 do arquivo `.jar`? Porque se uma biblioteca open-source foi recompilada internamente a partir do código-fonte (ou reempacotada em um *fat JAR* / *uber JAR*), o hash criptográfico do arquivo muda completamente, mas as evidências internas de `vendor`, `product` e `version` permanecem intactas e são detectadas pelos Analyzers!

## Como verificar
Como avisa o `README.md` oficial, a partir da versão **`11.0.0+`** o Java 11+ é obrigatório, e a atualização para a versão **`12.1.0+`** é mandatória devido às mudanças de compatibilidade na API v2.0 do NIST NVD.

## Conexões
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Veja também: Integração com a **API v2 do NIST NVD (`--nvdApiKey`)**, Cache de Banco **H2** e Estratégia de Espelhamento em CI/CD no OWASP Dependency-Check.
- [[depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl]] — Referência cruzada direta com depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
