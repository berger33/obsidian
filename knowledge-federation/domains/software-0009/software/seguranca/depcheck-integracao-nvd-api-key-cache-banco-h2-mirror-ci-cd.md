---
id: software.seguranca.tranche16.001512
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

# Integração com a **API v2 do NIST NVD (`--nvdApiKey`)**, Cache de Banco **H2** e Estratégia de Espelhamento em CI/CD no OWASP Dependency-Check

## Em uma frase
Por que rodar o **OWASP Dependency-Check** em um pipeline de CI/CD efêmero (GitHub Actions, GitLab CI, Jenkins) **sem configurar `--nvdApiKey` e sem persistir o diretório de dados (`--data`)** faz o build demorar mais de 30 minutos ou falhar com erro **`HTTP 403 Forbidden (Rate Limit)`**?

## Por que importa
Conforme documentado no `README.md` oficial (*NVD API Key Highly Recommended*), desde a versão `9.0.0+` o Dependency-Check migrou dos antigos *data-feeds* estáticos para a **API REST v2.0 do NIST NVD**: **(1)** Sem uma **NVD API Key** (`--nvdApiKey`), o NIST aplica um *rate limit* severo que torna o download inicial extremamente lento; e **(2)** Na versão `11.0.0+`, o banco de dados local **H2** foi atualizado (exigindo `dependency-check.sh --purge` ao migrar de versões antigas)!

## Como funciona
Em ambientes de CI/CD com múltiplos builds paralelos, se 20 runners usarem a mesma `--nvdApiKey` baixando o banco do zero ao mesmo tempo, eles estourarão o limite da API do NVD! A solução oficial é **manter um Cache compartilhado do diretório `data/` (ou atualizar o banco H2 uma vez a cada 4 horas em um job agendado e rodar os builds dos desenvolvedores com `--noupdate`)**!

## Exemplo
```bash
# Atualizar o banco H2 local usando a NVD API Key em um job de cache e rodar o scan rapido nos pipelines de build com --noupdate
dependency-check.sh --updateonly --nvdApiKey "${NVD_API_KEY}" --data /var/cache/odc-data
dependency-check.sh \
  --noupdate \
  --data /var/cache/odc-data \
  --project "Servico-Checkout" \
  --scan ./build/libs \
  --out ./odc-report
```

## Limites e trade-offs
Olhe a diferença brutal de velocidade e confiabilidade do padrão em 2 passos acima: o job agendado roda **`--updateonly --nvdApiKey "${NVD_API_KEY}"`** uma vez a cada poucas horas para manter o banco H2 em `/var/cache/odc-data` atualizado, e cada Pull Request dos desenvolvedores roda com **`--noupdate --data /var/cache/odc-data`** — concluindo o scan SCA em **menos de 15 segundos** e sem nunca tomar `403 Rate Limit` da API do NIST!

## Como verificar
Se você encontrar erros de incompatibilidade do banco H2 após atualizar a versão do Dependency-Check no cache compartilhado, basta executar **`dependency-check.sh --purge --data /var/cache/odc-data`** (ou `mvn dependency-check:purge` / `./gradlew dependencyCheckPurge`).

## Conexões
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Veja também: Arquitetura do **OWASP Dependency-Check (`dependency-check`)**: Coleta de Evidências (`vendor`, `product`, `version`), Índice **Lucene CPE** e Níveis de Confiança.
- [[depcheck-analisadores-ecossistemas-jar-dotnet-npm-golang-python-experimental]] — Veja também: Analisadores Multi-Linguagem do OWASP Dependency-Check: **Java (`JarAnalyzer` / Maven / Gradle)**, **.NET 8**, **Go (`go.mod`)**, **Node.js (`npm audit`)**, **Ruby (`bundle-audit`)** e **Elixir (`mix_audit`)**.
- [[depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline]] — Referência cruzada direta com depcheck-plugins-maven-gradle-aggregate-failbuildoncvss-pipeline.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
