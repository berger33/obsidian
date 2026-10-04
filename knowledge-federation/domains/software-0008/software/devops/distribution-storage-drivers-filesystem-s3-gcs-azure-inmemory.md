---
id: software.devops.tranche13.001263
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

# CNCF Distribution: Drivers de Armazenamento (filesystem, s3, gcs, azure e inmemory) e Parâmetros de Performance

## Em uma frase
A seção `storage` do Distribution abstrai o backend físico de blobs e manifestos por meio de drivers mutuamente exclusivos: `filesystem` (disco local/NFS com `maxthreads`), `s3` (Amazon S3 e compatíveis como MinIO/Ceph com `forcepathstyle`, `chunksize`, `multipartcopy*`), `gcs` (Google Cloud Storage), `azure` (Azure Blob Storage) e `inmemory`.

## Por que importa
Usar o driver `filesystem` em múltiplas réplicas sem armazenamento compartilhado faz com que uma camada enviada para a réplica A retorne `404 Blob Unknown` quando o cliente tenta baixar da réplica B.

## Como funciona
Para produção em nuvem ou on-premises escalável, configura-se um driver de armazenamento de objetos (`s3`, `gcs` ou `azure`) com criptografia (`encrypt: true`), ajuste de `chunksize` (padrão `5242880` / 5 MB) e controle de concorrência de tags (`tag.concurrencylimit: 8`).

## Exemplo
```yaml
version: 0.1
storage:
  s3:
    region: sa-east-1
    bucket: prod-oci-registry-blobs
    encrypt: true
    secure: true
    v4auth: true
    chunksize: 10485760
    rootdirectory: /registry
  tag:
    concurrencylimit: 8
```

## Limites e trade-offs
Conectar o driver `s3` a um armazenamento compatível com S3 on-premises (como MinIO ou Ceph RGW) sem definir `forcepathstyle: true` e `regionendpoint` causa falha de resolução DNS no formato virtual-hosted-style.

## Como verificar
Em storages compatíveis com S3 fora da AWS, habilite `forcepathstyle: true` e configure `regionendpoint` apontando para a URL HTTPS do storage.

## Conexões
- [[distribution-configuracao-yaml-overrides-variaveis-ambiente-otel]] — Veja também: CNCF Distribution: Configuração YAML (/etc/distribution/config.yml), Overrides por Variáveis REGISTRY_* e OpenTelemetry.
- [[distribution-delete-enabled-maintenance-uploadpurging-readonly-gc]] — Veja também: CNCF Distribution: Deleção de Manifestos (delete.enabled), Limpeza de Uploads (uploadpurging) e Modo Readonly para GC.

## Fontes
- [CNCF Distribution Official Documentation — Configuration Reference (/etc/distribution/config.yml, REGISTRY_* Env Vars, Storage, Auth & Proxy)](https://distribution.github.io/distribution/about/configuration/) — Referência oficial de configuração do CNCF Distribution detalhando drivers de storage (filesystem, s3, gcs, azure), cache Redis, auth (token/JWKS/htpasswd), proxy pull-through, webhooks e OpenTelemetry; consultado em 2026-10-03.
- [CNCF Distribution GitHub — README.md (OCI Distribution Spec Implementation, registry:3 Image & Architecture)](https://raw.githubusercontent.com/distribution/distribution/main/README.md) — README oficial do distribution/distribution (Apache-2.0) explicando o papel do projeto como motor base do ecossistema de container registries; consultado em 2026-10-03.
- [CNCF Distribution — Official GitHub Repository](https://github.com/distribution/distribution) — Repositório oficial do CNCF Distribution; consultado em 2026-10-03.
