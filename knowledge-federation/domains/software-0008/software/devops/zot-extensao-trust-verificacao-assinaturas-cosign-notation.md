---
id: software.devops.tranche13.001227
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

# Project Zot: Extensão trust para Armazenamento e Verificação de Assinaturas Cosign e Notation

## Em uma frase
Por meio da extensão `extensions.trust` e do suporte nativo à API OCI Referrers (` OCI 1.1`), o `zot` armazena, vincula e verifica assinaturas criptográficas geradas tanto pelo **Sigstore Cosign** quanto pelo **Notary Project Notation**.

## Por que importa
Armazenar assinaturas de imagem sem validar se elas correspondem a chaves públicas ou certificados X.509 confiáveis da organização permite que artefatos assinados por chaves desconhecidas passem despercebidos na interface e nas buscas do registro.

## Como funciona
Habilitando `extensions.trust` (`enable: true`, `cosign: true`, `notation: true`), os administradores podem fazer upload de chaves públicas do Cosign e certificados de confiança do Notation para o `zot`, que passa a avaliar e expor nas consultas da API `search` e na UI se cada imagem possui assinatura confiável e dentro da validade.

## Exemplo
```json
{
  "extensions": {
    "search": { "enable": true },
    "trust": {
      "enable": true,
      "cosign": true,
      "notation": true
    }
  }
}
```

## Limites e trade-offs
Habilitar `extensions.trust` sem habilitar `extensions.search` impede a utilização dos endpoints de verificação e consulta de estado de confiança das assinaturas.

## Como verificar
Ative sempre `extensions.search` junto com `extensions.trust` e valide a configuração com `zot verify config.json`.

## Conexões
- [[zot-extensao-search-trivy-cve-scanning-graphql]] — Veja também: Project Zot: Extensão search com Scanner de Vulnerabilidades CVE (Trivy) e Consultas GraphQL.
- [[zot-storage-driver-s3-dynamodb-cache-fastrestart-cluster]] — Veja também: Project Zot: Backend S3, Cache Driver, fastRestart e Escalonamento Horizontal em Cluster.

## Fontes
- [Project Zot GitHub — README.md (OCI-Native Distribution & Image Spec Implementation, Single Binary & Built-in Extensions)](https://raw.githubusercontent.com/project-zot/zot/main/examples/README.md) — README oficial do project-zot/zot (Apache-2.0) detalhando a arquitetura OCI-only sem camadas Docker legadas, empacotamento em binário único com extensões embutidas e binário minimal; consultado em 2026-10-03.
- [Project Zot Official Examples — examples/README.md (Config Matrix: Storage, Auth, TLS, Sync, Search, Scrub, Lint & Metrics)](https://raw.githubusercontent.com/project-zot/zot/main/README.md) — Catálogo oficial de configurações do Zot cobrindo storage local/S3, deduplicação, GC, htpasswd/LDAP/OIDC/mTLS, RBAC, replicação on-demand e métricas; consultado em 2026-10-03.
- [Project Zot — Official GitHub Repository](https://github.com/project-zot/zot) — Repositório oficial CNCF Sandbox do Project Zot; consultado em 2026-10-03.
