---
id: software.devops.tranche13.001224
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

# Project Zot: Autenticação (mTLS, htpasswd, LDAP, Bearer/OIDC e API Keys) e Controle de Acesso

## Em uma frase
A seção `http.auth` e `http.accessControl` do `zot` suporta autenticação mútua TLS (mTLS), arquivo `htpasswd` com passphrases bcrypt, integração LDAP, tokens Bearer/OpenID Connect e geração de API Keys, combinados com autorização baseada em identidade por repositório.

## Por que importa
Expor um registro OCI interno sem autenticação e sem separar permissões de leitura (`read`) das permissões de escrita (`create`, `update`, `delete`) permite que qualquer workload sobrescreva imagens de produção ou delete tags críticas.

## Como funciona
No bloco `http`, configura-se `tls` (`cert`, `key`, `cacert`), os provedores em `auth` (incluindo `failDelay` para mitigar força bruta) e as políticas granulares em `accessControl`, onde padrões de caminhos de repositórios mapeiam grupos ou usuários para listas de ações permitidas (`read`, `create`, `update`, `delete`, `detectManifestCollision`).

## Exemplo
```json
{
  "http": {
    "address": "0.0.0.0",
    "port": "5000",
    "tls": {
      "cert": "/etc/zot/certs/server.cert",
      "key": "/etc/zot/certs/server.key"
    },
    "auth": {
      "htpasswd": {
        "path": "/etc/zot/htpasswd"
      },
      "failDelay": 5
    }
  }
}
```

## Limites e trade-offs
Omitir `"failDelay"` em registros expostos a redes amplas com autenticação baseada em senha (`htpasswd` ou LDAP) facilita ataques automatizados de adivinhação de credenciais sem penalidade de latência.

## Como verificar
Defina `"failDelay"` (por exemplo, `5` segundos), force TLS em `http.tls` e restrinja escrita em repositórios de produção exclusivamente às identidades de CI.

## Conexões
- [[zot-garbage-collection-gc-gcdelay-gctimewindow-retencao]] — Veja também: Project Zot: Coleta de Lixo em Background (gc, gcDelay e gcTimeWindow em UTC) e Políticas de Retenção.
- [[zot-extensao-sync-espelhamento-on-demand-periodico-assinaturas]] — Veja também: Project Zot: Extensão sync para Espelhamento Periódico e Pull-Through Cache Sob Demanda.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
