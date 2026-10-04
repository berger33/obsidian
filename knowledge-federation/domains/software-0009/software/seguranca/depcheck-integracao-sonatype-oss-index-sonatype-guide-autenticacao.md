---
id: software.seguranca.tranche16.001516
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

# Enriquecimento de Análise com **Sonatype OSS Index / Sonatype Guide** e **CISA Known Exploited Vulnerabilities (`KEV`)** no OWASP Dependency-Check

## Em uma frase
Por que combinar o banco de dados **NIST NVD (baseado em `CPE`)** com o analisador **Sonatype OSS Index / Sonatype Guide (baseado em coordenadas exatas de pacote `Package URL — PURL`)** e com o catálogo **CISA Known Exploited Vulnerabilities (`KEV`)** aumenta drasticamente a precisão do OWASP Dependency-Check?

## Por que importa
Porque o **NVD** identifica softwares pelo nome de produto (`CPE`), enquanto o **Sonatype OSS Index / Sonatype Guide** identifica bibliotecas diretamente pelo seu **`Package URL` (`pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1`)** — capturando vulnerabilidades em pacotes Maven, npm, PyPI e NuGet que às vezes ainda não receberam um CPE formal no NVD!

## Como funciona
E atenção ao aviso importante destacado no `README.md` oficial (*Sonatype OSS Index mandatory authentication and migration to Sonatype Guide*): desde setembro de 2025 a autenticação por token tornou-se obrigatória no OSS Index e, a partir de abril de 2026, iniciou-se a migração para tokens de API do **Sonatype Guide**; **sem credenciais configuradas, o Dependency-Check desativa automaticamente o analisador OSS Index**!

## Exemplo
```bash
# Executar o Dependency-Check passando as credenciais de autenticacao do Sonatype OSS Index / Guide via variaveis/flags no CI
dependency-check.sh \
  --nvdApiKey "${NVD_API_KEY}" \
  --ossIndexUsername "${OSSINDEX_USER}" \
  --ossIndexPassword "${OSSINDEX_TOKEN}" \
  --project "Core-Banking" \
  --scan ./target \
  --out ./odc-report
```

## Limites e trade-offs
Além do NVD e do Sonatype, o Dependency-Check baixa e cruza automaticamente o catálogo **CISA Known Exploited Vulnerabilities (`known_exploited_vulnerabilities.json`)**: quando uma CVE encontrada nas suas dependências consta na lista oficial da CISA de vulnerabilidades **ativamente exploradas por atacantes no mundo real**, o relatório destaca esse alerta imediatamente para priorização máxima de correção!

## Como verificar
Se a sua empresa rodar em rede corporativa fechada sem assinatura do Sonatype Guide, passe `--disableOssIndex` para evitar avisos de autenticação nos logs de build.

## Conexões
- [[depcheck-tratamento-falsos-positivos-suppression-xml-cpe-cve-purl]] — Veja também: Triagem e Supressão Auditável de Falsos Positivos no OWASP Dependency-Check: Arquivo **`suppressions.xml` (`--suppression`)**, `packageUrl`, `cpe`, `cve` e `until`.
- [[depcheck-analise-javascript-retirejs-npm-audit-yarn-pnpm-lockfiles]] — Veja também: Auditoria de Dependências Frontend e Node.js no OWASP Dependency-Check: **`RetireJS Analyzer`**, `package-lock.json`, `pnpm-lock.yaml` e `yarn.lock`.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Referência cruzada direta com depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
