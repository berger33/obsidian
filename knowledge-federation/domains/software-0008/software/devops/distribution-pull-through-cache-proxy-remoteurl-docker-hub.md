---
id: software.devops.tranche13.001268
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

# CNCF Distribution: Configuração de Pull-Through Cache (proxy.remoteurl) para Espelhamento de Registries

## Em uma frase
O CNCF Distribution pode operar como um cache pull-through transparente configurando a seção `proxy` (`remoteurl`, `username`, `password`, `ttl`) no `/etc/distribution/config.yml`, armazenando localmente imagens buscadas de um registro upstream como o Docker Hub.

## Por que importa
Clusters de CI/CD que criam ambientes efêmeros constantemente sofrem falhas de build por rate limit de pulls anônimos no Docker Hub (`toomanyrequests`) se não utilizarem um proxy cache autenticado.

## Como funciona
Quando `proxy.remoteurl: https://registry-1.docker.io` está configurado, o Distribution intercepta requisições de `pull`, verifica se o manifesto atualizado e os blobs já estão no storage local, busca na origem apenas o que falta e remove artefatos expirados conforme o `ttl`.

## Exemplo
```yaml
proxy:
  remoteurl: https://registry-1.docker.io
  username: "${DOCKERHUB_USER}"
  password: "${DOCKERHUB_TOKEN}"
  ttl: 168h
```

## Limites e trade-offs
Tentar fazer `docker push` de imagens próprias para uma instância do Distribution configurada com `proxy.remoteurl` falha porque instâncias em modo proxy cache operam exclusivamente como espelhos somente leitura da origem configurada.

## Como verificar
Mantenha instâncias separadas do Distribution: uma dedicada a `proxy.remoteurl` (pull-through cache) e outra sem `proxy` para hospedar imagens internas publicadas pelos pipelines.

## Conexões
- [[distribution-storage-redirect-middlewares-cloudfront-cdn-offload]] — Veja também: CNCF Distribution: Redirecionamento de Blobs (storage.redirect) e Middlewares de CDN (CloudFront).
- [[distribution-notifications-webhooks-eventos-push-pull-delete]] — Veja também: CNCF Distribution: Sistema de Notificações por Webhook (notifications.endpoints) e Filas de Eventos.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
