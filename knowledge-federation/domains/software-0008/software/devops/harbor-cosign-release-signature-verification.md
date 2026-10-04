---
id: software.devops.tranche02.000148
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/goharbor/harbor/main/README.md", "https://github.com/goharbor/harbor"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Verificação criptográfica de instaladores do Harbor com Cosign a partir da v2.15.0

## Em uma frase
A subseção `Verifying Release Signatures` do README documenta que, a partir da versão `v2.15.0`, os artefatos de release do Harbor são assinados criptograficamente com Cosign (`v2.0+`) para garantir autenticidade e integridade, mostrando o comando exato `cosign verify-blob --bundle harbor-offline-installer-v2.15.0.tgz.sigstore.json --certificate-oidc-issuer https://token.actions.githubusercontent.com --certificate-identity-regexp '^https://github.com/goharbor/harbor/.github/workflows/publish_release.yml@refs/tags/v.*$' harbor-offline-installer-v2.15.0.tgz` (com saída esperada `Verified OK`) e apontando para o guia completo `docs/signature-verification.md`.

## Por que importa
Como o registro de contêineres é o ponto central de distribuição de binários para toda a infraestrutura, verificar a assinatura criptográfica do próprio instalador do Harbor protege contra adulteração na cadeia de suprimentos antes da instalação.

## Como funciona
Baixe sempre o bundle `.sigstore.json` junto com o instalador offline do Harbor e execute `cosign verify-blob` validando o emissor OIDC do GitHub Actions e a expressão regular do workflow `publish_release.yml` antes de extrair o pacote.

## Exemplo
Um engenheiro de plataforma automatiza no script de instalação a checagem `cosign verify-blob` do pacote `harbor-offline-installer-v2.15.0.tgz` e aborta o deploy se a saída não for `Verified OK`.

## Limites e trade-offs
Não execute `cosign verify-blob` sem restringir `--certificate-oidc-issuer` e `--certificate-identity-regexp` ao repositório oficial `goharbor/harbor`.

## Como verificar
Conferi a subseção Verifying Release Signatures no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-deployment-options-docker-compose-helm-operator]] — Veja também: Opções de implantação: Docker Compose, Helm Chart (harbor-helm) e Harbor Operator.
- [[harbor-oci-distribution-conformance-and-compatibility]] — Veja também: Testes de conformidade OCI Distribution e matriz de compatibilidade de adaptadores.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor — Repositório Oficial no GitHub](https://github.com/goharbor/harbor) — Repositório oficial do Harbor com código-fonte, api/v2.0/swagger.yaml, docs/signature-verification.md e releases.; consultado em 2026-10-03.
