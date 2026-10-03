---
id: software.devops.tranche13.001222
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md", "https://raw.githubusercontent.com/project-zot/zot/main/README.md", "https://github.com/project-zot/zot"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Zot: Armazenamento com Deduplicação Inline (dedupe), hydrateBlobOnRead, subPaths e maxRepos

## Em uma frase
Na seção `storage` do `zot`, é possível habilitar deduplicação inline de camadas compartilhadas (`"dedupe": true`), controlar a hidratação de blobs em leituras (`"hydrateBlobOnRead"`), limitar o número máximo de repositórios (`"maxRepos"`) e particionar múltiplos sistemas de arquivos ou buckets por prefixo (`"subPaths"`).

## Por que importa
Imagens de containers frequentemente compartilham camadas base idênticas entre dezenas de repositórios; sem deduplicação por hard links/cache de blobs e sem cota de criação de novos repositórios, o armazenamento se esgota rapidamente.

## Como funciona
Com `"dedupe": true`, o `zot` evita duplicar blobs idênticos no mesmo store. Por padrão (`"hydrateBlobOnRead": false`), leituras `HEAD` e `GET` verificam apenas o caminho local do repositório para preservar a semântica `AtomicDelete` da OCI Distribution Spec (um blob deletado de um repositório continua ausente nele mesmo que exista no cache de outro repositório). Já `"maxRepos": 100` rejeita pushes que criariam novos repositórios acima do limite com `HTTP 429`, permitindo pushes em repositórios já existentes.

## Exemplo
```json
{
  "distSpecVersion": "1.1.0",
  "storage": {
    "rootDirectory": "/var/lib/zot",
    "dedupe": true,
    "hydrateBlobOnRead": false,
    "maxRepos": 500
  },
  "http": {
    "address": "0.0.0.0",
    "port": "5000"
  }
}
```

## Limites e trade-offs
Habilitar `"hydrateBlobOnRead": true` sem configurar `"accessControl"` adequado pode fazer com que uma requisição `HEAD`/`GET` rematerialize no repositório de destino um blob que havia sido deletado localmente mas ainda constava no cache compartilhado.

## Como verificar
Mantenha `"hydrateBlobOnRead": false` (o padrão oficial) para garantir o comportamento `AtomicDelete` da especificação OCI e valide o arquivo com `zot verify`.

## Conexões
- [[zot-arquitetura-registro-oci-nativo-serve-verify-schema]] — Veja também: Project Zot: Arquitetura de Registry OCI-Nativo, Validação de Config (zot verify) e JSON Schema (zot schema).
- [[zot-garbage-collection-gc-gcdelay-gctimewindow-retencao]] — Veja também: Project Zot: Coleta de Lixo em Background (gc, gcDelay e gcTimeWindow em UTC) e Políticas de Retenção.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
