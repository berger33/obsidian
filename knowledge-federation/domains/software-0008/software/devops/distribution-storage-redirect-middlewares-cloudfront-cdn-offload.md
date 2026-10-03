---
id: software.devops.tranche13.001267
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

# CNCF Distribution: Redirecionamento de Blobs (storage.redirect) e Middlewares de CDN (CloudFront)

## Em uma frase
Por padrão (`storage.redirect.disable: false`), quando o Distribution usa um backend de objetos como S3 ou GCS, requisições de download de camadas (`GET /v2/<name>/blobs/<digest>`) retornam um redirecionamento HTTP `307 Temporary Redirect` com uma URL pré-assinada do bucket ou CDN (via middleware `cloudfront` ou `redirect`), descarregando a banda pesada dos Pods do registry.

## Por que importa
Se o binário do registry tiver que fazer proxy em memória de cada gigabyte de blob baixado por centenas de nós Kubernetes, a rede e a CPU dos Pods do registry tornam-se o gargalo principal.

## Como funciona
Mantendo `storage.redirect.disable: false` (ou configurando `middleware.storage` com `name: cloudfront`, `baseurl`, `privatekey`, `keypairid` e filtro de IP por região AWS `ipfilteredby: awsregion`), a autenticação do manifesto ocorre no registry, mas o download pesado dos blobs vai direto do cliente (`containerd`) para o S3 ou CloudFront.

## Exemplo
```yaml
storage:
  redirect:
    disable: false
middleware:
  storage:
    - name: cloudfront
      options:
        baseurl: https://d111111abcdef8.cloudfront.net/
        privatekey: /etc/distribution/cf-pk.pem
        keypairid: K2JCJMDEHXQW5F
        duration: 3000s
```

## Limites e trade-offs
Deixar `storage.redirect.disable: false` em clusters privados cujos worker nodes têm acesso ao serviço interno do registry mas **não** têm rota de rede ou regra de firewall liberada para o endpoint do S3/MinIO faz o `docker pull` falhar ao seguir o redirecionamento `307`.

## Como verificar
Se os clientes não puderem acessar o endpoint do Object Storage diretamente, defina `storage.redirect.disable: true` para que o registry faça o proxy dos blobs.

## Conexões
- [[distribution-alta-disponibilidade-http-secret-redis-blobdescriptor-cache]] — Veja também: CNCF Distribution: Alta Disponibilidade com http.secret Compartilhado e Cache de Blob Descriptors no Redis.
- [[distribution-pull-through-cache-proxy-remoteurl-docker-hub]] — Veja também: CNCF Distribution: Configuração de Pull-Through Cache (proxy.remoteurl) para Espelhamento de Registries.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
