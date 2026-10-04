---
id: software.seguranca.tranche16.001518
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

# Operando o OWASP Dependency-Check em Ambientes **Air-Gapped (Redes Isoladas)** ou com **Banco de Dados Central PostgreSQL / MySQL / MS SQL**

## Em uma frase
Em grandes bancos, órgãos de defesa ou fábricas de software com centenas de pipelines concorrentes e runners de CI/CD que **não têm acesso direto à internet externa**, como operar o **OWASP Dependency-Check** sem que nenhum runner precise acessar a API do NIST NVD na internet e sem duplicar dezenas de caches do banco H2?

## Por que importa
O Dependency-Check suporta duas arquiteturas corporativas para esse cenário: **(Arquitetura 1 — Banco de Dados Relacional Centralizado: PostgreSQL, MySQL/MariaDB ou MS SQL Server)** e **(Arquitetura 2 — Mirror Interno de Diretório `--data`)**!

## Como funciona
Na **Arquitetura 1**, um único serviço interno em uma DMZ com acesso controlado ao NIST NVD executa `dependency-check.sh --updateonly` gravando os dados diretamente em um banco **PostgreSQL central (`--connectionString jdbc:postgresql://db-sec.interno:5432/odc --dbDriverName org.postgresql.Driver --dbUser ... --dbPassword ...`)**, e todos os 500 runners de CI/CD internos rodam com **`--noupdate`** lendo em modo somente-leitura desse PostgreSQL central!

## Exemplo
```bash
# Executar o Dependency-Check em um runner de CI/CD sem internet (--noupdate) conectando-se a um banco PostgreSQL centralizado da organizacao
dependency-check.sh \
  --noupdate \
  --connectionString "jdbc:postgresql://10.10.20.50:5432/dependencycheck" \
  --dbDriverName "org.postgresql.Driver" \
  --dbUser "odc_readonly" \
  --dbPassword "${ODC_DB_PASS}" \
  --disableOssIndex \
  --project "Sistema-AirGapped" \
  --scan ./app
```

## Limites e trade-offs
Veja por que usar uma conta **`odc_readonly`** (somente-leitura no PostgreSQL) para os runners de CI/CD junto com **`--noupdate`** e **`--disableOssIndex`** é a arquitetura perfeita para redes isoladas: **(1)** Zero tráfego de internet durante os builds; **(2)** Zero contenção de lock de escrita (que acontece no banco H2 em arquivo quando dois processos tentam abrir o mesmo arquivo ao mesmo tempo!); e **(3)** Atualização centralizada em um único ponto!

## Como verificar
Para inicializar o schema das tabelas no PostgreSQL antes da primeira carga, a equipe do Dependency-Check fornece os scripts SQL oficiais (`initialize_postgres.sql`) no repositório GitHub.

## Conexões
- [[depcheck-analise-javascript-retirejs-npm-audit-yarn-pnpm-lockfiles]] — Veja também: Auditoria de Dependências Frontend e Node.js no OWASP Dependency-Check: **`RetireJS Analyzer`**, `package-lock.json`, `pnpm-lock.yaml` e `yarn.lock`.
- [[depcheck-formatos-relatorio-sarif-junit-json-gitlab-defectdojo-github]] — Veja também: Integração de Relatórios do OWASP Dependency-Check (`SARIF`, `JUnit`, `JSON`, `HTML`, `CSV`, `XML`) com **GitHub Code Scanning, GitLab e OWASP DefectDojo**.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd]] — Referência cruzada direta com depcheck-integracao-nvd-api-key-cache-banco-h2-mirror-ci-cd.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
