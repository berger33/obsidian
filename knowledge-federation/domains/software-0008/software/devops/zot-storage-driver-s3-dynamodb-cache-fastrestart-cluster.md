---
id: software.devops.tranche13.001228
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

# Project Zot: Backend S3, Cache Driver, fastRestart e Escalonamento Horizontal em Cluster

## Em uma frase
Para implantações de grande escala, o `zot` suporta armazenamento de objetos compatível com **Amazon S3** (`storageDriver` com `name: "s3"`), driver de cache para deduplicação, inicialização rápida (`fastRestart`) e agrupamento stateless em múltiplos nós (`cluster`).

## Por que importa
Em registros com mais de 1 TB e milhares de repositórios no S3, percorrer todos os objetos do bucket durante a inicialização para reconciliar o `metaDB` pode levar vários minutos se `fastRestart` não estiver configurado.

## Como funciona
No bloco `storage`, configura-se o `storageDriver` S3 (lendo credenciais de variáveis de ambiente, perfil IAM ou arquivo) e a opção `fastRestart` para acelerar o boot; no bloco de nível superior `cluster`, listam-se os membros de scale-out, a chave de hash (`hashKey`) e o TLS intra-cluster para distribuir requisições de forma consistente.

## Exemplo
```json
{
  "storage": {
    "rootDirectory": "/var/lib/zot",
    "dedupe": true,
    "storageDriver": {
      "name": "s3",
      "region": "sa-east-1",
      "bucket": "corp-zot-registry",
      "secure": true
    }
  }
}
```

## Limites e trade-offs
Executar múltiplas réplicas do `zot` apontando para o mesmo bucket S3 sem configurar o bloco `cluster` e o banco de metadados/cache compartilhado gera inconsistências de estado de índice e colisão de tarefas de GC.

## Como verificar
Ao escalar o `zot` para múltiplas réplicas sobre S3, configure explicitamente a seção `cluster` e valide o schema com `zot schema` e `zot verify`.

## Conexões
- [[zot-extensao-trust-verificacao-assinaturas-cosign-notation]] — Veja também: Project Zot: Extensão trust para Armazenamento e Verificação de Assinaturas Cosign e Notation.
- [[zot-extensoes-scrub-lint-metrics-eventos-observabilidade]] — Veja também: Project Zot: Verificação de Integridade de Blobs (scrub), Linting de Imagens (lint) e Métricas Prometheus.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
