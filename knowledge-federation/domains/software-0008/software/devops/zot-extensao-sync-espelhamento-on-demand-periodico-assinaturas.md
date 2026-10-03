---
id: software.devops.tranche13.001225
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

# Project Zot: Extensão sync para Espelhamento Periódico e Pull-Through Cache Sob Demanda

## Em uma frase
A extensão `extensions.sync` do `zot` permite sincronizar imagens e artefatos OCI de registros remotos (Docker Hub, GHCR, ECR, Harbor ou outra instância `zot`) tanto por agendamento periódico (`pollInterval`) quanto sob demanda (`onDemand: true`) no instante em que um nó Kubernetes solicita o pull.

## Por que importa
Quando centenas de nós Kubernetes puxam imagens diretamente de registros públicos na internet, falhas externas ou limites de taxa (`429 Too Many Requests` do Docker Hub) interrompem o escalonamento de Pods no cluster.

## Como funciona
Na configuração de `extensions.sync`, define-se uma lista de `registries` com `urls`, `onDemand`, `pollInterval`, `tlsVerify` e regras de `content` (filtrando por prefixo de repositório e regex de tags ou SemVer). O `zot` copia não apenas as camadas da imagem OCI, mas também artefatos referenciados associados, como assinaturas Cosign e Notation e SBOMs.

## Exemplo
```json
{
  "extensions": {
    "sync": {
      "enable": true,
      "registries": [
        {
          "urls": ["https://ghcr.io"],
          "onDemand": true,
          "tlsVerify": true,
          "content": [
            {
              "prefix": " score-spec/*"
            }
          ]
        }
      ]
    }
  }
}
```

## Limites e trade-offs
Habilitar espelhamento de repositórios remotos amplos sem filtrar tags por regex ou SemVer no bloco `content` pode fazer o sync periódico baixar milhares de tags históricas e esgotar o disco.

## Como verificar
Use `onDemand: true` para caches de borda ou restrinja o bloco `content` com filtros de tags SemVer quando usar `pollInterval`.

## Conexões
- [[zot-autenticacao-mtls-htpasswd-ldap-oidc-api-keys]] — Veja também: Project Zot: Autenticação (mTLS, htpasswd, LDAP, Bearer/OIDC e API Keys) e Controle de Acesso.
- [[zot-extensao-search-trivy-cve-scanning-graphql]] — Veja também: Project Zot: Extensão search com Scanner de Vulnerabilidades CVE (Trivy) e Consultas GraphQL.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
