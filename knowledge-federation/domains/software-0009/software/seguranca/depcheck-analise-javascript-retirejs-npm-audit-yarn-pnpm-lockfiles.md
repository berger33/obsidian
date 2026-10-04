---
id: software.seguranca.tranche16.001517
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

# Auditoria de Dependências Frontend e Node.js no OWASP Dependency-Check: **`RetireJS Analyzer`**, `package-lock.json`, `pnpm-lock.yaml` e `yarn.lock`

## Em uma frase
Muitas aplicações corporativas Java/.NET/Python empacotam dentro de `src/main/resources/static/` ou `wwwroot/` bibliotecas JavaScript antigas copiadas manualmente (como `jquery-1.12.4.min.js`, `bootstrap.min.js`, `lodash.js` ou `moment.js`) que **não constam em nenhum `package.json`**! Como o OWASP Dependency-Check detecta vulnerabilidades tanto em pacotes modernos do `npm`/`pnpm`/`yarn` quanto nesses arquivos `.js` estáticos órfãos?

## Por que importa
Atuando em duas frentes complementais: **(1) Para projetos modernos com Lockfiles (`package-lock.json`, `npm-shrinkwrap.json`, `yarn.lock`, `pnpm-lock.yaml`)**, os analisadores de Node.js auditam toda a árvore transitiva de pacotes; e **(2) Para arquivos `.js` soltos dentro do projeto ou dentro de arquivos `.war`/`.jar`**, o **`RetireJS Analyzer`** embutido no Dependency-Check inspeciona assinaturas, cabeçalhos de comentários e hashes/expressões regulares do repositório **Retire.js**!

## Como funciona
Assim, mesmo que alguém tenha copiado um arquivo `jquery.min.js` vulnerável a DOM XSS diretamente para a pasta `public/js/` há 6 anos sem usar `npm`, o `RetireJS Analyzer` do Dependency-Check o descobre e alerta na hora!

## Exemplo
```bash
# Auditar um diretorio de assets frontend estaticos e lockfiles Node.js com o RetireJS Analyzer do Dependency-Check
dependency-check.sh \
  --project "Portal-Web-Frontend" \
  --scan ./src/main/webapp \
  --format HTML --format JSON \
  --out ./odc-frontend
```

## Limites e trade-offs
Se o seu projeto possui pastas com arquivos `.js` proprietários minificados que geram ruído ou se você quiser filtrar arquivos por conteúdo (como arquivos de licença/copyright que mencionam nomes de bibliotecas em comentários), use a opção **`--retireJsFilter`** ou **`--retireJsForceUpdate`**!

## Como verificar
Lembre-se do requisito documentado no `README.md`: para analisar projetos `npm`, `pnpm` ou `yarn`, o respectivo binário (`npm`, `pnpm` ou `yarn`) deve estar disponível no `PATH` do agente de CI.

## Conexões
- [[depcheck-integracao-sonatype-oss-index-sonatype-guide-autenticacao]] — Veja também: Enriquecimento de Análise com **Sonatype OSS Index / Sonatype Guide** e **CISA Known Exploited Vulnerabilities (`KEV`)** no OWASP Dependency-Check.
- [[depcheck-execucao-offline-air-gapped-espaco-corporativo-central-db]] — Veja também: Operando o OWASP Dependency-Check em Ambientes **Air-Gapped (Redes Isoladas)** ou com **Banco de Dados Central PostgreSQL / MySQL / MS SQL**.
- [[depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene]] — Referência cruzada direta com depcheck-arquitetura-sca-evidencias-vendor-product-version-cpe-lucene.
- [[depcheck-analisadores-ecossistemas-jar-dotnet-npm-golang-python-experimental]] — Referência cruzada direta com depcheck-analisadores-ecossistemas-jar-dotnet-npm-golang-python-experimental.

## Fontes
- [OWASP Dependency-Check Official GitHub Repository (`dependency-check/DependencyCheck`)](https://raw.githubusercontent.com/dependency-check/DependencyCheck/main/README.md) — repositório oficial da ferramenta SCA OWASP Dependency-Check cobrindo CLI, plugins Maven/Gradle, NVD API Key, cache H2 e analisadores multi-linguagem; consultado em 2026-10-03.
- [OWASP Dependency-Check Official Internals Documentation (`general/internals.html`)](https://dependency-check.github.io/DependencyCheck/general/internals.html) — documentação arquitetural oficial explicando Analyzers, coleta de Evidence (`vendor`, `product`, `version`), Lucene CPE Index e níveis de confiança; consultado em 2026-10-03.
