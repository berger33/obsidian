---
id: software.devops.tranche13.001265
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
fontes: ["https://distribution.github.io/distribution/about/configuration/", "https://raw.githubusercontent.com/distribution/distribution/main/README.md", "https://github.com/distribution/distribution"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CNCF Distribution: Autenticação com htpasswd, Token Server Externo (JWT/JWKS) e mTLS

## Em uma frase
A seção `auth` do Distribution suporta três modos de autenticação (`htpasswd` para autenticação básica com senhas bcrypt, `token` para delegação OAuth2/JWT a um servidor de autorização externo com validação via `rootcertbundle` ou `jwks` e algoritmos como `EdDSA`/`HS256`, e `silly` apenas para desenvolvimento), além de mTLS em `http.tls.clientcas`.

## Por que importa
Usar o modo `auth.silly` (que aceita qualquer requisição que simplesmente envie um cabeçalho `Authorization` não-vazio) fora de testes locais deixa o registro completamente aberto.

## Como funciona
Em implantações standalone enxutas, utiliza-se `auth.htpasswd` (`realm: basic-realm`, `path: /etc/distribution/htpasswd`) obrigatoriamente sobre HTTPS (`http.tls`); em plataformas corporativas (como Harbor ou Portus), utiliza-se `auth.token` apontando `realm`, `service`, `issuer` e `jwks` para que o registry valide tokens JWT assinados com permissões granulares de pull/push por repositório.

## Exemplo
```yaml
auth:
  token:
    autoredirect: true
    realm: https://auth.example.com/token
    service: registry.example.com
    issuer: registry-token-issuer
    jwks: /etc/distribution/auth-jwks.json
    signingalgorithms:
      - EdDSA
      - RS256
```

## Limites e trade-offs
Utilizar `auth.htpasswd` com entradas geradas sem algoritmo bcrypt (como MD5 ou SHA1 do Apache antigo) faz a autenticação falhar no Distribution, que aceita apenas hashes bcrypt no arquivo htpasswd.

## Como verificar
Gere senhas do `htpasswd` exclusivamente com a flag `-B` (`htpasswd -Bc htpasswd usuario`) e exija TLS em `http.tls`.

## Conexões
- [[distribution-delete-enabled-maintenance-uploadpurging-readonly-gc]] — Veja também: CNCF Distribution: Deleção de Manifestos (delete.enabled), Limpeza de Uploads (uploadpurging) e Modo Readonly para GC.
- [[distribution-alta-disponibilidade-http-secret-redis-blobdescriptor-cache]] — Veja também: CNCF Distribution: Alta Disponibilidade com http.secret Compartilhado e Cache de Blob Descriptors no Redis.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
