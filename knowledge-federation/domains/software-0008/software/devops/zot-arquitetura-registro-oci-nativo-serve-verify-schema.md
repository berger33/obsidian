---
id: software.devops.tranche13.001221
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
fontes: ["https://raw.githubusercontent.com/project-zot/zot/main/README.md", "https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md", "https://github.com/project-zot/zot"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Zot: Arquitetura de Registry OCI-Nativo, Validação de Config (zot verify) e JSON Schema (zot schema)

## Em uma frase
O **zot** (`project-zot/zot`, projeto CNCF Sandbox) é um registro de imagens e artefatos pronto para produção e neutro de fornecedor que armazena imagens exclusivamente no formato **OCI Image Specification** em disco/S3 e fala **OCI Distribution Specification** na rede, sem camadas legadas específicas do Docker.

## Por que importa
Registros tradicionais carregam dívida técnica de formatos de manifesto antigos e exigem múltiplos componentes externos acoplados, enquanto o `zot` empacota armazenamento OCI puro, deduplicação, coleta de lixo e extensões opcionais em um único binário Go.

## Como funciona
O comportamento do servidor é controlado por um arquivo JSON ou YAML iniciado com `zot serve <config-file>`. Antes de subir ou recarregar o serviço em produção, o mesmo binário permite exportar a referência completa em JSON Schema draft 7 (`zot schema > zot-config-schema.json`) e validar estaticamente qualquer arquivo candidato com `zot verify <config-file>`.

## Exemplo
```bash
zot schema > zot-config-schema.json
zot verify /etc/zot/config.json
zot serve /etc/zot/config.json
```

## Limites e trade-offs
Tentar fazer push de manifestos legados Docker v2 Schema 1 (depreciados) para o `zot` falha porque o `zot` exige conformidade estrita com as especificações OCI Image e OCI Distribution.

## Como verificar
Adicione `zot verify config.json` ao pipeline de CI da infraestrutura do registry e verifique a conformidade do endpoint HTTP em `/v2/`.

## Conexões
- [[zot-storage-dedupe-hydrate-blob-on-read-subpaths-maxrepos]] — Veja também: Project Zot: Armazenamento com Deduplicação Inline (dedupe), hydrateBlobOnRead, subPaths e maxRepos.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
