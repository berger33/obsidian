---
id: software.devops.tranche13.001223
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

# Project Zot: Coleta de Lixo em Background (gc, gcDelay e gcTimeWindow em UTC) e Políticas de Retenção

## Em uma frase
O `zot` realiza coleta de lixo (Garbage Collection) nativa em background quando `"gc": true` está definido em `storage`, removendo blobs órfãos e manifestos não referenciados mais antigos que `"gcDelay"` (por exemplo, `"2h"`) e permitindo restringir o início das varreduras periódicas a uma janela diária em UTC com `"gcTimeWindow"`.

## Por que importa
Em registros que exigem colocar o servidor inteiro em modo somente leitura (`readonly`) para rodar garbage collection offline, a limpeza periódica interrompe pipelines de CI/CD; por outro lado, rodar GC pesado no horário de pico adiciona contenção de locks no armazenamento.

## Como funciona
Configurando `"gc": true`, `"gcDelay": "2h"` e `"gcTimeWindow": "01:00-08:00"` (sempre interpretado em UTC, suportando janelas que cruzam a meia-noite como `"22:00-06:00"`), o `zot` inicia as varreduras globais apenas fora do horário de pico e permite que uma varredura iniciada dentro da janela termine sem travar no meio.

## Exemplo
```json
{
  "storage": {
    "rootDirectory": "/var/lib/zot",
    "dedupe": true,
    "gc": true,
    "gcDelay": "2h",
    "gcTimeWindow": "01:00-06:00"
  }
}
```

## Limites e trade-offs
Alterar `"gcTimeWindow"` no arquivo de configuração e fazer apenas reload em quente sem reiniciar o processo `zot` atualiza o valor em memória, mas não reprograma as tarefas periódicas de GC que já foram agendadas na inicialização do servidor.

## Como verificar
Reinicie o serviço `zot` sempre que alterar `"gcTimeWindow"` e lembre-se de converter o horário desejado para UTC.

## Conexões
- [[zot-storage-dedupe-hydrate-blob-on-read-subpaths-maxrepos]] — Veja também: Project Zot: Armazenamento com Deduplicação Inline (dedupe), hydrateBlobOnRead, subPaths e maxRepos.
- [[zot-autenticacao-mtls-htpasswd-ldap-oidc-api-keys]] — Veja também: Project Zot: Autenticação (mTLS, htpasswd, LDAP, Bearer/OIDC e API Keys) e Controle de Acesso.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
