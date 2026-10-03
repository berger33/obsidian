---
id: software.devops.tranche16.001548
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://timoni.sh/concepts", "https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md", "https://github.com/stefanprodan/timoni"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Timoni: assinatura criptográfica (`--sign`) e verificação (`--verify`) de módulos OCI com Cosign

## Em uma frase
Os comandos `timoni mod push --sign` e `timoni mod pull --verify` (bem como `timoni apply` / `bundle apply`) integram suporte nativo ao Sigstore Cosign (por chave privada ou *keyless* via OIDC) para assinar e autenticar módulos OCI.

## Por que importa
Como um módulo Timoni define os `Deployment`, `ClusterRole` e `DaemonSet` que serão aplicados com privilégios no cluster, um comprometimento do container registry permitiria injetar containers maliciosos se a integridade e proveniência do módulo não fossem verificadas criptograficamente antes do deploy.

## Como funciona
No pipeline de release (por exemplo GitHub Actions com token OIDC), o autor publica o módulo com `timoni mod push ./my-app oci://ghcr.io/org/modules/my-app -v 1.2.0 --sign=cosign`. No lado do consumidor, `timoni mod pull ... --verify=cosign` (ou configurações de verificação no bundle) valida a assinatura no Rekor/Fulcio ou contra a chave pública fornecida antes de extrair ou aplicar o CUE.

## Exemplo
```bash
timoni mod push ./my-app oci://ghcr.io/org/modules/my-app -v 1.2.0 --sign=cosign --cosign-key=cosign.key
timoni mod pull oci://ghcr.io/org/modules/my-app -v 1.2.0 -o /tmp/my-app --verify=cosign --cosign-key=cosign.pub
```

## Limites e trade-offs
A verificação keyless OIDC exige especificar as identidades de certificado esperadas (emissor OIDC e expressão de subject/repositório) para impedir que qualquer terceiro autenticado no Fulcio assine um artefato válido.

## Como verificar
Execute `timoni mod pull` com `--verify=cosign` apontando para uma chave pública diferente e confirme que o Timoni bloqueia o download com erro de verificação de assinatura.

## Conexões
- [[timoni-oci-artifacts-media-types-builds-reprodutiveis-git]] — Veja também: Timoni: distribuição de módulos e bundles como artefatos OCI reproduzíveis (`application/vnd.timoni.*`).
- [[timoni-artifact-push-pull-transporte-bundles-runtimes]] — Veja também: Timoni: transporte de bundles, runtimes e arquivos arbitrários com `timoni artifact push` e `pull`.

## Fontes
- [Timoni GitHub — README.md (CUE-Powered Kubernetes Package Manager, Modules, Bundles, OCI Artifacts & AI Agent MCP Integration)](https://timoni.sh/concepts) — README oficial do stefanprodan/timoni detalhando a arquitetura CUE, comparação com Helm/Kustomize, fluxo de módulos e bundles e integração MCP; consultado em 2026-10-03.
- [Timoni Official Documentation — Concepts (Module, Instance, Bundle, OCI Artifact Media Types, Flux SSA Drift Detection & Cosign Signing)](https://raw.githubusercontent.com/stefanprodan/timoni/main/README.md) — Documentação oficial de conceitos do Timoni cobrindo vendoring de CRDs, Server-Side Apply com garbage collection, bundles e media types OCI; consultado em 2026-10-03.
- [Timoni — Official GitHub Repository](https://github.com/stefanprodan/timoni) — Repositório oficial Apache-2.0 do Timoni; consultado em 2026-10-03.
