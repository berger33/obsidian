---
id: software.devops.tranche13.001266
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

# CNCF Distribution: Alta Disponibilidade com http.secret Compartilhado e Cache de Blob Descriptors no Redis

## Em uma frase
Para executar múltiplas réplicas do CNCF Distribution atrás de um balanceador de carga, é obrigatório compartilhar exatamente o mesmo valor de `http.secret` entre todas as instâncias e recomendável configurar `storage.cache.blobdescriptor: redis` para reduzir chamadas lentas de metadados ao S3/GCS.

## Por que importa
Se cada Pod do `registry` não definir `http.secret` (gerando uma chave aleatória diferente em memória ao iniciar), um upload de camada iniciado no Pod 1 falhará com erro de validação de estado HMAC quando o próximo chunk cair no Pod 2.

## Como funciona
No `config.yml`, define-se `http.secret` (via variável `REGISTRY_HTTP_SECRET`) com o mesmo segredo criptográfico em todas as réplicas e configura-se a seção `redis` junto com `storage.cache.blobdescriptor: redis` (`blobdescriptorsize: 10000`) para manter em memória os descritores de camadas consultados a cada `HEAD /v2/<repo>/blobs/<digest>`.

## Exemplo
```yaml
storage:
  cache:
    blobdescriptor: redis
    blobdescriptorsize: 10000
http:
  addr: 0.0.0.0:5000
  secret: "${REGISTRY_HTTP_SECRET}"
  draintimeout: 60s
```

## Limites e trade-offs
Deixar o valor de exemplo `http.secret: asecretforlocaldevelopment` em produção permite que clientes forjem estados de upload assinados no servidor.

## Como verificar
Gere um valor aleatório forte de 32+ bytes para `REGISTRY_HTTP_SECRET` armazenado em um `Secret` Kubernetes compartilhado por todas as réplicas do Deployment.

## Conexões
- [[distribution-autenticacao-htpasswd-token-jwt-jwks-mtls]] — Veja também: CNCF Distribution: Autenticação com htpasswd, Token Server Externo (JWT/JWKS) e mTLS.
- [[distribution-storage-redirect-middlewares-cloudfront-cdn-offload]] — Veja também: CNCF Distribution: Redirecionamento de Blobs (storage.redirect) e Middlewares de CDN (CloudFront).

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
